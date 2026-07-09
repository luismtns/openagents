---
name: openagents-upgrade
description: |
  Update the OpenAgents skill suite to the latest version. Executes
  `npx skills update` in a subagent to fetch and install the newest
  release from skills.sh. Use when the user says "upgrade", "update",
  "check for updates", "get latest", or "update openagents".
  Part of the OpenAgents multi-agent orchestration suite.
allowed-tools: Bash(npx skills update *)
disable-model-invocation: true
context: fork
version: 1.12.0
author: Luis Bovo <luis@luis.dev>
license: MIT
---

# openagents upgrade

Update the OpenAgents skill suite to the latest version.

## Upgrade process

1. Run `npx skills update` to fetch and install all skill updates
2. Verify the installation: `test -f ~/.agents/skills/openagents/SKILL.md`
3. Report the result:
   - **Success**: "OpenAgents updated successfully. Changes will take effect in your next session."
   - **Failure**: "Update failed. Try running `npx skills update` manually."

## Notes

- After upgrading, restart your agent session for changes to take effect.
- This updates all skills from skills.sh, not just OpenAgents.
- To check the current version before upgrading, use `openagents info`.