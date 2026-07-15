# Doctor adversarial cases

| Case | Expected classification |
|------|-------------------------|
| All three v2 skills visible at one consistent version | PASS |
| Legacy skill still visible | WARN |
| Missing handoff skill | FAIL |
| CLI binary absent | WARN with Markdown fallback |
| Arbitrary symlink target | FAIL after resolved-target comparison |
| Agent identity inferred only from API key | UNKNOWN |
| Non-Git project | WARN |
| Check requires reading a secret value | FAIL and do not read |

Doctor never repairs any case. It returns sanitized evidence and manual steps.
