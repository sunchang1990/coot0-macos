#!/bin/bash
# setup.sh -- rebuild the patched Coot tree from the pristine source plus the numbered patch series.
# Usage: bash setup.sh            (creates ./coot-src, a git repo: baseline commit + patches applied)
#        COOT_PRISTINE=/path bash setup.sh
# To add a patch: edit files in ./coot-src, then:  bash newpatch.sh NNNN-short-name
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
PRISTINE="${COOT_PRISTINE:-$HOME/Downloads/coot-0.9.8.96}"
[ -d "$PRISTINE" ] || { echo "pristine tree not found: $PRISTINE"; exit 1; }
rm -rf "$HERE/coot-src"
cp -R "$PRISTINE" "$HERE/coot-src"
find "$HERE/coot-src" -name '._*' -delete
cd "$HERE/coot-src"
git init -q
git add -A >/dev/null 2>&1
git -c user.name=port -c user.email=port@localhost commit -qm "pristine 0.9.8.96"
n=0
for p in "$HERE"/patches/*.patch; do
  [ -f "$p" ] || continue
  git apply --whitespace=nowarn "$p" && n=$((n+1)) || { echo "FAILED to apply $p"; exit 1; }
done
git add -A >/dev/null 2>&1
git -c user.name=port -c user.email=port@localhost commit -qm "series applied" --allow-empty
echo "patched tree ready: $HERE/coot-src ($n patches applied)"
