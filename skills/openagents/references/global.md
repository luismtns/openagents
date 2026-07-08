# openagents global

Agent-agnostic handshake and ecosystem verification.

## Agent detection

Multi-signal strategy (env vars → config dirs → binaries, first match wins).
The full matrix lives in [references/detect.md](references/detect.md) — read
it on demand; do not duplicate it here.

## Handshake

**1. Detect** — check env vars first, then `test -d ~/.config/<agent>`, then `command -v <binary>`.

**2. Verify skill** — `test -f ~/.agents/skills/openagents/SKILL.md`

**3. Create symlinks** — for every agent that doesn't auto-discover
`~/.agents/`, mirror the canonical source into its native path. This is what
makes the setup unified across all your agents.

Skills:

```bash
mkdir -p ~/.cursor/skills && ln -sfn ~/.agents/skills/openagents ~/.cursor/skills/openagents
mkdir -p ~/.zed/skills && ln -sfn ~/.agents/skills/openagents ~/.zed/skills/openagents
```

Rules (global, unified across agents):

```bash
mkdir -p ~/.cursor && ln -sfn ~/.agents/rules ~/.cursor/rules
mkdir -p ~/.zed && ln -sfn ~/.agents/rules ~/.zed/rules
```

Only create links for installed/detected agents. Targets are the canonical
`~/.agents/skills/openagents` and `~/.agents/rules` (basename-guarded), so no
other skills or rules are ever touched.

**4. Report** — format:

```
Agent: opencode (env: OPENCODE_CALLER)
Config: ~/.config/opencode/ (opencode.jsonc)
Skill: ~/.agents/skills/openagents/SKILL.md — installed
Others: claude-code (dir), cursor (binary)
Repo: myproject — AGENTS.md (present), .agents/rules (N rules)
Rules synced: claude ✓ cursor ✗ zed ✗  (run `openagents global` / `init` to link)
Ecosystem: healthy
```