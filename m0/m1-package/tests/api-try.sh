#!/bin/bash
# api-try.sh FILE   (build 31) -- try scripting calls on the test data without a window; see tests/api_try.py.
# FILE: lines "py: ..." or "scm: ...", blocks separated by blank lines, each block in a fresh Coot. "#" lines are comments.
# Prints, for each line, the value, what it printed and what it changed (molecules, maps, view, settings).
HERE="$(cd "$(dirname "$0")/.." && pwd)"
IN="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi
W="${API_TRY_WORK:-$STATE/work/api-try}"; mkdir -p "$W/home"
OUT="$W/try-out.txt"; : > "$OUT"
killtree() { local c; for c in $(pgrep -P "$1"); do killtree "$c"; done; kill -9 "$1" 2>/dev/null; }
python3 -I -c '
import json, sys
blocks, cur = [], []
for l in open(sys.argv[1]):
    l = l.rstrip("\n")
    if not l.strip():
        if cur: blocks.append(cur); cur = []
        continue
    if l.lstrip().startswith("#"): continue
    cur.append(l)
if cur: blocks.append(cur)
for b in blocks: print(json.dumps(b))' "$IN" | while IFS= read -r BLOCK; do
  rm -rf "${W:?}/data"; "$HERE/tests/api-data.sh" "$W/data"
  ( cd "$W/data" && COOT_HOME_OVERRIDE="$W/home" API_INDEX="$HERE/docs/api/api-index.json" API_TRY_OUT="$OUT" API_TRY_HERE="$HERE/tests" \
      API_TRY_BLOCK="$BLOCK" COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 COOT_KEEP_CWD=1 \
      "$HERE/run-coot.sh" --no-graphics --python --no-state-script --no-startup-scripts --script "$HERE/tests/api_try.py" < /dev/null > "$W/last-try.log" 2>&1 ) &
  pid=$!; n=0
  while kill -0 $pid 2>/dev/null; do sleep 1; n=$((n+1)); [ $n -ge ${API_TRY_TIMEOUT:-120} ] && { killtree $pid; echo "   (block killed after $n s)" >> "$OUT"; break; }; done
  wait $pid 2>/dev/null; rc=$?
  tail -1 "$OUT" | grep -q -- "--- end of block" || echo "   (Coot stopped: rc $rc; last lines of the log:) $(tail -3 "$W/last-try.log" | tr '\n' ' ')" >> "$OUT"
done
cat "$OUT"
