# handoff terminal selection

Detect capabilities, not identity. Read only `TERM_PROGRAM` and the presence of
the allowlisted signals in SKILL.md; never enumerate or copy environment data.

1. Classify `uname -s`: Darwin is macOS; Linux is Linux; MINGW, MSYS, and
   CYGWIN are Windows. Linux plus `WSL_DISTRO_NAME` is WSL; return Markdown
   because crossing into the correct distribution is not verified.
2. Observed SSH, CI, container signals, and unknown OS return Markdown. A
   missing TTY also returns Markdown unless a recognized local terminal and GUI
   capability are independently observed; tool subprocesses may lack host TTY.
3. Treat `TERM_PROGRAM=vscode` as integrated even if inherited signals exist.
   Then recognize WT_SESSION, WEZTERM_PANE, KITTY_WINDOW_ID, KONSOLE_VERSION,
   GNOME_TERMINAL_SCREEN, ALACRITTY_WINDOW_ID, Apple_Terminal, and iTerm.app.
4. Conflicting non-integrated signals return Markdown; never turn a signal
   value into a command.
5. Try the same recognized and supported external client first. For integrated
   or unsupported clients, prefer the native candidate. Try only launchers
   found by `command -v`, in this fixed order: Linux `x-terminal-emulator`,
   `gnome-terminal`, `konsole`; macOS `Terminal.app`; Windows `wt.exe`.

| Adapter | Argument-safe invocation shape |
|---------|--------------------------------|
| GNOME Terminal | `gnome-terminal --working-directory=<cwd> -- <agent argv>` |
| Konsole | `konsole --workdir <cwd> -e <agent argv>` |
| Kitty | `kitty --detach --directory <cwd> <agent argv>` |
| WezTerm | `wezterm start --cwd <cwd> -- <agent argv>` |
| Linux default | `x-terminal-emulator -e <agent argv>`; inherit current cwd |
| Windows Terminal | `wt.exe -w new -d <cwd> <agent argv>` |
| Terminal.app | Open a restricted generated `.command` with `open -na Terminal` |

Use an adapter only if local help supports the shown shape. Its child argv must
start with the resolved Claude, OpenCode, or Codex executable; never use a shell
interpreter, `eval`, `-c`, `/c`, or command concatenation. Shell-quote each
dynamic argument independently and reject NUL or newline; uncertainty returns
Markdown. A macOS launcher must be mode 700 with one fixed `cd` and one `exec`.
Require verified nonblocking/detach behavior; foreground-only adapters are
unsupported. If same-client launch is unavailable, try the native candidate
once, then return Markdown and a sanitized command with no private paths.
