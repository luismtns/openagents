# validate

Pre-release validation checklist. Run before every release:

```bash
bash scripts/validate.sh
```

## Structure check

```
skills/openagents/SKILL.md           — main skill must exist
skills/openagents/references/        — 11 reference files
.agents/rules/                       — validate.md + distributed-skills.md + agentskills.md
.claude-plugin/plugin.json           — plugin manifest
.github/workflows/validate.yml       — CI validation
.github/workflows/publish.yml        — CI release automation
scripts/validate.sh                  — local validator
README.md, LICENSE, CHANGELOG.md, skills.sh.json, skillfish.json
```

## Frontmatter validation (agentskills.io spec)

| Field | Required | Notes |
|-------|----------|-------|
| `name` | **yes** | Must match directory name, lowercase kebab-case, 1-64 chars |
| `description` | **yes** | Must contain "Use when" + trigger keywords, 1-1024 chars |
| `license` | no | SPDX identifier if present |
| `compatibility` | no | Environment requirements if any |
| `metadata` | no | Arbitrary key-value map |
| `allowed-tools` | no | *Experimental* — scope Bash if present (e.g. `Bash(git:*)`) |
| `version` | no | Valid semver if releasing |
| `author` | no | Author info if releasing |

## Progressive disclosure

- SKILL.md under 200 lines (5000 tokens max)
- Each reference file under 50 lines
- No deeply nested file references (max 1 level deep from SKILL.md)

## skills.sh compatibility

- `skills.sh.json` uses `groupings` (not old `categories`)
- `$schema` points to `https://skills.sh/schemas/skills.sh.schema.json`
- Each skill slug in `groupings` matches a directory under `skills/`

## Claude Plugin

- `.claude-plugin/plugin.json` has valid `name`, `version`, `description`, `repository`
- `.claude-plugin/marketplace.json` has valid structure if present
- `version` in plugin.json matches SKILL.md frontmatter

## Release readiness

- `version` bumped in SKILL.md frontmatter
- `version` bumped in `.claude-plugin/plugin.json`
- `CHANGELOG.md` has `[Unreleased]` or new version section
- `git tag v{VERSION}` created and pushed
- `bash scripts/validate.sh` passes cleanly