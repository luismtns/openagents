# handoff format

Use these headings exactly. Omit no section; write `None known` or
`Not verified` when appropriate.

```markdown
# Agent Handoff

## Objective
## Scope And Constraints
## Decisions
## Evidence And References
## Workspace Checkpoint
## Verification Performed
## Open Risks And Questions
## Next Action
## Suggested Skills
## Receiver Protocol
```

The workspace checkpoint should contain project name, branch, abbreviated
HEAD, clean/dirty/unknown status, counts by status, a fingerprint of the
complete porcelain status inventory with optional locks and `core.fsmonitor`
disabled, safe relevant paths, and test results.
Do not reveal a path containing identity or sensitive information; mark the
checkpoint unverifiable instead. For tracked dirty content, record a
fingerprint of `git diff --binary --no-ext-diff --no-textconv HEAD` without
exposing the diff. If untracked files exist, mark exact content validation
unavailable and require the receiver to stop. For a non-Git project, say that
commit-based validation is unavailable.

The receiver protocol must require the next agent to verify project, branch,
HEAD, status-inventory fingerprint, tracked-diff fingerprint, and references
before acting. Any divergence, omitted sensitive path, or unverifiable
untracked state must stop the work and be reported to the user. The receiver
must not revert existing changes or execute the next action until validation
succeeds.
