---
name: openagents
description: |
  Multi-agent workflow orchestration for AI coding agents.
  Handles agent detection and handshake, project initialization,
  skill creation and registration, and deep codebase analysis
  for rule generation.
  Use when setting up multi-agent, initializing projects,
  creating skills or rules, or generating project rules.
  Triggers: openagents global, openagents init, openagents add,
    openagents rules, configure agents, check agents,
    verify setup, init project, project setup, analyze project,
    generate rules, refresh rules, create skill, add skill,
    register skill, package skill.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(mkdir:*),
  Bash(ln:*), Bash(test:*), Bash(uname:*), Bash(echo:*),
  Bash(pwd:*), Bash(ls:*), Bash(find:*)
version: 1.4.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline, zed
tags: [openagents, multi-agent, orchestration, setup, init, rules, skills]
---

# openagents

Multi-agent workflow orchestration for AI coding agents.

Load this skill, then route to the right subcommand:

| Invocation | Read | When |
|------------|------|------|
| `openagents:global` / `openagents global` | [references/global.md](references/global.md) | Detect agent, verify global multi-agent setup, handshake |
| `openagents:init` / `openagents init` | [references/init.md](references/init.md) | Scaffold project AGENTS.md and rules |
| `openagents:add` / `openagents add` | [references/add.md](references/add.md) | Create new skills or rules in multi-agent context |
| `openagents:rules` / `openagents rules` | [references/rules.md](references/rules.md) | Deep codebase analysis for rule generation |

## How it works

The skill detects which AI coding agent is running, adapts configuration
paths accordingly, and orchestrates multi-agent workflows across your
ecosystem. No agent-specific config is shipped — the skill reads your
environment and adjusts.

## Capability constraints

| Tool | Purpose | Scope |
|------|---------|-------|
| Read, Write, Glob, Grep | Read/write project files (AGENTS.md, rules, SKILL.md) | Local filesystem only |
| Bash(mkdir:*) | Create `.agents/rules/`, per-agent symlink dirs | Local filesystem |
| Bash(ln:*) | Create symlinks for agents that don't auto-discover `~/.agents/skills/` | Local filesystem |
| Bash(test:*) | Check file existence, env vars, agent detection | Read-only checks |
| Bash(uname:*) | Detect OS for agent-compatible paths | Read-only |
| Bash(echo:*) | Report status to user | No side effects |
| Bash(pwd:*) | Resolve project root | Read-only |
| Bash(ls:*) | List project files for analysis | Read-only |
| Bash(find:*) | Discover files for rule generation | Read-only |
| Bash(git:*) | Stage/commit skill files (add, rules subcommands) | Git operations only |

The skill does NOT execute downloaded code, make network requests,
install packages, or fetch remote content. All operations are
local filesystem and git operations.
