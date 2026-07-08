# agentskills (canonical references)

Base source for the Agent Skills format, best practices, efficiency, and
prompt design. The openagents skill follows this standard — when in doubt,
prefer these links over ad-hoc decisions.

## Authoritative links

- **agentskills.io spec** — https://agentskills.io/specification
- **agentskills.io best practices** — https://agentskills.io/skill-creation/best-practices
- **optimizing descriptions** — https://agentskills.io/skill-creation/optimizing-descriptions
- **evaluating skills** — https://agentskills.io/skill-creation/evaluating-skills
- **client showcase** — https://agentskills.io/clients
- **Anthropic overview** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- **Anthropic best practices** — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- **Anthropic engineering blog** — https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

## Format (shared by agentskills.io + Anthropic)

- `SKILL.md` with YAML frontmatter: `name` (1-64, `^[a-z0-9]+(-[a-z0-9]+)*$`,
  no leading/trailing/double hyphens) and `description` (1-1024, what + when).
- Optional: `license`, `compatibility`, `metadata`, `allowed-tools`.
- Progressive disclosure: metadata (~100 tok) → SKILL.md body (<5000 tok) →
  `references/`, `scripts/`, `assets/` on demand. Keep SKILL.md under 500 lines,
  reference files under 50, references one level deep from SKILL.md.

## Best-practice principles

- **Concise is key**: assume the model is smart; justify every token.
- **Degrees of freedom**: narrow/low-freedom (exact scripts, fragile ops) vs
  open/high-freedom (general guidance, context-driven). Match to fragility.
- **Descriptions**: third person, specific, with trigger keywords; one field,
  both what and when.
- **Eval-driven**: build evals before docs; baseline → minimal instructions →
  iterate. Test across models (Haiku/Sonnet/Opus).
- **Feedback loops**: validator → fix → repeat for quality-critical steps.
- **Consistency**: one term throughout; no Windows paths; no time-sensitive
  info (use "old patterns" section); avoid offering too many options.
- **Scripts over generated code** for deterministic ops; handle errors, no
  "voodoo constants", make execute-vs-read intent explicit.
