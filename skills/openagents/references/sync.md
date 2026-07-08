# openagents:sync

## Overview

Detects and resolves drift between global skills (`~/.agents/skills/`) and project-local skills (`.opencode/skills/`, `.claude/skills/`).

## Scan

Check these locations for skill directories:

| Scope | Paths |
|-------|-------|
| Global | `~/.agents/skills/*/` |
| Project (opencode) | `.opencode/skills/*/` |
| Project (claude) | `.claude/skills/*/` |
| Project (agents) | `.agents/skills/*/` |

## Comparison

For each skill found in any location, compare:

1. **Version** — from `version` field in SKILL.md frontmatter
2. **Modified date** — file modification timestamp
3. **Content hash** — SHA256 of SKILL.md body (optional)

Report the sync state:

| State | Meaning |
|-------|---------|
| `LATEST` | Version and content match global |
| `OUTDATED` | Project version is behind global |
| `NEW_LOCAL` | Skill exists locally but not globally |
| `ORPHANED` | Skill exists locally but removed from global |
| `MODIFIED` | Local has uncommitted changes vs global |

## Workflow

1. Scan all locations
2. Report summary to user
3. For each OUTDATED skill: show version diff, ask to update
4. For each ORPHANED skill: ask to remove
5. For each NEW_LOCAL skill: ask to promote to global
6. Apply confirmations

## Update types

**Symlinked skills** — replace symlink target (simplest, most common)
**Copied skills** — overwrite with incoming version, preserve local modifications if user chooses
**Orphaned** — `rm -rf .opencode/skills/<orphan>/` after confirmation
