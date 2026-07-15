---
name: openagents
description: |
  Read-only hub for cross-agent work continuity. Reports observable project
  state and routes to portable handoff or diagnostics. Use when the user says
  "openagents", asks what OpenAgents can do, or wants a concise local status.
allowed-tools: Read Glob Grep Bash(command -v claude) Bash(command -v codex) Bash(command -v opencode) Bash(git rev-parse --abbrev-ref HEAD) Bash(git rev-parse --short HEAD) Bash(git --no-optional-locks -c core.fsmonitor=false status --short) Bash(pwd)
version: 1.12.0
author: Luis Bovo
license: MIT
user-invocable: true
tags: [openagents, cross-agent, handoff, diagnostics]
---

# openagents

OpenAgents carries operational context between coding agents. It does not
install, synchronize, repair, update, or remove agent configuration.

## Default workflow

1. Read [references/status.md](references/status.md).
2. Report only facts observable in the current workspace.
3. Label ambiguous agent signals as `UNKNOWN`, never as confirmed identity.
4. Recommend one of the two focused skills when relevant.

## Skills

| Skill | Use |
|-------|-----|
| `openagents-handoff` | Create portable continuation context or explicitly export it to another agent |
| `openagents-doctor` | Run read-only diagnostics and report evidence-backed remediation steps |

## Capability constraints

- Read-only tools only.
- No package execution, network requests, writes, symlinks, or repairs.
- A config directory or binary means "observed", not "currently running".
- Markdown portability is not the same as verified agent integration.
