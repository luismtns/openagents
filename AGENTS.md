<!-- openagents -->
# OpenAgents Skill Pack

A single skill with built-in subcommands for multi-agent workflow orchestration.
Available from [skills.sh/luismtns/openagents](https://skills.sh/luismtns/openagents). Load with:

```
skill({ name: "openagents" })
```

Then route to the right subcommand:

| Subcommand | Use case |
|------------|----------|
| `openagents:global` | Detect agent, handshake, verify global multi-agent setup |
| `openagents:init` | Scaffold project AGENTS.md and rules |
| `openagents:add` | Create new skills or rules in multi-agent context |
| `openagents:rules` | Deep codebase analysis for rule generation |

Agent-agnostic: opencode, claude-code, cursor, codex, cline, zed.

## Project rules (`.agents/rules/`)

- `validate.md` — pre-release validation checklist
- `distributed-skills.md` — naming, frontmatter, and layout conventions

Rules are agent-agnostic in `.agents/rules/` and symlinked from `.claude/rules/`.
<!-- openagents -->
