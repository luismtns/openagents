# generation

When adding a new subcommand or skill to this pack, follow the established
pattern in `skills/openagents/references/`:

1. **Create the instruction file** at `skills/openagents/references/<topic>.md`
   (kebab-case, `# openagents <topic>` heading, under 50 lines). Keep it
   one level deep from `SKILL.md`.
2. **Register the route** — add a row to the `| Invocation | Read | When |`
   table in `SKILL.md` pointing at the new reference file.
3. **Extend triggers** — add trigger phrases to the `description` field in
   `SKILL.md` frontmatter so the agent discovers the subcommand.
4. **Track the file** — add the new path to the `required_paths` array in
   `scripts/validate.sh` so CI fails if it goes missing.
5. **Bump + document** — increment `version` in `SKILL.md`,
   `claude-plugin/.claude-plugin/plugin.json`, and
   `.claude-plugin/marketplace.json`; add a `## [Unreleased]` (or version)
   entry to `CHANGELOG.md`.
6. **Validate** — run `bash scripts/validate.sh` and confirm 0 warnings
   before pushing.

## Cross-cutting concerns

- **Defensive by default**: destructive ops (`rm`, `uninstall`, `clean`) must
  scope to the `openagents` skill only and ask for confirmation; never remove
  other skills or files outside the intended path.
- **Token efficiency**: prefer declarative tables over inline scripts; keep
  reference files under 50 lines.
- **Spec alignment**: follow the agentskills.io / Anthropic Agent Skills
  format (see `.agents/rules/agentskills.md`).
