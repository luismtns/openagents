---
name: openagents-rm
description: |
  Remove project-level artifacts created by OpenAgents subcommands.
  Mirrors the creation side of init, add, and global. Supports
  removing rules, AGENTS.md, individual skills, all artifacts, or
  just agent symlinks. Never removes files outside the current project
  directory. Use when the user says "rm", "remove", "delete",
  "clean up", or "remove rules/skills". Part of the OpenAgents
  multi-agent orchestration suite.
allowed-tools: Read Write Glob Grep Bash(test:*) Bash(echo:*)
  Bash(rm:*) Bash(ls:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents rm

Remove project-level artifacts created by openagents subcommands.
Mirrors the creation side of `init`, `add`, and `global`.

## Subcommands

| Command | Action |
|---------|--------|
| `openagents rm rules` | Remove `.agents/rules/` and agent symlinks |
| `openagents rm agents` | Remove `AGENTS.md` |
| `openagents rm skill <name>` | Remove `skills/<name>/` and its `skills.sh.json` entry |
| `openagents rm all` | Remove everything openagents created |
| `openagents rm symlinks` | Remove agent-specific symlinks only |

## Details

**Rules** -- deletes `.agents/rules/` and any agent symlinks
(`.claude/rules`, `.cursor/rules`, `.zed/rules`).

**AGENTS.md** -- deletes the file.

**Skill** -- deletes `skills/<name>/` and removes the entry from
`skills.sh.json` (filtering out empty groups).

**All** -- runs all of the above plus cleans up any remaining `.agents/`
artifacts.

## Safety

- All destructive operations ask for confirmation before proceeding
- Never removes files outside the current project directory
- `openagents rm all` does not touch `~/.agents/` -- use `openagents uninstall` for global cleanup