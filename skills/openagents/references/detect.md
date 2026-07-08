# openagents detect

Canonical multi-signal agent detection. Used by `status`, `global`, and
`init`. Strategy: env vars → config dirs → binaries (first match wins).

| Agent | Env var / Config dir | Binary | Skill path |
|-------|---------------------|--------|------------|
| opencode | `OPENCODE_CALLER` / `~/.config/opencode/` | `opencode` | auto |
| claude-code | `CLAUDE_CODE_SSE_PORT` / `~/.claude/` | `claude` | auto |
| cursor | `CURSOR_TRACE_ID` / `~/.cursor/` | `cursor` | symlink |
| codex | `CODEX_CONFIG_DIR` / `~/.codex/` | `codex` | auto |
| cline | `CLINE_CONFIG_DIR` / `~/.clinerules` | `cline` | auto |
| zed | `ZED_CONFIG_DIR` / `~/.zed/` | `zed` | symlink |
| gemini-cli | `GEMINI_API_KEY` / `~/.gemini/` | `gemini` | auto |
| antigravity | `~/.antigravity/` | `antigravity` | auto |
| deepagents | `~/.deepagents/` | `deepagents` | auto |
| github-copilot | — | `github-copilot` | auto |
| kimi-code-cli | `~/.kimi/` | `kimi` | auto |
| mimocode | `~/.mimocode/` | `mimo` | plugin |
| warp | `~/.warp/` | `warp` | auto |
| amp | `~/.amp/` | `amp` | auto |

Agents that don't auto-discover `~/.agents/skills/` get a symlink from their
skill path to `~/.agents/skills/openagents` (see `global.md` handshake).
