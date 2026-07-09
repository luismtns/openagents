---
name: openagents-init
description: |
  Scaffold a new project with AGENTS.md, .agents/rules/, and per-agent
  symlinks. Detects language and framework from project files, generates
  a project AGENTS.md with conventions and build/test/lint commands,
  creates .agents/rules/, and symlinks into each agent's native path.
  Use when the user says "init", "setup project", "scaffold",
  "initialize multi-agent", or when .agents/ or AGENTS.md is missing.
  Part of the OpenAgents multi-agent orchestration suite.
allowed-tools: Read Write Glob Grep Bash(mkdir:*) Bash(ln:*)
  Bash(test:*) Bash(echo:*) Bash(ls:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents init

Per-project scaffolding for OpenAgents. Generates `AGENTS.md`, sets up
`.agents/rules/`, and creates agent symlinks.

## Detection

Read project root files to detect:
- **Language** -- `*.py`, `*.go`, `*.rs`, `package.json`
- **Framework** -- inspect `package.json` deps (next, react, vue, etc.)
- **Package manager** -- lockfile (`pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`)

## Generate AGENTS.md

Write `AGENTS.md` with this structure, then append conventions and
architecture sections:

```markdown
<!-- openagents -->
# <project>
<description>

## Agent instructions
- Language: <lang> | Framework: <fw> | PM: <pm>
- Build: `<cmd>` | Test: `<cmd>` | Lint: `<cmd>`
```

## Rules directory

Create `.agents/rules/` with an initial rule file containing build, test,
lint commands and project conventions.

## Symlink

Make the canonical project rules visible to every agent you use. For agents
that don't auto-discover `.agents/rules/`, symlink their native rules path:

```bash
for a in claude cursor zed; do
  mkdir -p ".$a"
  ln -sfn ../.agents/rules ".$a/rules"
done
```

This realizes the unified multi-agent setup: one `.agents/rules/` source,
mirrored into each agent's path so skills and rules are identical everywhere.