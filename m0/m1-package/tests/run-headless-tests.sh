#!/bin/bash
# Headless self-test of this installation (no window needed): ./tests/run-headless-tests.sh
# Runs Coot's embedded Python 3 and Guile 3 against the bundled data and prints one line per suite.
HERE="$(cd "$(dirname "$0")/.." && pwd)"
export COOT0_NO_BROWSER=1   # (build 28) Help entries that open documents only print what they would open
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"                                    # (build 17) explicit
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$HOME/Library/Application Support/coot0"   # installed by install.sh: per user
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$HOME/Library/Application Support/Coot-0.9.8.96"; fi   # same rule as run-coot.sh
OUT="$STATE/work/headless-tests"; mkdir -p "$OUT"
# A folder that came through a browser / AirDrop / cloud download carries the macOS quarantine flag and run-coot.sh refuses to start
# from it: every suite would then fail with an empty result.  Say so once, with the command that fixes it.
if [ -f "$HERE/lib/libgtk-quartz-2.0.0.dylib" ] && [ -z "$COOT_IGNORE_QUARANTINE" ] && xattr -p com.apple.quarantine "$HERE/bin/coot-bin" >/dev/null 2>&1; then
  echo "== headless tests NOT RUN: this folder still has the macOS download quarantine flag =="
  echo "Clear the flag once (if you trust this copy) and run the tests again:"
  echo "    xattr -dr com.apple.quarantine \"$HERE\""
  echo "    \"$HERE/tests/run-headless-tests.sh\""
  exit 3
fi
run() {  # name, extra-args, script, seconds
  local name=$1 extra=$2 script=$3 secs=${4:-180}
  rm -f "$OUT/$name.txt"
  ( COOT_NO_DEFAULT_TOOLBAR=1 COOT_KEEP_CWD= "$HERE/run-coot.sh" --no-graphics $extra --no-state-script --no-startup-scripts --script "$script" > "$OUT/$name.txt" 2>&1 ) &
  local pid=$!
  for i in $(seq 1 $secs); do sleep 1; kill -0 $pid 2>/dev/null || break; done
  kill -0 $pid 2>/dev/null && { kill -9 $pid 2>/dev/null; echo "  (timeout)"; }
  wait $pid 2>/dev/null
  printf "%-26s %s\n" "$name" "$(grep -h '^SUMMARY' "$OUT/$name.txt" | tail -1)"
  grep -h '^FAIL' "$OUT/$name.txt" | sed 's/^/    /'
}
echo "== headless tests ($(date)) =="
run python-api     "--python" "$HERE/tests/api_python.py"
run scheme-api     ""         "$HERE/tests/api_scheme.scm"
run data-and-maps  "--python" "$HERE/tests/data_python.py"
run ondemand-make  "--python" "$HERE/tests/ondemand_make.py" 120 > /dev/null
run ondemand-read  "--python" "$HERE/tests/ondemand_read.py"
run refine-zone    "--python" "$HERE/tests/refine_python.py"
run process-helpers ""         "$HERE/tests/process_scheme.scm"
run api-docs       "--python" "$HERE/tests/api_docs_check.py"          # (build 26) docs/api matches this Coot
if [ -f "$HERE/lib/libgtk-quartz-2.0.0.dylib" ]; then   # self-contained bundle only
  run bundle-python   "--python" "$HERE/tests/bundle_python.py"
  run bundle-scheme   ""         "$HERE/tests/bundle_scheme.scm"
fi
if [ -f "$HERE/lib/libRDKitGraphMol.1.dylib" ]; then   # builds with RDKit ("enhanced ligand tools")
  run rdkit-python    "--python" "$HERE/tests/rdkit_python.py"
  run rdkit-scheme    ""         "$HERE/tests/rdkit_scheme.scm"
fi
if [ -f "$HERE/share/coot/python/_gtk2core.py" ]; then   # scripted GUI layer (PyGTK 2 compatibility on the bundled GTK 2)
  run gtk2compat      "--python" "$HERE/tests/gtk2compat_python.py"
  run gui-scripts     "--python" "$HERE/tests/gui_python_load.py"
  run gui-dialogs     "--python" "$HERE/tests/gui_python_dialogs.py"
  run gui-glyco       "--python" "$HERE/tests/gui_glyco_sliders.py" 240
  run gui-toolbar     "--python" "$HERE/tests/gui_toolbar_defaults.py" 240
  run gui-rcrane      "--python" "$HERE/tests/gui_rcrane.py" 900      # RCrane: trace / extend chain / rotamerize on tRNA 1EHZ (about 3-8 minutes)
  run refmac-run      "--python" "$HERE/tests/refmac_run_python.py" 480
  run cookbook        "--python" "$HERE/tests/cookbook_run.py" 900       # (build 26) every recipe of docs/cookbook, Python and Scheme
fi
# (build 17) install.sh / coot0 / uninstall.sh in throw-away home folders
if [ -x "$HERE/tests/installer_test.sh" ]; then
  bash "$HERE/tests/installer_test.sh" > "$OUT/installer.txt" 2>&1
  printf "%-26s %s\n" "installer" "$(grep -h '^SUMMARY' "$OUT/installer.txt" | tail -1)"; grep -h '^FAIL' "$OUT/installer.txt" | sed 's/^/    /'
fi
# the monomer library must be found completely at startup (a wrong path used to be silently papered over by on-demand loading)
bad=$(grep -h -E 'ERROR: dictionary|WARNING:: file .* does not exist|energy lib .* not found|link type .* not found' "$OUT"/data-and-maps.txt "$OUT"/refine-zone.txt 2>/dev/null | head -3)
if [ -z "$bad" ]; then printf "%-26s %s\n" "startup-dictionaries" "SUMMARY 1 / 1"; else printf "%-26s %s\n" "startup-dictionaries" "SUMMARY 0 / 1"; echo "$bad" | sed 's/^/    FAIL /'; fi
echo "full outputs: $OUT"
