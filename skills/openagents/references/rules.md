# openagents:rules

Deep codebase analysis for comprehensive rule generation.

Scans the project, identifies architecture patterns and conventions,
then generates or updates `.agents/rules/` with validated rules.

## Scan

### 1. Project structure

```bash
find . -maxdepth 3 -type f -name "*.md" -o -name "*.json" -o -name "*.yaml" | head -30
ls src/ 2>/dev/null || ls lib/ 2>/dev/null || ls app/ 2>/dev/null
```

### 2. Configuration files

Read these if present to understand the project:

- `README.md` — project purpose, commands
- `package.json` / `Cargo.toml` / `go.mod` — dependencies, scripts
- `tsconfig.json` / `pyproject.toml` — language settings
- `.github/workflows/` — CI pipeline
- `Dockerfile` — deployment model

### 3. Architecture patterns

Identify:
- Framework (React, Next.js, Django, etc.)
- State management pattern
- API style (REST, GraphQL, tRPC)
- Database ORM
- Testing approach
- Code organization (feature-based, layer-based)

## Generate rules

Write `.agents/rules/validate.md` with appropriate conventions.

## Validate with user

Present the generated rules and ask for confirmation before writing.

Key questions:
1. Does the architecture analysis match your understanding?
2. Are the build/test commands correct?
3. Any additional conventions to add?
4. Any obsolete rules to remove?

## Update

Write the validated rules to `.agents/rules/` and symlink if the agent
expects a different path (`.claude/rules/`, `.cursor/rules/`).
