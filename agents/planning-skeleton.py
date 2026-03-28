# =============================================================================
# SECTION 1: IMPORTS
# =============================================================================
import os
import json

import google.genai as genai
from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part


# =============================================================================
# SECTION 2: CONFIGURATION
# =============================================================================
API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL_NAME = "gemini-2.5-flash"

APP_NAME = "planning_app"
USER_ID = "user1"
SESSION_ID = "session1"


# =============================================================================
# SECTION 3: CORE PATTERN IMPLEMENTATION
# Planning pattern: goal decomposition → subtask execution → replanning on failure
# =============================================================================

# --- 3a. Planner Agent ---
# Decomposes a complex goal into an ordered list of subtasks.
planner_agent = LlmAgent(
    name="Planner",
    model=MODEL_NAME,
    instruction="""You are a strategic planner. When given a complex goal:
1. Break it down into 3-7 concrete, executable subtasks.
2. For each subtask specify: a short action description and the expected output.
3. Return ONLY valid JSON in this exact format (no prose):
{
  "subtasks": [
    {"id": 1, "action": "<what to do>", "expected_output": "<what success looks like>"},
    ...
  ]
}
Keep subtasks focused, ordered by dependency, and achievable independently.""",
)


def decompose_goal(goal: str) -> list[dict]:
    """Call the planner agent and return the list of subtasks."""
    session_service = InMemorySessionService()
    session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id="plan_session"
    )
    runner = Runner(
        agent=planner_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    message = Content(parts=[Part(text=f"Goal: {goal}")])
    response_text = ""
    for event in runner.run(
        user_id=USER_ID, session_id="plan_session", new_message=message
    ):
        if event.is_final_response():
            response_text = event.content.parts[0].text

    # Parse the JSON plan; return empty list on failure
    try:
        # Strip markdown fences if present
        cleaned = response_text.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("```")[1]
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        plan = json.loads(cleaned)
        return plan.get("subtasks", [])
    except (json.JSONDecodeError, AttributeError):
        return []


# --- 3b. Executor Agent ---
# Processes a single subtask and returns the result as a string.
executor_agent = LlmAgent(
    name="Executor",
    model=MODEL_NAME,
    instruction="""You are a meticulous executor. You receive a single subtask and
any relevant context from previously completed steps. Execute the subtask thoroughly
and return a concise result (2-5 sentences). Do not ask clarifying questions; make
reasonable assumptions and proceed.""",
)


def execute_subtask(subtask: dict, context: str) -> tuple[bool, str]:
    """
    Execute a single subtask.
    Returns (success: bool, result: str).
    Success is True when the executor returns a non-empty, plausible result.
    """
    session_service = InMemorySessionService()
    session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id="exec_session"
    )
    runner = Runner(
        agent=executor_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    prompt = (
        f"Subtask: {subtask['action']}\n"
        f"Expected output: {subtask['expected_output']}\n"
        f"Context from previous steps:\n{context if context else 'None'}"
    )
    message = Content(parts=[Part(text=prompt)])
    result_text = ""
    for event in runner.run(
        user_id=USER_ID, session_id="exec_session", new_message=message
    ):
        if event.is_final_response():
            result_text = event.content.parts[0].text

    success = bool(result_text and len(result_text.strip()) > 10)
    return success, result_text


# --- 3c. Replanning Step ---
# Triggered when a subtask fails; asks the planner to produce a revised subtask.
replan_agent = LlmAgent(
    name="Replanner",
    model=MODEL_NAME,
    instruction="""You are a replanning expert. A subtask has failed. Given:
- The original subtask description
- The reason for failure
- Context from previously completed steps

Produce a single revised subtask that achieves the same goal via an alternative approach.
Return ONLY valid JSON:
{"id": <same id>, "action": "<revised action>", "expected_output": "<expected output>"}""",
)


def replan_subtask(failed_subtask: dict, failure_reason: str, context: str) -> dict:
    """
    Generate a replacement subtask for a failed one.
    Returns a revised subtask dict (falls back to the original on parse error).
    """
    session_service = InMemorySessionService()
    session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID, session_id="replan_session"
    )
    runner = Runner(
        agent=replan_agent,
        app_name=APP_NAME,
        session_service=session_service,
    )
    prompt = (
        f"Failed subtask: {json.dumps(failed_subtask)}\n"
        f"Failure reason: {failure_reason}\n"
        f"Context from completed steps:\n{context if context else 'None'}"
    )
    message = Content(parts=[Part(text=prompt)])
    response_text = ""
    for event in runner.run(
        user_id=USER_ID, session_id="replan_session", new_message=message
    ):
        if event.is_final_response():
            response_text = event.content.parts[0].text

    try:
        cleaned = response_text.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.split("```")[1]
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
        revised = json.loads(cleaned)
        return revised
    except (json.JSONDecodeError, AttributeError):
        # Fall back to the original subtask if parsing fails
        return failed_subtask


# --- 3d. Executor Loop with Replanning ---
def run_planning_loop(goal: str, max_retries: int = 1) -> dict:
    """
    Full planning loop:
      1. Decompose goal into subtasks (planner).
      2. Execute subtasks in sequence (executor).
      3. On failure, replan and retry up to max_retries times.

    Returns a results dict with the goal, subtask outcomes, and a final summary.
    """
    print(f"\n[Planning] Goal: {goal}")

    # Step 1 — Goal decomposition
    subtasks = decompose_goal(goal)
    if not subtasks:
        return {"goal": goal, "error": "Planner failed to generate subtasks.", "results": []}

    print(f"[Planning] Decomposed into {len(subtasks)} subtask(s).")

    completed_results = []
    context = ""

    # Step 2 — Sequential subtask execution with replanning on failure
    for subtask in subtasks:
        print(f"  → Subtask {subtask['id']}: {subtask['action']}")
        retries = 0
        success = False
        result = ""

        while retries <= max_retries:
            success, result = execute_subtask(subtask, context)
            if success:
                break

            # Step 3 — Replanning triggered on failure
            retries += 1
            if retries <= max_retries:
                print(f"    [Replanning] Subtask {subtask['id']} failed. Generating alternative.")
                subtask = replan_subtask(
                    failed_subtask=subtask,
                    failure_reason="Executor returned an empty or insufficient result.",
                    context=context,
                )
                print(f"    [Replanning] Revised action: {subtask['action']}")

        status = "completed" if success else "failed_after_replanning"
        completed_results.append({
            "id": subtask["id"],
            "action": subtask["action"],
            "status": status,
            "result": result,
        })
        # Append this step's result to the running context
        context += f"\nStep {subtask['id']} ({status}): {result[:300]}"

    return {"goal": goal, "subtask_results": completed_results}


# =============================================================================
# SECTION 4: MAIN EXECUTION BLOCK — MINIMAL WORKING EXAMPLE
# =============================================================================
if __name__ == "__main__":
    # Configure the Gemini client
    if not API_KEY:
        raise EnvironmentError("Set the GEMINI_API_KEY environment variable before running.")
    genai.configure(api_key=API_KEY)

    # Define a complex goal to demonstrate the planning pattern
    example_goal = (
        "Research the top 3 programming languages for AI development in 2025, "
        "summarise their key strengths, and recommend the best one for a beginner."
    )

    # Run the full planning loop
    output = run_planning_loop(goal=example_goal, max_retries=1)

    # Display results
    print("\n=== PLANNING RESULTS ===")
    print(f"Goal: {output['goal']}\n")
    for item in output.get("subtask_results", []):
        print(f"[{item['status'].upper()}] Subtask {item['id']}: {item['action']}")
        print(f"  Result: {item['result'][:200]}...\n" if len(item['result']) > 200 else f"  Result: {item['result']}\n")
