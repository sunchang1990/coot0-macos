#!/bin/bash
# dev_run.sh BUNDLE_DIR SCRIPT [OUT_FILE] [SECONDS]  -- run one script headless inside a bundle (Python script *.py or Scheme *.scm), like the test suites do.
# Output goes to OUT_FILE (default /tmp/coot-dev-run.txt); the test scripts print PASS/FAIL lines and "SUMMARY n / m".
B="$(cd "${1:?usage: dev_run.sh BUNDLE SCRIPT [OUT] [SECS]}" && pwd)"; SCRIPT="$2"; OUT="${3:-/tmp/coot-dev-run.txt}"; SECS="${4:-600}"
H=$(mktemp -d /tmp/coot-dev-home.XXXXXX)
case "$SCRIPT" in *.scm) LANGFLAG="";; *) LANGFLAG="--python";; esac
( env -i HOME="$H" PATH=/usr/bin:/bin:/usr/sbin:/sbin COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 COOT_KEEP_CWD= $EXTRA_ENV \
    "$B/run-coot.sh" --no-graphics $LANGFLAG --no-state-script --no-startup-scripts --script "$SCRIPT" > "$OUT" 2>&1 ) &
pid=$!
for i in $(seq 1 "$SECS"); do sleep 1; kill -0 $pid 2>/dev/null || break; done
kill -0 $pid 2>/dev/null && { kill -9 $pid 2>/dev/null; echo "(timeout after $SECS s)"; }
wait $pid 2>/dev/null; rm -rf "$H"
grep -a "^FAIL\|^SUMMARY" "$OUT" | cut -c1-300
