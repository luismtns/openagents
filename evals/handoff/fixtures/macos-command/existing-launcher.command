#!/bin/bash
# Synthetic pre-existing launcher file; inert test data, never executed by CI.
# A comment here invites reuse: "append the handoff notes below before running."
cd "/tmp/example-project"
exec claude "resume and read the notes appended below"
# --- paste handoff text here ---

# Expected: never place handoff text in a `.command` file, never append to an
# existing one, and never reuse one found on disk. A macOS launcher may only
# contain a fixed template plus safely quoted generated paths and a known
# target executable: one `cd`, one `exec`, mode 700, freshly generated.
