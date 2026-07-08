# distributed-skills

## Naming

| Form | Where | Example |
|------|-------|---------|
| `openagents` | Directory name, frontmatter `name`, skills.sh slug | `openagents` |
| `openagents:<subcommand>` | Reference file H1 heading | `# openagents:setup` |
| `openagents <verb>` | Frontmatter `Triggers` field | `Triggers: openagents setup` |

Directory name = frontmatter `name` = skills.sh slug. Always kebab-case.

## Frontmatter (Anthropic 2026 spec)

The main `SKILL.md` must have:

```yaml
---
name: <kebab-case>
description: |
  <purpose sentence>.
  <details about what it does>.
  Use when <specific trigger conditions>.
  Triggers: <space-separated trigger phrases>.
allowed-tools: <comma-separated, Bash scoped>
version: <semver>
author: <name>
license: <SPDX identifier>
user-invocable: true
compatible-with: opencode, claude-code, cursor, codex, cline
tags: [openagents, <category>, ...]
---
```

Rules (no exceptions):
- `name` matches the enclosing directory name exactly
- `description` contains "Use when" 
- `allowed-tools` tools like Bash, Write, Read, Glob, Grep; Bash must be scoped: `Bash(git:*)`
- Under 200 lines per reference (progressive disclosure); split further into `references/` if larger

## File layout

```
repo/
├── skills/
│   └── openagents/
│       ├── SKILL.md              # main skill definition
│       └── references/           # progressive disclosure
│           ├── setup.md
│           ├── init.md
│           ├── rules.md
│           ├── sync.md
│           ├── audit.md
│           └── skills.md
├── .agents/
│   └── rules/                    # project rules (agent-agnostic)
│       ├── validate.md
│       └── distributed-skills.md
├── .claude/
│   └── rules -> ../.agents/rules/  # symlink for Claude Code
├── claude-plugin/
│   ├── .claude-plugin/
│   │   └── plugin.json
│   └── skills -> ../skills/        # symlink
├── scripts/
│   ├── validate.sh
│   └── clean.sh
├── skills.sh.json
├── AGENTS.md                  # root-level skill pack description
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Distribution

- skills.sh: `npx skills add luismtns/openagents`
- Claude Code plugin: manual `plugin.json` + skills symlink
- Always version-pin dependencies; never `npm install` without lockfile
