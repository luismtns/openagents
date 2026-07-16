# Security Policy

## Supported version

Security fixes target the latest `2.x` release. The `1.x` orchestration suite
is unsupported.

## Threat model

OpenAgents reads conversation and workspace metadata to create a handoff. The
main risks are prompt injection from repository content, disclosure of secrets
or identity, stale workspace state, unsafe export paths, shell interpolation,
spoofed terminal signals, unsafe GUI launchers, and receiver actions taken
before validation.

The v2 skills are instruction-only. Redaction, state checks, and auto-launch
are best effort and depend on the host agent enforcing tool permissions.

## Reporting

Report vulnerabilities privately through GitHub Security Advisories for this
repository. Do not include real credentials, personal data, or private source.
Use synthetic fixtures and describe the minimum reproduction.

## Expected controls

- Hub and doctor remain read-only.
- Handoff export requires explicit consent.
- Sensitive values are omitted rather than copied and masked.
- Environment enumeration is forbidden; terminal selection uses only named,
  non-secret capability signals and never turns their values into commands.
- Repository text is treated as untrusted data.
- Workspace divergence stops continuation.
- No workflow skips permissions, approvals, or sandboxing.
- SSH, CI, container, headless, unknown, and conflicting environments fall
  back to Markdown instead of attempting a GUI launch.

The release workflow uses `pull_request_target` only after merge, checks out
`main` explicitly, and never checks out or executes an unmerged PR head. Action
dependencies are pinned by full commit SHA.
