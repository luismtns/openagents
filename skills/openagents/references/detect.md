# openagents detect

Canonical multi-signal agent detection. Used by `status`, `global`, and
`init`. Strategy: env vars → config dirs → binaries (first match wins).

| Agent | Env var / Config dir | Binary | Skill path | Rules path |
|-------|---------------------|--------|------------|------------|
| opencode | `OPENCODE_CALLER` / `~/.config/opencode/` | `opencode` | auto | auto (`~/.agents/rules/`) |
| claude-code | `CLAUDE_CODE_SSE_PORT` / `~/.claude/` | `claude` | auto | auto (`~/.claude/rules/`) |
| cursor | `CURSOR_TRACE_ID` / `~/.cursor/` | `cursor` | symlink | symlink (`.cursor/rules`) |
| codex | `CODEX_CONFIG_DIR` / `~/.codex/` | `codex` | auto | auto (`~/.agents/rules/`) |
| cline | `CLINE_CONFIG_DIR` / `~/.clinerules` | `cline` | auto | auto (`~/.agents/rules/`) |
| zed | `ZED_CONFIG_DIR` / `~/.zed/` | `zed` | symlink | symlink (`.zed/rules`) |
| gemini-cli | `GEMINI_API_KEY` / `~/.gemini/` | `gemini` | auto | auto (`~/.agents/rules/`) |
| antigravity | `~/.antigravity/` | `antigravity` | auto | auto (`~/.agents/rules/`) |
| deepagents | `~/.deepagents/` | `deepagents` | auto | auto (`~/.agents/rules/`) |
| github-copilot | — | `github-copilot` | auto | per integration |
| kimi-code-cli | `~/.kimi/` | `kimi` | auto | auto (`~/.agents/rules/`) |
| mimocode | `~/.mimocode/` | `mimo` | plugin | plugin |
| warp | `~/.warp/` | `warp` | auto | auto (`~/.agents/rules/`) |
| amp | `~/.amp/` | `amp` | auto | auto (`~/.agents/rules/`) |

Agents that don't auto-discover `~/.agents/skills/` get a symlink from their
skill path to `~/.agents/skills/openagents` (see `global.md` handshake).
The same applies to rules: agents that don't auto-discover `~/.agents/rules/`
get a symlink from their native rules path to the canonical `.agents/rules/`
(project) or `~/.agents/rules/` (global).
