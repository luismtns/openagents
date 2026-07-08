# openagents:global

Agent-agnostic handshake and ecosystem verification.

Detects the running AI coding agent, maps its configuration paths, and
ensures the multi-agent ecosystem is operational across all agents
supported by the skills.sh ecosystem.

## Agent detection

Read these signals in order of reliability. Use the `detect_agent` function
from the multi-signal strategy below.

### Known agents in the skills.sh ecosystem

| Agent | Env var | Config dir | Binary | Process | Skill auto-discover |
|-------|---------|------------|--------|---------|-------------------|
| opencode | `OPENCODE_CALLER` / `OPENCODE_CONFIG_DIR` | `~/.config/opencode/` | `opencode` | `opencode` | auto |
| claude-code | `CLAUDE_CODE_SSE_PORT` / `CLAUDE_CODE_CONFIG_DIR` | `~/.claude/` | `claude` | `claude` | auto |
| cursor | `CURSOR_TRACE_ID` / `CURSOR_CONFIG_DIR` | `~/.cursor/` | `cursor` | `cursor` | symlink needed |
| codex | `CODEX_CONFIG_DIR` | `~/.codex/` | `codex` | `codex` | auto |
| cline | `CLINE_CONFIG_DIR` | `~/.clinerules` (file) or `~/.cline/` | `cline` | `cline` | auto |
| zed | `ZED_CONFIG_DIR` | `~/.zed/` | `zed` | `zed` | symlink needed |
| antigravity | — | `~/.antigravity/` | `antigravity` | `antigravity` | auto |
| deepagents | — | `~/.deepagents/` | `deepagents` | `deepagents` | auto |
| gemini-cli | `GEMINI_API_KEY` | `~/.gemini/` | `gemini` | `gemini` | auto |
| github-copilot | — | — | `github-copilot` | `github-copilot` | auto |
| kimi-code-cli | — | `~/.kimi/` | `kimi` | `kimi` | auto |
| mimocode | — | `~/.mimocode/` | `mimo` | `mimo` | auto |
| warp | — | `~/.warp/` | `warp` | `warp` | auto |
| amp | — | `~/.amp/` | `amp` | `amp` | auto |

## Handshake steps

### 1. Detect

Use multi-signal detection: env vars → running processes → config dirs → binaries.
Report all signals found, not just the first match.

```bash
detect_agent() {
  # Phase 1: Env vars (strongest signal — proves agent is actively running)
  [ -n "$OPENCODE_CALLER$OPENCODE_CONFIG_DIR" ] && { echo "opencode (env)"; return; }
  [ -n "$CLAUDE_CODE_SSE_PORT$CLAUDE_CODE_CONFIG_DIR" ] && { echo "claude-code (env)"; return; }
  [ -n "$CURSOR_TRACE_ID$CURSOR_CONFIG_DIR" ] && { echo "cursor (env)"; return; }
  [ -n "$CODEX_CONFIG_DIR" ] && { echo "codex (env)"; return; }
  [ -n "$CLINE_CONFIG_DIR" ] && { echo "cline (env)"; return; }
  [ -n "$ZED_CONFIG_DIR" ] && { echo "zed (env)"; return; }
  [ -n "$GEMINI_API_KEY" ] && { echo "gemini-cli (env)"; return; }

  # Phase 2: Running processes (active but may not have env vars)
  for proc in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo; do
    ps aux 2>/dev/null | grep -v grep | grep -qi "$proc" && { echo "$proc (process)"; return; }
  done

  # Phase 3: Config directories (agent installed but may not be running)
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

  # Phase 4: Available binaries (installed but never configured)
  for bin in opencode claude cursor codex cline zed antigravity deepagents gemini kimi warp mimo amp; do
    command -v "$bin" &>/dev/null && { echo "$bin (binary)"; return; }
  done

  echo "unknown"
}
AGENT=$(detect_agent)
```

### 2. Map paths

Each agent discovers skills differently. Define the path map:

| Agent | Skill discovery path | Config format |
|-------|---------------------|---------------|
| opencode | `~/.agents/skills/` (auto) | `opencode.jsonc` |
| claude-code | `~/.agents/skills/` (auto) | `CLAUDE.md` |
| cursor | `~/.cursor/skills/` (symlink required) | `~/.cursor/rules/` |
| codex | `~/.agents/skills/` (auto) | `CODEX.md` |
| cline | `~/.agents/skills/` (auto) | `~/.clinerules` |
| zed | `~/.zed/skills/` (symlink required) | `~/.zed/settings.json` |
| antigravity | `~/.agents/skills/` (auto) | — |
| deepagents | `~/.agents/skills/` (auto) | — |
| gemini-cli | `~/.agents/skills/` (auto) | — |
| github-copilot | `~/.agents/skills/` (auto) | — |
| kimi-code-cli | `~/.agents/skills/` (auto) | — |
| mimocode | `~/.local/share/mimocode/` (plugin-based) | — |
| warp | `~/.agents/skills/` (auto) | — |
| amp | `~/.agents/skills/` (auto) | — |

### 3. Verify

Check that `~/.agents/skills/openagents/SKILL.md` exists and is readable.

For agents that don't auto-discover `~/.agents/skills/` (cursor, zed), create
symlinks:

```bash
mkdir -p ~/.cursor/skills
ln -sfn ~/.agents/skills/openagents ~/.cursor/skills/openagents
mkdir -p ~/.zed/skills
ln -sfn ~/.agents/skills/openagents ~/.zed/skills/openagents
```

Also check all installed skills:

```bash
echo "Installed skills:"
ls ~/.agents/skills/ 2>/dev/null || echo "  (none)"
```

### 4. Report

Summarize detected agent, paths, and status. Format:

```
Agent: opencode (env)
  Config: ~/.config/opencode/
  Config format: opencode.jsonc
  Skill path: ~/.agents/skills/ (auto)
  Skill status: installed

Other agents detected on this system:
  - claude-code (env): ~/.claude/
  - cursor (binary): /usr/bin/cursor
  - mimocode (config): ~/.mimocode/

Repo: /home/user/project
  AGENTS.md: present
  .agents/rules: present

Ecosystem: healthy
```

If the ecosystem is healthy, report ready. If not, diagnose the missing piece.

## Routing note

All subcommands accept two equivalent forms:
- `openagents:<subcommand>` (colon syntax — opencode convention)
- `openagents <subcommand>` (space syntax — natural language)

Both invoke the same workflow. The bare `openagents` (no subcommand) always
runs the default status check in [status.md](status.md).
