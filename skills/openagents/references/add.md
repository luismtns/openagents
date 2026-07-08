# openagents add

Create and register new skills or rules. Generates a SKILL.md with
frontmatter, registers in skills.sh.json, and validates the structure.

## Create a skill

| # | Step | Action |
|---|------|--------|
| 1 | Name | Lowercase kebab-case, matches directory, unique ecosystem-wide |
| 2 | Write SKILL.md | Frontmatter (see below) + instructions |
| 3 | References | Split into `references/<topic>.md` when >~200 lines. No frontmatter; heading: `# <name>:<topic>` |
| 4 | Register | Add entry to `skills.sh.json` under `groupings` |
| 5 | Validate | Run validation script |

### SKILL.md frontmatter

```yaml
---
name: <name>
description: |
  <what it does and when to use it>
  Triggers: <trigger phrases>.
allowed-tools: Read, Write, Glob, Grep, Bash(...)
version: 0.1.0
author: <name>
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
