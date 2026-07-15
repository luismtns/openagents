---
name: openagents-doctor
description: |
  Read-only diagnostics for OpenAgents and cross-agent handoff readiness.
  Reports PASS, WARN, FAIL, or UNKNOWN with evidence and safe manual steps.
  Use when the user says "doctor", requests diagnostics, or a handoff cannot
  be exported. It never repairs, installs, deletes, or rewrites configuration.
allowed-tools: Read Glob Grep Bash(command -v claude) Bash(command -v codex) Bash(command -v opencode) Bash(git rev-parse --abbrev-ref HEAD) Bash(git rev-parse --short HEAD) Bash(git --no-optional-locks -c core.fsmonitor=false status --short) Bash(pwd) Bash(uname)
version: 2.0.0
author: Luis Bovo
license: MIT
user-invocable: true
tags: [openagents, diagnostics, read-only]
---

# openagents doctor

Read [references/checks.md](references/checks.md), execute only applicable
read-only checks, and cite the observed evidence.

## Report format

```text
OpenAgents Doctor
Project: <name>
[PASS|WARN|FAIL|UNKNOWN] <check> -- <evidence>
Summary: <counts>
Manual next steps: <commands or documentation; do not execute>
```

Never classify an arbitrary symlink as healthy without resolving and comparing
its target. Never read environment values, credentials, or private Git remotes.
