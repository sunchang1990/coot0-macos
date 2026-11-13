#!/bin/bash
# dev_sync.sh BUNDLE_DIR  -- copy the Python / Scheme files you changed in m0/coot-src into an existing bundle (no recompile).
# Only files that already exist in the bundle are updated (a NEW file: copy it yourself and tell the assemble scripts).
# Mapping: python/X -> share/coot/python/X, rcrane/X -> share/coot/python/rcrane/X, scheme/X -> share/coot/scheme/X,
#          compat/pygtk2/X -> share/coot/python/X (the PyGTK-2 replacement); m1-package/tests/* -> BUNDLE/tests/, and the docs / launcher.
# C++ files are never synced: after editing them rebuild coot-bin (CLAUDE.md, "C++ rebuild").
set -e
HERE="$(cd "$(dirname "$0")/.." && pwd)"; B="${1:?usage: dev_sync.sh BUNDLE_DIR}"
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1
cd "$HERE/coot-src"
BASE=$(git rev-list --max-parents=0 HEAD | tail -1)
sync() { local src=$1 dst=$2; [ -f "$src" ] && [ -f "$dst" ] || return 0; cmp -s "$src" "$dst" || { rm -f "$dst"; cp "$src" "$dst"; echo "synced ${dst#$B/}"; }; }
while IFS= read -r f; do
  case "$f" in
    python/*)         sync "$f" "$B/share/coot/python/${f#python/}" ;;
    rcrane/*)         sync "$f" "$B/share/coot/python/rcrane/${f#rcrane/}" ;;
    scheme/*)         sync "$f" "$B/share/coot/scheme/${f#scheme/}" ;;
    compat/pygtk2/tests/*|compat/pygtk2/tools/*|compat/pygtk2/_gtk2_*.json) ;;
    compat/pygtk2/*)  sync "$f" "$B/share/coot/python/${f#compat/pygtk2/}" ;;
  esac
done < <( (git diff --name-only "$BASE"; git ls-files --others --exclude-standard) | sort -u )
# package files (tests, launcher, installer, docs): also NEW ones are copied (build 17)
put() { local src=$1 dst=$2; [ -f "$src" ] || return 0; cmp -s "$src" "$dst" 2>/dev/null || { rm -f "$dst"; cp -p "$src" "$dst"; echo "synced ${dst#$B/}"; }; }
for f in "$HERE"/m1-package/tests/*; do put "$f" "$B/tests/$(basename "$f")"; done
for f in TEST-PROTOCOL.md CHANGELOG.md collect-results.sh run-coot.sh install.sh uninstall.sh "Install coot0.command" README-FIRST.txt VERSION; do put "$HERE/m1-package/$f" "$B/$f"; done
# licence files (build 19): LICENSE / LICENSING.md / CORRESPONDING_SOURCE.md from the repository root, the generated list and texts from m1-package
for f in LICENSE LICENSING.md CORRESPONDING_SOURCE.md; do put "$HERE/../$f" "$B/$f"; done
put "$HERE/m1-package/THIRD_PARTY_LICENSES.md" "$B/THIRD_PARTY_LICENSES.md"
if [ -d "$HERE/m1-package/licenses" ]; then
  out=$(rsync -a --delete --itemize-changes "$HERE/m1-package/licenses/" "$B/licenses/" | wc -l | tr -d ' ')
  [ "$out" != "0" ] && echo "synced licenses/ ($out changes)"
fi
# uncommitted C++ edits are a reminder, nothing more
if [ -n "$(git status --porcelain | grep -E '\.(cc|c|h|hh|cpp|mm|m)$' || true)" ]; then
  echo "NOTE: uncommitted C++ edits (need a coot-bin rebuild):"; git status --porcelain | grep -E '\.(cc|c|h|hh|cpp|mm|m)$' | sed 's/^/  /'
fi
