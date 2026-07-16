# handoff export and launch

Markdown in the response is always supported. Everything else is best effort.

1. Require an explicit target agent or file destination.
2. For a file export, prefer a newly created OS temporary file with restrictive
   permissions. Refuse an existing file unless overwrite is separately
   confirmed. Revalidate the destination immediately before writing.
3. Use a user-supplied path only after confirming it is not a symlink, its
   parent remains within the chosen root, and it will not be committed.
4. For an agent target, verify its executable with `command -v`, inspect its
   local `--help`, and create the handoff in a restricted temporary file.
5. Follow [terminals.md](terminals.md). Detect capabilities before choosing a
   fixed adapter; terminal or agent binary presence never proves identity.
6. Launch in the current project directory with a fixed prompt that tells the
   receiver to read the file, validate state, report divergence, and wait.
7. Never pass flags that skip permissions, approvals, or sandboxing.
8. Pass an argument vector, not shell source. The macOS `.command` exception
   may contain only a fixed template plus safely quoted generated paths and a
   known target executable; never place handoff text in it.
9. Treat a zero launcher exit as `launch requested`, not proof that the target
   session opened. Always return complete Markdown in the source conversation;
   a nonzero exit or uncertain construction also gets a manual fallback.

Build `<agent argv>` only from these locally confirmed shapes:

| Target | Required help shape | Interactive argv |
|--------|---------------------|------------------|
| Claude | positional `[prompt]` | resolved `claude`, bootstrap prompt |
| OpenCode | `--prompt` | resolved `opencode`, `--prompt`, bootstrap prompt |
| Codex | positional `[PROMPT]` | resolved `codex`, bootstrap prompt |

The bootstrap is fixed except for the temporary handoff path. Unknown or
changed help returns Markdown; never improvise stdin piping or another target.
