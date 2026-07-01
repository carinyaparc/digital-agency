#!/bin/sh
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/scripts/git-hooks/pre-commit"
DST="$ROOT/.git/hooks/pre-commit"

if [ ! -d "$ROOT/.git/hooks" ]; then
  echo "error: .git/hooks not found — run from a git checkout" >&2
  exit 1
fi

cp "$SRC" "$DST"
chmod +x "$DST"
echo "Installed pre-commit hook → $DST"
