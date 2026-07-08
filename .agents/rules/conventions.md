# conventions

## Principles

Rules for evolving this skill pack: single source of truth, progressive
disclosure, and validation-before-release. Every change must pass
`bash scripts/validate.sh` in CI.

## Naming

- **Skill directory**: kebab-case, must equal the frontmatter `name` and the
  skills.sh slug (`skills/<name>/`, `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$`).
- **Subcommands**: space-separated `openagents <subcommand>` (never colons).
- **Reference headings**: `# <name> <topic>` (space-separated, no colon) —
  matching existing files like `# openagents global`.
- **Rule files** (`.agents/rules/`): kebab-case, descriptive (`validate.md`,
  `distributed-skills.md`).

## Frontmatter

- `SKILL.md` order: `name`, `description` (with "Use when" + triggers),
  `allowed-tools` (scoped, e.g. `Bash(git:*)`), `version`, `author`, `license`,
  `user-invocable`, `compatible-with`, `tags`.
- Bump `version` in SKILL.md, `claude-plugin/.claude-plugin/plugin.json`, and
  `.claude-plugin/marketplace.json` together on every release.

## Linting and formatting

- No linter/formatter — markdown + POSIX bash only.
- Progressive disclosure enforced by `validate.sh`: reference files under 50
  lines, `SKILL.md` under 500 lines, references one level deep from `SKILL.md`.

## Testing

- No unit tests. The gate is `bash scripts/validate.sh` (frontmatter, file
  structure, symlinks, JSON schema). Runs on every push/PR via
  `.github/workflows/validate.yml`.
