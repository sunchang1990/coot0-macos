#!/bin/bash
# Gather everything needed to diagnose a first-light test into one text file (no personal data beyond system/display info and the logs).
HERE="$(cd "$(dirname "$0")" && pwd)"
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"                                    # (build 17) explicit
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"   # installed by install.sh: per user
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi
mkdir -p "$HERE/results"
OUT="$HERE/results/m1-results-$(date +%Y%m%d-%H%M%S).txt"
{
  echo "# Coot M1 test results  $(date)"
  echo "## system"; sw_vers; uname -m; sysctl -n machdep.cpu.brand_string 2>/dev/null
  echo "## folder: $HERE"
  if xattr -p com.apple.quarantine "$HERE/bin/coot-bin" >/dev/null 2>&1; then echo "download quarantine flag: SET  (run-coot.sh refuses to start; clear it with:  xattr -dr com.apple.quarantine \"$HERE\" )"; else echo "download quarantine flag: not set"; fi
  echo "## displays"; system_profiler SPDisplaysDataType 2>/dev/null | grep -E "Chipset Model|Metal|Resolution|UI Looks|Retina|Display Type|Main Display" 
  echo; echo "## headless self-test (latest run)"
  for f in "$STATE"/work/headless-tests/*.txt; do [ -f "$f" ] && printf "%-22s %s\n" "$(basename "$f" .txt)" "$(grep -h '^SUMMARY' "$f" | tail -1)"; done
  [ -d "$STATE/work/headless-tests" ] || echo "(no headless self-test has been run yet: $STATE/work/headless-tests does not exist)"
  echo; echo "## GUI audit (latest results/gui-audit-*.txt; run ./tests/run-gui-audit.sh)"
  f=$(ls -t "$STATE"/results/gui-audit-*.txt 2>/dev/null | head -1); if [ -n "$f" ]; then echo "### $f"; cat "$f"; else echo "(no GUI audit has been run yet)"; fi
  echo; echo "## GUI smoke test (latest)"
  f=$(ls -t "$STATE"/results/gui-smoke-*.txt 2>/dev/null | head -1); if [ -n "$f" ]; then echo "### $f"; cat "$f"; else echo "(not run)"; fi
  echo; echo "## your answers"; cat "$HERE/results/answers.txt" 2>/dev/null
  echo; echo "## GL seam messages from all launches"; grep -h "coot-gl-seam" "$STATE"/logs/*.log 2>/dev/null | sort | uniq -c
  echo; echo "## RCrane, Traceback and ERROR lines of the last 3 launch logs (first 150 each; file:line)"
  ls -t "$STATE"/logs/coot-*.log 2>/dev/null | head -3 | while IFS= read -r f; do
    echo "### $f"; grep -n -E "RCrane|Traceback|ERROR::|Unbound variable|TypeError|NameError|AttributeError" "$f" | head -150 | cut -c1-300
  done
  echo; echo "## launch logs (last 3: first 60 and last 150 lines each)"
  ls -t "$STATE"/logs/coot-*.log 2>/dev/null | head -3 | while IFS= read -r f; do
    echo "### $f"; head -60 "$f"; echo "[...]"; tail -150 "$f"
  done
  echo; echo "## crash reports (latest 2, from ~/Library/Logs/DiagnosticReports)"
  ls -t ~/Library/Logs/DiagnosticReports/coot-bin* 2>/dev/null | head -2 | while read f; do echo "### $f"; head -c 30000 "$f"; echo; done
} > "$OUT" 2>&1
echo "Wrote $OUT"
echo "Please tell me it is done; I can read it from the test folder."
