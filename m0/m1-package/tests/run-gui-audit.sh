#!/bin/bash
# GUI audit of the real window.  Run this from Terminal on the Mac (it opens Coot, opens and closes every menu entry and
# dialog by itself for a few minutes, restarts Coot if one entry crashes it, and writes results/gui-audit-<time>.txt):
#     ./tests/run-gui-audit.sh            (everything)
#     COOT_AUDIT_ONLY="Calculate" ./tests/run-gui-audit.sh      (only menu paths matching a regular expression)
#     COOT_AUDIT_BUTTONS=0 ./tests/run-gui-audit.sh             (do not click the buttons inside dialogs)
#     COOT_AUDIT_HANG=120 ./tests/run-gui-audit.sh              (seconds without progress before Coot is killed and the entry is noted as HANG; default 300)
HERE="$(cd "$(dirname "$0")/.." && pwd)"
export COOT0_NO_BROWSER=1   # (build 28) Help entries that open documents only print what they would open
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"                                    # (build 17) explicit
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"   # installed by install.sh: per user
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi
export COOT_AUDIT_DIR="$STATE/work/gui-audit"; mkdir -p "$COOT_AUDIT_DIR" "$STATE/results"
rm -f "$COOT_AUDIT_DIR"/audit_out.txt* "$COOT_AUDIT_DIR"/progress.txt "$COOT_AUDIT_DIR"/coot_run_*.log
export COOT_AUDIT_EXIT=1
# The audit presses every button it finds, including "Save Preferences", "Save State", "Save Graphics Size and Positions" and Curlew's "Install".
# It therefore runs with a throw-away HOME and working directory, so nothing it does can leak into your own preferences, state files or work folder.
AUDIT_TMP="$(mktemp -d "${TMPDIR:-/tmp}/coot-audit.XXXXXX")"; mkdir -p "$AUDIT_TMP/home" "$AUDIT_TMP/cwd"
export COOT_HOME_OVERRIDE="$AUDIT_TMP/home" COOT_KEEP_CWD=1 COOT_NO_SPLASH=1
cd "$AUDIT_TMP/cwd"
HANG="${COOT_AUDIT_HANG:-300}"
START=0
echo "Coot GUI audit: Coot will open and work through every menu entry by itself (several minutes). Please do not touch the mouse or keyboard."
for attempt in $(seq 1 60); do
  COOT_AUDIT_START=$START "$HERE/run-coot.sh" --no-state-script --script "$HERE/tests/gui_audit.py" > "$COOT_AUDIT_DIR/coot_run_$attempt.log" 2>&1 < /dev/null &
  PID=$!
  # watchdog: the audit writes progress.txt before every entry and every button; a stalled Coot is killed after $HANG seconds
  (
    while kill -0 $PID 2>/dev/null; do
      sleep 5
      if [ -f "$COOT_AUDIT_DIR/progress.txt" ]; then
        AGE=$(( $(date +%s) - $(stat -f %m "$COOT_AUDIT_DIR/progress.txt") ))
        if [ $AGE -gt $HANG ] && ! grep -q "^DONE" "$COOT_AUDIT_DIR/progress.txt"; then
          echo "HANG" >> "$COOT_AUDIT_DIR/progress.txt"; kill -9 $PID 2>/dev/null; pkill -9 -f "coot-bin.*gui_audit.py" 2>/dev/null; break
        fi
      fi
    done
  ) &
  WD=$!
  wait $PID 2>/dev/null; kill $WD 2>/dev/null; wait $WD 2>/dev/null
  if grep -q "^DONE" "$COOT_AUDIT_DIR/progress.txt" 2>/dev/null; then break; fi
  LAST=$(head -1 "$COOT_AUDIT_DIR/progress.txt" | cut -f1); WHAT=$(head -1 "$COOT_AUDIT_DIR/progress.txt" | cut -f2- | tr '\t' ' ')
  case "$LAST" in ''|*[!0-9]*) echo "audit could not start (see $COOT_AUDIT_DIR/coot_run_$attempt.log)"; break;; esac
  KIND="CRASH"; grep -q "^HANG" "$COOT_AUDIT_DIR/progress.txt" && KIND="HANG"
  echo "AUDIT $LAST | $WHAT | $KIND | Coot ended while this entry was running (restarting after it)" | tee -a "$COOT_AUDIT_DIR/audit_out.txt"
  START=$((LAST+1))
done
R="$STATE/results/gui-audit-$(date +%Y%m%d-%H%M%S).txt"
cp "$COOT_AUDIT_DIR/audit_out.txt" "$R" 2>/dev/null
echo; echo "---- summary ----"
for k in ok WARN ERR NO-HANDLER SKIP CRASH HANG; do printf "%-11s %s\n" "$k" "$(grep -c "| $k |" "$R")"; done
echo "problems:"; grep -E "\| (WARN|ERR|NO-HANDLER|CRASH|HANG) \|" "$R" | cut -c1-260
echo "full list: $R"
echo "(the audit ran in the throw-away folder $AUDIT_TMP; your Coot preferences and work folder were not touched)"
