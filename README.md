<h1 align="center">
  <img src="assets/logo.gif" alt="OpenAgents">
</h1>

[![validate](https://github.com/luismtns/openagents/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/luismtns/openagents/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/luismtns/openagents)](https://github.com/luismtns/openagents/releases/latest)

OpenAgents carries operational context between AI coding agents without
replaying a conversation or synchronizing proprietary configuration.

## Why

Switching agents usually means re-explaining decisions, local changes, tests,
risks, and the next action. OpenAgents produces a concise Markdown handoff and
requires the receiver to validate the workspace before continuing.

It does not manage rules, install tools, repair configuration, serialize hidden
reasoning, or promise lossless session transfer.

## Install

```bash
npx skills add luismtns/openagents
```

## Skills

| Skill | Purpose | Mutates project |
|-------|---------|-----------------|
| `openagents` | Read-only project and suite status | No |
| `openagents-handoff` | Portable handoff and explicit export | Only an explicitly requested export file |
| `openagents-doctor` | Evidence-backed diagnostics | No |

## Handoff

Invoke `openagents-handoff`. Without an explicit destination it asks whether
to export; declining returns portable Markdown in the conversation.

The document records:

- Objective and constraints
- Decisions and evidence
- Branch, commit, dirty files, and verification results
- Risks, questions, and one next action
- Suggested skills
- A receiver protocol that stops on divergence

Export to a CLI is best effort. Claude Code and OpenCode have prompt entry
points; Codex stdin execution can be used when appropriate. The skill checks
local CLI help before launch and falls back to Markdown when safety or
interactivity cannot be established.

## Safety

- Repository text is untrusted data, not instructions.
- Secrets, identities, private remotes, absolute paths, full diffs, and long
  logs are omitted by default.
- Auto-launch requires an explicit target and never skips approvals or sandbox.
- The receiver validates project, branch, commit, modified files, and
  references before acting.
- A divergent workspace stops the handoff instead of reconciling silently.

See [SECURITY.md](SECURITY.md) for the threat model and reporting process.

## Portability

| Tier | Meaning |
|------|---------|
| Markdown portable | Copy/paste into any agent that accepts Markdown |
| Export assisted | OpenAgents knows a documented prompt entry point |
| Auto-launch verified | A CLI version, OS, and result were reproduced |
| Community | Reported by contributors but not maintained as a guarantee |

Portability is a format property, not a claim that every agent integration was
tested. Current evidence belongs in the skill's export workflow and release
notes, not in a permanent universal compatibility promise.

## Development

```bash
bash scripts/validate.sh
```

The validator checks the three-skill layout, frontmatter, versions, manifests,
references, release configuration, fixture inventory, and static safety
contracts. Behavioral fixture execution remains a manual pre-release gate
because product runtime is instruction-only.

## Releases

Development is PR-first with `main` as the only permanent branch. Every PR must
carry exactly one `release:*` label. Eligible releases also require one
`change:*` category. After squash merge, a serialized GitHub workflow updates
the changelog and all version manifests, validates the result, commits the
release, creates the tag, and publishes the GitHub Release.

`release:none` skips versioning. Failed releases leave the merge intact and
open a deduplicated issue. Reruns resume the same version instead of incrementing
again. See [CONTRIBUTING.md](CONTRIBUTING.md) for labels and review rules.

No cleanup or local publish command is provided. Installation, update, and
removal belong to the `skills` CLI.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Security-sensitive changes require new
adversarial fixtures and a clean local validation run.
