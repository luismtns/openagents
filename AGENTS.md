<!-- openagents -->
# OpenAgents Skill Pack

A single skill with multiple subcommands for multi-agent workflow orchestration.
Install via `npx skills add luismtns/openagents` and load with:

- `skill({ name: "openagents" })` — then use `/openagents:setup`, `:init`, `:rules`, `:sync`, `:audit`, `:skills`

Agent-agnostic: opencode, claude-code, cursor, codex, cline, zed all supported.

## Project rules (`.agents/rules/`)

- `validate.md` — pre-release validation checklist
- `distributed-skills.md` — naming, frontmatter, and layout conventions

Rules are agent-agnostic in `.agents/rules/` and symlinked from `.claude/rules/`.
<!-- openagents -->
