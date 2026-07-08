---
name: openagents-init
description: |
  Per-project initialization of the OpenAgents ecosystem.
  Scans the current repository for language, framework, package manager, and
  project structure, then generates project-level AGENTS.md (or CLAUDE.md for
  compatibility) with relevant conventions, build commands, and architecture notes.
  Use when starting work on a new or unfamiliar project.
  Triggers: openagents init, init project, project setup.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(npm:*), Bash(cargo:*), Bash(go:*), Bash(python3:*), Bash(ls:*), Bash(echo:*), Bash(test:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, init, project, setup]
---

# openagents:init

## Overview

Scans the current project repository and bootstraps a project-level AGENTS.md with conventions, commands, and architecture notes.

## Detection

Read key files to determine project characteristics:

| File | What it reveals |
|------|----------------|
| `package.json` | Node.js, npm/bun/yarn, scripts, dependencies |
| `Cargo.toml` | Rust, cargo commands |
| `pyproject.toml` | Python, ruff/poetry/pdm, test commands |
| `go.mod` | Go module, build commands |
| `composer.json` | PHP, Laravel/Symfony |
| `Gemfile` | Ruby, Rails |
| `Makefile` | Custom build targets |
| `Dockerfile` | Container setup |
| `.github/workflows/` | CI pipeline commands |

## Workflow

1. **Scan** — Read project root for indicator files, read `README.md` if present
2. **Question** — Ask user:
   - Project type (library, app, monorepo, service)
   - Build/test/lint commands if not auto-detectable
   - Architecture conventions (layers, patterns)
   - Any existing documentation to reference
3. **Generate** — Create `.opencode/AGENTS.md` (primary) and/or `.claude/CLAUDE.md` (compatibility):
   - Project identity and tech stack
   - Build/test/lint commands with exact syntax
   - Directory structure map
   - Coding conventions
   - Architecture decisions
4. **Recommend** — Suggest relevant global skills for this project type
5. **Verify** — Run a build or test command to confirm accuracy

## Output template

```markdown
# <project> — <type>

Tech stack: <language>, <framework>, <package-manager>

## Commands
- Build: `<command>`
- Test: `<command>`
- Lint: `<command>`
- Typecheck: `<command>`

## Structure
- `<dir>` — <purpose>
- `<dir>` — <purpose>

## Conventions
- <convention 1>
- <convention 2>
```

## Notes

- Never overwrite an existing AGENTS.md without showing a diff first
- Preserve any pre-existing instructions, append new ones
- Use `/init` as a lighter alternative when full OpenAgents setup is not needed
