# Distributed skills

## Public inventory

Exactly three skills are distributed:

- `openagents`
- `openagents-handoff`
- `openagents-doctor`

The same inventory must appear in `skills.sh.json`, the Claude plugin package,
README, and validation checks.

## Compatibility language

Agent Skills frontmatter provides packaging compatibility. Handoff content is
portable Markdown. Neither fact proves a particular agent discovers the skill
or can be launched automatically.

Record integrations by capability:

- Markdown portable
- Export assisted
- Auto-launch verified
- Community reported

Auto-launch verification records the agent CLI, terminal client, operating
system, and observed result.

## Releases

- Use SemVer across all skills, `package.json`, plugin, and marketplace.
- `package.json` is the version source; all other manifests must match it.
- Every PR declares one `release:*` label and eligible releases one `change:*`
  category. `release:none` performs no release.
- A merged eligible PR triggers a serialized workflow that updates changelog
  and versions, validates, commits to `main`, creates the tag, and creates the
  GitHub Release.
- Reruns resume a PR already present in the changelog instead of bumping again.
- Validation is mandatory and warnings are release failures.
- Actions are pinned by SHA and write permission exists only in release scope.
- Registry submission is a separate explicit maintainer action.
