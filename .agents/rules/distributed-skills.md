# distributed-skills

## Naming

| Form | Where | Example |
|------|-------|---------|
| `openagents` | Directory name, frontmatter `name`, skills.sh slug | `openagents` |
| `openagents:<subcommand>` | Reference file H1 heading | `# openagents:global` |
| `openagents <verb>` | Frontmatter `Triggers` field | `Triggers: openagents global` |

Directory name = frontmatter `name` = skills.sh slug. Always kebab-case.

## Frontmatter (opencode spec)

The main `SKILL.md` must start with YAML frontmatter. Recognized fields:

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | lowercase kebab-case, matches directory |
| `description` | yes | 1-1024 chars, includes "Use when" + triggers |
| `license` | no | SPDX identifier |
| `compatibility` | no | Agent compatibility string |
| `metadata` | no | string-to-string map for extra fields |

Unknown frontmatter fields are ignored by opencode but may be read by
other agents (claude-code, codex).

Name regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

Rules (no exceptions):
- `name` matches the enclosing directory name exactly
- `description` contains "Use when"
- Under 200 lines per reference (progressive disclosure); split further
  into `references/` if larger

## File layout

```
repo/
├── skills/
│   └── openagents/
│       ├── SKILL.md              # main skill definition
│       └── references/           # progressive disclosure
│           ├── status.md         # default status workflow
│           ├── global.md         # agent handshake
│           ├── init.md           # project scaffolding
│           ├── add.md            # skill/rules creation
│           ├── rules.md          # deep analysis + rule generation
│           ├── rm.md             # remove project artifacts
│           └── uninstall.md      # uninstall guidance
├── .agents/
│   └── rules/                    # project rules (agent-agnostic)
│       ├── validate.md
│       └── distributed-skills.md
├── .claude/
│   └── rules -> ../.agents/rules/  # symlink for Claude Code
├── scripts/
│   ├── validate.sh
│   └── clean.sh
├── skills.sh.json
├── AGENTS.md
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Distribution

- skills.sh: `npx skills add luismtns/openagents`
- Always version-pin dependencies; never `npm install` without lockfile
