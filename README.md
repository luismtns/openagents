<h1 align="center">
  <img src="assets/logo.gif" alt="OpenAgents">
</h1>

[![skills.sh](https://skills.sh/b/luismtns/openagents)](https://skills.sh/luismtns/openagents)
[![validate](https://github.com/luismtns/openagents/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/validate.yml)
[![release](https://github.com/luismtns/openagents/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/publish.yml)
[![GitHub release](https://img.shields.io/github/v/release/luismtns/openagents)](https://github.com/luismtns/openagents/releases/latest)

Multi-agent workflow orchestration for AI coding agents.

OpenAgents is a **distributable skill pack** that configures your AI coding agent for multi-agent workflows. It provides project analysis, rule generation, skill synchronization, and ecosystem auditing. Self-contained and agent-agnostic.

## Installation

The skills are distributed via any skill manager:

```bash
# Via skills.sh (recommended)
npx skills add luismtns/openagents

# Via Claude Code plugin
/plugin install openagents@luismtns/openagents
```

Once installed, run the setup skill in your AI coding agent:

```bash
/openagents:setup     # verify and configure agents for multi-agent standard
/openagents:init      # initialize a project
/openagents:rules     # deep analysis + generate project rules
```

## Skills

| Command | Purpose |
|---------|---------|
| `/openagents:setup` | Verify and configure agents for multi-agent standard |
| `/openagents:init` | Per-project init: analyze repo, create AGENTS.md |
| `/openagents:rules` | Deep analysis + grill-me + rule generation |
| `/openagents:sync` | Synchronize global ↔ project skills |
| `/openagents:audit` | Audit the skills ecosystem |
| `/openagents:skills` | Search, install, and manage skills |

## Agent Compatibility

OpenAgents works with any AI coding agent that supports the [Agent Skills](https://skills.sh) standard:

| Agent | Auto-discovery path |
|-------|-------------------|
| OpenCode | `~/.config/opencode/skills/` or `~/.agents/skills/` |
| Claude Code | `~/.claude/skills/` or `~/.agents/skills/` |
| Codex | `~/.codex/skills/` or `~/.agents/skills/` |
| Cursor | `~/.cursor/skills/` or `~/.agents/skills/` |
| Cline | `~/.agents/skills/` |
| Zed | `~/.agents/skills/` |

## License

MIT
