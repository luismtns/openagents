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
  Bash(ln:*), Bash(cp:*), Bash(test:*), Bash(uname:*), Bash(echo:*),
  Bash(pwd:*), Bash(npx:*), Bash(ls:*), Bash(find:*), Bash(wc:*),
  Bash(rm:*), Bash(diff:*), Bash(du:*), Bash(cat:*), Bash(npm:*)
version: 1.3.0
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
| `openagents:global` / `openagents global` | [references/global.md](references/global.md) | Detect agent, handshake, verify global setup |
| `openagents:init` / `openagents init` | [references/init.md](references/init.md) | Scaffold project, generate AGENTS.md |
| `openagents:add` / `openagents add` | [references/add.md](references/add.md) | Create skills, rules, register distribution |
| `openagents:rules` / `openagents rules` | [references/rules.md](references/rules.md) | Deep codebase analysis, generate rules |

## How it works

The skill detects which AI coding agent is running, adapts configuration
paths accordingly, and orchestrates multi-agent workflows across your
ecosystem. No agent-specific config is shipped — the skill reads your
environment and adjusts.
