# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [1.5.0] - 2026-07-08

### Added

- `openagents` bare command and `openagents:status` — default workflow shows agent status, repo status, available commands, and next steps
- Multi-signal agent detection: env vars → running processes → config dirs → binaries (covers 14+ agents)
- Agent support expanded from 6 to 14: opencode, claude-code, cursor, codex, cline, zed, antigravity, deepagents, gemini-cli, github-copilot, kimi-code-cli, mimocode, warp, amp
- `references/status.md` — new reference file for the default status workflow
- Invocation section in SKILL.md clarifying `:` and space syntax are equivalent

### Changed

- `references/global.md` — comprehensive agent detection matrix with all 14 agents, multi-phase handshake
- `AGENTS.md` — updated with status subcommand and full agent list
- SKILL.md description triggers — added `detect agent`, `agent status`, `multi-agent setup`, `ecosystem check`

## [1.6.0] - 2026-07-08

### Added

- `openagents:rm` / `openagents rm` — remove rules, skills, AGENTS.md, symlinks, or all project artifacts
- `openagents:uninstall` / `openagents uninstall` — uninstall guidance via `npx skills remove openagents`
- `references/rm.md` — remove command with target-specific and batch removal
- `references/uninstall.md` — standard uninstall workflow with global/project detection
- Triggers expanded: `remove skill`, `delete skill`, `remove rules`, `delete rules`, `uninstall`, `cleanup`, `remove openagents`, `delete openagents`

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
