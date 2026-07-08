---
name: openagents-rules
description: |
  Deep analysis of the current project for comprehensive rule generation.
  Scans the entire codebase, reads configuration files, identifies architecture
  patterns and conventions, runs the grill-me protocol to validate understanding
  with the user, and generates or updates all project-level agent rules and skills.
  Also suggests simplification or removal of obsolete rules.
  Use when a project needs thorough rule coverage or existing rules are stale.
  Triggers: openagents rules, analyze project, generate rules, refresh rules.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(npm:*), Bash(cargo:*), Bash(python3:*), Bash(go:*), Bash(ls:*), Bash(test:*), Bash(find:*), Bash(echo:*), Bash(wc:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, rules, analysis, grill-me, architecture]
---

# openagents:rules

## Overview

Generates or refreshes project-level agent rules by deep analysis of the codebase combined with user validation via the grill-me pattern.

## Phase 1: Scan

Use parallel subagents (via `Task`) to scan multiple areas:

| Area | What to extract |
|------|----------------|
| **Source tree** | Language, framework, entry points, module boundaries |
| **Config files** | TSConfig, ESLint, Prettier, Tailwind, Docker, CI workflows, Makefile |
| **Dependencies** | Key libraries, runtime versions, peer dependencies |
| **Testing** | Test framework, coverage config, test patterns, mocks |
| **Docs** | README, CONTRIBUTING, ADRs, architecture docs |
| **Existing rules** | Current AGENTS.md, CLAUDE.md, `.cursor/rules/`, `.claude/rules/` |
| **Git history** | Branch strategy, commit conventions, PR templates |

## Phase 2: Grill-me

Ask the user sequentially:

1. What is this project's primary purpose?
2. What architecture patterns are in use (layered, hexagonal, feature-based)?
3. What are the critical code paths a new agent must understand?
4. Are there security-sensitive areas or deployment requirements?
5. What conventions are not obvious from the code (naming, error handling, logging)?
6. What should agents NEVER do in this project?

## Phase 3: Generate

Create/update project rules in this priority order:

1. `.opencode/AGENTS.md` — primary project instructions
2. `.claude/CLAUDE.md` — Claude Code compatibility (if detected)
3. `.opencode/skills/<project-topic>/SKILL.md` — project-specific skills if needed
4. `.github/copilot-instructions.md` — GitHub Copilot (if relevant)

Each rule file should contain:
- Project identity and architecture
- Exact build/test/lint/typecheck commands
- Directory structure with purpose annotations
- Code conventions with examples
- Agent behavior rules (dos and don'ts)

## Phase 4: Audit existing rules

For each existing rule file and skill found:

| Question | Action |
|----------|--------|
| Is it still accurate? | Keep or update |
| Is it redundant with another file? | Merge and remove |
| Does it duplicate what the agent can infer? | Remove |
| Has its project context changed? | Rewrite |

Present a summary of changes and let the user confirm before writing.
