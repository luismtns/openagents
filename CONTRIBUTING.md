# Contributing

OpenAgents accepts focused changes to portable handoff, read-only status, and
diagnostics. Lifecycle management and configuration synchronization are out of
scope.

## Before opening a change

1. Add or update an adversarial fixture for behavioral changes.
2. Keep references one level below SKILL.md.
3. Run `bash scripts/validate.sh`.
4. Review `git diff --check` and the complete diff.
5. Describe any unverified agent or platform claim explicitly.

## Pull request workflow

- Create a temporary feature branch from `main`.
- Use conventional commits while preparing the PR.
- Use a concise, user-facing PR title; squash merge makes it the `main` commit.
- Apply exactly one version label: `release:major`, `release:minor`,
  `release:patch`, or `release:none`.
- Eligible releases require exactly one category: `change:added`,
  `change:changed`, `change:deprecated`, `change:removed`, `change:fixed`, or
  `change:security`.
- `release:none` must not have a `change:*` label.
- Delete the feature branch after merge.

The post-merge workflow owns version files, changelog release headings, tags,
and GitHub Releases. Contributors must not bump versions in feature PRs.

Do not include secrets, private repository content, generated lock files, or
unrelated formatting changes.

Security reports belong in GitHub Security Advisories, not public issues.
