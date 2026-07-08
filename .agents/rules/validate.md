# validate

Before releasing or pushing, run the local validator:

```bash
bash scripts/validate.sh
```

## Manual e2e checklist

Run these steps to simulate what CI does:

### 1. Structure check

```
skills/openagents/SKILL.md       — main skill must exist
skills/openagents/references/    — 6 reference files for subcommands
claude-plugin/.claude-plugin/plugin.json
claude-plugin/skills             — must be symlink to ../../skills
scripts/validate.sh              — local validator
README.md, LICENSE, CHANGELOG.md, skills.sh.json
```

### 2. Frontmatter

| Field | Required | Notes |
|-------|----------|-------|
| `name` | yes | Must match directory name |
| `description` | yes | Must contain "Use when" |
| `allowed-tools` | yes | `Bash` must be scoped (e.g. `Bash(git:*)`) |
| `version` | yes | Valid semver |
| `author` | yes | |
| `license` | yes | |
| `user-invocable` | no | Include if skill is user-callable |
| `compatible-with` | no | List target agents |
| `tags` | no | Array of strings |

### 3. Temp install smoke test

```bash
tmpdir=$(mktemp -d)
mkdir -p "$tmpdir/skills"
ln -sfn "$(pwd)/skills"/* "$tmpdir/skills/"
# verify each symlink resolves
for d in "$tmpdir"/skills/*/; do
  [ -e "$d/SKILL.md" ] && echo "OK  $(basename "$d")" || echo "MISS $(basename "$d")"
done
rm -rf "$tmpdir"
```

### 4. Claude plugin check

- `claude-plugin/.claude-plugin/plugin.json` is valid JSON
- `claude-plugin/skills` symlink resolves to `../../skills`

### 5. skills.sh compatibility

- `skills.sh.json` uses `groupings` (not old `categories` format)
- `$schema` points to `https://skills.sh/schemas/skills.sh.schema.json`
- Each skill slug in `groupings` matches a directory under `skills/`
