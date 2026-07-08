---
name: e2e-validate
description: |
  End-to-end validation for the OpenAgents skill repository.
  Installs all skills to a temporary directory, validates frontmatter,
  checks symlink integrity, verifies claude-plugin structure, and reports
  per-skill health. Designed for local CI during development.
  NOT distributed — internal tool only.
  Use when validating the repo before release.
  Triggers: e2e validate, validate repo, test skills, check distribution.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(ln:*), Bash(rm:*), Bash(cp:*), Bash(mkdir:*), Bash(diff:*), Bash(ls:*), Bash(echo:*), Bash(test:*), Bash(find:*), Bash(pwd:*), Bash(mktemp:*), Bash(chmod:*)
version: 1.0.0
author: Luis Bovo <luis@luis.dev>
license: MIT
user-invocable: true
compatible-with: opencode
tags: [openagents, internal, test, validate, e2e]
---

# e2e:validate

## Overview

End-to-end validation suite for the OpenAgents repository. Runs all checks that the CI would run, plus smoke tests. Safe to run repeatedly — uses a temp directory and cleans up.

## Workflow

### Phase 1: Structure

Check the repo has the required paths:

| Path | Must exist |
|------|-----------|
| `skills/*/SKILL.md` | All 6 skills |
| `claude-plugin/.claude-plugin/plugin.json` | Plugin manifest |
| `claude-plugin/skills` | Symlink to `../../skills` |
| `scripts/validate.sh` | Local validator |
| `README.md`, `LICENSE`, `CHANGELOG.md`, `skills.sh.json` | Distribution files |

Report any missing paths.

### Phase 2: Frontmatter validation

Run `bash scripts/validate.sh` and capture output. If it fails, report which skills failed and which fields are missing.

For each SKILL.md, verify:
- `name` matches enclosing directory name
- `description` contains "Use when"
- `allowed-tools` has Bash scoped
- `version`, `author`, `license`, `tags` present

### Phase 3: Temp install smoke test

```bash
tmpdir=$(mktemp -d)
mkdir -p "$tmpdir/skills"
ln -sfn "$(pwd)/skills"/* "$tmpdir/skills/"
```

Verify each symlink resolves to the correct source. Check the skill name from frontmatter matches the directory name.

Clean up: `rm -rf "$tmpdir"`

### Phase 4: Claude plugin check

Verify:
- `claude-plugin/.claude-plugin/plugin.json` has valid JSON with required fields
- `claude-plugin/skills` is a symlink pointing to `../../skills`
- The symlink resolves correctly

### Phase 5: Summary

Produce a report like:

```
e2e:validate — OpenAgents

Structure:  ✅ 12/12 paths OK
Frontmatter: ✅ 6/6 skills valid
Temp install: ✅ 6/6 symlinks OK
Plugin:       ✅ plugin.json valid, symlink OK
Total:        ✅ PASS
```

If any phase fails, report the specific failure and suggest the fix.
