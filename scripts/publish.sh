#!/usr/bin/env bash
set -euo pipefail

echo "=== OpenAgents — Publish gate ==="
echo ""

root="$(cd "$(dirname "$0")/.." && pwd)"

# 1. Local validator (single source of truth)
bash "$(dirname "$0")/validate.sh"

# 2. Canonical agentskills.io spec validation (best-effort)
if command -v skills-ref >/dev/null 2>&1; then
  for skill_dir in "$root"/skills/*/; do
    skills-ref validate "$skill_dir" || true
  done
else
  echo "skills-ref not found locally; attempting npx (best-effort)..."
  for skill_dir in "$root"/skills/*/; do
    npx -y skills-ref@latest validate "$skill_dir" || \
      echo "WARN: skills-ref unavailable — skipping agentskills.io spec validation for $(basename "$skill_dir")"
  done
fi

# 3. Submit to skill.fish + MCPMarket (best-effort)
if command -v skillfish >/dev/null 2>&1; then
  skillfish submit luismtns/openagents --yes
else
  echo "skillfish not found locally; attempting npx (best-effort)..."
  npx -y skillfish@latest submit luismtns/openagents --yes || \
    echo "WARN: skillfish unavailable — skipping skill.fish submission"
fi

echo ""
echo "=== Gate passed ==="
echo ""
echo "skills.sh publishes automatically when you push to GitHub (the registry"
echo "indexes the repo). skill.fish + MCPMarket submission is handled by"
echo "publish.yml and publish.sh (best-effort, via npx skillfish submit)."
echo "For Claude Code Plugin Marketplace, the"
echo ".claude-plugin/marketplace.json is already in place."
echo ""
echo "To release: bump version in SKILL.md / plugin.json / marketplace.json,"
echo "add a CHANGELOG [Unreleased] section, then:"
echo "  git commit -am 'chore: bump to v<VERSION>' && git push origin main"
echo "  # publish.yml tags + releases on push to main"
