# Agentic Design Patterns — Extension Context

This Extension provides 28 agentic design pattern skills based on
*Agentic Design Patterns* by Antonio Gulli.

## How This Extension Works

- **Skills** activate automatically when you describe a relevant task.
  You do not need to invoke them explicitly.
- **`/gen-skeleton <pattern>`** generates a Python code skeleton for any pattern.
- This context file is loaded at the start of every session.

---

## 28 Patterns — Quick Reference

### Core Patterns

| Pattern | When to Use |
|---------|------------|
| `prompt-chaining` | Sequential steps where each output feeds the next |
| `routing` | Dynamic selection of handler based on input type |
| `parallelization` | Independent tasks that can run concurrently |
| `reflection` | Self-evaluation and iterative improvement |
| `tool-use` | Calling external APIs, databases, or functions |
| `planning` | Breaking complex goals into ordered subtasks |
| `multi-agent-collaboration` | Coordinating multiple specialized agents |

### State Management

| Pattern | When to Use |
|---------|------------|
| `memory-management` | Persisting context across sessions |
| `learning-adaptation` | Adjusting behavior based on feedback |
| `mcp-setup` | Connecting to external tools via Model Context Protocol |
| `goal-setting` | Defining and tracking long-term agent objectives |

### Reliability

| Pattern | When to Use |
|---------|------------|
| `exception-handling` | Graceful degradation and recovery from errors |
| `human-in-the-loop` | Human review at critical decision points |
| `rag` | Grounding responses in retrieved, up-to-date knowledge |

### Advanced Patterns

| Pattern | When to Use |
|---------|------------|
| `a2a` | Agent-to-agent communication protocols |
| `resource-aware` | Optimizing for cost, latency, and token budget |
| `reasoning` | Structured chain-of-thought and problem decomposition |
| `guardrails` | Enforcing safety, policy, and output constraints |
| `evaluation` | Measuring and benchmarking agent performance |
| `prioritization` | Ranking and scheduling tasks by urgency and impact |
| `exploration` | Systematic discovery in unknown or large environments |

### Appendices

`appendix-prompt-engineering` · `appendix-gui-agents` · `appendix-agentic-frameworks` · `appendix-agentspace` · `appendix-ai-cli` · `appendix-coding-agents` · `appendix-reasoning-engines`

---

## Model Selection Guide

| Task Type | Recommended Model | Thinking Budget |
|-----------|------------------|----------------|
| Simple pipelines — `prompt-chaining`, `routing` | `gemini-2.5-flash-lite` | Not supported |
| Medium complexity — `tool-use`, `rag`, `parallelization` | `gemini-2.5-flash` | Dynamic (leave unset) |
| Complex reasoning — `planning`, `reasoning`, `evaluation` | `gemini-2.5-flash` or `gemini-2.5-pro` | Set high |
| Large-scale coordination — `multi-agent-collaboration`, `a2a` | `gemini-2.5-pro` | Set high |

**Thinking Budget guidance:**
- **Leave unset** for most tasks — the model decides dynamically based on query complexity.
- **Set high** when accuracy is critical and you can tolerate higher latency and cost.
- **Set to 0** to fully disable thinking for speed-sensitive or real-time tasks.
- `gemini-2.5-flash-lite` does **not** support Thinking Budget.

---

## Key Technical Decisions

When generating or reviewing agentic code with this library, apply these conventions:

| Component | Use | Avoid |
|-----------|-----|-------|
| Gemini SDK | `google-genai` | `google-generativeai` (deprecated) |
| ADK Agent class | `LlmAgent` | `Agent` |
| ADK Runner | `Runner` + `InMemorySessionService` | `InMemoryRunner` |
| LangChain vector store | `langchain-chroma` | `langchain_community.vectorstores.Chroma` |
| LangChain text splitter | `langchain-text-splitters` | `langchain.text_splitter` |
| LangChain conversation | `RunnableWithMessageHistory` | `ConversationChain` (deprecated) |
| Embeddings | `client.models.embed_content()` | `vertexai.TextEmbeddingModel` |
