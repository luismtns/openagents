# openagents init

Per-project scaffolding for OpenAgents. Generates `AGENTS.md`, sets up
`.agents/rules/`, and creates agent symlinks.

## Detection

- **Language** — `*.py`, `*.go`, `*.rs`, `package.json`
- **Framework** — inspect `package.json` deps (next, react, vue, etc.)
- **Package manager** — lockfile (`pnpm-lock.yaml`, `yarn.lock`, `package-lock.json`)

## Generate AGENTS.md

Write `AGENTS.md` with this structure, then append conventions and
architecture sections:

```markdown
<!-- openagents -->
# <project>
<description>

## Agent instructions
- Language: <lang> | Framework: <fw> | PM: <pm>
- Build: `<cmd>` | Test: `<cmd>` | Lint: `<cmd>`
```

## Rules directory

Create `.agents/rules/` with an initial rule file containing build, test,
lint commands and project conventions.

## Symlink

Make the canonical project rules visible to every agent you use. For agents
that don't auto-discover `.agents/rules/`, symlink their native rules path:

```bash
for a in claude cursor zed; do
  mkdir -p ".$a"
  ln -sfn ../.agents/rules ".$a/rules"
done
```

This realizes the unified multi-agent setup: one `.agents/rules/` source,
mirrored into each agent's path so skills and rules are identical everywhere.
