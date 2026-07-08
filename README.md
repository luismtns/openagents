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

    S -->|routes to| R["SKILL.md router"]

    R -->|global| G["references/global.md"]
    R -->|init| I["references/init.md"]
    R -->|add| A["references/add.md"]
    R -->|rules| RL["references/rules.md"]

    G --> D{"detect agent"}
    D -->|opencode| OC["~/.config/opencode/"]
    D -->|claude-code| CC["~/.claude/"]
    D -->|codex| CX["~/.codex/"]
    D -->|cursor| CR["~/.cursor/skills/"]
    D -->|cline| CL["~/.clinerules"]
    D -->|zed| ZD["~/.zed/"]

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
| `openagents:global` | Detects the running agent, maps config paths, verifies the multi-agent ecosystem | First-time setup, checking agent configurations |
| `openagents:init` | Generates AGENTS.md, detects language/framework, creates `.agents/rules/` | Starting a new project, onboarding |
| `openagents:add` | Scaffolds new skills, registers distribution, validates structure | Creating a new skill or rule pack |
| `openagents:rules` | Deep codebase scan, pattern identification, rule generation | When a project needs thorough rule coverage |

## Agent compatibility

| Agent | Skill discovery | Auto-discover `~/.agents/skills/` |
|-------|----------------|-----------------------------------|
| opencode | `~/.agents/skills/` | Yes |
| claude-code | `~/.agents/skills/` | Yes |
| codex | `~/.agents/skills/` | Yes |
| cursor | `~/.cursor/skills/` (symlink) | No |
| cline | `~/.agents/skills/` | Yes |
| zed | `~/.zed/skills/` (symlink) | No |

## Project structure

```
skills/openagents/
├── SKILL.md                  # Unified frontmatter + routing table
└── references/
    ├── global.md             # Agent-agnostic handshake protocol
    ├── init.md               # Project scaffolding
    ├── add.md                # Skill/rules creation
    └── rules.md              # Deep analysis + rule generation

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
