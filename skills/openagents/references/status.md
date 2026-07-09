# openagents (default)

## 1. Detect agent

Detect via env vars -> config dirs -> binaries (first match wins). The
detection matrix is in the openagents SKILL.md -- read on demand.

## 2. Status check

Per detected/installed agent, verify skill **and** rules are linked to the
canonical source (unified multi-agent setup), plus repo state:

```bash
test -f ~/.agents/skills/openagents/SKILL.md && echo "global skill: installed" || echo "global skill: MISSING"
for a in claude cursor zed; do
  test -L ~/.${a}/skills/openagents && echo "$a: skill linked" || echo "$a: skill NOT linked"
  test -L ~/.${a}/rules && echo "$a: rules linked" || echo "$a: rules NOT linked"
done
echo "Repo: $(basename $(pwd))"
test -f AGENTS.md && echo "AGENTS.md: present" || echo "AGENTS.md: missing"
ls .agents/rules/*.md 2>/dev/null | awk '{print NR, $0}'
for a in claude cursor zed; do test -L ".$a/rules" && echo "$a rules: linked" || echo "$a rules: NOT linked"; done
for a in enablement coding review; do test -L ".claude/skills/openagents-$a" && echo "openagents-$a: linked" || echo "openagents-$a: NOT linked"; done
```

Agents that auto-discover `~/.agents/` (opencode, codex, cline, gemini,
warp, amp, ...) need no symlink.

## 3. Available commands

| Invocation | Action |
|------------|--------|
| `openagents` / `openagents status` | This status (default) |
| `openagents global` | Agent detection + handshake + symlinks |
| `openagents init` | Scaffold AGENTS.md + .agents/rules/ |
| `openagents add` | Create and register new skills or rules |
| `openagents rules` | Deep codebase analysis -> generate rules |
| `openagents rm <rules|agents|skill <name>|symlinks|all>` | Remove project artifacts |
| `openagents doctor` | Diagnose and repair broken setup |
| `openagents info` | Show version, agents, distribution channels |
| `openagents upgrade` | Update openagents to latest version |
| `openagents uninstall` | Remove openagents skill globally |

## 4. Next steps

- **skill MISSING** -> `npx skills add luismtns/openagents`
- **no AGENTS.md** -> `openagents init`
- **skill NOT linked** (cursor/zed) -> `openagents global`
- **rules NOT linked** -> `openagents global` (global) or `openagents init` / `openagents rules` (project)
- **symlinks broken** -> `openagents doctor`
- **all green** -> unified setup is healthy, no action needed