#!/usr/bin/env sh
set -eu
echo "Installing Crayon CLI v0.5.8 (Python CLI)"
PYTHON=""
for candidate in python3 python; do
  if command -v "$candidate" >/dev/null 2>&1; then
    version="$("$candidate" -c 'import sys; print("%d.%d" % sys.version_info[:2])')"
    major="${version%%.*}"
    minor="${version#*.}"
    if [ "$major" -gt 3 ] || { [ "$major" -eq 3 ] && [ "$minor" -ge 10 ]; }; then
      PYTHON="$candidate"
      break
    fi
  fi
done
[ -n "$PYTHON" ] || { echo "Python 3.10+ is required." >&2; exit 1; }
"$PYTHON" -m pip install .
crayon doctor
echo "Installation complete."
