---
name: openagents-info
description: |
  Display technical details about the OpenAgents installation: version
  number, list of installed sub-skills, detected AI coding agents,
  active distribution channels (skills.sh, skill.fish, plugin), and
  install path (global vs project). Use when the user says "info",
  "version", "about", "installed skills", "what's installed", or
  "show configuration". Does NOT check health — use `openagents status`
  for that. Does NOT repair — use `openagents doctor` for that.
  Part of the OpenAgents multi-agent orchestration suite.
allowed-tools: Read Bash(test:*) Bash(echo:*) Bash(pwd:*)
  Bash(ls:*) Bash(uname:*)
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents info

Display detailed information about the OpenAgents installation.

## Information to gather

1. **Version**: read from `skills/openagents/SKILL.md` frontmatter `version:`
2. **Installed sub-skills**: list `skills/openagents-*/SKILL.md` directories
3. **Global install check**: `test -f ~/.agents/skills/openagents/SKILL.md`
4. **Detected agents**: check env vars and config dirs for each agent type
5. **Install path**: where is the skill installed from (global vs project)?
6. **Distribution channels**: check `skills.sh.json`, `skillfish.json`, `plugin.json`
7. **Platform**: `uname -s` for OS information

## Report format

```
OpenAgents Info
================
Version:    1.12.0
Path:       /home/user/projects/myapp/.agents/skills/openagents (project)
Global:     installed at ~/.agents/skills/openagents
Sub-skills: openagents-global, openagents-init, openagents-add, ...

Detected agents:
  opencode   (env: OPENCODE_CALLER)
  claude-code (config: ~/.claude/)
  cursor     (binary: /usr/bin/cursor)

Distribution:
  skills.sh  active (skills.sh.json)
  skill.fish active (skillfish.json)
  plugin     active (plugin.json)

Platform: Linux x86_64
```