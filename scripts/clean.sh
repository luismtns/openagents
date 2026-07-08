#!/usr/bin/env bash
set -euo pipefail

AGENTS_HOME="$HOME/.agents"
SKILLS_DIR="$AGENTS_HOME/skills"
MANIFEST="$AGENTS_HOME/AGENTS.md"

echo "=== OpenAgents Cleanup ==="
echo ""
echo "This script removes OpenAgents global skills and manifest."
echo "It does NOT touch project-local skills (./opencode/skills/, ./.claude/skills/)."
echo ""

# Discover
shopt -s nullglob
to_remove=("$SKILLS_DIR"/openagents-*)

if [ ${#to_remove[@]} -eq 0 ] && [ ! -f "$MANIFEST" ]; then
  echo "Nothing to clean — no OpenAgents skills or manifest found."
  exit 0
fi

echo "Will remove:"
for d in "${to_remove[@]}"; do
  echo "  symlink  $d"
done
if [ -f "$MANIFEST" ]; then
  echo "  file     $MANIFEST"
fi
echo ""

read -r -p "Proceed? [y/N] " reply
if [[ ! "$reply" =~ ^[Yy]$ ]]; then
  echo "Aborted."
  exit 1
fi

# Remove skill symlinks
removed=0
for d in "${to_remove[@]}"; do
  if [ -L "$d" ]; then
    rm "$d" && echo "  Removed symlink: $d" && removed=$((removed+1))
  elif [ -d "$d" ]; then
    rm -rf "$d" && echo "  Removed directory: $d" && removed=$((removed+1))
  fi
done

# Remove manifest
if [ -f "$MANIFEST" ]; then
  rm "$MANIFEST" && echo "  Removed manifest: $MANIFEST"
fi

echo ""
echo "=== Done — $removed skill(s) removed ==="
echo ""
echo "To reinstall, run:  npx skills add luismtns/openagents"
echo "                    cp AGENTS.md ~/.agents/AGENTS.md"
