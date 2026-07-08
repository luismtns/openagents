# openagents uninstall

Remove **only** the openagents skill — defensive by design, never touches
other skills. Only paths whose basename is exactly `openagents` are in scope:

| Path | Type |
|------|------|
| `~/.agents/skills/openagents` | Skill directory (real) |
| `~/.claude/skills/openagents` | Symlink |
| `~/.cursor/skills/openagents` | Symlink |
| `~/.zed/skills/openagents` | Symlink |
| `~/.agents/.skill-lock.json` → `openagents` | Lock entry |

## Standard uninstall (recommended)

```bash
npx skills remove openagents --global --yes   # global
npx skills remove openagents --yes             # project
```

`npx skills remove` targets by name, so it removes only openagents.

## Manual cleanup (scoped, with guard)

Never use `scripts/clean.sh` for this — it is a separate global nuke that
removes ALL skills. Guard every step: remove only basename `openagents`.

```bash
# Real skill dir
test "$(basename ~/.agents/skills/openagents)" = "openagents" && rm -rf ~/.agents/skills/openagents
# Agent symlinks (openagents-named only)
for a in claude cursor zed; do
  link=~/.${a}/skills/openagents
  test -L "$link" && test "$(basename "$link")" = "openagents" && rm -f "$link"
done
# Lock entry: delete the "openagents" object under "skills" in ~/.agents/.skill-lock.json
```

## Final step — restart your agent

The skill is loaded in the current session and cannot uninstall itself
programmatically. After running the commands above, **restart your AI agent**
(close/reopen the session or restart the CLI/IDE) for the change to take effect.
