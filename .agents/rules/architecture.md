# Architecture

OpenAgents v2 is an instruction-only, three-skill package.

## Responsibilities

| Path | Responsibility |
|------|----------------|
| `skills/openagents/` | Read-only status and routing |
| `skills/openagents-handoff/` | Portable context creation and explicit export |
| `skills/openagents-doctor/` | Read-only diagnostics and manual guidance |
| `evals/` | Adversarial cases and human evaluation rubrics |
| `scripts/` | Repository validation and post-merge release preparation |
| `claude-plugin/`, `.claude-plugin/` | Distribution metadata |

## Boundaries

- Runtime behavior lives in SKILL.md and one-level references.
- Hub and doctor never mutate files or configuration.
- Handoff writes only after explicit export consent.
- Package managers own install, update, and removal.
- No component synchronizes rules, skills, MCP, hooks, or agent settings.
- Markdown portability is distinct from verified CLI auto-launch.
- Release automation may change only changelog and version-bearing manifests.
