# openagents rules: validate

Steps 4-5 of `openagents rules` — confirm with the user, then write.

## 4. Validate with user

Present a summary before writing:

```
Project: my-app
Framework: Next.js 14 (App Router)
Language: TypeScript (strict)
Testing: Vitest, co-located *.test.tsx
Structure: feature-based under src/
  ├── app/          — routes (Next.js file-based)
  ├── components/   — shared UI
  ├── features/     — domain modules
  ├── lib/          — utilities, API client
  └── types/        — shared types

Rules to generate:
  1. conventions.md — naming, imports, testing
  2. architecture.md — directory layout, boundaries
  3. generation.md — new feature scaffold pattern

Proceed? [Y/n]
```

Wait for confirmation. If the user requests changes, edit the affected rule
file before writing. If they want to add rules, merge their input into the
appropriate file.

## 5. Write

Write all three files to `.agents/rules/`. Create the directory if missing.

If the agent expects rules at a different path (`.claude/rules/`,
`.cursor/rules/`), create a symlink:

```bash
mkdir -p .claude
ln -sfn ../.agents/rules .claude/rules
```
