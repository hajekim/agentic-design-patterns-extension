#!/usr/bin/env python3
"""
MCP server for Agentic Design Patterns skill search.
Exposes tools to list, search, and retrieve pattern skills.

Requirements: pip install mcp
"""

from pathlib import Path
from typing import Optional

from mcp.server.fastmcp import FastMCP

# Skills directory is located next to this server file
SKILLS_DIR = Path(__file__).parent / "skills"

mcp = FastMCP("agentic-patterns")

PATTERN_CATEGORIES = {
    "core": [
        "prompt-chaining", "routing", "parallelization", "reflection",
        "tool-use", "planning", "multi-agent-collaboration",
    ],
    "state": ["memory-management", "learning-adaptation", "mcp-setup", "goal-setting"],
    "reliability": ["exception-handling", "human-in-the-loop", "rag"],
    "advanced": [
        "a2a", "resource-aware", "reasoning", "guardrails",
        "evaluation", "prioritization", "exploration",
    ],
    "appendix": [
        "appendix-prompt-engineering", "appendix-gui-agents",
        "appendix-agentic-frameworks", "appendix-agentspace",
        "appendix-ai-cli", "appendix-coding-agents", "appendix-reasoning-engines",
    ],
}

ALL_PATTERNS = [p for patterns in PATTERN_CATEGORIES.values() for p in patterns]

PATTERN_DESCRIPTIONS = {
    # Core
    "prompt-chaining":           "Sequential steps where each output feeds the next",
    "routing":                   "Dynamic selection of handler based on input type",
    "parallelization":           "Independent tasks that can run concurrently",
    "reflection":                "Self-evaluation and iterative improvement",
    "tool-use":                  "Calling external APIs, databases, or functions",
    "planning":                  "Breaking complex goals into ordered subtasks",
    "multi-agent-collaboration": "Coordinating multiple specialized agents",
    # State
    "memory-management":         "Persisting context across sessions",
    "learning-adaptation":       "Adjusting behavior based on feedback",
    "mcp-setup":                 "Connecting to external tools via Model Context Protocol",
    "goal-setting":              "Defining and tracking long-term agent objectives",
    # Reliability
    "exception-handling":        "Graceful degradation and recovery from errors",
    "human-in-the-loop":         "Human review at critical decision points",
    "rag":                       "Grounding responses in retrieved, up-to-date knowledge",
    # Advanced
    "a2a":                       "Agent-to-agent communication protocols",
    "resource-aware":            "Optimizing for cost, latency, and token budget",
    "reasoning":                 "Structured chain-of-thought and problem decomposition",
    "guardrails":                "Enforcing safety, policy, and output constraints",
    "evaluation":                "Measuring and benchmarking agent performance",
    "prioritization":            "Ranking and scheduling tasks by urgency and impact",
    "exploration":               "Systematic discovery in unknown or large environments",
    # Appendix
    "appendix-prompt-engineering":   "Structuring prompts for reliability in agentic workflows",
    "appendix-gui-agents":           "Agents that interact with GUIs via vision or accessibility APIs",
    "appendix-agentic-frameworks":   "Comparing ADK, LangChain, LangGraph, and CrewAI",
    "appendix-agentspace":           "Deploying and managing agents on Google AgentSpace",
    "appendix-ai-cli":               "Building AI-powered command-line interfaces",
    "appendix-coding-agents":        "Agents that write, review, and execute code autonomously",
    "appendix-reasoning-engines":    "Selecting reasoning models and configuring Thinking Budget",
}

# mcp-setup skill lives in a folder named 'mcp' (not 'mcp-setup')
PATTERN_DIR_MAP = {"mcp-setup": "mcp"}


def _skill_path(pattern_name: str) -> Path:
    dir_name = PATTERN_DIR_MAP.get(pattern_name, pattern_name)
    return SKILLS_DIR / dir_name / "SKILL.md"


def _read_skill(pattern_name: str) -> Optional[str]:
    path = _skill_path(pattern_name)
    return path.read_text(encoding="utf-8") if path.exists() else None


@mcp.tool()
def list_patterns(category: str = "") -> str:
    """
    List agentic design patterns from the 28-pattern library.

    Args:
        category: Optional filter — one of: core, state, reliability, advanced, appendix.
                  Leave empty to list all 28 patterns grouped by category.

    Returns:
        Formatted list of pattern names.
    """
    if category:
        if category not in PATTERN_CATEGORIES:
            valid = ", ".join(f"`{c}`" for c in PATTERN_CATEGORIES)
            return f"Unknown category '{category}'. Valid categories: {valid}."
        patterns = PATTERN_CATEGORIES[category]
        lines = [f"**{category.title()} Patterns ({len(patterns)}):**"]
        for p in patterns:
            desc = PATTERN_DESCRIPTIONS.get(p, "")
            lines.append(f"- `{p}` — {desc}")
        return "\n".join(lines)

    lines = ["**28 Agentic Design Patterns:**\n"]
    for cat, patterns in PATTERN_CATEGORIES.items():
        lines.append(f"### {cat.title()} ({len(patterns)})")
        for p in patterns:
            desc = PATTERN_DESCRIPTIONS.get(p, "")
            lines.append(f"- `{p}` — {desc}")
        lines.append("")
    lines.append("Tip: use `get_skill(pattern_name)` or `search_skills(query)` for details.")
    return "\n".join(lines)


@mcp.tool()
def get_skill(pattern_name: str) -> str:
    """
    Retrieve the full skill definition for an agentic design pattern.

    Args:
        pattern_name: Canonical pattern name, e.g. 'planning', 'rag', 'mcp-setup'.

    Returns:
        Full SKILL.md content, or a helpful error with suggestions.
    """
    content = _read_skill(pattern_name)
    if content:
        return content

    suggestions = [p for p in ALL_PATTERNS if pattern_name.lower() in p or p in pattern_name.lower()]
    if suggestions:
        return (
            f"Pattern '{pattern_name}' not found. "
            f"Did you mean: {', '.join(f'`{p}`' for p in suggestions)}?"
        )
    return f"Pattern '{pattern_name}' not found. Use `list_patterns()` to see all 28 valid names."


@mcp.tool()
def search_skills(query: str) -> str:
    """
    Search across all 28 skill definitions by keyword.

    Args:
        query: Keyword or phrase to search for in skill content.

    Returns:
        Matching patterns with a preview of the matched line.
    """
    query_lower = query.lower()
    results = []

    for pattern_name in ALL_PATTERNS:
        content = _read_skill(pattern_name)
        if not content:
            continue
        matches = [
            line.strip()
            for line in content.splitlines()
            if query_lower in line.lower() and line.strip()
        ]
        if matches:
            preview = matches[0][:120] + ("..." if len(matches[0]) > 120 else "")
            count = len(matches)
            results.append(
                f"**`{pattern_name}`** ({count} match{'es' if count > 1 else ''})\n  → {preview}"
            )

    if not results:
        return f"No patterns found matching '{query}'."
    return f"Found '{query}' in {len(results)} pattern(s):\n\n" + "\n\n".join(results)


if __name__ == "__main__":
    mcp.run()
