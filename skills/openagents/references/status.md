# openagents (default)

Default workflow for `openagents` (no subcommand) or `openagents status`.

## 1. Detect agent

Detect via env vars → config dirs → binaries (first match wins). Full matrix:
[references/detect.md](references/detect.md).

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

All subcommands — not just the recommended ones:

| Command | Action |
|---------|--------|
| `openagents` | This status (default) |
| `openagents status` | Same as above |
| `openagents global` | Agent detection + handshake + symlinks |
| `openagents init` | Scaffold `AGENTS.md` + `.agents/rules/` |
| `openagents add` | Create and register new skills or rules |
| `openagents rules` | Deep codebase analysis → generate rules |
| `openagents rm rules` | Remove `.agents/rules/` + symlinks |
| `openagents rm agents` | Remove `AGENTS.md` |
| `openagents rm skill <name>` | Remove `skills/<name>/` + `skills.sh.json` entry |
| `openagents rm symlinks` | Remove agent-specific symlinks only |
| `openagents rm all` | Remove everything openagents created (project only) |
| `openagents uninstall` | Remove the openagents skill (scoped, defensive) |

## 5. Next steps

- **skill MISSING** → `npx skills add luismtns/openagents`
- **no AGENTS.md** → `openagents init`
- **symlinks missing** → `openagents global`
- **all green** → no action needed