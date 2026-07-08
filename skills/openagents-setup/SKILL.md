---
name: openagents-setup
description: |
  Verifies and configures AI coding agents on the current machine to follow the
  OpenAgents multi-agent standard. Detects the running agent, checks that the
  global skills directory and manifest are in place, configures agent-specific
  settings for multi-agent compatibility, and verifies the ecosystem is operational.
  Use when setting up OpenAgents for the first time on a new machine.
  Triggers: openagents setup, configure agents, check agents, verify setup.
allowed-tools: Read, Write, Glob, Bash(git:*), Bash(mkdir:*), Bash(ln:*), Bash(cp:*), Bash(test:*), Bash(uname:*), Bash(echo:*), Bash(pwd:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline, zed
tags: [openagents, setup, configure, global]
---

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

### 1. Ensure skills directory structure

Check that the 6 skill directories exist under `~/.agents/skills/`:
- openagents-setup
- openagents-init
- openagents-rules
- openagents-sync
- openagents-audit
- openagents-skills

If missing, install via:

```bash
npx skills add luismtns/openagents
```

### 2. Create global manifest

Write `~/.agents/AGENTS.md`:

```markdown
# OpenAgents — Global Manifest

Available skills: openagents-setup, openagents-init, openagents-rules,
openagents-sync, openagents-audit, openagents-skills

Load any with the `skill` tool: `skill({ name: "openagents-<name>" })`
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

Confirm all 6 skills appear in the agent's skill discovery. Load this skill as a smoke test.

## Agent-specific notes

| Agent | Global instructions | Skills path |
|-------|-------------------|-------------|
| opencode | `~/.config/opencode/AGENTS.md` | `~/.agents/skills/` (auto) |
| claude-code | `~/.claude/CLAUDE.md` | `~/.agents/skills/` (auto) |
| codex | Codex UI settings | `~/.agents/skills/` (auto) |
| cursor | `~/.cursor/rules/` | `~/.cursor/skills/` |
| cline | `~/.clinerules` | `~/.agents/skills/` (auto) |
| zed | Zed settings | `~/.agents/skills/` (auto) |
