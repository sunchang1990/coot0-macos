#!/bin/bash
# installer_test.sh -- tests install.sh / coot0 / uninstall.sh in throw-away "home" folders (your own home is not touched).
# A copy of this folder (APFS clone: seconds, no extra space) with the download flag set on some files is installed twice for a
# zsh user and once for a bash user; coot0 is started (without a window) from a project folder; uninstall.sh is run.
# Prints PASS / FAIL lines and "SUMMARY n / m".  About 1-2 minutes.
HERE="$(cd "$(dirname "$0")/.." && pwd -P)"
SYS=/usr/bin:/bin:/usr/sbin:/sbin
T="$(mktemp -d "${TMPDIR:-/tmp}/coot0 installer test.XXXXXX")"
n=0; p=0
check() { n=$((n+1)); if eval "$2" >/dev/null 2>&1; then p=$((p+1)); echo "PASS $1"; else echo "FAIL $1"; fi; }
VERSION="$(cat "$HERE/VERSION" 2>/dev/null || echo none)"

PKG="$T/Down loads/Coot0 package"; mkdir -p "$T/Down loads"
cp -Rc "$HERE" "$PKG" 2>/dev/null || ditto "$HERE" "$PKG"
for d in logs work home results .cache; do [ -d "$PKG/$d" ] && find "$PKG/$d" -mindepth 1 -delete 2>/dev/null; done
for f in bin/coot-bin run-coot.sh lib/libgtk-quartz-2.0.0.dylib; do xattr -w com.apple.quarantine "0083;6734a1b2;Safari;" "$PKG/$f" 2>/dev/null; done

# ---- zsh user, default folder
H1="$T/home zsh"; mkdir -p "$H1"
( cd "$PKG" && env -i HOME="$H1" PATH=$SYS TMPDIR="$T" COOT0_LOGIN_SHELL=/bin/zsh ./install.sh --yes --no-self-test ) > "$T/install1.txt" 2>&1
rc=$?
D1="$H1/.local/share/coot0/$VERSION"; D1R="$(cd "$D1" 2>/dev/null && pwd -P)"   # coot0 records the real path (/tmp -> /private/tmp)
check "install.sh exists and finishes (exit 0)" "[ -x '$PKG/install.sh' ] && [ $rc = 0 ]"
check "installed into ~/.local/share/coot0/<version> with the marker file" "[ -x '$D1/bin/coot-bin' ] && [ -f '$D1/.coot0-installed' ]"
check "the installed copy has no download flag (quarantine)" "! xattr -r -l '$D1' | grep -q com.apple.quarantine"
check "the installer said it removed the download flag" "grep -q 'removed the download flag' '$T/install1.txt'"
check "~/.local/bin/coot0 exists, is executable and points to the installed copy" "[ -x '$H1/.local/bin/coot0' ] && [ -n '$D1R' ] && grep -qF 'COOT0_HOME=\"$D1R\"' '$H1/.local/bin/coot0'"
check "~/.zshrc gets one marked PATH line, and the installer printed it" "[ \$(grep -c '^# coot0-install' '$H1/.zshrc') = 1 ] && grep -qF 'export PATH=\"\$HOME/.local/bin:\$PATH\"' '$H1/.zshrc' && grep -q 'added to .*\.zshrc' '$T/install1.txt'"
check "zsh user without bash files: no ~/.bash_profile or ~/.bashrc created" "[ ! -e '$H1/.bash_profile' ] && [ ! -e '$H1/.bashrc' ]"

# (build 19) the package carries its licences: GPL-3.0 text, the licensing statement, the source offer, the third-party list,
# and a licence-text folder for every conda package in that list
check "the package has LICENSE (GPL-3.0), LICENSING.md, CORRESPONDING_SOURCE.md and THIRD_PARTY_LICENSES.md" "grep -q 'GNU GENERAL PUBLIC LICENSE' '$D1/LICENSE' && grep -q 'Version 3, 29 June 2007' '$D1/LICENSE' && grep -q 'Copyright (C) 2026' '$D1/LICENSING.md' && grep -q 'Written offer' '$D1/CORRESPONDING_SOURCE.md' && grep -q '^| rdkit ' '$D1/THIRD_PARTY_LICENSES.md'"
nmiss=$(awk -F'|' '/^\| [a-z0-9]/ && NF==6 {gsub(/ /,"",$2); print $2}' "$D1/THIRD_PARTY_LICENSES.md" 2>/dev/null | sort -u | while read c; do [ -d "$D1/licenses/$c" ] || echo "$c"; done | wc -l | tr -d ' ')
check "licence texts in licenses/ for the listed packages (missing: ${nmiss:-?})" "[ -d '$D1/licenses' ] && [ \$(ls '$D1/licenses' | wc -l) -ge 50 ] && [ '${nmiss:-x}' = 0 ]"
check "README-FIRST.txt says how coot0 is licensed" "grep -q '^LICENCE' '$D1/README-FIRST.txt'"

# ---- second install (an update of the same version): PATH line not repeated, the old copy is kept aside
( cd "$PKG" && env -i HOME="$H1" PATH=$SYS TMPDIR="$T" COOT0_LOGIN_SHELL=/bin/zsh ./install.sh --yes --no-self-test ) > "$T/install2.txt" 2>&1
check "installing again: still one PATH line in ~/.zshrc" "[ \$(grep -c '^# coot0-install' '$H1/.zshrc') = 1 ]"
check "installing again: the earlier copy is moved aside, not deleted" "ls -d '$D1'.replaced-* && [ -x '$D1/bin/coot-bin' ]"

# ---- coot0 from a project folder: works there, logs per user, launcher finds a Phenix 2.x reduce/probe in the home folder
PROJ="$T/my project"; mkdir -p "$PROJ" "$H1/phenix-9.9-0000/bin" "$T/no apps"
printf '#!/bin/sh\necho fake\n' > "$H1/phenix-9.9-0000/bin/reduce"; chmod 755 "$H1/phenix-9.9-0000/bin/reduce"
( cd "$PROJ" && env -i HOME="$H1" PATH=$SYS TMPDIR="$T" COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 COOT_APPS_DIR="$T/no apps" \
    "$H1/.local/bin/coot0" --no-graphics --python --no-state-script --no-startup-scripts --script "$D1/tests/install_check.py" ) > "$T/run.txt" 2>&1 &
pid=$!; for i in $(seq 1 240); do sleep 1; kill -0 $pid 2>/dev/null || break; done; kill -9 $pid 2>/dev/null; wait $pid 2>/dev/null
ST="$H1/Library/Application Support/coot0"
check "coot0 starts Coot (model, map, Scheme, Python)" "grep -q '^INSTALL-CHECK OK' '$T/run.txt'"
PROJ_REAL="$(cd "$PROJ" && pwd -P)"
check "coot0 works in the folder it is started from" "grep -qF 'cwd: $PROJ_REAL |' '$T/run.txt'"
check "logs and preferences go to ~/Library/Application Support/coot0, not into the installed copy" "ls '$ST'/logs/coot-*.log && [ -d '$ST/home' ] && [ -z \"\$(ls '$D1/logs')\" ]"
check "launcher finds reduce of a Phenix 2.x in the home folder (bin/reduce)" "grep -qF 'reduce=$H1/phenix-9.9-0000/bin/reduce' '$T/run.txt'"
check "coot0 uses the Retina (2x) 3D view by default" "grep -q '| retina=1 |' '$T/run.txt'"
( cd "$PROJ" && env -i HOME="$H1" PATH=$SYS TMPDIR="$T" COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 \
    "$H1/.local/bin/coot0" --legacy --no-graphics --python --no-state-script --no-startup-scripts --script "$D1/tests/install_check.py" ) > "$T/legacy.txt" 2>&1 &
pid=$!; for i in $(seq 1 240); do sleep 1; kill -0 $pid 2>/dev/null || break; done; kill -9 $pid 2>/dev/null; wait $pid 2>/dev/null
check "coot0 --legacy: standard resolution, Coot starts (the option is not passed on to Coot)" "grep -q '| retina=0 |' '$T/legacy.txt' && grep -q '^INSTALL-CHECK OK' '$T/legacy.txt' && ! grep -qi 'legacy' <(grep -iE 'unrecognized|unknown|invalid' '$T/legacy.txt')"
# the unpacked folder: remove the download flag that was set above on purpose first (starting a flagged coot-bin makes
# macOS show its "Not Opened" malware dialog on the screen: seen 13 Nov during the build-17/18 test runs)
xattr -dr com.apple.quarantine "$PKG" 2>/dev/null
( cd "$PROJ" && env -i HOME="$H1" PATH=$SYS TMPDIR="$T" COOT_NO_SPLASH=1 COOT_NO_DEFAULT_TOOLBAR=1 \
    "$PKG/run-coot.sh" --no-graphics --python --no-state-script --no-startup-scripts --script "$D1/tests/install_check.py" ) > "$T/folder.txt" 2>&1 &
pid=$!; for i in $(seq 1 240); do sleep 1; kill -0 $pid 2>/dev/null || break; done; kill -9 $pid 2>/dev/null; wait $pid 2>/dev/null
check "the unpacked folder (./run-coot.sh, not installed) keeps the standard resolution, and Coot starts" "grep -q '| retina=0 |' '$T/folder.txt' && grep -q '^INSTALL-CHECK OK' '$T/folder.txt'"
check "no Coot started by this test was a copy with the download flag" "! grep -q 'quarantine flag' '$T/folder.txt' '$T/run.txt' '$T/legacy.txt'"
( cd "$PROJ" && env -i HOME="$H1" PATH=$SYS "$H1/.local/bin/coot0" --diagnose ) > "$T/diag.txt" 2>&1
check "coot0 --diagnose reports the Mac and the installed version" "grep -q 'Checking this Mac' '$T/diag.txt' && grep -qF 'installed version: $D1' '$T/diag.txt'"

# ---- bash user with an existing ~/.bashrc, own folder (--prefix)
H2="$T/home bash"; mkdir -p "$H2"; echo "# my bashrc" > "$H2/.bashrc"
( cd "$PKG" && env -i HOME="$H2" PATH=$SYS TMPDIR="$T" COOT0_LOGIN_SHELL=/bin/bash ./install.sh --yes --no-self-test --prefix "$H2/Applications/coot zero" ) > "$T/install3.txt" 2>&1
D2R="$(cd "$H2/Applications/coot zero/$VERSION" 2>/dev/null && pwd -P)"
check "--prefix: installed into the chosen folder" "[ -x '$H2/Applications/coot zero/$VERSION/bin/coot-bin' ] && [ -n '$D2R' ] && grep -qF 'COOT0_HOME=\"$D2R\"' '$H2/.local/bin/coot0'"
check "bash user: PATH line in ~/.bash_profile (login shells) and ~/.bashrc, and in ~/.zshrc" "grep -q '^# coot0-install' '$H2/.bash_profile' && grep -q '^# coot0-install' '$H2/.bashrc' && grep -q '^# coot0-install' '$H2/.zshrc' && grep -q '^# my bashrc' '$H2/.bashrc'"

# ---- uninstall (zsh user)
( env -i HOME="$H1" PATH=$SYS "$H1/.local/bin/coot0" --uninstall --yes ) > "$T/uninstall.txt" 2>&1
check "uninstall: coot0 command and installed copy removed" "[ ! -e '$H1/.local/bin/coot0' ] && [ ! -e '$D1' ]"
check "uninstall: PATH line removed from ~/.zshrc, a copy of the old file kept" "! grep -q 'coot0-install' '$H1/.zshrc' && grep -q 'coot0-install' '$H1/.zshrc.before-coot0-uninstall'"
check "uninstall --yes keeps the preferences and logs" "[ -d '$ST/logs' ]"

echo "SUMMARY $p / $n"
case "$T" in *"coot0 installer test."*) chmod -R u+w "$T" 2>/dev/null; rm -rf "$T";; esac
