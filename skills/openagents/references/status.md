# openagents (default)

Default workflow when `openagents` is invoked without a subcommand.
Shows contextual agent + repo status, available commands, and next steps.

Both `openagents` and `openagents:status` trigger this workflow.

## 1. Detect primary agent

Multi-signal strategy: env vars → processes → config dirs → binaries.

```bash
detect_agent() {
  [ -n "$OPENCODE_CALLER$OPENCODE_CONFIG_DIR" ] && { echo "opencode (env)"; return; }
  [ -n "$CLAUDE_CODE_SSE_PORT$CLAUDE_CODE_CONFIG_DIR" ] && { echo "claude-code (env)"; return; }
  [ -n "$CURSOR_TRACE_ID$CURSOR_CONFIG_DIR" ] && { echo "cursor (env)"; return; }
  [ -n "$CODEX_CONFIG_DIR" ] && { echo "codex (env)"; return; }
  [ -n "$CLINE_CONFIG_DIR" ] && { echo "cline (env)"; return; }
  [ -n "$ZED_CONFIG_DIR" ] && { echo "zed (env)"; return; }
  [ -n "$GEMINI_API_KEY" ] && { echo "gemini-cli (env)"; return; }
  for proc in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo; do
    ps aux 2>/dev/null | grep -v grep | grep -qi "$proc" && { echo "$proc (process)"; return; }
  done
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
  [ -d ~/.kimi ] && { echo "kimi-code-cli (config)"; return; }
  [ -d ~/.amp ] && { echo "amp (config)"; return; }
  [ -d ~/.warp ] && { echo "warp (config)"; return; }
  for bin in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo amp; do
    command -v "$bin" &>/dev/null && { echo "$bin (binary)"; return; }
  done
  echo "unknown"
}
AGENT=$(detect_agent)

# Build list of agents actually present on this system
detected_agents() {
  local list=""
  for d in ~/.config/opencode ~/.claude ~/.cursor ~/.codex ~/.cline ~/.zed ~/.mimocode ~/.antigravity ~/.deepagents ~/.gemini ~/.kimi ~/.amp ~/.warp; do
    if [ -e "$d" ]; then
      name=$(basename "$d")
      name="${name#.}"      # strip leading dot from hidden dirs
      list="$list $name"
    fi
  done
  echo "$list"
}
AGENTS_PRESENT=$(detected_agents)
```

## 2. Check global ecosystem

```bash
REPO_NAME=$(basename "$(pwd)")
echo "Agent: $AGENT"
echo "Global ecosystem:"
test -f ~/.agents/skills/openagents/SKILL.md \
  && echo "- openagents skill: installed" \
  || echo "- openagents skill: MISSING"

# Only check symlinks for agents actually present
for a in $AGENTS_PRESENT; do
  case "$a" in
    cursor)
      test -L ~/.cursor/skills/openagents \
        && echo "- cursor symlink: present" \
        || echo "- cursor symlink: missing"
      ;;
    zed)
      test -L ~/.zed/skills/openagents \
        && echo "- zed symlink: present" \
        || echo "- zed symlink: missing"
      ;;
  esac
done

echo "- Skills: $(ls ~/.agents/skills/ 2>/dev/null | tr '\n' ' ')"
```

## 3. Check repo status

```bash
echo "Repo status ($REPO_NAME):"
test -f AGENTS.md \
  && echo "- AGENTS.md: present" \
  || echo "- AGENTS.md: missing (run openagents:init)"
if [ -d .agents/rules ]; then
  RULES_COUNT=$(ls .agents/rules/*.md 2>/dev/null | wc -l)
  echo "- Rules dir: present ($RULES_COUNT rules)"
else
  echo "- Rules dir: missing (run openagents:init)"
fi
test -L .claude/rules \
  && echo "- Claude rules: present" \
  || echo "- Claude rules: not found"
```

## 4. Suggest next steps

```bash
echo "Next steps:"
echo "- openagents:global — full handshake + create missing symlinks"
echo "- openagents:add — create new skills or rules"
echo "- openagents:rules — deep codebase analysis to refresh rules"
echo "- openagents:rm — remove rules, skills, or project artifacts"
echo "- openagents:uninstall — remove openagents skill"
```

## Routing note

All subcommands accept two equivalent forms:
- `openagents:<subcommand>` (colon syntax)
- `openagents <subcommand>` (space syntax)

The bare `openagents` (no subcommand) always runs this default status check.
