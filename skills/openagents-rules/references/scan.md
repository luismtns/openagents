# openagents rules (scan)

Steps 1-2 of `openagents rules` -- sanity check then architecture extraction.

## 1. Sanity check

Read project root files first. If none exist, abort gracefully:

```
README.md, package.json, Cargo.toml, go.mod, pyproject.toml,
Gemfile, setup.py, index.ts, main.ts, src/main.ts, App.tsx,
main.py, src/main.py, index.js, main.go, CMakeLists.txt
```

If the project is too minimal (no entry point, no config):
> "Project seems minimal. Run `openagents init` first to scaffold
> structure, then `openagents rules` for deep analysis.
> Generate minimal conventions-only rules anyway? [y/N]"

Decline -> stop. Accept -> skip to generation, produce only `conventions.md`
with language-level patterns.

## 2. Extract architecture

Read these to understand actual structure:

- **README.md** -- purpose, setup commands, team conventions
- **package.json / Cargo.toml / go.mod / pyproject.toml** -- framework, scripts, deps, test/lint/format
- **tsconfig.json / next.config.js / vite.config.ts / webpack.config.js** -- toolchain
- **.github/workflows/** -- CI steps
- **Dockerfile**, **.editorconfig**, **.prettierrc**, **.eslintrc** -- style
- **Makefile / Justfile / Taskfile.yml** -- custom commands

Scan the tree with Glob; read 2-3 files per major directory. Document as
**observation**, not prescription: directory/file naming, export style,
testing layout, state/API/error patterns.