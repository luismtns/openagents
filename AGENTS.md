<!-- openagents -->
# OpenAgents Skill Pack

A single skill with built-in subcommands for multi-agent workflow orchestration.
Install via `npx skills add luismtns/openagents` and load with:

```
skill({ name: "openagents" })
```

Route to the right subcommand:

| Subcommand | Use case |
|------------|----------|
| `openagents` / `openagents status` | Default — show agent status, repo status, and available commands |
| `openagents global` | Detect agent, handshake, verify global multi-agent setup |
| `openagents init` | Scaffold project AGENTS.md and rules |
| `openagents add` | Create new skills or rules in multi-agent context |
| `openagents rules` | Deep codebase analysis for rule generation |
| `openagents rm` | Remove rules, skills, AGENTS.md, or all project artifacts |
| `openagents uninstall` | Uninstall the openagents skill via npx skills remove |

Agent-agnostic: opencode, claude-code, cursor, codex, cline, zed,
antigravity, deepagents, gemini-cli, github-copilot,
kimi-code-cli, mimocode, warp, amp.

## Project rules (`.agents/rules/`)

- `validate.md` — pre-release validation checklist
- `distributed-skills.md` — naming, frontmatter, and layout conventions

Rules are agent-agnostic in `.agents/rules/` and symlinked from `.claude/rules/`.
<!-- openagents -->
