#!/bin/bash
# run-api-examples.sh [RESULTS.jsonl] [ONLY-substring]   (build 26)
# Tries the example of every Python and Scheme scripting function listed in docs/api (about 1,700 functions,
# 30-60 minutes) without a window, on the test data, and writes one JSON line per call.  A call that stops Coot
# (no screen, OpenGL) or hangs (more than 60 s) is recorded and the run goes on in a fresh Coot.
# This is what produced the "Tried" column of docs/api; run it again to check your own installation.
HERE="$(cd "$(dirname "$0")/.." && pwd)"
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi
W="$STATE/work/api-examples"; mkdir -p "$W/home"   # (its own home: no function may change your coot0 settings)
RES="${1:-$W/api-examples.jsonl}"; ONLY="$2"
INDEX="$HERE/docs/api/api-index.json"
[ -f "$INDEX" ] || { echo "no $INDEX"; exit 2; }
cp "$HERE"/test-data/tutorial-modern.pdb "$HERE"/test-data/rnasa-1.8-all_refmac1.mtz "$W/"
touch "$RES"
lines() { wc -l < "$RES" | tr -d ' '; }
last_start() { tail -1 "$RES" | grep '"ev": "start"'; }
mark() {  # status, why  -> an "end" line for the call that was running
  local s; s=$(last_start); [ -z "$s" ] && return
  local key lang; key=$(echo "$s" | sed 's/.*"key": "\([^"]*\)".*/\1/'); lang=$(echo "$s" | sed 's/.*"lang": "\([^"]*\)".*/\1/')
  echo "{\"ev\": \"end\", \"key\": \"$key\", \"lang\": \"$lang\", \"status\": \"$1\", \"why\": \"$2\"}" >> "$RES"
}
killtree() { local c; for c in $(pgrep -P "$1"); do killtree "$c"; done; kill -9 "$1" 2>/dev/null; }  # Coot itself, not only the subshell
runs=0
while :; do
  runs=$((runs+1)); [ $runs -gt 3000 ] && { echo "too many restarts"; break; }
  grep -q '"ev": "done"' "$RES" && break
  ( cd "$W" && COOT_HOME_OVERRIDE="$W/home" API_INDEX="$INDEX" API_RESULTS="$RES" API_ONLY="$ONLY" COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 COOT_KEEP_CWD=1 \
      "$HERE/run-coot.sh" --no-graphics --python --no-state-script --no-startup-scripts --script "$HERE/tests/api_examples_run.py" > "$W/last-run.log" 2>&1 ) &
  pid=$!; n=$(lines); idle=0; limit=150
  while kill -0 $pid 2>/dev/null; do
    sleep 1; m=$(lines)
    if [ "$m" != "$n" ]; then n=$m; idle=0; limit=60; else idle=$((idle+1)); fi
    if [ $idle -ge $limit ]; then killtree $pid; wait $pid 2>/dev/null; mark hung "no answer after 60 s (killed)"; break; fi
  done
  wait $pid 2>/dev/null; rc=$?
  if [ -n "$(last_start)" ]; then mark crash "Coot stopped while running it without a screen (rc $rc)"; fi
  if [ $rc -eq 4 ]; then echo "setup failed (see $W/last-run.log)"; break; fi
done
ok=$(grep -c '"status": "ok"' "$RES"); er=$(grep -c '"status": "error"' "$RES"); cr=$(grep -c '"status": "crash"' "$RES")
hu=$(grep -c '"status": "hung"' "$RES"); sk=$(grep -c '"status": "skipped"' "$RES")
echo "api examples: $ok ran, $er gave an error, $cr stopped Coot (no screen), $hu hung, $sk not run automatically; Coot started $runs times"
echo "results: $RES"
