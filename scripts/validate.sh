#!/usr/bin/env bash
set -euo pipefail

errors=0
warnings=0
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

  # === Required frontmatter (agentskills.io spec: name + description are the only required fields) ===
  for field in name description; do
    if ! grep -q "^${field}: " "$file"; then
      echo "  ERROR: missing required '${field}' in frontmatter"
      errors=$((errors+1))
    fi
  done

  # === Optional frontmatter warnings ===
  for field in allowed-tools version author license; do
    if ! grep -q "^${field}: " "$file"; then
      echo "  WARN: missing optional '${field}' in frontmatter (recommended for releases)"
      warnings=$((warnings+1))
    fi
  done

  # === "Use when" pattern in description ===
  if grep -q '^description:' "$file" && ! grep -q 'Use when' "$file"; then
    echo "  WARN: description missing 'Use when' pattern"
    warnings=$((warnings+1))
  fi

  # === Description length check ===
  if grep -q '^description:' "$file"; then
    desc_line=$(grep '^description: ' "$file" | head -1)
    desc_text="${desc_line#description: }"
    if [ ${#desc_text} -gt 1024 ]; then
      echo "  ERROR: description exceeds 1024 characters (${#desc_text})"
      errors=$((errors+1))
    fi
  fi

  # === Name regex validation ===
  if grep -q '^name: ' "$file"; then
    fname=$(grep '^name: ' "$file" | sed 's/^name: *//')
    if ! echo "$fname" | grep -qE '^[a-z0-9]+(-[a-z0-9]+)*$'; then
      echo "  ERROR: name '${fname}' must match ^[a-z0-9]+(-[a-z0-9]+)*$"
      errors=$((errors+1))
    fi
    if [ ${#fname} -gt 64 ]; then
      echo "  ERROR: name '${fname}' exceeds 64 characters (${#fname})"
      errors=$((errors+1))
    fi
    if [ "$fname" != "$name" ]; then
      echo "  ERROR: frontmatter name '${fname}' does not match directory '${name}'"
      errors=$((errors+1))
    fi
  fi

  # === Bash scoping in allowed-tools ===
  if grep -q '^allowed-tools:' "$file"; then
    tools=$(grep '^allowed-tools:' "$file" | sed 's/^allowed-tools: *//')
    if echo "$tools" | grep -q '\bBash\b' && ! echo "$tools" | grep -q 'Bash('; then
      echo "  ERROR: Bash in allowed-tools must be scoped (e.g. Bash(git:*))"
      errors=$((errors+1))
    fi
  fi

  # === Progressive disclosure: SKILL.md line count ===
  lines=$(wc -l < "$file")
  if [ "$lines" -gt 500 ]; then
    echo "  ERROR: ${lines} lines (500 max — must split into references/)"
    errors=$((errors+1))
  elif [ "$lines" -gt 200 ]; then
    echo "  WARN: ${lines} lines (consider splitting into references/)"
    warnings=$((warnings+1))
  fi

  # === References progressive disclosure ===
  ref_dir="$dir/references"
  if [ -d "$ref_dir" ]; then
    for ref_file in "$ref_dir"/*.md; do
      if [ -f "$ref_file" ]; then
        ref_lines=$(wc -l < "$ref_file")
        if [ "$ref_lines" -gt 50 ]; then
          echo "  WARN: $(basename "$ref_file") has ${ref_lines} lines (recommend < 50)"
          warnings=$((warnings+1))
        fi
      fi
    done
  fi

  echo "  OK (${lines} lines)"
  echo ""
done

# === skills.sh.json validation ===
echo "--- [skills.sh.json] ---"
if [ -f "$root/skills.sh.json" ]; then
  if ! echo "$(cat "$root/skills.sh.json")" | python3 -c "import sys,json; json.load(sys.stdin)" 2>/dev/null; then
    echo "  ERROR: skills.sh.json is not valid JSON"
    errors=$((errors+1))
  fi
  if grep -q '"$schema"' "$root/skills.sh.json"; then
    echo "  OK (schema present)"
  else
    echo "  WARN: skills.sh.json missing \$schema field"
    warnings=$((warnings+1))
  fi
else
  echo "  WARN: skills.sh.json not found"
  warnings=$((warnings+1))
fi
echo ""

# === Claude Plugin validation ===
echo "--- [claude-plugin] ---"
plugin="$root/claude-plugin/.claude-plugin/plugin.json"
if [ -f "$plugin" ]; then
  for field in name version description repository; do
    if ! grep -q "\"${field}\"" "$plugin"; then
      echo "  WARN: plugin.json missing '${field}'"
      warnings=$((warnings+1))
    fi
  done
  echo "  OK (plugin.json present)"
else
  echo "  WARN: claude-plugin/plugin.json not found"
  warnings=$((warnings+1))
fi
echo ""

# === GitHub Actions validation ===
echo "--- [.github/workflows] ---"
if [ -f "$root/.github/workflows/validate.yml" ]; then
  echo "  OK (validate.yml)"
else
  echo "  WARN: validate.yml not found"
  warnings=$((warnings+1))
fi
if [ -f "$root/.github/workflows/publish.yml" ]; then
  echo "  OK (publish.yml)"
else
  echo "  WARN: publish.yml not found"
  warnings=$((warnings+1))
fi
echo ""

echo "=== Results ==="
if [ "$errors" -gt 0 ]; then
  echo "FAILED: $errors error(s), $warnings warning(s)"
  exit 1
fi
echo "PASSED: $warnings warning(s)"
exit 0