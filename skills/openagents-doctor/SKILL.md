---
name: openagents-doctor
description: |
  Repair a broken OpenAgents multi-agent setup. Fixes missing symlinks,
  recreates broken skill links in agent paths, resolves version mismatches,
  and suggests targeted fixes for each issue found. Use when the user
  says "doctor", "repair", "fix setup", "fix symlinks", "resolve issues",
  or when status reports problems that need fixing. Does NOT report
  health — use `openagents` for that. Part of the OpenAgents
  multi-agent orchestration suite.
allowed-tools: Read Write Glob Grep Bash(test:*) Bash(echo:*)
  Bash(mkdir:*) Bash(ln:*) Bash(rm -rf .agents/rules) Bash(rm -f .claude/rules .cursor/rules .zed/rules) Bash(pwd:*) Bash(ls:*)
  Bash(uname:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents doctor

Diagnose and repair a broken OpenAgents multi-agent setup.

## Diagnostics

Run each check and report pass/fail:

1. **Global skill installed**: `test -f ~/.agents/skills/openagents/SKILL.md`
2. **AGENTS.md present**: `test -f AGENTS.md`
3. **Project rules exist**: `ls .agents/rules/*.md 2>/dev/null`
4. **Agent symlinks**:
   - `.claude/rules` -> `.agents/rules/`
   - `.cursor/rules` -> `.agents/rules/`
   - `.zed/rules` -> `.agents/rules/`
5. **Agent detection**: can the current agent be detected? Check env vars, config dirs, binaries.
6. **Version consistency**: check that installed version matches the expected latest.
7. **skills.sh.json valid**: parse and verify structure.

## Repairs

After each check, offer to fix on failure:

- **Missing symlink** -> create it
- **Missing AGENTS.md** -> suggest `openagents-init`
- **Missing global skill** -> `npx skills add luismtns/openagents -g -y`
- **Missing rules** -> suggest `openagents-rules` or create minimal conventions.md

## Report format

```
OpenAgents Doctor
==================
[PASS] Global skill installed
[FAIL] AGENTS.md -- missing -> run: openagents-init
[PASS] Project rules present (3 files)
[FAIL] .cursor/rules symlink -- broken -> repair? [Y/n]
[PASS] Agent detection
[PASS] Version consistency
[PASS] skills.sh.json valid

Summary: 5/7 passed, 2 issues found
```