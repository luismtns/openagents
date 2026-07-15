<!-- openagents -->
# OpenAgents

A small skill suite for carrying operational context between AI coding agents.
Runtime behavior is instruction-only; repository scripts validate packaging
and adversarial fixtures.

Install via `npx skills add luismtns/openagents` and load with:

```
skill({ name: "openagents-<name>" })
```

## Skills

| Invocation | Skill name | Use case |
|------------|-----------|----------|
| `openagents` | `openagents` | Read-only local status and routing |
| `openagents-handoff` | `openagents-handoff` | Portable Markdown handoff and explicit export |
| `openagents-doctor` | `openagents-doctor` | Read-only diagnostics with manual remediation |

Markdown output is portable by design. Auto-launch is best effort and must not
be described as verified for an agent without a reproduced test.

## Project rules (`.agents/rules/`)

- `architecture.md` - v2 boundaries and responsibilities
- `conventions.md` - authoring and safety conventions
- `validate.md` - local and pre-release gates
- `distributed-skills.md` - distribution claims and versioning

Run `bash scripts/validate.sh` before asking the user to review the unstaged diff.
Do not bump versions in feature changes. Release labels on the merged PR drive
the post-merge version and changelog automation.
