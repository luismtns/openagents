---
name: openagents-audit
description: |
  Comprehensive audit of the entire skills ecosystem on the current machine.
  Scans all skill locations (global, per-project, per-agent), reports each skill's
  name, path, version, author, line count, and origin. Identifies duplicates,
  conflicts, overly large skills, and skills missing required frontmatter fields.
  Use when reviewing the health of your skills installation or before cleanup.
  Triggers: openagents audit, audit skills, check skills, inventory.
allowed-tools: Read, Glob, Grep, Bash(ls:*), Bash(echo:*), Bash(wc:*), Bash(find:*), Bash(test:*), Bash(du:*), Bash(cat:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, audit, skills, list, review]
---

# openagents:audit

## Overview

Produces a complete inventory of all installed skills across all locations, with health checks.

## Scan locations

Search these directories for `skills/*/SKILL.md`:

- `~/.agents/skills/`
- `~/.config/opencode/skills/`
- `~/.claude/skills/`
- `~/.codex/skills/`
- `~/.cursor/skills/`
- `.opencode/skills/` (project)
- `.claude/skills/` (project)
- `.agents/skills/` (project)
- `~/.config/opencode/agents/` (agent files)

Also check for rule files:
- `~/.config/opencode/AGENTS.md`
- `~/.claude/CLAUDE.md`
- `.opencode/AGENTS.md`
- `.claude/CLAUDE.md`
- `.claude/rules/`

## Report

Present a structured report:

### Summary
```
Skills found:    <N>
Locations:      <global, project, agent>
Total size:     <N> KB across <N> files
```

### Per-skill table

| skill | path | v | author | lines | health |
|-------|------|---|--------|-------|--------|
| openagents-install | ~/.agents/skills/ | 1.0.0 | Luis Bovo | 87 | PASS |
| obsolete-skill | .claude/skills/ | — | — | 320 | FAIL |

### Health checks

| Check | Description |
|-------|-------------|
| `name` | Matches directory name, kebab-case |
| `description` | Present, has "Use when" pattern |
| `allowed-tools` | Present, Bash scoped |
| `version` | Present, valid semver |
| `author` | Present |
| `license` | Present |
| Size | Under 200 lines (progressive disclosure) |
| Duplicates | Same skill name in multiple locations |

### Recommendations

- Remove orphaned skills
- Update outdated skills (suggest running `/openagents:sync`)
- Split oversized skills into references/
- Merge duplicate skills
