# Agentic Design Patterns — Gemini CLI Extension

> **28 agent skills** for building production-ready AI agents, packaged as a Gemini CLI Extension.
> Install once. Skills activate automatically as you work.

## Quick Install

```bash
gemini extensions install https://github.com/hajekim/skills-agentic-design-patterns
```

Restart Gemini CLI after installation. All 28 skills are immediately available.

---

## What Is This?

This is a **Gemini CLI Extension** — a single installable package that bundles 28 specialized agent skills based on proven agentic design patterns from [*Agentic Design Patterns*](https://github.com/hajekim/skills-agentic-design-patterns) by Antonio Gulli.

Each skill contains:
- A structured **DEFINE → PLAN → ACTION** workflow
- **Implementation examples** in Google ADK, LangChain, and LangGraph
- **1,376 trigger phrases** in English, Korean, Japanese, and Chinese

### Skills vs. Extensions

| | Skills | Extension (this repo) |
|--|--------|-----------------------|
| What it is | Individual `SKILL.md` files | A package containing skills + future capabilities |
| Install command | `gemini skills install <url>` | `gemini extensions install <url>` |
| Extensible with MCP, Hooks, Commands | No | Yes |

---

## Extension Structure

```
agentic-design-patterns/
├── gemini-extension.json        ← Extension manifest (name, version, description)
├── README.md
└── skills/                      ← 28 skill definitions
    ├── prompt-chaining/
    │   └── SKILL.md
    ├── planning/
    │   └── SKILL.md
    ├── rag/
    │   └── SKILL.md
    └── ... (25 more)
```

---

## How Skills Activate

Gemini CLI uses **progressive disclosure**: at startup, it loads only the `name` and `description` from each skill. When your request semantically matches a skill, the model automatically loads the full skill instructions via the `activate_skill` tool.

```
You type a request
    → Gemini scans name + description of all 28 skills
    → Model identifies matching skill(s)
    → Full SKILL.md loaded into context
    → Agent executes with complete skill guidance
```

You never need to invoke skills manually — just describe what you want to build.

---

## Skill Directory

### Core Patterns

| Skill | When to Use |
|-------|-------------|
| **Prompt Chaining** | Multi-step pipelines with sequential LLM calls |
| **Routing** | Classify and direct requests to specialized handlers |
| **Parallelization** | Run independent sub-tasks concurrently |
| **Reflection** | Generate → Critique → Refine quality loops |
| **Tool Use** | Extend agents with APIs, search, code execution |
| **Planning** | Decompose high-level goals into executable steps |
| **Multi-Agent Collaboration** | Specialist agent teams for complex domains |

### State Management

| Skill | When to Use |
|-------|-------------|
| **Memory Management** | Persist context across turns and sessions |
| **Learning & Adaptation** | Agents that improve from feedback and experience |
| **MCP** | Standardized tool and resource integration |
| **Goal Setting** | Long-running agents with measurable objectives |

### Reliability

| Skill | When to Use |
|-------|-------------|
| **Exception Handling** | Retry, fallback, circuit breaker patterns |
| **Human-in-the-Loop** | Approval gates for high-risk actions |
| **RAG** | Ground responses in retrieved external knowledge |

### Advanced Patterns

| Skill | When to Use |
|-------|-------------|
| **A2A Communication** | Cross-boundary agent interoperability |
| **Resource-Aware Optimization** | Token budgets, model cascades, cost control |
| **Reasoning Techniques** | Chain-of-Thought, ReAct, Tree of Thought |
| **Guardrails & Safety** | Input/output filtering, constitutional AI |
| **Evaluation & Monitoring** | LLM-as-judge, production telemetry |
| **Prioritization** | Dynamic task scheduling, deadline-awareness |
| **Exploration & Discovery** | Strategy search via ε-greedy, UCB, A/B testing |

### Appendix Skills

| Skill | When to Use |
|-------|-------------|
| **Prompt Engineering** | Reliable structured outputs with Pydantic |
| **GUI & Real-World Agents** | Visual interfaces, Computer Use, Browser Use |
| **Agentic Frameworks** | LangChain vs LangGraph vs ADK vs CrewAI selection |
| **Google AgentSpace** | No-code enterprise agent deployment |
| **AI CLI Agents** | Claude Code, Gemini CLI, Aider workflows |
| **Coding Agent Teams** | Vibe Coding, Human-Agent Team patterns |
| **Reasoning Engines** | Thinking models, inference-time compute scaling |

---

## Multilingual Trigger System

Skills respond to **1,376 trigger phrases** across four languages. Gemini CLI's semantic model matching means you can describe your intent naturally in any supported language.

### Trigger Coverage

| Language | Triggers |
|----------|--------:|
| English  | 474 |
| Korean   | 337 |
| Japanese | 284 |
| Chinese  | 281 |
| **Total** | **1,376** |

### English

```
"Build a multi-step agent pipeline"              → Prompt Chaining
"Create a multi-agent system for code review"   → Multi-Agent Collaboration
"set up MCP server"                              → MCP
"semantic search over documents"                 → RAG
"retry logic for API failures"                   → Exception Handling
"choose agent framework"                         → Agentic Frameworks
"thinking model for complex reasoning"           → Reasoning Engines
"How do I prevent my agent from hallucinating?" → RAG + Guardrails
```

### Korean (한국어)

```
"프롬프트 체이닝으로 파이프라인 만들어줘"       → Prompt Chaining
"에이전트 팀 구성하는 방법 알려줘"              → Multi-Agent Collaboration
"병렬 작업 실행하는 에이전트 어떻게 만들어?"    → Parallelization
"MCP 구성을 해줘"                              → MCP
"메모리뱅크 만들어줘"                          → Memory Management
"RAG 파이프라인 구성해줘"                      → RAG
"추론 모델 언제 써야 해?"                      → Reasoning Engines
"어떤 프레임워크 써야 해"                      → Agentic Frameworks
```

### Japanese (日本語)

```
"マルチエージェントを構築したい"                → Multi-Agent Collaboration
"並列処理するエージェントを作って"              → Parallelization
"MCPサーバーを設定したい"                      → MCP
"エージェントにメモリを持たせたい"              → Memory Management
"RAGパイプラインを作りたい"                    → RAG
"推論モデルの使い方を教えて"                   → Reasoning Engines
"どのフレームワークを使うべきか"               → Agentic Frameworks
```

### Chinese (中文)

```
"帮我构建多智能体系统"                         → Multi-Agent Collaboration
"怎么让智能体并行处理任务"                     → Parallelization
"配置MCP服务器"                               → MCP
"帮我记住对话内容"                             → Memory Management
"搭建RAG知识库问答系统"                       → RAG
"该用哪个框架构建智能体"                       → Agentic Frameworks
"推理模型和普通模型有什么区别"                 → Reasoning Engines
```

---

## Managing the Extension

```bash
# List all installed extensions and their loaded skills
gemini extensions list

# Update to the latest version
gemini extensions update agentic-design-patterns

# Disable for current workspace only
gemini extensions disable agentic-design-patterns --scope workspace

# Re-enable
gemini extensions enable agentic-design-patterns

# Uninstall completely
gemini extensions uninstall agentic-design-patterns
```

Inside an active Gemini CLI session:

```
/extensions list        → view all extensions and their status
/skills list            → view all available skills
```

---

## Model Reference

Skills default to `gemini-2.5-flash`. Upgrade for accuracy-critical workloads:

| Use Case | Recommended Model |
|----------|-------------------|
| General agent tasks, routing, formatting | `gemini-2.5-flash` |
| Complex reasoning, math, code debugging | `gemini-2.5-flash-thinking` |
| Research-grade analysis, strategic planning | `gemini-2.5-pro` |

See the [Reasoning Engines skill](skills/appendix-reasoning-engines/SKILL.md) for a full model selection guide.

---

## Agent Complexity Levels

Every skill maps to one of four levels. Start at Level 0 and add complexity only when needed:

| Level | Name | Key Skills |
|-------|------|------------|
| **0** | Core Reasoning | Prompt Chaining, Reflection, Reasoning Techniques |
| **1** | Connected Problem-Solver | Tool Use, RAG, Memory Management, MCP |
| **2** | Strategic Problem-Solver | Planning, Routing, Guardrails, Evaluation |
| **3** | Collaborative Multi-Agent | Multi-Agent Collaboration, A2A, Parallelization |

---

## Requirements

```bash
pip install google-genai google-adk langchain langchain-google-genai
pip install langgraph crewai chromadb
pip install langchain-chroma langchain-text-splitters

export GOOGLE_API_KEY="your-api-key-here"
```

---

## Looking for the Skills-Only Version?

This repository is the **Gemini CLI Extension** version.
For Antigravity, Claude Code, or standalone skill installation, use the **Skills-only version**:

```
https://github.com/hajekim/skills-agentic-design-patterns
```

---

## Source

Based on **"Agentic Design Patterns"** by Antonio Gulli
424 pages · 21 chapters · 6 appendices

---

## License

MIT License — free to use, modify, and distribute.
