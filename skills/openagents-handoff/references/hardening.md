# recommended companion hardening

`allowed-tools` grants what the skill needs; it cannot express "never add this
flag" or "never read this file" as an exception to an allow rule. Deny rules
are evaluated before allow rules and apply regardless of what the skill
requests or what an injected instruction attempts. Add these to the host's own
`settings.json` `permissions.deny` for defense in depth; they are not shipped
by the skill itself and nothing here changes skill behavior on its own.

Block known permission-bypass flags on every launch target:

```
Bash(* --dangerously-skip-permissions *)
Bash(* --allow-dangerously-skip-permissions *)
Bash(* --dangerously-bypass-approvals-and-sandbox *)
Bash(* --dangerously-bypass-hook-trust *)
Bash(* --auto *)
```

Block reads of common secret-shaped files regardless of any skill's allow
list:

```
Read(**/.env)
Read(**/.env.*)
Read(**/*.pem)
Read(**/id_rsa*)
Read(**/.ssh/**)
Read(**/.aws/**)
Read(**/credentials.json)
```

Re-check these patterns against each target CLI's own `--help` output when it
changes; flag names are the CLI's, not this skill's, and this list is a
snapshot, not a guarantee of completeness.
