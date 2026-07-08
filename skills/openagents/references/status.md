# openagents (default)

Default workflow for `openagents` (no subcommand) or `openagents status`.

## 1. Detect agent

Check env vars first, then config dirs, then binaries:

| Signal | Agent |
|--------|-------|
| `OPENCODE_CALLER` / `~/.config/opencode/` | opencode |
| `CLAUDE_CODE_SSE_PORT` / `~/.claude/` | claude-code |
| `CURSOR_TRACE_ID` / `~/.cursor/` | cursor |
| `CODEX_CONFIG_DIR` / `~/.codex/` | codex |
| `CLINE_CONFIG_DIR` / `~/.clinerules` | cline |
| `ZED_CONFIG_DIR` / `~/.zed/` | zed |
| `GEMINI_API_KEY` / `~/.gemini/` | gemini-cli |
| `~/.mimocode/` | mimocode |
| `command -v opencode` | opencode (binary) |
| `command -v claude` | claude-code (binary) |

## 2. Ecosystem check

```bash
test -f ~/.agents/skills/openagents/SKILL.md && echo "installed" || echo "MISSING"
test -L ~/.cursor/skills/openagents && echo "cursor: linked" || echo "cursor: not linked"
test -L ~/.zed/skills/openagents && echo "zed: linked" || echo "zed: not linked"
```

## 3. Repo status

```bash
echo "Repo: $(basename $(pwd))"
test -f AGENTS.md && echo "AGENTS.md: present" || echo "AGENTS.md: missing"
ls .agents/rules/*.md 2>/dev/null | awk '{print NR, $0}'
test -L .claude/rules && echo "Claude rules: linked" || echo "Claude rules: not linked"
```

## 4. Available commands

| Command | Action |
|---------|--------|
| `openagents` | This status |
| `openagents global` | Handshake + symlinks |
| `openagents init` | Scaffold project |
| `openagents add` | Create new skills |
| `openagents rules` | Deep analysis |
| `openagents rm` | Remove artifacts |
| `openagents uninstall` | Remove skill |

## 5. Next steps

- **skill MISSING** → `npx skills add luismtns/openagents`
- **no AGENTS.md** → `openagents init`
- **symlinks missing** → `openagents global`
- **all green** → no action needed