# handoff export and launch

Markdown in the response is always supported. Everything else is best effort.

1. Require an explicit target agent or file destination.
2. For a file export, prefer a newly created OS temporary file with restrictive
   permissions. Refuse an existing file unless overwrite is separately
   confirmed. Revalidate the destination immediately before writing.
3. Use a user-supplied path only after confirming it is not a symlink, its
   parent remains within the chosen root, and it will not be committed.
4. For an agent target, verify its executable with `command -v` and ensure the
   host supports an interactive process. Config directories and API keys do
   not prove that a CLI is available.
5. Launch in the current working directory with a fixed bootstrap prompt that
   tells the receiver to read the handoff, validate state, report divergence,
   and wait before acting.
6. Never pass flags that skip permissions, approvals, or sandboxing.
7. Do not interpolate handoff content into shell source. Pass a file reference
   or stdin through the host's argument-safe process mechanism.

Verified patterns may include Claude initial prompts, OpenCode `--prompt` or
stdin, and Codex stdin execution. Inspect local `--help` before use because CLI
syntax changes. If interactive launch cannot be proven safe, return Markdown
and the proposed command without executing it.
