<!-- openagents -->
# OpenAgents Skill Pack

This repository provides 6 OpenAgents skills for multi-agent workflow orchestration.
Install via `npx skills add luismtns/openagents` or load individual skills with:

- `skill({ name: "openagents-install" })` — one-time global setup
- `skill({ name: "openagents-init" })` — per-project scaffolding
- `skill({ name: "openagents-setup-rules" })` — deep analysis + rule generation
- `skill({ name: "openagents-sync" })` — sync skills across machines
- `skill({ name: "openagents-audit" })` — audit skill usage
- `skill({ name: "openagents-skills" })` — discover and manage skills

Agent-agnostic: opencode, claude-code, cursor, codex, cline, zed all supported.

## Project rules (`.agents/rules/`)

- `validate.md` — pre-release validation checklist
- `distributed-skills.md` — naming, frontmatter, and layout conventions

Rules are agent-agnostic in `.agents/rules/` and symlinked from `.claude/rules/`.
<!-- openagents -->
