# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [1.4.0] - 2026-07-08

### Added

- Security badges in README (Socket, Snyk) linking to skills.sh audit pages
- `scripts/clean.sh` — comprehensive cleanup of all global skills, symlinks, and npm/npx caches
- Capability constraints table in SKILL.md documenting purpose and scope of each tool

### Changed

- Trimmed `allowed-tools` from 21 to 13 entries (removed unused: npx, npm, rm, diff, du, cat, wc, cp)
- `references/add.md`: replaced `npx skills add` distribution instruction with local-only symlink installation

### Security

- Fixed Snyk W012 (Medium): removed unverifiable external dependency reference (`npx skills add`)
- Fixed Socket Anomaly: narrowed tool scope, added capability proportionality documentation
- Added explicit note: skill does NOT execute downloaded code, make network requests, or install packages

## [1.3.0] - 2026-07-08

### Added

- Agent-agnostic handshake protocol in `references/global.md`
  - Detects running agent via env vars, config dirs, and process list
  - Maps agent-specific config paths and skill discovery locations
  - Creates symlinks for agents that don't auto-discover `~/.agents/skills/`
- `references/add.md` — scaffold new skills, register distribution, validate structure
- Mermaid architecture diagram in README showing full workflow
- Comprehensive trigger descriptions for all agents

### Changed

- Restructured from 6 subcommands to 4: `global`, `init`, `add`, `rules`
  - Removed: `sync`, `audit`, `skills` (too specialized; absorbed into `add`)
  - Renamed: `setup` → `global` (broader scope: handshake + ecosystem verification)
- Frontmatter follows opencode spec (`name`, `description`, `license`, `compatibility`,
  `metadata`) with Anthropic extras in `metadata` for claude-code/codex compatibility
- README now has Mermaid diagram + full documentation

### Removed

- `skills/openagents/references/setup.md`, `init.md`, `rules.md`, `sync.md`,
  `audit.md`, `skills.md` — replaced by 4 new references
- `.opencode/commands/` — custom commands are local config, not distribution

## [1.2.0] - 2026-07-08

### Changed

- Consolidated 6 individual skills into a single `openagents` package
- skills/openagents/SKILL.md routes all subcommands via routing table
- Each subcommand lives in `references/*.md`
