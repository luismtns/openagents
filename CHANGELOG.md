# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [1.0.0] - 2026-07-08

### Added

- 6 core skills: openagents-setup, openagents-init, openagents-rules, openagents-sync, openagents-audit, openagents-skills
- Agent-agnostic distribution via skills.sh
- Claude Code plugin format
- Local validator script and CI workflows
- skills.sh.json with orchestration and maintenance groupings
- Project rules (.agents/rules/)
- Makefile with validate and clean targets

### Upgrade Notes

```bash
npx skills add luismtns/openagents
```
