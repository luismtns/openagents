# openagents doctor checks

Run only checks supported by the host and report unavailable checks as UNKNOWN.

| Check | PASS | WARN / FAIL |
|-------|------|-------------|
| Suite | Host registry proves exactly the three v2 skills are visible | Missing v2 skill; no enumerable registry is UNKNOWN |
| Version | All visible skills report the same version | Mixed or unreadable versions |
| Git | Branch, HEAD, and status can be read | Not a Git repo is WARN, not FAIL |
| Handoff | Markdown output needs no integration | Required proprietary format is FAIL |
| Export | Requested CLI binary and TTY are available | Missing capability is WARN with Markdown fallback |
| Privacy | No secret value was read | Any request to inspect secret values is FAIL |

Legacy names: `openagents-global`, `openagents-init`, `openagents-add`,
`openagents-rules`, `openagents-rm`, `openagents-info`, `openagents-upgrade`,
`openagents-uninstall`, `openagents-audit`, `openagents-setup`,
`openagents-skills`, and `openagents-sync`.

Recommend manual commands only. Do not install, update, remove, relink, edit,
or invoke package managers.

Visibility means the current host's own skill listing or registry, not guessed
filesystem paths. OpenAgents v2 owns no symlinks, so unrelated links are out of
scope. CLI binaries are only observed capabilities, never agent identity.
