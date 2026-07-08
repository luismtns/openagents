<h1 align="center">
  <img src="assets/logo.gif" alt="OpenAgents">
</h1>

[![skills.sh](https://skills.sh/b/luismtns/openagents)](https://skills.sh/luismtns/openagents)
[![validate](https://github.com/luismtns/openagents/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/validate.yml)
[![release](https://github.com/luismtns/openagents/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/publish.yml)
[![GitHub release](https://img.shields.io/github/v/release/luismtns/openagents)](https://github.com/luismtns/openagents/releases/latest)
[![Socket](https://img.shields.io/badge/Socket-Pass-brightgreen?logo=socketdotio)](https://www.skills.sh/luismtns/openagents/openagents/security/socket)
[![Snyk](https://img.shields.io/badge/Snyk-Medium-yellow?logo=snyk)](https://www.skills.sh/luismtns/openagents/openagents/security/snyk)

Multi-agent workflow orchestration for AI coding agents.

A single distributable skill that detects your agent, adapts to it, and
orchestrates multi-agent workflows across your ecosystem.

## How it works

```mermaid
flowchart TD
    U["you: setup multi-agent"] -->|trigger| S["skill(name: openagents)"]
    U2["you: init project"] -->|trigger| S
    U3["you: create a skill"] -->|trigger| S
    U4["you: analyze the project"] -->|trigger| S
    U5["you: check status"] -->|trigger| S
    U6["you: remove artifacts"] -->|trigger| S

    S -->|routes to| R["SKILL.md router"]

    R -->|status| ST["references/status.md"]
    R -->|global| G["references/global.md"]
    R -->|init| I["references/init.md"]
    R -->|add| A["references/add.md"]
    R -->|rules| RL["references/rules.md"]
    R -->|rm| RM["references/rm.md"]
    R -->|uninstall| UI["references/uninstall.md"]

    G --> D{"detect agent"}
    D -->|opencode| OC["~/.config/opencode/"]
    D -->|claude-code| CC["~/.claude/"]
    D -->|codex| CX["~/.codex/"]
    D -->|cursor| CR["~/.cursor/skills/"]
    D -->|cline| CL["~/.clinerules"]
    D -->|zed| ZD["~/.zed/"]
    D -->|mimocode| MC["~/.mimocode/"]
    D -->|antigravity| AG["~/.antigravity/"]
    D -->|deepagents| DA["~/.deepagents/"]
    D -->|gemini-cli| GC["~/.gemini/"]
    D -->|github-copilot| GH["~/.github-copilot/"]
    D -->|kimi-code-cli| KI["~/.kimi/"]
    D -->|warp| WP["~/.warp/"]
    D -->|amp| AP["~/.amp/"]

    I --> L["detect language"]
    L --> GEN["write AGENTS.md"]
    GEN --> RD["create .agents/rules/"]

    A --> SC["scaffold SKILL.md"]
    SC --> REG["register in skills.sh.json"]

    RL --> SN["scan codebase"]
    SN --> P["identify patterns"]
    P --> GR["generate rules"]
    GR --> V["validate with user"]
```

## Installation

```bash
npx skills add luismtns/openagents
```

Then load in any AI coding agent:

```
skill({ name: "openagents" })
```

## Subcommands

| Subcommand | What it does | When to use |
|------------|-------------|-------------|
| `openagents` / `openagents status` | Shows agent status, repo status, available commands, and next steps | Default entry point, checking current setup |
| `openagents:global` | Detects the running agent, maps config paths, verifies the multi-agent ecosystem | First-time setup, checking agent configurations |
| `openagents:init` | Generates AGENTS.md, detects language/framework, creates `.agents/rules/` | Starting a new project, onboarding |
| `openagents:add` | Scaffolds new skills, registers distribution, validates structure | Creating a new skill or rule pack |
| `openagents:rules` | Deep codebase scan, pattern identification, rule generation | When a project needs thorough rule coverage |
| `openagents:rm` | Removes rules, skills, AGENTS.md, symlinks, or all project artifacts | Cleaning up project scaffolding |
| `openagents:uninstall` | Uninstalls the openagents skill via `npx skills remove` | Removing the skill from your ecosystem |

## Agent compatibility

| Agent | Skill discovery | Auto-discover `~/.agents/skills/` |
|-------|----------------|-----------------------------------|
| opencode | `~/.agents/skills/` | Yes |
| claude-code | `~/.agents/skills/` | Yes |
| codex | `~/.agents/skills/` | Yes |
| cursor | `~/.cursor/skills/` (symlink) | No |
| cline | `~/.agents/skills/` | Yes |
| zed | `~/.zed/skills/` (symlink) | No |
| antigravity | `~/.agents/skills/` | Yes |
| deepagents | `~/.agents/skills/` | Yes |
| gemini-cli | `~/.agents/skills/` | Yes |
| github-copilot | `~/.agents/skills/` | Yes |
| kimi-code-cli | `~/.agents/skills/` | Yes |
| mimocode | `~/.local/share/mimocode/` (plugin-based) | No |
| warp | `~/.agents/skills/` | Yes |
| amp | `~/.agents/skills/` | Yes |

## Project structure

```
skills/openagents/
├── SKILL.md                  # Unified frontmatter + routing table
└── references/
    ├── status.md             # Default status workflow
    ├── global.md             # Agent-agnostic handshake protocol
    ├── init.md               # Project scaffolding
    ├── add.md                # Skill/rules creation
    ├── rules.md              # Deep analysis + rule generation
    ├── rm.md                 # Remove project artifacts
    └── uninstall.md          # Uninstall guidance

.agents/rules/
├── validate.md               # Pre-release validation
└── distributed-skills.md     # Naming and layout conventions

scripts/
├── validate.sh               # Local CI validator
└── clean.sh                  # Global skill cleanup

AGENTS.md                     # Root-level skill pack description
CHANGELOG.md                  # Version history
skills.sh.json                # skills.sh distribution config
```

## Development

```bash
# Validate locally
bash scripts/validate.sh

# Full cleanup (removes all global skills, npm/npx cache)
bash scripts/clean.sh

# Reinstall after changes
bash scripts/clean.sh && npx skills add luismtns/openagents -y -g
```
