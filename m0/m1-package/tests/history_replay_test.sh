#!/bin/bash
# history_replay_test.sh  (build 35) -- the commands Coot writes (terminal echo, 0-coot-history.py, 0-coot-history.scm) can be
# replayed.  Without a window, in a throw-away folder:
#   1. Coot runs a few commands (model, two maps, settings whose recorded names were wrong in 0.9.8.96, a delete, Updating Maps'
#      calculate_maps_and_stats_py, then the echo switched to Scheme) and exits, writing its history files;
#   2. 0-coot-history.py is replayed in a fresh Coot (Python), 3. 0-coot-history.scm in another (Scheme): both must run to the
#      end without an error and give the same model (residue A41 deleted) and settings.
# Prints PASS / FAIL lines and "SUMMARY n / m".  About 1 minute.
HERE="$(cd "$(dirname "$0")/.." && pwd -P)"
T="$(mktemp -d "${TMPDIR:-/tmp}/coot0 history test.XXXXXX")"
n=0; p=0
check() { n=$((n+1)); if eval "$2" >/dev/null 2>&1; then p=$((p+1)); echo "PASS $1"; else echo "FAIL $1"; fi; }
TD="$HERE/test-data"
run() {  # output, script, extra args, folder: Coot without a window, in that folder, at most 180 s
  mkdir -p "$4"
  ( cd "$4" && COOT_KEEP_CWD=1 COOT_NO_DEFAULT_TOOLBAR=1 COOT_NO_SPLASH=1 "$HERE/run-coot.sh" --no-graphics --python \
      --no-startup-scripts $3 --script "$2" > "$1" 2>&1 ) &
  local pid=$!; for i in $(seq 1 180); do sleep 1; kill -0 $pid 2>/dev/null || break; done; kill -9 $pid 2>/dev/null; wait $pid 2>/dev/null
  sed -i '' $'s/\x1b\\[[0-9;]*m//g' "$1" 2>/dev/null     # the echo is bold: drop the terminal colour codes
}

cat > "$T/make.py" <<EOF
imol = read_pdb("$TD/tutorial-modern.pdb")
m = make_and_draw_map("$TD/rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
d = make_and_draw_map("$TD/rnasa-1.8-all_refmac1.mtz", "DELFWT", "PHDELWT", "", 0, 1)
set_imol_refinement_map(m)
set_scroll_by_wheel_mouse(1)
set_map_radius_em(20.0)
get_symmetry_as_calphas_state(imol)
set_auto_read_do_difference_map_too(1)
delete_residue(imol, "A", 41, "")
residue_exists_qm(imol, "A", 42, "")
calculate_maps_and_stats_py(imol, m, m, d)
if "coot0_set_command_echo" in globals(): coot0_set_command_echo("scheme")   # (build 35)
set_map_radius_em(21.0)
save_coordinates(imol, "saved.pdb")    # no unsaved changes, so coot_checked_exit quits without asking
coot_checked_exit(0)                   # (build 36) recorded in the history: replaying must not quit
EOF
run "$T/make.txt" "$T/make.py" "" "$T/make"
# keep the two files as written by this run (each later Coot run writes its own history into the folder it runs in)
cp "$T/make/0-coot-history.py" "$T/make/0-coot-history.scm" "$T/" 2>/dev/null
check "Coot wrote 0-coot-history.py and 0-coot-history.scm" "[ -s '$T/0-coot-history.py' ] && [ -s '$T/0-coot-history.scm' ]"
check "terminal echo is Python by default and names the real function: calculate_maps_and_stats_py(0, 1, 1, 2)" \
      "grep -qx 'calculate_maps_and_stats_py(0, 1, 1, 2)' '$T/make.txt' && ! grep -q '^(calculate-maps-and-stats' '$T/make.txt'"
check "coot0_set_command_echo(\"scheme\") switches the echo to Scheme: (set-map-radius-em 21.00)" "grep -qx '(set-map-radius-em 21.00)' '$T/make.txt'"
check "names that were wrong in 0.9.8.96 are recorded right (set-scroll-by-wheel-mouse, set-map-radius-em, get-symmetry-as-calphas-state, set-auto-read-do-difference-map-too)" \
      "grep -q '^(set-scroll-by-wheel-mouse 1)' '$T/0-coot-history.scm' && grep -q '^(set-map-radius-em 20.00)' '$T/0-coot-history.scm' && grep -q '^(get-symmetry-as-calphas-state 0)' '$T/0-coot-history.scm' && grep -q '^(set-auto-read-do-difference-map-too 1)' '$T/0-coot-history.scm'"
check "text arguments are recorded in quotes (0.9.8.96: (does-residue-exist-p 0 A 42 ))" "grep -qF '(does-residue-exist-p 0 \"A\" 42 \"\")' '$T/0-coot-history.scm' && grep -qF 'does_residue_exist_p(0, \"A\", 42, \"\")' '$T/0-coot-history.py'"
check "quitting is recorded as a comment in both files (build 35 replayed it and Coot quit)" "grep -qF '# coot_checked_exit(0)   -- Coot was quit here (not replayed)' '$T/0-coot-history.py' && grep -qF '; (coot-checked-exit 0)   -- Coot was quit here (not replayed)' '$T/0-coot-history.scm'"
check "a Python-only command is a comment in the Scheme history, with its Python call" \
      "grep -qF '; (calculate-maps-and-stats 0 1 1 2)   -- Python only: calculate_maps_and_stats_py(0, 1, 1, 2)' '$T/0-coot-history.scm'"

# replay: the history file, then a few lines that print what the replay produced
{ cat "$T/0-coot-history.py"; cat <<'EOF'

print("REPLAY-PY", graphics_n_molecules(), residue_exists_qm(0, "A", 41, ""), residue_exists_qm(0, "A", 42, ""), round(get_map_radius_em(), 1) if "get_map_radius_em" in globals() else "-")
coot_real_exit(0)
EOF
} > "$T/replay.py"
run "$T/replay-py.txt" "$T/replay.py" "--no-state-script" "$T/replay-py"
check "0-coot-history.py replays to the end without an error" "[ -s '$T/0-coot-history.py' ] && grep -q '^REPLAY-PY' '$T/replay-py.txt' && ! grep -qE 'Traceback|NameError|is not defined' '$T/replay-py.txt'"
check "  ... and gives the same result (3 molecules, A41 deleted, A42 there)" "grep -qE '^REPLAY-PY 3 False True' '$T/replay-py.txt'"
{ cat "$T/0-coot-history.scm"; cat <<'EOF'

(format #t "REPLAY-SCM ~a ~a ~a~%" (graphics-n-molecules) (residue-exists? 0 "A" 41 "") (residue-exists? 0 "A" 42 ""))
(coot-real-exit 0)
EOF
} > "$T/replay.scm"
run "$T/replay-scm.txt" "$T/replay.scm" "--no-state-script" "$T/replay-scm"
check "0-coot-history.scm replays to the end without an error" "[ -s '$T/0-coot-history.scm' ] && grep -q '^REPLAY-SCM' '$T/replay-scm.txt' && ! grep -qiE 'unbound variable|wrong number of arguments|^ERROR' '$T/replay-scm.txt'"
check "  ... and gives the same result (3 molecules, A41 deleted, A42 there)" "grep -qE '^REPLAY-SCM 3 #f #t' '$T/replay-scm.txt'"
echo "SUMMARY $p / $n"
[ -n "$KEEP_HISTORY_TEST" ] && echo "kept: $T" || rm -rf "${T:?}"
