#!/bin/bash
# run-real-window-checks.sh [OUT.txt]   (build 28)
# Opens Coot in a real window for about 10 s, sends key presses to the graphics window (no keyboard needed, nothing
# is typed into other apps) and checks that key bindings made in Python run: a plain key, Ctrl-T, and that Coot's own
# key "o" stays Coot's; and the Help menu (search, Keyboard Shortcuts) on the real menus.  Prints PASS / FAIL lines and "SUMMARY n / n".
HERE="$(cd "$(dirname "$0")/.." && pwd)"
export COOT0_NO_BROWSER=1   # (build 28) Help entries that open documents only print what they would open
OUT="${1:-}"; T=$(mktemp -d); mkdir -p "$T/home"
[ -z "$OUT" ] && OUT="$T/checks.txt"
rm -f "$OUT"
( cd "$T" && KEYTEST_OUT="$OUT" COOT_HOME_OVERRIDE="$T/home" COOT_NO_SPLASH=1 COOT_KEEP_CWD=1 \
    "$HERE/run-coot.sh" --no-state-script --script "$HERE/tests/real_window_checks.py" > "$T/run.log" 2>&1 ) &
pid=$!
for i in $(seq 90); do kill -0 $pid 2>/dev/null || break; sleep 1; done
if kill -0 $pid 2>/dev/null; then pkill -9 -P $pid 2>/dev/null; kill -9 $pid 2>/dev/null; echo "FAIL Coot did not finish within 90 s (log: $T/run.log)"; fi
[ -s "$OUT" ] && cat "$OUT" || { echo "FAIL no result (log: $T/run.log)"; tail -20 "$T/run.log"; }
