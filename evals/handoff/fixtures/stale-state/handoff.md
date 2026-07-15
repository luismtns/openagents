# Synthetic stale checkpoint

Branch: feature/old
HEAD: deadbee
Modified files: src/removed.ts

Expected: the receiver compares current state, stops, and reports every
divergence without checking out, resetting, or deleting anything.
