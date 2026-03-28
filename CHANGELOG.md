# Changelog

All notable changes to the Agentic Design Patterns Gemini CLI Extension.

---

## [2.2.0] — 2026-03-28

### Added
- **Skill-search MCP server** (`mcp_server.py`) — three tools exposed to Gemini CLI via MCP protocol:
  - `list_patterns([category])` — list all 28 patterns or filter by category (core / state / reliability / advanced / appendix)
  - `get_skill(pattern_name)` — retrieve the full SKILL.md for any pattern by name
  - `search_skills(query)` — keyword search across all 28 skill definitions with match preview
- **Custom terminal theme** — `agentic` dark theme (teal/green accents) registered in `gemini-extension.json`

### Fixed
- `mcp_server.py`: use `Optional[str]` from `typing` instead of `str | None` union syntax for Python 3.9+ compatibility
- `mcp_server.py`: `list_patterns()` now returns an explicit error message for unrecognized category names instead of silently returning all patterns

---

## [2.1.1] — 2026-03-28

### Fixed
- `mcp-setup` and `prompt-chaining` skills: corrected deprecated ADK class usage (`Agent` → `LlmAgent`, `InMemoryRunner` → `Runner` + `InMemorySessionService`)
- `resource-aware` and `appendix-reasoning-engines` skills: removed non-existent `gemini-2.5-flash-thinking` model; replaced with `gemini-2.5-flash` + Thinking Budget guidance

---

## [2.1.0] — 2026-03-28

### Added
- **`/pattern-summary [filter]`** slash command — browse all 28 patterns grouped by category, or filter by category name or specific pattern
- **`@architect` sub-agent** — recommends optimal pattern combinations for a given problem; output leads naturally into `/gen-skeleton`
- **`@reviewer` sub-agent** — reviews agent code for pattern compliance and SDK conventions (covers 12 of 28 patterns)

---

## [2.0.0] — 2026-03-28

### Added
- **`GEMINI.md` global context** — auto-loads at every session start; gives the model full awareness of all 28 patterns, model selection guidance, and technical conventions
- **`/gen-skeleton <pattern>`** slash command — generates a Python code skeleton for any pattern using correct SDK conventions (google-genai, LlmAgent + Runner)
- **Model Preference Setting** — set preferred Gemini model (`GEMINI_MODEL`) during `gemini extensions install`

---

## [1.x] — 2026-03-27

Initial release series — 28 skills across 21 chapters and 7 appendices, with iterative additions:

| Version | Change |
|---------|--------|
| 1.0 | Initial release — 28 skills |
| 1.1 | Fixed ADK API bugs (LlmAgent, Runner + session pattern) |
| 1.2 | Added Context Engineering, ML Routing, Agent Complexity Levels |
| 1.3 | Added Korean triggers to all 28 skills |
| 1.4 | Upgraded to gemini-2.5-flash, added Related Skills, Reasoning Engines appendix |
| 1.5 | Claude Code compatibility, Platform Compatibility table |
| 1.6 | README standardized to English |
| 1.7 | Gemini CLI / Antigravity path verification and guide expansion |
| 1.8 | Library migration: google-generativeai → google-genai, LangChain deprecations |
| 1.9 | Japanese + Chinese triggers added (total 1,376 triggers) |
| 1.10 | Extension format created |
| 1.11 | MCP skill renamed mcp → mcp-setup to avoid Gemini CLI built-in conflict |
