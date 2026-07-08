#!/usr/bin/env bash
set -euo pipefail

errors=0
root="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== OpenAgents Skill Validation ==="
echo ""

for dir in "$root"/skills/*/; do
  name=$(basename "$dir")
  file="$dir/SKILL.md"
  echo "--- [$name] ---"

  if [ ! -f "$file" ]; then
    echo "  ERROR: SKILL.md not found"
    errors=$((errors+1))
    continue
  fi

  # Check required frontmatter fields (Anthropic 2026 spec)
  for field in name description allowed-tools version author license; do
    if ! grep -q "^${field}: " "$file"; then
      echo "  ERROR: missing '${field}' in frontmatter"
      errors=$((errors+1))
    fi
  done

  # Check "Use when" pattern in description
  if grep -q '^description:' "$file" && ! grep -q 'Use when' "$file"; then
    echo "  WARN: description missing 'Use when' pattern"
  fi

  # Check Bash scoping in allowed-tools
  if grep -q '^allowed-tools:' "$file"; then
    tools=$(grep '^allowed-tools:' "$file" | sed 's/^allowed-tools: *//')
    if echo "$tools" | grep -q '\bBash\b' && ! echo "$tools" | grep -q 'Bash('; then
      echo "  ERROR: Bash in allowed-tools must be scoped (e.g. Bash(git:*))"
      errors=$((errors+1))
    fi
  fi

  # Check name matches directory
  if grep -q '^name: ' "$file"; then
    fname=$(grep '^name: ' "$file" | sed 's/^name: *//')
    if [ "$fname" != "$name" ]; then
      echo "  ERROR: frontmatter name '${fname}' does not match directory '${name}'"
      errors=$((errors+1))
    fi
  fi

  # Check line count (progressive disclosure)
  lines=$(wc -l < "$file")
  if [ "$lines" -gt 200 ]; then
    echo "  WARN: ${lines} lines (consider splitting into references/)"
  fi

  echo "  OK (${lines} lines)"
  echo ""
done

echo "=== Results ==="
if [ "$errors" -gt 0 ]; then
  echo "FAILED: $errors validation errors"
  exit 1
fi
echo "All skills validated successfully"
