# openagents uninstall

Remove the openagents skill from the agent ecosystem. The skill is
distributed via [skills.sh](https://skills.sh/luismtns/openagents) and
installed with `npx skills add`.

## Standard uninstall

| Scope | Command |
|-------|---------|
| Global | `npx skills remove openagents --global --yes` |
| Project | `npx skills remove openagents --yes` |
| Both | Run both commands above |

Global removal cleans `~/.agents/skills/openagents/` and all agent symlinks.
Project removal cleans `project/.agents/skills/openagents/`.

## Manual cleanup

If `npx skills remove` is unavailable:

- Delete `~/.agents/skills/openagents/`
- Remove agent-specific symlinks (`~/.cursor/skills/openagents`, etc.)
- Stale lock file entries in `~/.agents/.skill-lock.json` are safe to ignore

## Post-uninstall project cleanup

Remove project artifacts separately:

- Run `openagents rm all` inside the project directory
- Or manually delete `.agents/` and `AGENTS.md`

These are project-level files and are not removed by `npx skills remove`.

## Note

The skill cannot uninstall itself programmatically — it's loaded and
running. This subcommand provides instructions for the user to execute.
