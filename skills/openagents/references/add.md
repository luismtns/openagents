# openagents:add

Create and register new skills or rules in the multi-agent ecosystem.

Generates a skill directory with `SKILL.md`, registers it in
`skills.sh.json`, and validates the structure.

## Create a skill

### 1. Choose a name

The name must be lowercase kebab-case, match the directory name, and
be unique across the ecosystem.

```bash
SKILL_NAME="<name>"
mkdir -p skills/$SKILL_NAME
```

### 2. Write SKILL.md

```yaml
---
name: $SKILL_NAME
description: |
  <what the skill does and when to use it>
  Triggers: <space-separated trigger phrases>.
allowed-tools: Read, Write, Glob, Grep, Bash(...)
version: 0.1.0
author: <name>
license: MIT
user-invocable: true
tags: [<category>]
---

# $SKILL_NAME

<instructions>
```

Keep the description comprehensive — it's the primary trigger mechanism
for all agents.

### 3. Add references (if needed)

```bash
mkdir -p skills/$SKILL_NAME/references
```

Split content across reference files when the SKILL.md exceeds ~200 lines.
Each reference file has no frontmatter and starts with `# $SKILL_NAME:<topic>`.

### 4. Register in skills.sh.json

```json
{
  "groupings": [
    {
      "title": "<category>",
      "description": "<group description>",
      "skills": ["$SKILL_NAME"]
    }
  ]
}
```

### 5. Validate

```bash
bash scripts/validate.sh
```

## Distribution

After creating skills, distribute via:

```bash
npx skills add luismtns/<repo>
```

Or for local development:

```bash
mkdir -p ~/.agents/skills
ln -sfn $(pwd)/skills/* ~/.agents/skills/
```
