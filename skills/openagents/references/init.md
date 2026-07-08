# openagents:init

Per-project scaffolding for the OpenAgents ecosystem.

Generates `AGENTS.md`, sets up `.agents/rules/`, and creates symlinks
for the detected agent.

## Detection

Identify the project language, framework, and package manager:

```bash
# Language
ls *.py &>/dev/null && LANG=python
ls *.go &>/dev/null && LANG=go
ls *.rs &>/dev/null && LANG=rust
ls package.json &>/dev/null && LANG=node

# Framework (Node)
grep -q '"next"' package.json 2>/dev/null && FRAMEWORK=next
grep -q '"react"' package.json 2>/dev/null && FRAMEWORK=react

# Package manager
ls pnpm-lock.yaml &>/dev/null && PM=pnpm
ls yarn.lock &>/dev/null && PM=yarn
ls package-lock.json &>/dev/null && PM=npm
```

## Generate AGENTS.md

Write `AGENTS.md` with:

```markdown
<!-- openagents -->
# <project>

<description>

## Agent instructions

- Language: <lang>
- Framework: <framework>
- Package manager: <pm>
- Build: <build command>
- Test: <test command>
- Lint: <lint command>
- Typecheck: <typecheck command>

## Conventions

Follow the existing patterns in this codebase.

## Architecture

<key modules and their responsibilities>
```

## Set up rules directory

```bash
mkdir -p .agents/rules
```

Create an initial rule file if useful patterns are detected:

```markdown
# <project>-rules

## Commands

- Build: `<build cmd>`
- Test: `<test cmd>`
- Lint: `<lint cmd>`

## Conventions

<project-specific conventions>
```

## Symlink for agent detection

If the agent uses a different rules path, create a symlink:

```bash
ln -sfn .agents/rules .claude/rules  # claude-code
```
