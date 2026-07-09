<h1 align="center">
  <img src="assets/logo.gif" alt="OpenAgents">
</h1>

[![skills.sh](https://skills.sh/b/luismtns/openagents)](https://skills.sh/luismtns/openagents)
[![validate](https://github.com/luismtns/openagents/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/validate.yml)
[![release](https://github.com/luismtns/openagents/actions/workflows/publish.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/publish.yml)
[![GitHub release](https://img.shields.io/github/v/release/luismtns/openagents)](https://github.com/luismtns/openagents/releases/latest)
[![Socket](https://img.shields.io/badge/Socket-Pass-brightgreen?logo=socketdotio)](https://www.skills.sh/luismtns/openagents/openagents/security/socket)
[![Snyk](https://img.shields.io/badge/Snyk-Medium-yellow?logo=snyk)](https://www.skills.sh/luismtns/openagents/openagents/security/snyk)

A multi-skill orchestration suite for AI coding agents. Each subcommand is
an independent, discoverable skill — agents auto-discover them by name
and activate only the specific skill needed.

## How it works

openagents gives you **one unified setup of skills and rules for every AI
agent you use**. `.agents/` (project) and `~/.agents/` (machine-global) are
the canonical source; `openagents global` / `init` / `rules` symlink them
into each agent's native path, so skills and rules are identical no matter
which agent you open.

```mermaid
flowchart LR
    U["you: openagents init<br>openagents global<br>openagents rules<br>..."] -->|agent matches description| OA["openagents-init<br>SKILL.md"]
    U -->|agent matches description| OG["openagents-global<br>SKILL.md"]
    U -->|agent matches description| OR["openagents-rules<br>SKILL.md"]
    U -->|agent matches description| OH["openagents<br>SKILL.md (hub)"]
    OH -->|status| ST["show agent + sync matrix"]
    OH -->|doctor| DR["diagnose + repair"]
    OG -->|handshake| GL["detect agent, link skills + rules"]
    OI["openagents-init<br>SKILL.md"] -->|scaffold| SC["AGENTS.md + rules"]
    OA["openagents-add<br>SKILL.md"] -->|create| AD["new skills"]
    OR -->|scan, generate, validate| RL["rules files"]
    ORI["openagents-rm<br>SKILL.md"] -->|remove| RM["project artifacts"]
    OUI["openagents-uninstall<br>SKILL.md"] -->|guide| UI["npx skills remove"]
```

## Installation

```bash
# Via skills.sh
npx skills add luismtns/openagents

# Via skill.fish
npx skillfish add luismtns/openagents
```

Then load in any AI coding agent:

```
# opencode
skill({ name: "openagents" })       # hub (status, doctor)
skill({ name: "openagents-init" })  # project scaffolding
skill({ name: "openagents-global" }) # handshake + symlinks
# ... each subcommand is its own skill

# claude-code
/openagents:init   # as plugin
/openagents-init   # as standalone skill

# cursor / zed
/openagents-init
```

## Subcommands

| Invocation | Skill | What it does | When to use |
|------------|-------|-------------|-------------|
| `openagents` / `openagents status` | openagents | Shows agent status, repo health, available commands | Default entry point, checking current setup |
| `openagents global` | openagents-global | Detects running agent, verifies multi-agent ecosystem, creates symlinks | First-time setup, checking agent configurations |
| `openagents init` | openagents-init | Generates AGENTS.md, detects language/framework, creates `.agents/rules/` | Starting a new project, onboarding |
| `openagents add` | openagents-add | Scaffolds new skills, registers distribution, validates structure | Creating a new skill or rule pack |
| `openagents rules` | openagents-rules | Deep codebase scan, pattern identification, rule generation | When a project needs thorough rule coverage |
| `openagents rm` | openagents-rm | Removes rules, skills, AGENTS.md, symlinks, or all project artifacts | Cleaning up project scaffolding |
| `openagents doctor` | openagents-doctor | Diagnose and repair broken symlinks, missing files, version mismatches | When status shows issues or setup seems broken |
| `openagents info` | openagents-info | Shows version, installed sub-skills, detected agents, distribution channels | Checking what's installed and configured |
| `openagents upgrade` | openagents-upgrade | Runs `npx skills update` to fetch latest version | Updating to the newest release |
| `openagents uninstall` | openagents-uninstall | Uninstalls the openagents skill via `npx skills remove` | Removing the skill from your ecosystem |

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
skills/
├── openagents/                    # Hub: status + doctor + detection matrix
│   ├── SKILL.md
│   └── references/
│       └── status.md
├── openagents-global/             # Handshake + symlinks
│   └── SKILL.md
├── openagents-init/               # Project scaffolding
│   └── SKILL.md
├── openagents-add/                # Create skills/rules
│   └── SKILL.md
├── openagents-rules/              # Codebase analysis
│   ├── SKILL.md
│   └── references/
│       ├── scan.md
│       ├── generate.md
│       └── validate.md
├── openagents-rm/                 # Remove artifacts
│   └── SKILL.md
├── openagents-doctor/             # Diagnose + repair
│   └── SKILL.md
├── openagents-info/               # Version + channels
│   └── SKILL.md
├── openagents-upgrade/            # Self-update
│   └── SKILL.md
└── openagents-uninstall/          # Global uninstall
    └── SKILL.md

.agents/rules/
├── validate.md               # Pre-release validation
├── distributed-skills.md     # Naming, layout, ecosystem distribution
└── agentskills.md            # Canonical Agent Skills references (base source)

scripts/
├── validate.sh               # Local CI validator
├── clean.sh                  # Global skill cleanup (nuke — not for uninstall)
└── publish.sh                # Release gate: skills-ref + skills.sh publish

AGENTS.md                     # Skill pack documentation
CHANGELOG.md                  # Version history
skills.sh.json                # skills.sh distribution config (10 skills)
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