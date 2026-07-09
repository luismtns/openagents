#!/usr/bin/env bash
set -euo pipefail

errors=0
warnings=0
root="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== OpenAgents Skill Validation ==="
echo ""

# === Skill validation ===
for dir in "$root"/skills/*/; do
  name=$(basename "$dir")
  file="$dir/SKILL.md"
  echo "--- [skills/$name] ---"

  if [ ! -f "$file" ]; then
    echo "  ERROR: SKILL.md not found"
    errors=$((errors+1))
    continue
  fi

  # Required frontmatter (agentskills.io spec: name + description only)
  for field in name description; do
    if ! grep -q "^${field}: " "$file"; then
      echo "  ERROR: missing required '${field}' in frontmatter"
      errors=$((errors+1))
    fi
  done

  # Optional frontmatter warnings
  for field in allowed-tools version author license; do
    if ! grep -q "^${field}: " "$file"; then
      echo "  WARN: missing optional '${field}' in frontmatter (recommended for releases)"
      warnings=$((warnings+1))
    fi
  done

  # "Use when" pattern in description
  if grep -q '^description:' "$file" && ! grep -q 'Use when' "$file"; then
    echo "  WARN: description missing 'Use when' pattern"
    warnings=$((warnings+1))
  fi

  # Description length
  if grep -q '^description: ' "$file"; then
    desc_line=$(grep '^description: ' "$file" | head -1)
    desc_text="${desc_line#description: }"
    if [ ${#desc_text} -gt 1024 ]; then
      echo "  ERROR: description exceeds 1024 characters (${#desc_text})"
      errors=$((errors+1))
    fi
  fi

  # Name regex
  if grep -q '^name: ' "$file"; then
    fname=$(grep '^name: ' "$file" | head -1 | sed 's/^name: *//')
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

  # Bash scoping
  if grep -q '^allowed-tools:' "$file"; then
    tools=$(grep '^allowed-tools:' "$file" | sed 's/^allowed-tools: *//')
    if echo "$tools" | grep -q '\bBash\b' && ! echo "$tools" | grep -q 'Bash('; then
      echo "  ERROR: Bash in allowed-tools must be scoped (e.g. Bash(git:*))"
      errors=$((errors+1))
    fi
  fi

  # Progressive disclosure: SKILL.md line count
  lines=$(wc -l < "$file")
  if [ "$lines" -gt 500 ]; then
    echo "  ERROR: ${lines} lines (500 max -- must split into references/)"
    errors=$((errors+1))
  elif [ "$lines" -gt 200 ]; then
    echo "  WARN: ${lines} lines (consider splitting into references/)"
    warnings=$((warnings+1))
  fi

  # References progressive disclosure
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

# === Required file structure ===
echo "--- [file structure] ---"
required_paths=(
  "skills/openagents/SKILL.md"
  "skills/openagents/references/status.md"
  "skills/openagents-global/SKILL.md"
  "skills/openagents-init/SKILL.md"
  "skills/openagents-add/SKILL.md"
  "skills/openagents-rules/SKILL.md"
  "skills/openagents-rules/references/scan.md"
  "skills/openagents-rules/references/generate.md"
  "skills/openagents-rules/references/validate.md"
  "skills/openagents-rm/SKILL.md"
  "skills/openagents-doctor/SKILL.md"
  "skills/openagents-info/SKILL.md"
  "skills/openagents-upgrade/SKILL.md"
  "skills/openagents-uninstall/SKILL.md"
  ".agents/rules/validate.md"
  ".agents/rules/distributed-skills.md"
  ".agents/rules/agentskills.md"
  "claude-plugin/.claude-plugin/plugin.json"
  "skills.sh.json"
  "skillfish.json"
  "CHANGELOG.md"
  "LICENSE"
  "README.md"
  ".github/workflows/validate.yml"
  ".github/workflows/publish.yml"
)

all_found=true
for f in "${required_paths[@]}"; do
  if [ -f "$root/$f" ]; then
    echo "  OK  $f"
  else
    echo "  MISS $f"
    all_found=false
    errors=$((errors+1))
  fi
done

if [ "$all_found" = true ]; then
  echo "  All required files present"
fi
echo ""

# === skills.sh.json validation ===
echo "--- [skills.sh.json] ---"
if [ -f "$root/skills.sh.json" ]; then
  if ! python3 -c "import sys,json; json.load(open(sys.argv[1]))" "$root/skills.sh.json" 2>/dev/null; then
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

# === Claude Plugin manifest ===
echo "--- [claude-plugin/plugin.json] ---"
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
  echo "  ERROR: claude-plugin/.claude-plugin/plugin.json not found"
  errors=$((errors+1))
fi
echo ""

# === Claude Code marketplace (root-level) ===
echo "--- [.claude-plugin/marketplace.json] ---"
marketplace="$root/.claude-plugin/marketplace.json"
if [ -f "$marketplace" ]; then
  if ! python3 -c "import sys,json; json.load(open(sys.argv[1]))" "$marketplace" 2>/dev/null; then
    echo "  ERROR: marketplace.json is not valid JSON"
    errors=$((errors+1))
  fi
  for field in name plugins; do
    if ! grep -q "\"${field}\"" "$marketplace"; then
      echo "  ERROR: marketplace.json missing required '${field}'"
      errors=$((errors+1))
    fi
  done
  echo "  OK (marketplace.json present and valid)"
else
  echo "  WARN: .claude-plugin/marketplace.json not found (recommended for plugin marketplace distribution)"
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