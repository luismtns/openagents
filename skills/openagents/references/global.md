# openagents global

Agent-agnostic handshake and ecosystem verification.

## Agent detection

Check in order: env vars → config dirs → binaries (first match wins).

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

## Handshake

**1. Detect** — check env vars first, then `test -d ~/.config/<agent>`, then `command -v <binary>`.

**2. Verify skill** — `test -f ~/.agents/skills/openagents/SKILL.md`

**3. Create symlinks** (for cursor, zed):

```bash
mkdir -p ~/.cursor/skills && ln -sfn ~/.agents/skills/openagents ~/.cursor/skills/openagents
mkdir -p ~/.zed/skills && ln -sfn ~/.agents/skills/openagents ~/.zed/skills/openagents
```

**4. Report** — format:

```
Agent: opencode (env: OPENCODE_CALLER)
Config: ~/.config/opencode/ (opencode.jsonc)
Skill: ~/.agents/skills/openagents/SKILL.md — installed
Others: claude-code (dir), cursor (binary)
Repo: myproject — AGENTS.md (present), .agents/rules (3 rules)
Ecosystem: healthy
```