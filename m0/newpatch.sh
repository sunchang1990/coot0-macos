#!/bin/bash
# newpatch.sh NAME -- record the current uncommitted edits in ./coot-src as patches/NAME.patch
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; NAME="$1"; [ -n "$NAME" ] || { echo "usage: newpatch.sh NNNN-name"; exit 1; }
cd "$HERE/coot-src"
git add -A >/dev/null 2>&1
git diff --cached --no-color --binary > "$HERE/patches/$NAME.patch"
git -c user.name=port -c user.email=port@localhost commit -qm "$NAME"
echo "wrote patches/$NAME.patch ($(grep -c '^diff --git' "$HERE/patches/$NAME.patch") files, $(wc -l < "$HERE/patches/$NAME.patch") lines)"
