---
name: openagents-add
description: |
  Create and register new skills or rules within an OpenAgents project.
  Generates a SKILL.md with frontmatter, registers the skill in
  skills.sh.json, and validates the structure. Use when the user says
  "add skill", "create skill", "register skill", "new skill",
  "add rule", or "create rule". Part of the OpenAgents multi-agent
  orchestration suite.
allowed-tools: Read Write Glob Grep Bash(test:*) Bash(echo:*)
  Bash(mkdir:*) Bash(ls:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents add

Create and register new skills or rules. Generates a SKILL.md with
frontmatter, registers in skills.sh.json, and validates the structure.

## Create a skill

| # | Step | Action |
|---|------|--------|
| 1 | Name | Lowercase kebab-case, matches directory, unique ecosystem-wide |
| 2 | Write SKILL.md | Frontmatter (see below) + instructions |
| 3 | References | Split into `references/<topic>.md` when >~200 lines. No frontmatter; heading: `# <name> <topic>` (space-separated, matching the other reference files) |
| 4 | Register | Add entry to `skills.sh.json` under `groupings` |
| 5 | Validate | Run validation script |

### SKILL.md frontmatter

```yaml
---
name: SKILL_NAME_HERE
description: |
  <what it does and when to use it>
  Triggers: <trigger phrases>.
allowed-tools: Read, Write, Glob, Grep, Bash(...)
version: 0.1.0
author: AUTHOR_NAME_HERE
license: MIT
user-invocable: true
tags: [<category>]
---
```

### Registration entry

```json
{"groupings": [{"title": "<category>", "description": "<group description>", "skills": ["<name>"]}]}
```

## Local install

Symlink into the agent's skill path:

```
mkdir -p ~/.agents/skills && ln -sfn $(pwd)/skills/<name> ~/.agents/skills/<name>
```