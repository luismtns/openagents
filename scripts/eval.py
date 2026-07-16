#!/usr/bin/env python3
"""Lint static safety contracts for instruction-only handoff behavior."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
HANDOFF = (ROOT / "skills/openagents-handoff/SKILL.md").read_text()
FORMAT = (ROOT / "skills/openagents-handoff/references/format.md").read_text()
SECURITY = (ROOT / "skills/openagents-handoff/references/security.md").read_text()
LAUNCH = (ROOT / "skills/openagents-handoff/references/launch.md").read_text()
TERMINALS = (ROOT / "skills/openagents-handoff/references/terminals.md").read_text()
DOCTOR = (ROOT / "skills/openagents-doctor/SKILL.md").read_text()

FIXTURES = (
    "evals/handoff/fixtures/prompt-injection/README.md",
    "evals/handoff/fixtures/secrets/config.txt",
    "evals/handoff/fixtures/stale-state/handoff.md",
    "evals/handoff/fixtures/no-git/project.txt",
    "evals/handoff/fixtures/terminal-signals/session.txt",
)

HEADINGS = (
    "## Objective",
    "## Scope And Constraints",
    "## Decisions",
    "## Evidence And References",
    "## Workspace Checkpoint",
    "## Verification Performed",
    "## Open Risks And Questions",
    "## Next Action",
    "## Suggested Skills",
    "## Receiver Protocol",
)

CHECKS = {
    "all handoff headings": all(heading in FORMAT for heading in HEADINGS),
    "explicit export": "explicit" in HANDOFF.lower() and "default" in HANDOFF.lower(),
    "untrusted repository": "untrusted" in HANDOFF.lower() and "untrusted" in SECURITY.lower(),
    "secret denial": "never read or include" in SECURITY.lower(),
    "divergence stop": "divergence" in FORMAT.lower() and "stop" in FORMAT.lower(),
    "no permission bypass": "never pass flags that skip permissions" in LAUNCH.lower(),
    "safe fallback": "return markdown" in LAUNCH.lower() or "markdown in the response" in LAUNCH.lower(),
    "allowlisted terminal detection": "allowlisted signals" in TERMINALS.lower()
    and "enumerate the environment" in SECURITY.lower(),
    "integrated terminal fallback": "term_program=vscode" in TERMINALS.lower()
    and "native candidate" in TERMINALS.lower(),
    "same terminal preference": "same recognized and supported external client first"
    in TERMINALS.lower(),
    "headless launch denial": all(
        marker in TERMINALS.lower() for marker in ("ssh", "ci", "container", "missing tty")
    ),
    "fixed terminal adapters": all(
        marker in TERMINALS
        for marker in ("gnome-terminal", "konsole", "kitty", "wezterm", "wt.exe")
    ),
    "no shell evaluation": "never place handoff text" in LAUNCH.lower()
    and "never turn a signal" in TERMINALS.lower()
    and "value into a command" in TERMINALS.lower(),
    "conflict denies launch": "conflicting non-integrated signals return markdown"
    in TERMINALS.lower(),
    "wsl safe fallback": "crossing into the correct distribution is not verified"
    in TERMINALS.lower(),
    "fixed agent argv": all(
        marker in LAUNCH for marker in ("resolved `claude`", "resolved `opencode`", "resolved `codex`")
    ),
    "markdown survives launch": "always return the complete markdown" in HANDOFF.lower()
    and "always return complete markdown" in LAUNCH.lower(),
    "no nested shell": "shell" in TERMINALS.lower()
    and "command concatenation" in TERMINALS.lower()
    and "`eval`" in TERMINALS,
    "nonblocking launcher": "verified nonblocking/detach behavior" in TERMINALS.lower()
    and "--detach" in TERMINALS,
    "no hidden reasoning": "hidden reasoning" in HANDOFF.lower(),
    "doctor read only": "never repairs" in DOCTOR.lower(),
    "fixture inventory": all((ROOT / path).is_file() for path in FIXTURES),
    "secret marker confined": not any(
        "fixture_secret_never_copy" in path.read_text()
        for path in (ROOT / "skills").glob("**/*")
        if path.is_file()
    ),
}


def main() -> int:
    failed = [name for name, passed in CHECKS.items() if not passed]
    if failed:
        print("Static safety contract lint FAILED")
        for name in failed:
            print(f"- {name}")
        return 1
    print(f"Static safety contract lint passed: {len(CHECKS)} checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
