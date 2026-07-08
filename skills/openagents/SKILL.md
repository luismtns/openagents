---
name: openagents
description: |
  Manages the OpenAgents multi-agent ecosystem on the current machine
  and across projects. Detects the running agent, configures agent-specific
  settings for multi-agent compatibility, initializes projects with AGENTS.md,
  runs deep analysis for rule generation, synchronizes skills across machines,
  audits the ecosystem, and manages skill discovery and installation.
  Use when setting up, configuring, auditing, or maintaining the OpenAgents
  ecosystem on any machine or project.
  Triggers: openagents setup, openagents init, openagents rules,
    openagents sync, openagents audit, openagents skills,
    configure agents, check agents, verify setup, init project,
    project setup, analyze project, generate rules, refresh rules,
    sync skills, update skills, sync project, audit skills,
    check skills, inventory, manage skills, install skill,
    search skills, remove skill.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(mkdir:*),
  Bash(ln:*), Bash(cp:*), Bash(test:*), Bash(uname:*), Bash(echo:*),
  Bash(pwd:*), Bash(npm:*), Bash(cargo:*), Bash(go:*), Bash(python3:*),
  Bash(ls:*), Bash(find:*), Bash(wc:*), Bash(rm:*), Bash(diff:*),
  Bash(du:*), Bash(cat:*), Bash(npx:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline, zed
tags: [openagents, setup, init, rules, sync, audit, skills]
---

# openagents

A distributable skill pack for multi-agent workflow orchestration.

## Routing

When the user invokes a subcommand, load the corresponding reference file and follow its instructions.

| Invocation | Read |
|------------|------|
| `openagents:setup` / `openagents setup` | [references/setup.md](references/setup.md) |
| `openagents:init` / `openagents init` | [references/init.md](references/init.md) |
| `openagents:rules` / `openagents rules` | [references/rules.md](references/rules.md) |
| `openagents:sync` / `openagents sync` | [references/sync.md](references/sync.md) |
| `openagents:audit` / `openagents audit` | [references/audit.md](references/audit.md) |
| `openagents:skills` / `openagents skills` | [references/skills.md](references/skills.md) |
