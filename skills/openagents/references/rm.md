# openagents:rm

Remove project-level artifacts created by openagents subcommands.
Mirrors the creation side of `init`, `add`, and `global`.

## Usage

```
openagents:rm rules       # remove .agents/rules/ and agent symlinks
openagents:rm agents      # remove AGENTS.md
openagents:rm skill <name> # remove a skill from skills/<name>/
openagents:rm all          # remove everything created by openagents
openagents:rm symlinks     # remove agent-specific symlinks only
```

## Remove rules

Removes `.agents/rules/` and any agent-specific symlinks pointing to it:

```bash
# Remove rules directory
rm -rf .agents/rules

# Remove agent-specific symlinks
rm -f .claude/rules 2>/dev/null
rm -f .cursor/rules 2>/dev/null
```

## Remove AGENTS.md

```bash
rm -f AGENTS.md
```

## Remove a skill

Removes a skill directory created by `openagents:add`:

```bash
SKILL_NAME="<name>"
rm -rf "skills/$SKILL_NAME"
```

Also removes its entry from `skills.sh.json` if present:

```bash
# Remove the skill from the registry (Python helper)
python3 -c "
import json
with open('skills.sh.json') as f:
  cfg = json.load(f)
for g in cfg.get('groupings', []):
  g['skills'] = [s for s in g['skills'] if s != '$SKILL_NAME']
# Remove empty groups
cfg['groupings'] = [g for g in cfg['groupings'] if g['skills']]
with open('skills.sh.json', 'w') as f:
  json.dump(cfg, f, indent=2)
  f.write('\n')
" 2>/dev/null || echo "skills.sh.json not found or unchanged"
```

## Remove all

Run all of the above, plus clean up any remaining `.agents/` artifacts:

```bash
rm -rf .agents
rm -f AGENTS.md
rm -f .claude/rules .cursor/rules 2>/dev/null
```

## Safety

- All `rm` operations ask for confirmation before deleting
- The skill never removes files outside the current project directory
- `openagents:rm all` will not touch `~/.agents/` (global install) — use `openagents:uninstall` for that
