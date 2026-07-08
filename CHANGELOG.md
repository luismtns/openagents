# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Fixed

- `validate.yml`: wrong hardcoded path `.claude-plugin/plugin.json` → broken CI pipeline.
  Now calls `validate.sh` as single source of truth; file structure checked by `validate.sh`
- `publish.yml`: missing `git tag` creation before `gh release create` — pipeline silently
  skipped release creation because tag already existed from a previous attempt
- `claude-plugin/.claude-plugin/marketplace.json`: removed from inside plugin directory
  (marketplace belongs at repo root, not inside a plugin)
- `scripts/validate.sh`: consolidated file structure checks into same script;
  added `required_paths` array covering all 17 mandatory files; added marketplace.json
  validation at root-level path

### Added

- `.claude-plugin/marketplace.json` (repo root) — proper Claude Code Plugin Marketplace
  format per `code.claude.com/docs/en/plugin-marketplaces`, with correct schema URL
  `https://json.schemastore.org/claude-code-plugin-manifest.json`
- Defensive CI/CD rules in `distributed-skills.md`: single validation source, fail-fast,
  pre-submit gate, dry-run release (tag only, never pushes code), tag guard, unreleased
  gate, path verification, no hardcoded paths in workflows

### Changed

- `distributed-skills.md`: corrected file layout (removed stale `.claude-plugin/`
  references, added correct marketplace and plugin paths); added Claude Code Marketplace
  distribution channel with example JSON; added defensive CI/CD rules section
- `validate.yml`: removed duplicate inline file structure check (now delegated to
  `validate.sh`); streamlined to just `validate.sh` + symlink verification

### Removed

- `claude-plugin/.claude-plugin/marketplace.json` — duplicative; marketplace format now
  lives at repo-root `.claude-plugin/marketplace.json` per official Claude Code spec

## [1.8.0] - 2026-07-08

### Added

- `.github/workflows/validate.yml` — CI validation on push/PR (frontmatter, file structure, symlinks)
- `.github/workflows/publish.yml` — CD release automation triggered by `[Unreleased]` changelog
- `.claude-plugin/.claude-plugin/marketplace.json` — Claude Plugin marketplace discovery
- Multi-channel distribution rules in `distributed-skills.md` (skills.sh, plugin, well-known, git URL, local)
- Release and versioning rules in `distributed-skills.md` (SemVer, CHANGELOG, tagging, CI/CD)
- Progressive disclosure guidelines aligned with agentskills.io spec

### Changed

- `distributed-skills.md` rewritten to match agentskills.io specification exactly (required fields: only `name` + `description`; all others optional)
- `validate.md` updated: `allowed-tools`/`version`/`author`/`license` now optional; added name regex, progressive disclosure, Claude Plugin, GitHub Actions checks
- `scripts/validate.sh` rewritten: aligned with agentskills.io spec; added name regex validation, description length check, JSON validation for skills.sh.json, reference file progressive disclosure, Claude Plugin workflow checks
- `plugin.json` bumped from `1.0.0` to `1.8.0` to match SKILL.md version

## [1.7.0] - 2026-07-08

### Added

- `.agents/rules/token-efficiency.md` — guidelines for minimizing token consumption in reference files
- Defensive sanity check in `openagents rules` — aborts gracefully if project is too minimal, suggests `openagents init`

### Changed

- `references/rules.md` rewritten: extracts real architecture from projects (entry points, configs, CI, directory tree), generates 3 positive rule files (`conventions.md`, `architecture.md`, `generation.md`) — never hardcoded paths, never prohibitive tone
- Colon syntax (`openagents:subcommand`) removed entirely from all docs — space-separated only, works in all agents
- All 7 reference files simplified: ~635 → ~300 total lines (47% reduction)
- Removed `detect_agent()` bash script and `ps aux`/`which` from reference files — replaced with declarative detection tables

### Removed

- `compatible-with` frontmatter field (duplicates routing info)

## [1.5.0] - 2026-07-08

### Added

- `openagents` bare command and `openagents status` — default workflow shows agent status, repo status, available commands, and next steps
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

- `openagents rm` — remove rules, skills, AGENTS.md, symlinks, or all project artifacts
- `openagents uninstall` — uninstall guidance via `npx skills remove openagents`
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
