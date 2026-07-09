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