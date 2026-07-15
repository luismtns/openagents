#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$root/scripts/validate.py"
python3 "$root/scripts/eval.py"
python3 -m unittest discover -s "$root/tests" -p 'test_*.py'
git -C "$root" diff --check
