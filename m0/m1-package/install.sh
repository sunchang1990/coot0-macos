#!/bin/bash
# install.sh -- install Coot 0.9.8.96 for Apple Silicon ("coot0") for the current user.
#
#   ./install.sh                 check this Mac, copy Coot to ~/.local/share/coot0/<version> (you are asked; Enter = yes),
#                                write the command ~/.local/bin/coot0 and make sure it is on your PATH
#   ./install.sh --yes           the same without questions (default folder)
#   ./install.sh --prefix DIR    install into DIR/<version> instead of ~/.local/share/coot0/<version>
#   ./install.sh --diagnose      only report what this Mac has (also: coot0 --diagnose)
#   ./install.sh --no-self-test  skip the 30-second start test at the end
#
# Nothing outside these places is changed: <install folder>, ~/.local/bin/coot0, one marked PATH line in ~/.zshrc
# (and ~/.bash_profile / ~/.bashrc if you use bash), and ~/Library/Application Support/coot0 (your Coot preferences and logs,
# made at the first start).  uninstall.sh (also: coot0 --uninstall) undoes it.
set -u
SRC="$(cd "$(dirname "$0")" && pwd -P)"
VERSION="$(cat "$SRC/VERSION" 2>/dev/null || echo 0.9.8.96)"
MARK="# coot0-install"
BASE_DEFAULT="$HOME/.local/share/coot0"
BIN="$HOME/.local/bin"
STATE="$HOME/Library/Application Support/coot0"
ASK=1; PREFIX=""; DIAG_ONLY=""; SELFTEST=1
while [ $# -gt 0 ]; do
  case "$1" in
    --yes|-y) ASK="";;
    --prefix) PREFIX="${2:?--prefix needs a folder}"; shift;;
    --prefix=*) PREFIX="${1#--prefix=}";;
    --diagnose) DIAG_ONLY=1;;
    --no-self-test) SELFTEST="";;
    -h|--help) sed -n '2,14p' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "install.sh: unknown option $1 (see ./install.sh --help)"; exit 2;;
  esac
  shift
done
[ -t 0 ] || ASK=""          # no terminal to answer from: use the defaults

if [ -t 1 ]; then B=$'\033[1m'; G=$'\033[32m'; Y=$'\033[33m'; R=$'\033[31m'; N=$'\033[0m'; else B=""; G=""; Y=""; R=""; N=""; fi
ok()   { printf "  ${G}ok${N}    %s\n" "$*"; }
note() { printf "  ${Y}note${N}  %s\n" "$*"; }
bad()  { printf "  ${R}STOP${N}  %s\n" "$*"; }
info() { printf "        %s\n" "$*"; }
ask()  { # ask "question" default -> REPLY
  if [ -n "$ASK" ]; then printf "%s " "$1"; read -r REPLY || REPLY=""; [ -z "$REPLY" ] && REPLY="$2"; else REPLY="$2"; fi; }

# ---------------------------------------------------------------- checks
checks() {
  local fail=""
  echo "${B}Checking this Mac${N}"
  local arch; arch="$(uname -m)"
  if [ "$arch" = "arm64" ]; then ok "Apple Silicon (arm64)"
  elif [ "$(sysctl -n sysctl.proc_translated 2>/dev/null)" = "1" ]; then note "this Terminal runs under Rosetta; Coot itself will run natively (arm64)"
  else bad "this Mac has an Intel processor ($arch); this Coot is built for Apple Silicon only"; fail=1; fi
  local v major; v="$(sw_vers -productVersion 2>/dev/null)"; major="${v%%.*}"
  if [ -z "$major" ]; then bad "this is not macOS"; fail=1
  elif [ "$major" -ge 26 ]; then ok "macOS $v (tested: macOS 26)"
  elif [ "$major" -ge 11 ]; then note "macOS $v: should work, but only macOS 26 has been tested"
  else bad "macOS $v is too old (macOS 11 or newer is needed)"; fail=1; fi

  if xattr -p com.apple.quarantine "$SRC/bin/coot-bin" >/dev/null 2>&1 || xattr -p com.apple.quarantine "$SRC/run-coot.sh" >/dev/null 2>&1; then
    note "this folder has the macOS download flag (quarantine); it will be removed from Coot's files when installing"
    QUAR=1
  else ok "no download flag (quarantine) on this folder"; QUAR=""; fi

  # programs that Coot starts for some functions
  local ccp4="" d
  for d in "${CCP4:-}" $(ls -d /Applications/ccp4-* 2>/dev/null | sort -r); do
    [ -n "$d" ] && [ -x "$d/bin/refmac5" ] && { ccp4="$d"; break; }
  done
  if [ -n "$ccp4" ]; then ok "CCP4: $ccp4 (Run Refmac, Ligand Builder / SMILES -> acedrg, ProSMART, Privateer ...)"
  else note "CCP4 not found (looked in /Applications/ccp4-*): Run Refmac, acedrg (Ligand Builder Apply, SMILES) and other CCP4 programs are unavailable; Coot itself works"; fi
  local phx=""
  for d in $(ls -d /Applications/phenix-* "$HOME"/phenix-* 2>/dev/null | sort -r); do
    [ -x "$d/bin/reduce" ] || [ -x "$d/build/bin/phenix.reduce" ] || [ -x "$d/build/reduce/exe/reduce" ] && { phx="$d"; break; }
  done
  if [ -n "$phx" ]; then ok "Phenix: $phx (second source of reduce / probe)"
  else info "Phenix not found (optional: Coot 0.9 needs only its reduce / probe, which CCP4 also has)"; fi
  local t miss=""
  for t in reduce probe; do
    command -v $t >/dev/null 2>&1 || [ -x "$ccp4/bin/$t" ] || [ -x "$phx/bin/$t" ] || [ -x "$phx/build/$t/exe/$t" ] || miss="$miss $t"
  done
  if [ -z "$miss" ]; then ok "reduce and probe found (Probe Clashes, Add Hydrogens)"
  else note "not found:$miss (Probe Clashes / Add Hydrogens are unavailable; install CCP4 or Phenix)"; fi
  if command -v coot >/dev/null 2>&1; then info "another Coot is on your PATH as 'coot' ($(command -v coot)); it is not touched: this one is 'coot0'"; fi
  [ -z "$fail" ]
}

existing() {
  if [ -f "$BIN/coot0" ]; then
    local cur; cur="$(sed -n 's/^COOT0_HOME="\(.*\)"$/\1/p' "$BIN/coot0" | head -1)"
    info "installed now: coot0 -> ${cur:-?}"
  fi
  local d
  for d in "$BASE_DEFAULT"/*/; do [ -f "$d/.coot0-installed" ] && info "installed version: ${d%/}"; done
  [ -d "$STATE" ] && info "your Coot preferences and logs: $STATE"
  return 0
}

if [ -n "$DIAG_ONLY" ]; then
  checks; echo; echo "${B}Installed${N}"; existing
  [ -d "$STATE/logs" ] && info "last log: $(ls -t "$STATE"/logs/coot-*.log 2>/dev/null | head -1)"
  exit 0
fi

echo "${B}Coot $VERSION for Apple Silicon: installer${N}   (folder: $SRC)"
echo
if ! checks; then echo; echo "Not installed."; exit 1; fi
echo

# ---------------------------------------------------------------- where
BASE="${PREFIX:-$BASE_DEFAULT}"
if [ -z "$PREFIX" ] && [ -n "$ASK" ]; then
  echo "${B}Where to install${N}"
  ask "  Install into $BASE_DEFAULT/$VERSION ?  [Enter = yes, or type another folder]" ""
  if [ -n "$REPLY" ] && [ "$REPLY" != "y" ] && [ "$REPLY" != "yes" ] && [ "$REPLY" != "Y" ]; then BASE="${REPLY/#\~/$HOME}"; fi
fi
case "$BASE" in /*) ;; *) BASE="$PWD/$BASE";; esac
DEST="$BASE/$VERSION"
mkdir -p "$BASE" 2>/dev/null || { bad "cannot create $BASE"; exit 1; }
[ -w "$BASE" ] || { bad "$BASE is not writable"; exit 1; }
BASE="$(cd "$BASE" && pwd -P)"; DEST="$BASE/$VERSION"     # the real path (e.g. /tmp is a link to /private/tmp): coot0 and uninstall.sh compare it
need=$(du -sk "$SRC" | cut -f1); free=$(df -k "$BASE" | awk 'NR==2 {print $4}')
if [ -n "$free" ] && [ "$free" -lt $((need + 200000)) ]; then bad "not enough free disk space in $BASE (need about $((need/1024 + 200)) MB, free $((free/1024)) MB)"; exit 1; fi

echo "${B}Installing${N}"
if [ "$(cd "$DEST" 2>/dev/null && pwd -P)" = "$SRC" ]; then
  ok "already in place: $DEST"
else
  if [ -e "$DEST" ]; then
    old="$DEST.replaced-$(date +%Y%m%d-%H%M%S)"
    mv "$DEST" "$old" && note "an earlier copy of $VERSION was moved to $old (delete it when you no longer need it)"
  fi
  # file times must be kept (Coot's compiled Scheme files are checked by time).  On the same disk: APFS clones (seconds, no extra
  # space); otherwise ditto (a real copy, about 1 GB).
  if ! cp -Rc "$SRC" "$DEST" 2>/dev/null; then
    rm -rf "$DEST"
    info "copying about $((need/1024)) MB ..."
    if ! ditto "$SRC" "$DEST"; then bad "copying to $DEST failed"; exit 1; fi
  fi
  for d in logs work home results .cache; do [ -d "$DEST/$d" ] && find "$DEST/$d" -mindepth 1 -delete 2>/dev/null; done
  ok "copied to $DEST"
fi
xattr -dr com.apple.quarantine "$DEST" 2>/dev/null          # always (also files that were flagged one by one)
if xattr -p com.apple.quarantine "$DEST/bin/coot-bin" >/dev/null 2>&1; then bad "could not remove the download flag from $DEST"; exit 1; fi
[ -n "${QUAR:-}" ] && ok "removed the download flag (quarantine) from the installed copy"
printf 'installed %s from %s\n' "$(date '+%Y-%m-%d %H:%M')" "$SRC" > "$DEST/.coot0-installed"

mkdir -p "$BIN"
[ -f "$BIN/coot0" ] && ! grep -q "^$MARK" "$BIN/coot0" && cp -p "$BIN/coot0" "$BIN/coot0.before-coot0-install" && note "your own $BIN/coot0 was kept as coot0.before-coot0-install"
cat > "$BIN/coot0" <<EOF
#!/bin/bash
$MARK  (written $(date '+%Y-%m-%d') by $DEST/install.sh)
# coot0: Coot $VERSION for Apple Silicon.  Usage: coot0 [coot options and files]   e.g.  coot0 --pdb model.pdb --auto data.mtz
#   coot0 --legacy       standard resolution instead of the Retina (2x) 3D view (the default: --retina)
#   coot0 --diagnose     what this Mac has (CCP4, Phenix, ...) and where Coot keeps your preferences and logs
#   coot0 --self-test    the full self-test (about 15 minutes)
#   coot0 --uninstall    remove coot0
COOT0_HOME="$DEST"
case "\${1:-}" in
  --diagnose)  exec "\$COOT0_HOME/install.sh" --diagnose;;
  --self-test) exec "\$COOT0_HOME/tests/run-headless-tests.sh";;
  --uninstall) shift; exec "\$COOT0_HOME/uninstall.sh" "\$@";;
esac
# Coot 0.9 writes coot-backup/ and 0-coot-history.py into the folder it is started from: stay here if it is writable
if [ -w "\$PWD" ]; then export COOT_KEEP_CWD=1
else echo "coot0: \$PWD is not writable; Coot works in ~/Library/Application Support/coot0/work instead"; fi
exec "\$COOT0_HOME/run-coot.sh" "\$@"
EOF
chmod 755 "$BIN/coot0"
ok "command written: $BIN/coot0"

# ---------------------------------------------------------------- PATH
echo
echo "${B}PATH${N} (so that typing coot0 finds $BIN/coot0)"
LINE='export PATH="$HOME/.local/bin:$PATH"'
add_line() {  # add_line FILE
  local f="$1"
  if [ -f "$f" ] && grep -q "\.local/bin" "$f"; then ok "$f already puts ~/.local/bin on PATH (not changed)"; return; fi
  printf '\n%s (%s): make the coot0 command available\n%s\n' "$MARK" "$(date '+%Y-%m-%d')" "$LINE" >> "$f"
  ok "added to $f:"
  info "$MARK ..."
  info "$LINE"
}
LOGIN_SHELL="${COOT0_LOGIN_SHELL:-}"; [ -z "$LOGIN_SHELL" ] && LOGIN_SHELL="$(dscl . -read "/Users/$(id -un)" UserShell 2>/dev/null | awk '{print $2}')"; LOGIN_SHELL="${LOGIN_SHELL:-${SHELL:-/bin/zsh}}"
add_line "$HOME/.zshrc"                                                         # zsh: the macOS default shell
case "$LOGIN_SHELL" in */bash) add_line "$HOME/.bash_profile";; *) [ -f "$HOME/.bash_profile" ] && add_line "$HOME/.bash_profile";; esac
[ -f "$HOME/.bashrc" ] && add_line "$HOME/.bashrc"                               # bash started from another shell reads .bashrc
case ":$PATH:" in *":$BIN:"*) ON_PATH=1;; *) ON_PATH="";; esac

# ---------------------------------------------------------------- self-test
if [ -n "$SELFTEST" ]; then
  echo
  echo "${B}Start test${N} (Coot without a window: Python, Scheme, a model and a map; about 30 seconds the first time)"
  tdir="$(mktemp -d "${TMPDIR:-/tmp}/coot0-check.XXXXXX")"
  ( cd "$tdir" && COOT_NO_SPLASH=1 COOT_KEEP_CWD=1 COOT_NO_DEFAULT_TOOLBAR=1 "$DEST/run-coot.sh" --no-graphics --python --no-state-script \
      --no-startup-scripts --script "$DEST/tests/install_check.py" > "$tdir/out.txt" 2>&1 ) &
  pid=$!; i=0
  while kill -0 $pid 2>/dev/null && [ $i -lt 300 ]; do sleep 1; i=$((i+1)); done
  kill -0 $pid 2>/dev/null && { kill -9 $pid 2>/dev/null; echo "(stopped after 300 s)" >> "$tdir/out.txt"; }
  wait $pid 2>/dev/null
  if grep -q "^INSTALL-CHECK OK" "$tdir/out.txt"; then ok "$(grep '^INSTALL-CHECK OK' "$tdir/out.txt" | cut -c18-)"; rm -rf "$tdir"
  else bad "the start test failed; details: $tdir/out.txt"; grep -E "^INSTALL-CHECK|Error|error" "$tdir/out.txt" | head -5 | sed 's/^/        /'; fi
fi

# ---------------------------------------------------------------- summary
echo
echo "${B}Done.${N}  Coot $VERSION is installed in $DEST"
echo
if [ -n "$ON_PATH" ]; then
  echo "  Start it from any folder with:    ${B}coot0${N}          (e.g.  coot0 --pdb model.pdb --auto data.mtz)"
else
  echo "  Open a new Terminal window, then start it from any folder with:    ${B}coot0${N}"
  echo "  (in this window, until then:  $BIN/coot0 )"
fi
echo "  Coot works in the folder you start it from (coot-backup/, 0-coot-history.py), like Coot 0.9 on Linux."
echo "  The 3D view uses full Retina resolution; if it is slow or looks wrong:   coot0 --legacy   (standard resolution)"
echo "  Your preferences and logs:        $STATE"
echo "  Check this Mac again:              coot0 --diagnose"
echo "  Full self-test (~15 min):          coot0 --self-test"
echo "  Remove:                            coot0 --uninstall"
