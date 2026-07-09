# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added

- **Multi-skill architecture**: each subcommand is now an independent skill
  (`openagents`, `openagents-global`, `openagents-init`, `openagents-add`,
  `openagents-rules`, `openagents-rm`, `openagents-doctor`, `openagents-info`,
  `openagents-upgrade`, `openagents-uninstall`) — each with its own SKILL.md,
  frontmatter, description, triggers, and allowed-tools, enabling precise
  agent activation and auto-discovery in opencode, claude-code, cursor, zed,
  and all agentskills.io-compatible agents
- `openagents-doctor`: diagnose and repair broken multi-agent setup
- `openagents-info`: display version, detected agents, distribution channels
- `openagents-upgrade`: execute `npx skills update` to fetch latest version
- `skills.sh.json`: all 10 sub-skills registered in the OpenAgents group

### Changed

- `skills/openagents/SKILL.md`: simplified to hub role — status + command
  palette + agent detection matrix (no longer a routing table for subcommands)
- `skills/openagents/references/`: removed subcommand references (moved to
  independent skills); only `status.md` remains
- `scripts/validate.sh`: updated required paths to match new multi-skill layout
- `.agents/rules/distributed-skills.md`: updated file layout diagram
- `AGENTS.md`: lists all 10 independent skills with invocation table
- `claude-plugin/.claude-plugin/plugin.json`: bumped to 1.12.0
- `.claude-plugin/marketplace.json`: bumped plugin version to 1.12.0

## [1.10.0] - 2026-07-08

### Added

- **Unified multi-agent setup**: openagents now treats `.agents/` (project) and `~/.agents/` (global) as the canonical source for skills **and** rules, symlinked into every agent's native path so the setup is identical across all agents you use
- `references/detect.md`: added `rules_path` column to the agent matrix (auto-discovery vs symlink per agent)
- `references/global.md`: handshake now symlinks **rules** globally (e.g. `~/.cursor/rules`, `~/.zed/rules`) for agents that don't auto-discover `~/.agents/rules/`, alongside skills
- `references/init.md` / `rules-validate.md`: symlink project rules for **all** detected agents (`.claude/rules`, `.cursor/rules`, `.zed/rules`), not just `.claude`
- `references/status.md`: replaced the single ecosystem check with a **multi-agent sync matrix** (skill linked? / rules linked? per agent) and clearer Next steps
- `SKILL.md`: new "Unified multi-agent setup" concept section stating the openagents promise

### Changed

- `distributed-skills.md`: documented that rules follow the same symlink model as skills across agents
- `README.md` "How it works": states the unified-setup promise and updates the diagram

## [1.9.1] - 2026-07-08

### Fixed

- README "How it works" Mermaid diagram now renders on GitHub (removed the `\n` line break and parentheses inside a quoted node that caused a parse error: `Cannot read properties of undefined (reading 'render')`)
- Reference heading convention unified to space-separated `# <name> <topic>` — the new `rules-*.md`/`detect.md` and `add.md` used colon syntax, conflicting with the project convention (1.7.0) and existing files like `# openagents global`

## [1.9.0] - 2026-07-08

### Added

- `references/detect.md` — canonical agent detection matrix, de-duplicated from `status.md`/`global.md`
- `.agents/rules/agentskills.md` — canonical Agent Skills references (agentskills.io + Anthropic) as base source
- `scripts/publish.sh` — local release gate (validator + `skills-ref` spec check)
- Ecosystem distribution matrix in `distributed-skills.md` (skills.sh, Claude Code Marketplace, agentskills.io, Anthropic, per-agent discovery)

### Changed

- `references/uninstall.md` rewritten to be defensively scoped to the openagents skill only (basename guard, explicit symlink/lock targets) with a mandatory "restart your agent" final step
- `references/status.md` now lists ALL subcommands (incl. `rm` subcommands, `uninstall`), not just recommended ones
- `references/rules.md` split into index + `rules-scan.md` / `rules-generate.md` / `rules-validate.md` to comply with the <50-line reference rule
- `references/global.md` / `status.md` now reference `detect.md` instead of duplicating the agent matrix
- `distributed-skills.md` expanded with canonical reference links and the Agent Skills ecosystem matrix
- `token-efficiency.md` line limit unified to <50 (was 40)

### Security

- `uninstall.md` explicitly warns that `clean.sh` is a global nuke and must not be used to uninstall only openagents

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
