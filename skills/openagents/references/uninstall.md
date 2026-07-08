# openagents:uninstall

Remove the openagents skill from the agent ecosystem.
Uses the standard `npx skills remove` workflow.

## Standard uninstall

The openagents skill is distributed via [skills.sh](https://skills.sh/luismtns/openagents)
and installed with `npx skills add`. The standard uninstall uses the same tool:

### Global install (recommended)

```bash
npx skills remove openagents --global --yes
```

Removes from `~/.agents/skills/openagents/` and all agent-specific symlinks.

### Project-level install

```bash
npx skills remove openagents --yes
```

Removes from `project/.agents/skills/openagents/`.

### Remove from all locations

```bash
npx skills remove openagents --global --yes    # ~/.agents/skills/
npx skills remove openagents --yes             # ./.agents/skills/
```

## Manual cleanup

If `npx skills remove` is unavailable, clean up manually:

```bash
# Remove skill directory
rm -rf ~/.agents/skills/openagents

# Remove agent-specific symlinks
rm -f ~/.cursor/skills/openagents 2>/dev/null
rm -f ~/.zed/skills/openagents 2>/dev/null

# Check if lock file needs updating
# ~/.agents/.skill-lock.json will have a stale entry — safe to ignore
```

## Post-uninstall project cleanup

After uninstalling the skill, you may also want to remove project artifacts:

```bash
openagents:rm all
```

Or manually:
```bash
rm -rf .agents
rm -f AGENTS.md
```

These are project-level files and are not removed by `npx skills remove`.

## Note

The skill cannot uninstall itself programmatically — it's loaded and running.
The `uninstall` subcommand provides instructions for the user to execute.
