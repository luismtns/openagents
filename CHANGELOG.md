# Changelog

## 1.0.0 (2026-07-08)

### Added
- 6 core skills: openagents-install, openagents-init, openagents-setup-rules, openagents-sync, openagents-audit, openagents-skills
- Agent-agnostic distribution via skills.sh (`npx skills add luismtns/openagents`)
- Claude Code plugin format (`claude-plugin/.claude-plugin/plugin.json`)
- Local validator script (`scripts/validate.sh`)
- CI workflows for validation (push/PR) and publishing (tag)
- skills.sh.json with orchestration and maintenance groupings
- Project rules (`.agents/rules/validate.md`, `distributed-skills.md`)
- Makefile with install/validate/clean targets
