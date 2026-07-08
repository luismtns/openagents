# openagents:global

Agent-agnostic handshake and ecosystem verification.

Detects the running AI coding agent, maps its configuration paths, and
ensures the multi-agent ecosystem is operational.

## Agent detection

Read these signals in order. The first match wins.

| Signal | Where to check | opencode | claude-code | codex | cursor | cline | zed |
|--------|---------------|----------|-------------|-------|--------|-------|-----|
| Env var | `$AGENT_*` or tool-specific | `OPENCODE_*` | `CLAUDE_CODE*` | `CODEX_*` | `CURSOR_*` | `CLINE_*` | `ZED_*` |
| Config dir | `~/.config/<tool>/` | `~/.config/opencode/` | `~/.claude/` | `~/.codex/` | `~/.cursor/` | `~/.clinerules` | `~/.zed/` |
| Process | `ps aux \| grep <tool>` | `opencode` | `claude` | `codex` | `cursor` | `cline` | `zed` |
| Skill path | `~/.agents/skills/` | auto | auto | auto | `~/.cursor/skills/` | auto | `~/.zed/skills/` |

## Handshake steps

### 1. Detect

```bash
if [ -n "$OPENCODE_CONFIG_DIR" ]; then
  AGENT=opencode
elif [ -n "$CLAUDE_CODE_CONFIG_DIR" ]; then
  AGENT=claude-code
elif command -v cursor &>/dev/null; then
  AGENT=cursor
elif [ -d ~/.codex ]; then
  AGENT=codex
elif [ -f ~/.clinerules ]; then
  AGENT=cline
elif [ -d ~/.zed ]; then
  AGENT=zed
else
  AGENT=unknown
fi
```

### 2. Map paths

| Agent | Skill discovery path | Config format |
|-------|---------------------|---------------|
| opencode | `~/.agents/skills/` (auto) | `opencode.jsonc` |
| claude-code | `~/.agents/skills/` (auto) | `CLAUDE.md` |
| codex | `~/.agents/skills/` (auto) | `CODEX.md` |
| cursor | `~/.cursor/skills/` (symlink) | `~/.cursor/rules/` |
| cline | `~/.agents/skills/` (auto) | `~/.clinerules` |
| zed | `~/.zed/skills/` (symlink) | `~/.zed/settings.json` |

### 3. Verify

Check that `~/.agents/skills/openagents/SKILL.md` exists and is readable.

For agents that don't auto-discover `~/.agents/skills/` (cursor, zed), create
symlinks:

```bash
mkdir -p ~/.cursor/skills
ln -sfn ~/.agents/skills/openagents ~/.cursor/skills/openagents
```

### 4. Report

Summarize detected agent, paths, and status. If the ecosystem is healthy,
report ready. If not, diagnose the missing piece.
