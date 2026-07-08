# OpenAgents

Multi-agent workflow orchestration for AI coding agents.

OpenAgents is a **distributable skill pack** that configures your AI coding agent for multi-agent workflows. It provides project analysis, rule generation, skill synchronization, and ecosystem auditing — all through self-contained, agent-agnostic skills.

## Installation

```bash
# Via skills.sh (any agent)
npx skills add luismtns/openagents

# Via Claude Code plugin
/plugin install openagents@luismtns/openagents

# Manual: clone + symlink into your global skills
git clone https://github.com/luismtns/openagents.git
ln -sfn $(pwd)/openagents/skills/* ~/.agents/skills/
```

## Skills

| Command | Purpose |
|---------|---------|
| `/openagents:install` | One-time global setup: structure, configs, manifest |
| `/openagents:init` | Per-project init: analyze repo, create AGENTS.md |
| `/openagents:setup-rules` | Deep analysis + grill-me + rule generation |
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

All skills are stored in `~/.agents/skills/` — the universal global location read by most agents.

## Quick Start

```bash
# 1. Install the skills
npx skills add luismtns/openagents

# 2. Run global setup (one-time)
/openagents:install

# 3. Initialize your project
cd my-project
/openagents:init
```

## License

MIT
