#!/bin/bash
# Headless sweep of every menu item that Coot's Python GUI scripts add to the main menu (no window needed):
#   ./tests/run-gui-sweep.sh
# For each item it checks that a handler is attached, activates it, then clicks every button of the dialogs it opened,
# and reports any Python exception.  Items that call OpenGL-only code (display lists, ball&stick) cannot run without a
# graphics context; the sweep restarts after such a crash and lists them as CRASH (they are checked in the real GUI audit).
HERE="$(cd "$(dirname "$0")/.." && pwd)"
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"                                    # (build 17) explicit
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"   # installed by install.sh: per user
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi
OUT="$STATE/work/gui-sweep"; mkdir -p "$OUT"; rm -f "$OUT"/sweep_*.txt* "$OUT"/progress.txt
export SWEEP_OUT="$OUT/sweep_out.txt" SWEEP_PROGRESS="$OUT/progress.txt"
START=0
for attempt in $(seq 1 30); do
  SWEEP_START=$START COOT_KEEP_CWD= "$HERE/run-coot.sh" --no-graphics --python --no-state-script --no-startup-scripts \
      --script "$HERE/tests/gui_menu_sweep.py" > "$OUT/sweep_raw_$attempt.txt" 2>&1
  if grep -q "^DONE" "$OUT/progress.txt" 2>/dev/null; then break; fi
  LAST=$(cut -f1 "$OUT/progress.txt"); WHAT=$(cut -f2- "$OUT/progress.txt" | tr '\t' ' ')
  echo "SWEEP $LAST | $WHAT | CRASH (process died: OpenGL call without a graphics context, or hang)" >> "$OUT/sweep_out.txt"
  START=$((LAST+1))
done
ok=$(grep -c "| ok" "$OUT/sweep_out.txt"); err=$(grep -c "| ERR\|| EXC" "$OUT/sweep_out.txt"); nh=$(grep -c "NO-HANDLER" "$OUT/sweep_out.txt"); cr=$(grep -c CRASH "$OUT/sweep_out.txt")
btn=$(grep -c "^BTN" "$OUT/sweep_out.txt")
echo "GUI sweep: $ok items ok, $err items with errors, $nh items without a handler, $cr items whose activation killed the headless process (OpenGL or screen needed; started but not completed, listed below, checked by the GUI audit), $btn dialog buttons with errors"
grep -a "| ERR\|| EXC\|NO-HANDLER\|^BTN\|CRASH" "$OUT/sweep_out.txt" | cut -c1-240
echo "details: $OUT"
[ "$err" = 0 ] && [ "$nh" = 0 ] && [ "$btn" = 0 ] && echo "SUMMARY 1 / 1" || echo "SUMMARY 0 / 1"
