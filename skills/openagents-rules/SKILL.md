---
name: openagents-rules
description: |
  Deep codebase analysis that extracts real architecture and conventions,
  then generates generic, positive rules for .agents/rules/. Produces
  three files: conventions.md, architecture.md, and generation.md.
  Use when the user says "rules", "generate rules", "analyze project",
  "create rules", "codebase analysis", "project analysis", or
  "refresh rules". Part of the OpenAgents multi-agent orchestration suite.
allowed-tools: Read Write Glob Grep Bash(test:*) Bash(echo:*)
  Bash(mkdir:*) Bash(ln:*) Bash(pwd:*) Bash(ls:*) Bash(find:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents rules

Deep codebase analysis that extracts real architecture and conventions,
then generates generic, positive rules -- never hardcoded paths, never
prohibitive tone. Output is three `.agents/rules/` files.

Workflow (read each on demand):

1. **Sanity + extract** -> read [references/scan.md](references/scan.md) **before starting**
2. **Generate** -> read [references/generate.md](references/generate.md) after scan completes
3. **Validate with user + write** -> read [references/validate.md](references/validate.md) before writing

## Safety

- If the project is too minimal, abort gracefully and suggest `openagents-init`.
- Every rule is generic (pattern, not path), positive, and verifiable.
- Agent expects rules at a different path -> symlink: `ln -sfn ../.agents/rules .claude/rules`