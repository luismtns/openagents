---
name: openagents-skills
description: |
  Skill manager for the OpenAgents ecosystem.
  Searches known skill repositories (mattpocock, anthropic, proyecto26,
  vercel-labs) for available skills, lists currently installed skills, and
  installs or removes skills on demand. Integrates with skills.sh, Claude
  plugins, and direct GitHub sources.
  Use when you want to discover, install, or remove AI coding agent skills.
  Triggers: openagents skills, manage skills, install skill, search skills,
  list skills, remove skill.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(ln:*), Bash(rm:*), Bash(cp:*), Bash(ls:*), Bash(echo:*), Bash(test:*), Bash(npx:*), Bash(mkdir:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, skills, manager, search, install]
---

# openagents:skills

## Overview

Search, install, and remove AI coding agent skills from known registries and GitHub.

## Known repositories

| Source | Repo | Format |
|--------|------|--------|
| mattpocock | `github.com/mattpocock/skills` | SKILL.md |
| anthropic | `github.com/anthropics/skills` | SKILL.md |
| proyecto26 (system-design) | `github.com/proyecto26/system-design-skills` | SKILL.md |
| vercel-labs | `github.com/vercel-labs/agent-skills` | SKILL.md |
| skills.sh | Any repo via `npx skills add` | SKILL.md |

## Actions

### `search` — Find skills

```markdown
Search query: <keyword>

Results:
| source | skill | description |
|--------|-------|-------------|
| mattpocock | diagnose | Debugging and diagnosis workflow |
| mattpocock | tdd | Test-driven development loop |
```

Search known repos via their GitHub API or local clone cache.

### `list` — Show installed

Show all skills currently in `~/.agents/skills/` and project-local skill dirs.

### `install` — Add a skill

Source can be:

| Source format | Example |
|---------------|---------|
| GitHub shorthand | `mattpocock/skills:diagnose` |
| Full git URL | `https://github.com/mattpocock/skills.git` |
| Local path | `/path/to/skills` |
| skills.sh | `npx skills add owner/repo` |

Steps:
1. Clone or fetch source repo into temp dir
2. Copy the skill directory to `~/.agents/skills/<name>/`
3. Verify frontmatter and required fields
4. Report success

### `remove` — Delete a skill

1. List installed skills
2. Confirm removal with user
3. `rm -rf ~/.agents/skills/<name>/`
4. Remove any project-local symlinks

## Notes

- Always ask for confirmation before installing or removing
- Check for name conflicts before installing
- Prefer symlinks over copies when the source is local
- Use `npx skills` when available for general-purpose installs
