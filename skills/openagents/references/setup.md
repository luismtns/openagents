# openagents:setup

## Overview

Configures your current machine for the OpenAgents ecosystem. This is a one-time operation per machine.

## Detection

1. Identify the running agent:
   - **opencode**: `OPENCODE_` env vars, config at `~/.config/opencode/`
   - **claude-code**: `CLAUDE_CODE` env vars, config at `~/.claude/`
   - **codex**: `CODEX_` env vars, config at `~/.codex/`
   - **cursor**: `CURSOR_` env vars
   - Fallback: read `~/.agents/skills/` (agent-agnostic)

## Steps

### 1. Ensure skill directory

Check that the `openagents` skill directory exists under `~/.agents/skills/`.

If missing, install via:

```bash
npx skills add luismtns/openagents
```

### 2. Create global manifest

Write `~/.agents/AGENTS.md`:

```markdown
# OpenAgents — Global Manifest

Available skill: openagents

Load with the `skill` tool: `skill({ name: "openagents" })`
```

### 3. Configure detected agent

If **opencode**:
- Ensure `~/.config/opencode/AGENTS.md` references OpenAgents
- Add `instructions` field to `~/.config/opencode/opencode.jsonc` pointing to `~/.agents/AGENTS.md`

If **claude-code**:
- Ensure `~/.claude/CLAUDE.md` references OpenAgents
- Claude Code already reads `~/.agents/skills/` automatically

If **cursor**:
- Symlink skills into Cursor's skill directory:
  ```bash
  mkdir -p ~/.cursor/skills
  ln -sfn ~/.agents/skills/* ~/.cursor/skills/
  ```

### 4. Verify

Confirm the `openagents` skill appears in the agent's skill discovery. Load this skill as a smoke test.

## Agent-specific notes

| Agent | Global instructions | Skills path |
|-------|-------------------|-------------|
| opencode | `~/.config/opencode/AGENTS.md` | `~/.agents/skills/` (auto) |
| claude-code | `~/.claude/CLAUDE.md` | `~/.agents/skills/` (auto) |
| codex | Codex UI settings | `~/.agents/skills/` (auto) |
| cursor | `~/.cursor/rules/` | `~/.cursor/skills/` |
| cline | `~/.clinerules` | `~/.agents/skills/` (auto) |
| zed | Zed settings | `~/.agents/skills/` (auto) |
