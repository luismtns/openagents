# openagents rules

Deep codebase analysis for comprehensive rule generation. Scans project
structure, identifies architecture patterns and conventions, then
generates or updates `.agents/rules/` with validated rules.

## Scan

### 1. Project structure

Review directory layout, source entry points, and key file extensions.

### 2. Configuration files

Read these if present:

- `README.md` — project purpose, commands
- `package.json` / `Cargo.toml` / `go.mod` — dependencies, scripts
- `tsconfig.json` / `pyproject.toml` — language settings
- `.github/workflows/` — CI pipeline
- `Dockerfile` — deployment model

### 3. Architecture patterns

Identify framework (React, Next.js, Django, etc.), state management, API
style (REST, GraphQL, tRPC), database ORM, testing approach, and code
organization (feature-based, layer-based).

## Generate rules

Write `.agents/rules/validate.md` with appropriate conventions.

## Validate with user

Present the generated rules and ask for confirmation:

1. Does the architecture analysis match your understanding?
2. Are the build/test commands correct?
3. Any additional conventions to add?
4. Any obsolete rules to remove?

## Update

Write validated rules to `.agents/rules/` and symlink if the agent expects
a different path (`.claude/rules/`, `.cursor/rules/`).
