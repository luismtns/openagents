---
name: openagents-install
description: |
  One-time global setup of the OpenAgents multi-agent ecosystem on the current machine.
  Detects the running AI coding agent, creates the global skills directory structure,
  configures agent-specific settings, writes the OpenAgents manifest, and verifies
  that all 6 OpenAgents skills are discoverable by the agent.
  Use when installing OpenAgents for the first time on a new machine.
  Triggers: openagents install, setup openagents, init openagents global.
allowed-tools: Read, Write, Glob, Bash(git:*), Bash(mkdir:*), Bash(ln:*), Bash(cp:*), Bash(test:*), Bash(uname:*), Bash(echo:*), Bash(pwd:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, setup, install, global]
---

# openagents:install

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

Check `~/.agents/skills/openagents/` exists with the 6 skill directories:
- openagents-install
- openagents-init
- openagents-setup-rules
- openagents-sync
- openagents-audit
- openagents-skills

If this repository was cloned, symlink or copy:

```bash
mkdir -p ~/.agents/skills
ln -sfn $(pwd)/skills/* ~/.agents/skills/
```

### 2. Create global manifest

Write `~/.agents/AGENTS.md`:

```markdown
# OpenAgents — Global Manifest

Available skills: openagents-install, openagents-init, openagents-setup-rules,
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

### 4. Verify

Confirm all 6 skills appear in the agent's skill discovery. Load this skill as a smoke test.

## Agent-specific notes

| Agent | Global instructions | Skills path |
|-------|-------------------|-------------|
| opencode | `~/.config/opencode/AGENTS.md` | `~/.agents/skills/` (auto) |
| claude-code | `~/.claude/CLAUDE.md` | `~/.agents/skills/` (auto) |
| codex | Codex UI settings | `~/.agents/skills/` (auto) |
| cursor | `~/.cursor/rules/` | `~/.cursor/skills/` |
