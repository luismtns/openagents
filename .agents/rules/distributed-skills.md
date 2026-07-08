# distributed-skills

## Naming

| Form | Where | Example |
|------|-------|---------|
| `openagents` | Directory name, frontmatter `name`, skills.sh slug | `openagents` |
| `openagents <subcommand>` | Reference file H1 heading | `# openagents global` |
| `openagents <subcommand>` | Frontmatter `Triggers` field | `Triggers: openagents global` |

Use space-separated form `openagents <subcommand>` everywhere.
Directory name = frontmatter `name` = skills.sh slug. Always kebab-case.

## Frontmatter (agentskills.io spec)

Per the [Agent Skills specification](https://agentskills.io/specification),
the `SKILL.md` starts with YAML frontmatter.

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | **yes** | 1-64 chars, lowercase alphanum + hyphens only, must match parent dir name |
| `description` | **yes** | 1-1024 chars, non-empty. Must describe both **what** and **when** |
| `license` | no | SPDX identifier or reference to bundled license file |
| `compatibility` | no | Max 500 chars. Environment requirements (system packages, network, etc.) |
| `metadata` | no | Arbitrary key-value map for extra fields |
| `allowed-tools` | no | *Experimental*. Space-separated pre-approved tools |

`name` regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

Rules:
- `name` matches the enclosing directory name exactly
- `description` contains "Use when" + specific trigger keywords
- Under 500 lines / 5000 tokens per SKILL.md (progressive disclosure);
  split into `references/` if larger

## Progressive disclosure

Agents load skills in three tiers. Structure files accordingly:

1. **Tier 1 — Metadata** (~100 tokens): `name` + `description` loaded at startup for all skills
2. **Tier 2 — Instructions** (< 5000 tokens): Full SKILL.md body loaded on activation
3. **Tier 3 — Resources** (on demand): `references/`, `scripts/`, `assets/` loaded only when needed

Keep individual reference files under 50 lines each.

## File layout

```
repo/
├── skills/
│   └── openagents/
│       ├── SKILL.md              # main skill definition
│       └── references/           # progressive disclosure
│           ├── status.md
│           ├── global.md
│           ├── init.md
│           ├── add.md
│           ├── rules.md
│           ├── rm.md
│           └── uninstall.md
├── .agents/
│   └── rules/
│       ├── validate.md
│       └── distributed-skills.md
├── .claude/
│   └── rules -> ../.agents/rules/
├── .claude-plugin/
│   ├── plugin.json               # Claude Code plugin manifest
│   └── marketplace.json          # skills.sh plugin marketplace discovery
├── .github/
│   └── workflows/
│       ├── validate.yml          # CI: validation on push/PR
│       └── publish.yml           # CD: release on main merge
├── scripts/
│   ├── validate.sh
│   └── clean.sh
├── skills.sh.json
├── AGENTS.md
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Distribution channels

| Channel | Method | Scope |
|---------|--------|-------|
| **skills.sh (GitHub)** | `npx skills add luismtns/openagents` | Primary — public registry |
| **Claude Plugin marketplace** | `.claude-plugin/marketplace.json` | Claude Code native discovery |
| **Local path** | `npx skills add /path/to/repo` | Development and testing |
| **Git URL** | `npx skills add https://git.example.com/repo.git` | Self-hosted / enterprise |
| **Well-known URL** | Deploy to domain + configure `/.well-known/` | skills.sh well-known sources |

The `skills` CLI auto-detects which agents are installed and installs
skills to the correct directory. It supports GitHub, GitLab, any git URL,
local paths, and well-known sources.

## Security audits

skills.sh integrates with five security audit partners. Results appear
automatically after the first install:

- **Gen Agent Trust Hub** — code risk classification
- **Socket** — dependency and behavioral alerts
- **Snyk** — vulnerability scanning
- **Runlayer** — execution sandbox analysis
- **ZeroLeaks** — secret and credential detection

Skills that fail every partner audit are excluded from the directory.
Badges in README link to per-skill audit pages:
`https://skills.sh/luismtns/openagents/openagents/security/{partner}`

## Evals-driven iteration

Follow this loop for skill quality:

1. **Create evals**: `evals.json` with test cases, assertions, expected outputs
2. **Baseline**: measure pass rate without the skill
3. **Compare**: measure pass rate with the skill
4. **Analyze**: identify failure patterns
5. **Revise**: update instructions targeting specific failures
6. **Re-run**: repeat until pass rate plateaus

Use blind comparison (LLM judge, no version labels) for holistic quality.

## Release and versioning

### Version scheme

Follow [SemVer 2.0](https://semver.org/):

| Bump | When |
|------|------|
| **MAJOR** | Breaking changes to SKILL.md routing, removal of subcommands, breaking frontmatter changes |
| **MINOR** | New subcommands, new reference files, new features, expansion of agent support |
| **PATCH** | Bug fixes, doc improvements, CI changes, tool scope adjustments |

### Release checklist

1. Update `CHANGELOG.md` with `[Unreleased]` section per [Keep a Changelog](https://keepachangelog.com/)
2. Update `version` in `skills/openagents/SKILL.md` frontmatter
3. Update `version` in `claude-plugin/.claude-plugin/plugin.json`
4. Run `bash scripts/validate.sh`
5. Commit: `chore: bump to v{VERSION}`
6. Tag: `git tag v{VERSION} && git push origin v{VERSION}`
7. Create GitHub Release via `gh release create v{VERSION} --generate-notes`

### CI/CD automation

- **Validate workflow** (`.github/workflows/validate.yml`): runs on every push/PR —
  validates SKILL.md frontmatter, file structure, schema
- **Publish workflow** (`.github/workflows/publish.yml`): runs on push to `main` —
  creates GitHub Release automatically when CHANGELOG has an unreleased section

### CHANGELOG conventions

```
## [{VERSION}] - {YYYY-MM-DD}

### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
```

Each entry is a single bullet point in imperative mood.