# Agentic Design Patterns — Gemini CLI Extension

A Gemini CLI **Extension** packaging 28 agentic design pattern skills. Install with a single command and start building production-ready AI agents immediately.

## Install

```bash
gemini extensions install https://github.com/hajekim/agentic-design-patterns-extension
```

After installation, restart Gemini CLI. The 28 skills activate automatically when you describe what you want to build.

> Current version: **v2.2.1** — See [CHANGELOG.md](CHANGELOG.md) for full version history.

## What This Extension Provides

**28 agent skills** across four categories:

| Category | Skills |
|----------|--------|
| Core Patterns | Prompt Chaining, Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent Collaboration |
| State Management | Memory Management, Learning & Adaptation, MCP, Goal Setting |
| Reliability | Exception Handling, Human-in-the-Loop, RAG |
| Advanced Patterns | A2A, Resource-Aware, Reasoning, Guardrails, Evaluation, Prioritization, Exploration |
| Appendix | Prompt Engineering, GUI Agents, Agentic Frameworks, AgentSpace, AI CLI, Coding Agents, Reasoning Engines |

Skills use the **DEFINE → PLAN → ACTION** workflow and include implementation examples in Google ADK, LangChain, and LangGraph.

## How Skills Activate

Gemini CLI reads the `name` and `description` of each skill. When your request matches a skill's description, the model automatically loads the full skill instructions.

**1,376 trigger phrases** across four languages:

```
# English
"Build a multi-step agent pipeline"          → Prompt Chaining
"set up MCP server"                          → MCP
"choose agent framework"                     → Agentic Frameworks
"thinking model for complex reasoning"       → Reasoning Engines

# 한국어
"프롬프트 체이닝으로 파이프라인 만들어줘"    → Prompt Chaining
"MCP 구성을 해줘"                           → MCP
"메모리뱅크 만들어줘"                       → Memory Management
"추론 모델 언제 써야 해?"                   → Reasoning Engines

# 日本語
"マルチエージェントを構築したい"             → Multi-Agent Collaboration
"MCPサーバーを設定したい"                   → MCP
"RAGパイプラインを作りたい"                 → RAG

# 中文
"帮我构建多智能体系统"                      → Multi-Agent Collaboration
"配置MCP服务器"                            → MCP
"搭建RAG知识库问答系统"                    → RAG
```

## Commands & Agents

### Slash Commands

```bash
# Browse all 28 patterns grouped by category
/pattern-summary

# Filter by category: core / state / reliability / advanced / appendix
/pattern-summary reliability

# Look up a specific pattern
/pattern-summary planning

# Generate a Python code skeleton for a pattern
/gen-skeleton planning
/gen-skeleton rag
```

### Sub-agents (Preview)

```bash
# Get pattern combination recommendations for your problem
@architect "I need to build a customer support bot that learns from feedback"

# Review your agent code for pattern compliance
@reviewer <paste your code>
```

**Recommended workflow:**
1. `@architect` → get pattern recommendations
2. `/gen-skeleton <pattern>` → generate code skeleton
3. `@reviewer` → verify implementation

---

## Extension Management

```bash
# Check installed extensions and their skills
gemini extensions list

# Update to latest version
gemini extensions update agentic-design-patterns

# Disable without uninstalling
gemini extensions disable agentic-design-patterns

# Uninstall
gemini extensions uninstall agentic-design-patterns
```

## Platform Compatibility

| Platform | Installation | Activation |
|----------|-------------|------------|
| **Gemini CLI** | `gemini extensions install <url>` | Semantic — model reads description autonomously |
| **Antigravity** | Copy `skills/` to `.agents/skills/` | Keyword pattern matching |
| **Claude Code** | Symlink `skills/` to `.claude/skills/` | Semantic judgment + slash commands |

> For Antigravity and Claude Code, use the [Skills-only version](https://github.com/hajekim/agentic-design-patterns-skills).

## Extension Structure

```
agentic-design-patterns/
├── gemini-extension.json     ← Extension manifest (v2.2.1)
├── GEMINI.md                 ← Global context: pattern guide, model guide, tech decisions
├── mcp_server.py             ← Skill-search MCP server (list_patterns, get_skill, search_skills)
├── commands/
│   ├── gen-skeleton.toml    ← /gen-skeleton <pattern> — generate code skeleton
│   └── pattern-summary.toml ← /pattern-summary [filter] — browse patterns
├── agents/
│   ├── architect.md         ← Recommend optimal pattern combinations
│   └── reviewer.md          ← Review code for pattern compliance
└── skills/                   ← 28 skill definitions
    ├── planning/
    │   └── SKILL.md
    ├── rag/
    │   └── SKILL.md
    └── ...
```

## Trigger Coverage

| Language | Count |
|----------|------:|
| English  | 474   |
| Korean   | 337   |
| Japanese | 284   |
| Chinese  | 281   |
| **Total**| **1,376** |

## Model Reference

| Task Type | Recommended Model | Thinking Budget |
|-----------|------------------|----------------|
| Simple pipelines — prompt-chaining, routing | `gemini-2.5-flash-lite` | Not supported |
| Medium complexity — tool-use, RAG, parallelization | `gemini-2.5-flash` | Dynamic (leave unset) |
| Complex reasoning — planning, reasoning, evaluation | `gemini-2.5-flash` or `gemini-2.5-pro` | Set high |
| Large-scale coordination — multi-agent, a2a | `gemini-2.5-pro` | Set high |

Thinking Budget is an adjustable reasoning depth parameter available on Flash and Pro models (not Flash-Lite). Leave it unset for most tasks — the model decides dynamically.

## Source

Based on **"Agentic Design Patterns"** by Antonio Gulli (424 pages, 21 chapters + 6 appendices).

## License

MIT License — free to use, modify, and distribute.
