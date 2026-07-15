# Generation

When changing a skill:

1. Update the smallest relevant SKILL.md or one-level reference.
2. Add an adversarial fixture when behavior or security changes.
3. Keep manifests limited to the three public skills.
4. Leave versions unchanged and select release/category labels on the PR.
5. Run `bash scripts/validate.sh`.
6. Present the unstaged diff for human review.

Do not add a new skill when an existing workflow can own the behavior. Do not
reintroduce setup, sync, rules generation, repair, update, uninstall, or cleanup
features without a new product review and threat model.
