# openagents (default)

Default workflow when `openagents` is invoked without a subcommand.
Shows global agent + repo status, available commands, and next steps.

Both `openagents` and `openagents:status` trigger this workflow.

## 1. Detect agent

Use a multi-signal strategy: env vars → running processes → config dirs → binaries.
Report **all** signals found, not just the first match.

```bash
detect_agent() {
  # --- Phase 1: Env vars (strongest signal) ---
  [ -n "$OPENCODE_CALLER$OPENCODE_CONFIG_DIR" ] && { echo "opencode (env)"; return; }
  [ -n "$CLAUDE_CODE_SSE_PORT$CLAUDE_CODE_CONFIG_DIR" ] && { echo "claude-code (env)"; return; }
  [ -n "$CURSOR_TRACE_ID$CURSOR_CONFIG_DIR" ] && { echo "cursor (env)"; return; }
  [ -n "$CODEX_CONFIG_DIR" ] && { echo "codex (env)"; return; }
  [ -n "$CLINE_CONFIG_DIR" ] && { echo "cline (env)"; return; }
  [ -n "$ZED_CONFIG_DIR" ] && { echo "zed (env)"; return; }
  [ -n "$GEMINI_API_KEY" ] && { echo "gemini-cli (env)"; return; }

  # --- Phase 2: Running processes ---
  for proc in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo; do
    ps aux 2>/dev/null | grep -v grep | grep -qi "$proc" && { echo "$proc (process)"; return; }
  done

  # --- Phase 3: Config directories ---
  [ -d ~/.config/opencode ] && { echo "opencode (config)"; return; }
  [ -d ~/.claude ] && { echo "claude-code (config)"; return; }
  [ -f ~/.clinerules ] && { echo "cline (config)"; return; }
  [ -d ~/.cursor ] && { echo "cursor (config)"; return; }
  [ -d ~/.zed ] && { echo "zed (config)"; return; }
  [ -d ~/.mimocode ] && { echo "mimocode (config)"; return; }
  [ -d ~/.codex ] && { echo "codex (config)"; return; }
  [ -d ~/.antigravity ] && { echo "antigravity (config)"; return; }
  [ -d ~/.deepagents ] && { echo "deepagents (config)"; return; }
  [ -d ~/.gemini ] && { echo "gemini-cli (config)"; return; }

  # --- Phase 4: Available binaries ---
  for bin in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo; do
    command -v "$bin" &>/dev/null && { echo "$bin (binary)"; return; }
  done

  echo "unknown"
}
AGENT=$(detect_agent)
```

## 2. Check global ecosystem

| Check | How |
|-------|-----|
| Skill installed | `test -f ~/.agents/skills/openagents/SKILL.md` |
| Symlinks | `test -L ~/.cursor/skills/openagents` or `test -L ~/.zed/skills/openagents` |
| All installed agents | `ls ~/.agents/skills/ 2>/dev/null` |

```bash
echo "=== Agent ==="
echo "Detected: $AGENT"

echo ""
echo "=== Global ecosystem ==="
test -f ~/.agents/skills/openagents/SKILL.md \
  && echo "  openagents skill: installed" \
  || echo "  openagents skill: MISSING"
test -L ~/.cursor/skills/openagents \
  && echo "  cursor symlink: present" \
  || echo "  cursor symlink: missing (run openagents:global)"
test -L ~/.zed/skills/openagents \
  && echo "  zed symlink: present" \
  || echo "  zed symlink: missing (run openagents:global)"
echo "  Skills installed: $(ls ~/.agents/skills/ 2>/dev/null | tr '\n' ' ')"
```

## 3. Check repo status

| Check | How |
|-------|-----|
| AGENTS.md exists | `test -f AGENTS.md` |
| Rules directory | `test -d .agents/rules` |
| Agent rules symlink | `test -L .claude/rules` or equivalent |

```bash
echo "=== Repo status ==="
test -f AGENTS.md \
  && echo "  AGENTS.md: present" \
  || echo "  AGENTS.md: missing (run openagents:init)"
test -d .agents/rules \
  && echo "  Rules dir: present" \
  || echo "  Rules dir: missing (run openagents:init)"
```

## 4. List available subcommands

| Command | Description |
|---------|-------------|
| `openagents` / `openagents status` | Default — show agent status, repo status, and available commands |
| `openagents:global` / `openagents global` | Full handshake and ecosystem verification |
| `openagents:init` / `openagents init` | Scaffold project AGENTS.md and rules |
| `openagents:add` / `openagents add` | Create new skills or rules |
| `openagents:rules` / `openagents rules` | Deep codebase analysis for rule generation |

## 5. Suggest next steps

Based on status:

- **Agent unknown** → at least one agent config dir or binary was found — inspect manually
- **Global skill missing** → reinstall with `npx skills add luismtns/openagents`
- **No AGENTS.md** → run `openagents:init`
- **Rules outdated** → run `openagents:rules`
- **Symlinks missing** → run `openagents:global` to create them
- **All green** → run `openagents:global` for full handshake

## Routing note

All subcommands accept two equivalent forms:
- `openagents:<subcommand>` (colon syntax — opencode convention)
- `openagents <subcommand>` (space syntax — natural language)

Both invoke the same workflow. The bare `openagents` (no subcommand) always
runs this default status check.
