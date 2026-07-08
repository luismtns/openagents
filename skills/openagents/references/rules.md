# openagents rules

Deep codebase analysis that extracts real architecture and conventions,
then generates generic, positive rules — never hardcoded paths, never
prohibitive tone. Output is three `.agents/rules/` files.

Workflow (read each on demand — one level deep):

1. **Sanity + extract** → [references/rules-scan.md](references/rules-scan.md)
2. **Generate** the three rule files → [references/rules-generate.md](references/rules-generate.md)
3. **Validate with user + write** → [references/rules-validate.md](references/rules-validate.md)

## Safety

- If the project is too minimal, abort gracefully and suggest `openagents init`.
- Every rule is generic (pattern, not path), positive, and verifiable.
- Agent expects rules at a different path → symlink: `ln -sfn ../.agents/rules .claude/rules`
