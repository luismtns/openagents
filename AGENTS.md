<!-- openagents -->
# OpenAgents Skill Suite

A multi-skill orchestration suite for AI coding agents. Each subcommand is
an independent, discoverable skill.

Install via `npx skills add luismtns/openagents` and load with:

```
skill({ name: "openagents-<name>" })
```

## Skills

| Invocation | Skill name | Use case |
|------------|-----------|----------|
| `openagents` | `openagents` | Show agent status, repo health, available commands |
| `openagents-global` | `openagents-global` | Detect agent, handshake, verify global multi-agent setup |
| `openagents-init` | `openagents-init` | Scaffold project AGENTS.md and rules |
| `openagents-add` | `openagents-add` | Create new skills or rules in multi-agent context |
| `openagents-rules` | `openagents-rules` | Deep codebase analysis for rule generation |
| `openagents-rm` | `openagents-rm` | Remove rules, skills, AGENTS.md, or all project artifacts |
| `openagents-doctor` | `openagents-doctor` | Diagnose and repair broken setup |
| `openagents-info` | `openagents-info` | Show version, detected agents, distribution channels |
| `openagents-upgrade` | `openagents-upgrade` | Update openagents to latest version |
| `openagents-uninstall` | `openagents-uninstall` | Uninstall the openagents skill globally |

Agent-agnostic: opencode, claude-code, cursor, codex, cline, zed,
antigravity, deepagents, gemini-cli, github-copilot,
kimi-code-cli, mimocode, warp, amp.

## Project rules (`.agents/rules/`)

- `validate.md` — pre-release validation checklist
- `distributed-skills.md` — naming, frontmatter, and layout conventions

Rules are agent-agnostic in `.agents/rules/` and symlinked from `.claude/rules/`.