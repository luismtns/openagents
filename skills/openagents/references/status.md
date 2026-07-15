# openagents status

Produce a concise, read-only status report.

## Checks

1. Identify the project from the working directory, without exposing its
   absolute path.
2. If Git is available, report branch, abbreviated `HEAD`, and clean/dirty
   state. Do not include remotes, author identity, or diff contents.
3. Check whether `openagents`, `openagents-handoff`, and `openagents-doctor`
   are visible to the current agent. Report only what can be proven.
4. Detect known CLI binaries with `command -v`, but label them `observed`.
5. Never infer the currently running agent from API keys or one weak signal.

## Report

```text
OpenAgents <version from loaded skill frontmatter>
Project: <name> | Git: <branch>@<head> | Worktree: clean|dirty|unknown
Skills: <visible facts or unknown>
CLI signals: <observed binaries or none>
Next: handoff | doctor | none
```

Recommend `openagents-handoff` for transferring work and
`openagents-doctor` for detailed diagnostics. Do not offer repairs.
