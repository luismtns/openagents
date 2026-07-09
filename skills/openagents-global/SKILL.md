---
name: openagents-global
description: |
  Detect the running AI coding agent, handshake with the multi-agent
  ecosystem, verify global skills and rules at ~/.agents/, and symlink
  into agent-specific paths. Use when the user says "global", "handshake",
  "detect agent", "verify setup", "multi-agent check", or "sync agents".
  Part of the OpenAgents multi-agent orchestration suite.
allowed-tools: Read Write Glob Grep Bash(mkdir:*) Bash(ln:*)
  Bash(test:*) Bash(uname:*) Bash(echo:*) Bash(pwd:*) Bash(ls:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents global

Agent-agnostic handshake and ecosystem verification.

## Agent detection

Multi-signal strategy (env vars -> config dirs -> binaries, first match wins).
<!-- Matrix sync: update both openagents/SKILL.md and openagents-global/SKILL.md when adding agents -->
The detection matrix is defined in `openagents` hub; read it on demand.

| Agent | Env / Config | Binary | Auto-discovers |
|-------|-------------|--------|----------------|
| opencode | `OPENCODE_CALLER` / `~/.config/opencode/` | `opencode` | Yes |
| claude-code | `CLAUDE_CODE_SSE_PORT` / `~/.claude/` | `claude` | Yes |
| cursor | `CURSOR_TRACE_ID` / `~/.cursor/` | `cursor` | No (symlink) |
| codex | `CODEX_CONFIG_DIR` / `~/.codex/` | `codex` | Yes |
| cline | `CLINE_CONFIG_DIR` / `~/.clinerules` | `cline` | Yes |
| zed | `ZED_CONFIG_DIR` / `~/.zed/` | `zed` | No (symlink) |
| gemini-cli | `GEMINI_API_KEY` / `~/.gemini/` | `gemini` | Yes |
| antigravity | `~/.antigravity/` | `antigravity` | Yes |
| deepagents | `~/.deepagents/` | `deepagents` | Yes |
| github-copilot | -- | `github-copilot` | Varies |
| kimi-code-cli | `~/.kimi/` | `kimi` | Yes |
| mimocode | `~/.mimocode/` | `mimo` | Plugin |
| warp | `~/.warp/` | `warp` | Yes |
| amp | `~/.amp/` | `amp` | Yes |

## Handshake

**1. Detect** -- check env vars first, then `test -d ~/.config/<agent>`, then `command -v <binary>`.

**2. Verify skill** -- `test -f ~/.agents/skills/openagents/SKILL.md`

**3. Create symlinks** -- for every agent that doesn't auto-discover
`~/.agents/`, mirror the canonical source into its native path.
Symlink all openagents-* skills so every subcommand is discoverable:

Skills:
```bash
mkdir -p ~/.cursor/skills ~/.zed/skills
for d in ~/.agents/skills/openagents*; do
  [ -e "$d" ] || [ -L "$d" ] && ln -sfn "$d" ~/.cursor/skills/$(basename "$d")
  [ -e "$d" ] || [ -L "$d" ] && ln -sfn "$d" ~/.zed/skills/$(basename "$d")
done
```

Rules (global, unified across agents):
```bash
mkdir -p ~/.cursor && ln -sfn ~/.agents/rules ~/.cursor/rules
mkdir -p ~/.zed && ln -sfn ~/.agents/rules ~/.zed/rules
```

Only create links for installed/detected agents. Targets are the canonical
`~/.agents/skills/openagents` and `~/.agents/rules` (basename-guarded), so no
other skills or rules are ever touched.

**4. Report**:
```
Agent: opencode (env: OPENCODE_CALLER)
Config: ~/.config/opencode/ (opencode.jsonc)
Skill: ~/.agents/skills/openagents/SKILL.md -- installed
Others: claude-code (dir), cursor (binary)
Repo: myproject -- AGENTS.md (present), .agents/rules (N rules)
Rules synced: claude ✓ cursor ✗ zed ✗  (run `openagents global` / `openagents init` to link)
Ecosystem: healthy
```