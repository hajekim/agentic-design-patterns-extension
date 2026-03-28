# Changelog

All notable changes to the Agentic Design Patterns Gemini CLI Extension.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [2.2.4] — 2026-03-28

### Fixed
- `gemini-extension.json`: `version` field corrected from `2.2.0` to `2.2.3` to match README and CHANGELOG

### Added
- `mcp_server.py`: `PATTERN_DESCRIPTIONS` dictionary — 28 one-line descriptions covering all patterns
- `mcp_server.py`: `list_patterns()` now includes a one-line description per pattern (e.g. `` `planning` — Breaking complex goals into ordered subtasks ``)
- `GEMINI.md`: Appendix section expanded from a flat name list into a table with one-line description per appendix pattern; added note clarifying appendix patterns are reference/meta patterns, not runtime patterns
- `README.md`: `/gen-skeleton planning` example output added — shows the full Python skeleton generated (LlmAgent + Runner + InMemorySessionService)
- `README.md`: `@architect` and `@reviewer` sub-agent I/O formats documented — input prompt structure and output section breakdown

---

## [2.2.3] — 2026-03-28

### Changed
- `agentic` theme: shifted from blue feel to asphalt dark grey
  - `text.secondary`: `#6B9FCC` (blue) → `#8C9299` (neutral cool grey)
  - `text.link`: `#74ADEA` (bright blue) → `#6E8EB8` (muted blue — retains link visibility)
  - `status.success`: `#6DB5A5` (teal) → `#7A9490` (desaturated grey-teal)

---

## [2.2.2] — 2026-03-28

### Changed
- `agentic` theme: reduced green feel by shifting two colors away from green
  - `text.secondary`: `#6FB4C0` (teal/cyan) → `#6B9FCC` (shifted toward blue, less green component)
  - `status.success`: `#A1C281` (muted green) → `#6DB5A5` (teal-blue, green feel reduced)

---

## [2.2.1] — 2026-03-28

### Changed
- `agentic` theme colors updated to match the author's iTerm2 terminal profile (P3 → sRGB approximation):
  - `background.primary`: `#0d1117` → `#22252A`
  - `text.primary`: `#7ee8c8` → `#ACB2BE` (iTerm2 Foreground)
  - `text.secondary`: `#5a9e88` → `#6FB4C0` (iTerm2 Ansi 6 — Cyan)
  - `text.link`: `#4fc3f7` → `#74ADEA` (iTerm2 Ansi 4 — Blue)
  - `status.success`: `#56d364` → `#A1C281` (iTerm2 Ansi 2 — Green)
  - `status.warning`: `#e3b341` → `#DFC184` (iTerm2 Ansi 3 — Yellow)
  - `status.error`: `#f85149` → `#D17277` (iTerm2 Ansi 1 — Red)
  - `border.default`: `#21262d` → `#333843` (iTerm2 Selection Color)
  - `ui.comment`: `#8b949e` → `#767676` (iTerm2 Ansi 8 — Bright Black)

---

## [2.2.0] — 2026-03-28

### Added
- **Skill-search MCP server** (`mcp_server.py`) — a FastMCP server registered in `gemini-extension.json` that exposes three tools to Gemini CLI via the Model Context Protocol:
  - `list_patterns([category])` — list all 28 patterns grouped by category, or filter to a single category (`core` / `state` / `reliability` / `advanced` / `appendix`)
  - `get_skill(pattern_name)` — retrieve the full `SKILL.md` content for any named pattern; returns fuzzy suggestions on near-miss names
  - `search_skills(query)` — keyword search across all 28 skill definitions, returning matching patterns with a preview of the matched line and a match count
- **`PATTERN_DIR_MAP`** in `mcp_server.py` — handles the `mcp-setup` pattern whose skill file lives under the `mcp/` directory (not `mcp-setup/`) to avoid conflicts with the Gemini CLI built-in `/mcp` command
- **Custom terminal theme** — `agentic` dark theme registered in `gemini-extension.json` under `themes`; uses `#0d1117` background with teal primary text (`#7ee8c8`), green success (`#56d364`), and blue links (`#4fc3f7`)

### Fixed
- `mcp_server.py`: replaced `str | None` union syntax (Python 3.10+ only) with `Optional[str]` from `typing` for compatibility with Python 3.9
- `mcp_server.py`: `list_patterns()` previously silently returned all 28 patterns when passed an unrecognized category name; it now returns an explicit error message listing the five valid category names

---

## [2.1.1] — 2026-03-28

### Fixed
- `skills/mcp/SKILL.md`: replaced all uses of the deprecated `Agent` class with `LlmAgent`; replaced `InMemoryRunner` with the correct `Runner` + `InMemorySessionService` pattern from `google.adk.runners` and `google.adk.sessions`
- `skills/prompt-chaining/SKILL.md`: same ADK class corrections — `Agent` → `LlmAgent` in the import line and all three instantiation sites
- `skills/resource-aware/SKILL.md`: removed the non-existent `gemini-2.5-flash-thinking` model name from the model selection table; replaced with `gemini-2.5-flash` with a note to set Thinking Budget high for reasoning tasks
- `skills/appendix-reasoning-engines/SKILL.md`: replaced all eight occurrences of `gemini-2.5-flash-thinking` with `gemini-2.5-flash`; added Thinking Budget parameter guidance to clarify that reasoning depth is controlled via `thinking_config`, not a separate model variant

---

## [2.1.0] — 2026-03-28

### Added
- **`/pattern-summary [filter]`** slash command (`commands/pattern-summary.toml`) — lists all 28 patterns grouped by category when called with no argument; accepts a category name (`core`, `state`, `reliability`, `advanced`, `appendix`) or a specific pattern name as an optional filter; output is designed to lead naturally into `/gen-skeleton`
- **`@architect` sub-agent** (`agents/architect.md`) — given a natural-language problem description, recommends an optimal combination of patterns from the 28-pattern library with rationale; output explicitly suggests the next `/gen-skeleton <pattern>` command to run
- **`@reviewer` sub-agent** (`agents/reviewer.md`) — reviews pasted agent code for pattern compliance and correct SDK conventions; checklist covers 12 of 28 patterns (core + state + reliability); appendix patterns and some advanced patterns intentionally excluded as they are reference-only
- **`agents/planning-skeleton.py`** — reference implementation generated by `/gen-skeleton planning`; demonstrates the full planning loop (goal decomposition → sequential subtask execution → replanning on failure) using `LlmAgent` + `Runner` + `InMemorySessionService` and `google-genai`

---

## [2.0.1] — 2026-03-28

### Fixed
- `README.md`: corrected the Skills-only repository URL from the wrong `hajekim/skills-agentic-design-patterns` to the correct `hajekim/agentic-design-patterns-skills`
- `GEMINI.md`: all seven appendix pattern names in the quick-reference table were missing the `appendix-` prefix (e.g., `prompt-engineering` → `appendix-prompt-engineering`); corrected to match the canonical skill names used in trigger matching

---

## [2.0.0] — 2026-03-28

### Added
- **`GEMINI.md` global context file** — automatically loaded at every Gemini CLI session start via `"contextFileName": "GEMINI.md"` in the manifest; provides the model with a quick-reference table of all 28 patterns, model selection guidance (Flash-Lite / Flash / Pro + Thinking Budget), and technical conventions (correct SDK, ADK classes, LangChain packages)
- **`/gen-skeleton <pattern>`** slash command (`commands/gen-skeleton.toml`) — generates a complete, runnable Python code skeleton for any of the 28 patterns; enforces correct SDK conventions: `google-genai`, `LlmAgent`, `Runner`, `InMemorySessionService`; uses `gemini-2.5-flash` as the default model
- **Model Preference Setting** in `gemini-extension.json` — `GEMINI_MODEL` environment variable configurable during `gemini extensions install`; stored under `settings[]` with `sensitive: false`; defaults to Gemini CLI's own default when left blank
- **`"contextFileName"` field** in `gemini-extension.json` — replaces the previous absence of global context; points to `GEMINI.md` at the extension root

---

## [1.11] — 2026-03-27

### Changed
- Renamed the MCP setup skill directory from `mcp/` to retain `mcp/` as the folder name but changed the frontmatter `name` field from `mcp` to `mcp-setup` to avoid collision with the Gemini CLI built-in `/mcp` slash command; all trigger phrases updated accordingly

---

## [1.10] — 2026-03-27

### Added
- **Extension format** — created `gemini-extension.json` manifest and restructured files for distribution as a Gemini CLI Extension installable via `gemini extensions install <url>`
- **`github-release-extension/`** — local git clone of `hajekim/agentic-design-patterns-extension`; acts as the push target for Extension releases
- **`github-release-skills/`** — local git clone of `hajekim/agentic-design-patterns-skills`; acts as the push target for Skills-only releases

---

## [1.9] — 2026-03-27

### Added
- Japanese and Chinese trigger phrases added to all 28 skills; total trigger count reached **1,376** (English: 474, Korean: 337, Japanese: 284, Chinese: 281)

---

## [1.8] — 2026-03-27

### Changed
- Migrated all skill code examples from the deprecated `google-generativeai` SDK to `google-genai`
- Updated LangChain imports: `langchain_community.vectorstores.Chroma` → `langchain-chroma`; `langchain.text_splitter` → `langchain-text-splitters`; deprecated `ConversationChain` → `RunnableWithMessageHistory`
- Replaced `vertexai.TextEmbeddingModel` with `client.models.embed_content()` in embedding examples

---

## [1.7] — 2026-03-27

### Changed
- Expanded skill descriptions with verified Gemini CLI and Antigravity installation paths (`.gemini/skills/`, `.agents/skills/`)
- Added platform-specific activation notes clarifying semantic vs. keyword-based skill matching per platform

---

## [1.6] — 2026-03-27

### Changed
- Standardized all `README.md` content to English; removed bilingual mixed sections for consistency

---

## [1.5] — 2026-03-27

### Added
- Claude Code compatibility notes added to relevant skills
- Platform Compatibility table added to `README.md` comparing Gemini CLI, Antigravity, and Claude Code installation and activation methods

---

## [1.4] — 2026-03-27

### Added
- **Related Skills** cross-reference section added to all 28 `SKILL.md` files, linking patterns that are commonly combined
- **Appendix E — Reasoning Engines** skill added covering Thinking Budget, when to use reasoning models, and model selection guidance

### Changed
- Default model recommendation upgraded from `gemini-2.0-flash` to `gemini-2.5-flash` across all skill code examples

---

## [1.3] — 2026-03-27

### Added
- Korean trigger phrases added to all 28 skills (337 phrases total); skills now respond to natural Korean requests in addition to English

---

## [1.2] — 2026-03-27

### Added
- **Context Engineering** content added to relevant skills — guidance on structuring prompts for agentic workflows
- **ML Routing** patterns added to the routing skill — distinguishing rule-based, classifier-based, and LLM-based routing strategies
- **Agent Complexity Levels** section added to multi-agent and planning skills — helping practitioners choose the right complexity tier for their use case

---

## [1.1] — 2026-03-27

### Fixed
- All skill code examples corrected from deprecated ADK classes:
  - `Agent` → `LlmAgent` (from `google.adk.agents`)
  - `InMemoryRunner` → `Runner` (from `google.adk.runners`) + `InMemorySessionService` (from `google.adk.sessions`)
- Session creation and runner invocation patterns updated to match the current ADK API

---

## [1.0] — 2026-03-27

### Added
- Initial release of 28 agentic design pattern skills derived from *Agentic Design Patterns* by Antonio Gulli (424 pages, 21 chapters + 6 appendices)
- Skills organized across five categories: Core (7), State Management (4), Reliability (3), Advanced (7), Appendix (7)
- Each skill follows the **DEFINE → PLAN → ACTION** workflow with implementation examples in Google ADK, LangChain, and LangGraph
- English trigger phrases covering 474 natural-language requests across all 28 patterns
- `SKILL.md` frontmatter format: `name`, `description` (trigger phrases), full skill body
