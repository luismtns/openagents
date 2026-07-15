# Token efficiency

Guidelines for minimizing token consumption in AI agent reference files.

## Rules

- **Prefer declarative over imperative** — describe what to do in bullet points
  instead of writing inline bash scripts. Let the LLM generate code from the
  description.
- **Keep reference files under 50 lines** — longer files increase token cost for
  every invocation. If a file exceeds 50 lines, split into multiple files or
  simplify.
- **Use tables for structured data** — tables are token-efficient and
  LLM-friendly for status and diagnostic mappings.
- **No `ps aux` or `which`** — use `command -v`, `test -d`, `test -f`, env var
  checks instead. These work across Linux, macOS, and Windows.
- **No platform claims without tests** — prefer host tools, and document when a
  command or launch path is platform-specific.
- **Remove duplicate logic** — if the same function (e.g., `detect_agent`)
  appears in two reference files, move it to one and reference the other.
- **Use concise code blocks** — prefer short inline snippets over multi-line
  scripts. One-liners with `&&` / `||` are fine.
- **Minimize YAML/JSON frontmatter** — keep frontmatter to fields the skill
  framework actually parses. Remove optional fields like `compatible-with` that
  duplicate routing info.

## Why

Agents load reference files on demand, but every loaded line still competes
with task context. Short references make activation cheaper and easier to audit.
