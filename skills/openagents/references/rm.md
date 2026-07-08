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

**Rules** — deletes `.agents/rules/` and any agent symlinks
(`.claude/rules`, `.cursor/rules`, `.zed/rules`).

**AGENTS.md** — deletes the file.

**Skill** — deletes `skills/<name>/` and removes the entry from
`skills.sh.json` (filtering out empty groups).

**All** — runs all of the above plus cleans up any remaining `.agents/`
artifacts.

## Safety

- All destructive operations ask for confirmation before proceeding
- Never removes files outside the current project directory
- `openagents rm all` does not touch `~/.agents/` — use `openagents uninstall` for global cleanup
