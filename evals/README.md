# Evals

Each skill's `cases.md` documents adversarial scenarios and required results;
`fixtures/` holds the synthetic inputs those cases reference. `handoff/` also
has `rubric.md`, a human scoring sheet for release review.

`scripts/eval.py` is a static lint: it checks that the required safety
phrases appear in the skill prose, that every fixture file listed here
exists, and that no fixture's secret marker leaks into `skills/`. Passing it
proves the documented policy says the right things and the fixture inventory
is complete — it does not execute a live agent against these cases, so it is
not proof of runtime behavior. Treat a pass as a necessary floor, not a
substitute for periodically running the cases against a real agent session
and scoring the result against `rubric.md`.
