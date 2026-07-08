#!/usr/bin/env bash
set -euo pipefail

echo "=== OpenAgents — Full Skill Cleanup ==="
echo ""
echo "This script removes ALL skills from your global skill paths"
echo "and clears the skills.sh npm/npx cache for a fresh start."
echo ""
echo "The following locations WILL be cleaned:"
echo "  ~/.agents/skills/*          — all installed skills"
echo "  ~/.agents/AGENTS.md         — global manifest"
echo "  ~/.claude/skills/*          — claude skill symlinks (if any)"
echo "  ~/.claude/rules/*           — claude rules symlinks (if any)"
echo "  ~/.cursor/skills/*          — cursor skill symlinks (if any)"
echo "  ~/.zed/skills/*             — zed skill symlinks (if any)"
echo "  skills-lock.json            — project lock file"
echo "  npm cache (skills package)  — cached npm tarballs"
echo "  npx cache (skills CLI)      — cached npx invocations"
echo ""

read -r -p "Proceed with full cleanup? [y/N] " reply
if [[ ! "$reply" =~ ^[Yy]$ ]]; then
  echo "Aborted."
  exit 1
fi

echo ""
removed=0

# ── 1. ~/.agents/skills/ ──────────────────────────────────────────
if [ -d "$HOME/.agents/skills" ]; then
  count=$(ls -1 "$HOME/.agents/skills" 2>/dev/null | wc -l)
  rm -rf "$HOME/.agents/skills"/*
  rm -rf "$HOME/.agents/skills"/.* 2>/dev/null || true
  echo "  Cleaned ~/.agents/skills/ ($count entries)"
  removed=$((removed + count))
fi

# ── 2. ~/.agents/AGENTS.md ────────────────────────────────────────
if [ -f "$HOME/.agents/AGENTS.md" ]; then
  rm "$HOME/.agents/AGENTS.md"
  echo "  Removed ~/.agents/AGENTS.md"
fi

# ── 3. ~/.claude/skills/ ──────────────────────────────────────────
if [ -d "$HOME/.claude/skills" ]; then
  count=$(ls -1 "$HOME/.claude/skills" 2>/dev/null | wc -l)
  # Remove only broken symlinks (pointing to deleted skills) and openagents-* entries
  find "$HOME/.claude/skills" -maxdepth 1 -type l ! -exec test -e {} \; -delete 2>/dev/null || true
  for d in "$HOME/.claude/skills"/openagents*; do
    [ -e "$d" ] || [ -L "$d" ] && rm -rf "$d" 2>/dev/null && echo "  Removed $d"
  done
  echo "  Cleaned ~/.claude/skills/ ($count entries scanned)"
fi

# ── 5. ~/.claude/rules/ symlinks ──────────────────────────────────
if [ -d "$HOME/.claude/rules" ]; then
  count=$(find "$HOME/.claude/rules" -maxdepth 1 -type l 2>/dev/null | wc -l)
  find "$HOME/.claude/rules" -maxdepth 1 -type l -exec rm {} \; 2>/dev/null || true
  for d in "$HOME/.claude/rules"/openagents*; do
    [ -e "$d" ] && rm -rf "$d" && echo "  Removed $d"
  done
  echo "  Cleaned ~/.claude/rules/ ($count symlinks removed)"
  removed=$((removed + count))
fi

# ── 6. ~/.cursor/skills/ ──────────────────────────────────────────
if [ -d "$HOME/.cursor/skills" ]; then
  count=$(ls -1 "$HOME/.cursor/skills" 2>/dev/null | wc -l)
  rm -rf "$HOME/.cursor/skills"/*
  rm -rf "$HOME/.cursor/skills"/.* 2>/dev/null || true
  echo "  Cleaned ~/.cursor/skills/ ($count entries)"
  removed=$((removed + count))
fi

# ── 7. ~/.zed/skills/ ─────────────────────────────────────────────
if [ -d "$HOME/.zed/skills" ]; then
  count=$(ls -1 "$HOME/.zed/skills" 2>/dev/null | wc -l)
  rm -rf "$HOME/.zed/skills"/*
  rm -rf "$HOME/.zed/skills"/.* 2>/dev/null || true
  echo "  Cleaned ~/.zed/skills/ ($count entries)"
  removed=$((removed + count))
fi

# ── 8. skills-lock.json ───────────────────────────────────────────
lockfile="$(cd "$(dirname "$0")/.." && pwd)/skills-lock.json"
if [ -f "$lockfile" ]; then
  rm "$lockfile"
  echo "  Removed skills-lock.json"
fi

# ── 9. npm cache (skills packages) ────────────────────────────────
npm cache ls 2>/dev/null | grep skills | while read -r entry; do
  npm cache clean "$entry" 2>/dev/null || true
done 2>/dev/null || true
echo "  Cleaned npm cache (skills packages)"

# ── 10. npx cache (skills CLI) ────────────────────────────────────
if [ -d "$HOME/.npm/_npx" ]; then
  # Remove npx caches that contain "skills"
  for d in "$HOME/.npm/_npx"/*/; do
    if [ -f "$d/package.json" ] && grep -q '"skills"' "$d/package.json" 2>/dev/null; then
      rm -rf "$d"
      echo "  Removed npx cache: $(basename "$d")"
      removed=$((removed + 1))
    fi
  done
fi

echo ""
echo "=== Done — $removed items cleaned ==="
echo ""
echo "To reinstall, run:"
echo "  npm cache clean skills  && npx skills add luismtns/openagents"
echo ""
echo "Or simply:"
echo "  npx skills add luismtns/openagents"
