# openagents rules

Deep codebase analysis that extracts real architecture and conventions,
then generates generic, positive rules — never hardcoded paths, never
prohibitive tone. Output is three `.agents/rules/` files.

## 1. Sanity check

Read project root files first. If none of these exist, abort gracefully:

```
README.md, package.json, Cargo.toml, go.mod, pyproject.toml,
Gemfile, setup.py, index.ts, main.ts, src/main.ts, App.tsx,
main.py, src/main.py, index.js, main.go, CMakeLists.txt
```

If the project is too minimal (no entry point, no config):
> "Project seems minimal. Run `openagents init` first to scaffold
> structure, then `openagents rules` for deep analysis.
> Generate minimal conventions-only rules anyway? [y/N]"

If the user declines, stop. If they accept, skip to step 3 and generate
only `conventions.md` with language-level patterns.

## 2. Extract architecture

Read these files to understand the project's actual structure:

- **README.md** — purpose, setup commands, conventions the team follows
- **package.json** / `Cargo.toml` / `go.mod` / `pyproject.toml` — framework,
  scripts, dependencies, test runner, linter, formatter
- **tsconfig.json** / `tsconfig.build.json` — module resolution, paths, strictness
- **next.config.js** / `vite.config.ts` / `webpack.config.js` — build toolchain
- **.github/workflows/** — CI pipeline, lint/test/deploy steps
- **Dockerfile** — deployment model
- **.editorconfig**, `.prettierrc`, `.eslintrc` — code style
- **Makefile** / `Justfile` / `Taskfile.yml` — custom commands

Scan the directory tree with Glob to discover real structure:

```bash
# Top-level directories
ls -d */ 2>/dev/null
# Source tree depth (customize extensions per project language)
find src/ -type f \( -name '*.ts' -o -name '*.tsx' -o -name '*.js' \
  -o -name '*.jsx' -o -name '*.py' -o -name '*.rs' -o -name '*.go' \) \
  | head -80
```

Read a sample of files (2-3 per major directory) to extract naming
conventions and patterns. Document everything as **observation**, not
prescription:
- Directory naming: `feature/` vs `pages/` vs `components/` vs flat
- File naming: `PascalCase.tsx` vs `kebab-case.tsx` vs `camelCase.ts`
- Export style: named exports, default exports, barrel files
- Testing: `*.test.ts` co-located vs `__tests__/` vs `test/` directory
- State management, API layer, error handling patterns

## 3. Generate rules

Write three files to `.agents/rules/`. Every rule must be:

- **Generic**: describe the *pattern*, not the path. Use `src/` as alias;
  "Components live in a `components/` directory" not "Components in `src/app/components/ui/"`
- **Positive**: "Prefer explicit types" not "Don't use `any`"
- **Verifiable**: the LLM reading the rule can check the rule against code

### conventions.md

Language and framework conventions extracted from the project:

```markdown
# conventions

## Principles
<why these conventions exist — clarity, consistency, type safety>

## Naming
- <pattern>: <description>
- <pattern>: <description>

## Imports and exports
- <project-specific import style>

## Linting and formatting
- <linter config summary>

## Testing
- <test runner, naming, location>
```

### architecture.md

Directory structure and module boundaries — discovered, not assumed:

```markdown
# architecture

## Directory layout
```
<project tree summary, max depth 3>
<!-- NOTE: this is the structure at time of generation.
New directories should follow the same domain-driven or layer-driven split. -->
```

## Module responsibilities
- <directory>: <what belongs here>
- <directory>: <what belongs here>

## Boundaries
- <what crosses boundaries and how>
- <what stays within a boundary>
```

### generation.md

Pattern for creating new code — extracted from existing files:

```markdown
# generation

When creating a new <X>, follow the pattern established in <existing file>:

1. Create file at the appropriate directory under the same domain/layer pattern
2. Use the same export style as <similar file>
3. Follow the same error handling / state / API patterns as <similar file>
4. Add tests following the same structure as <similar file>

## Cross-cutting concerns
- <shared patterns: logging, error handling, validation, auth>
- <how to integrate new files into existing modules>
```

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

Wait for confirmation. If user requests changes, edit the affected rule
file before writing. If user wants to add rules, accept their input and
merge into the appropriate file.

## 5. Write

Write all three files to `.agents/rules/`. Create the directory if it
doesn't exist.

If the agent expects rules at a different path (`.claude/rules/`,
`.cursor/rules/`), create a symlink:

```bash
mkdir -p .claude
ln -sfn ../.agents/rules .claude/rules
```