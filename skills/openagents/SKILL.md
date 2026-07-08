---
name: openagents
description: |
  Multi-agent workflow orchestration for AI coding agents.
  Handles agent detection and handshake, project initialization,
  skill creation and registration, and deep codebase analysis
  for rule generation.
  Use when setting up multi-agent, initializing projects,
  creating skills or rules, or generating project rules.
  Triggers: openagents, openagents status, openagents global,
    openagents init, openagents add, openagents rules,
    openagents rm, openagents uninstall,
    configure agents, check agents, verify setup,
    init project, project setup, analyze project,
    generate rules, refresh rules, create skill, add skill,
    remove skill, delete skill, remove rules, delete rules,
    register skill, package skill, detect agent, agent status,
    multi-agent setup, ecosystem check, uninstall, cleanup,
    remove openagents, delete openagents.
    Use `openagents` (bare) to show agent status and available commands.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(mkdir:*),
  Bash(ln:*), Bash(test:*), Bash(uname:*), Bash(echo:*),
  Bash(pwd:*), Bash(ls:*), Bash(find:*)
version: 1.11.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline, zed,
  antigravity, deepagents, gemini-cli, github-copilot,
  kimi-code-cli, mimocode, warp, amp
tags: [openagents, multi-agent, orchestration, setup, init, rules, skills]
---

# openagents

Multi-agent workflow orchestration for AI coding agents.

Load this skill, then route to the right subcommand:

| Invocation | Read | When |
|------------|------|------|
| `openagents` / `openagents status` | [references/status.md](references/status.md) | Default — show agent status, repo status, and available commands |
| `openagents global` | [references/global.md](references/global.md) | Detect agent, verify global multi-agent setup, handshake |
| `openagents init` | [references/init.md](references/init.md) | Scaffold project AGENTS.md and rules |
| `openagents add` | [references/add.md](references/add.md) | Create new skills or rules in multi-agent context |
| `openagents rules` | [references/rules.md](references/rules.md) | Deep codebase analysis for rule generation |
| `openagents rm` | [references/rm.md](references/rm.md) | Remove rules, skills, AGENTS.md, or all project artifacts |
| `openagents uninstall` | [references/uninstall.md](references/uninstall.md) | Uninstall the openagents skill via npx skills remove |

## Invocation

Use space-separated subcommands: `openagents <subcommand>`.
This works in all agents (opencode, claude-code, cursor, codex, etc.).

The bare `openagents` (no subcommand) always runs the default status
workflow in [references/status.md](references/status.md).

## How it works

The skill detects which AI coding agent is running using a multi-signal
strategy (env vars → config dirs → binaries), covering all
agents in the skills.sh ecosystem. It adapts configuration paths
accordingly and orchestrates multi-agent workflows. No agent-specific
config is shipped — the skill reads your environment and adjusts.

## Unified multi-agent setup

The core promise of openagents: **any repo or machine has one unified
setup of skills and rules, shared by every AI agent you use.** The skill
treats `.agents/` (project) and `~/.agents/` (machine-global) as the
**canonical source** and symlinks them into each agent's native path, so
skills **and** rules are identical no matter which agent you open. Agents
that auto-discover `~/.agents/` need no action; agents that don't (cursor,
zed, …) get symlinks created by `openagents global` / `init` / `rules`.
See [references/detect.md](references/detect.md) for the per-agent
`skill_path` and `rules_path` matrix.

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
