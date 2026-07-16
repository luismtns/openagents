# Validation

Run the local gate before review:

```bash
bash scripts/validate.sh
```

The gate must fail on:

- Missing or extra public skill directories
- Invalid or unterminated frontmatter
- Name/directory mismatch
- Missing release metadata or inconsistent versions
- Unscoped Bash permissions
- Broken one-level reference links
- Invalid JSON manifests
- Manifest/skill inventory mismatch
- Missing governance or adversarial fixture files
- Missing terminal detection, fixed-adapter, or Markdown fallback contracts
- Missing PR label policy, recovery dispatch, or serialized release execution
- Reintroduction of the destructive cleanup script

Before commit, manually review `git status --short`, `git diff --stat`, full
`git diff`, `git diff --check`, handoff output, divergence handling, and secret
redaction. Registry publication and real releases are never part of local
validation.

For launch changes, also review detection precedence, argument separation,
headless denial, same-client preference, native fallback, and terminal-specific
claims.
