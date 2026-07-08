# openagents global

Agent-agnostic handshake and ecosystem verification.

## Agent detection

Multi-signal strategy (env vars → config dirs → binaries, first match wins).
The full matrix lives in [references/detect.md](references/detect.md) — read
it on demand; do not duplicate it here.

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