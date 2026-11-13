#!/bin/bash
# uninstall.sh -- remove coot0 (also: coot0 --uninstall).  Removes only what install.sh made:
#   ~/.local/bin/coot0, the marked PATH lines in ~/.zshrc / ~/.bash_profile / ~/.bashrc (a copy of each file is kept),
#   this installed copy (you are asked), and - only if you say so - your Coot preferences and logs in
#   ~/Library/Application Support/coot0.   ./uninstall.sh --yes  answers "yes" to removing the copy, "no" to the preferences.
set -u
HERE="$(cd "$(dirname "$0")" && pwd -P)"
MARK="# coot0-install"
BIN="$HOME/.local/bin"
STATE="$HOME/Library/Application Support/coot0"
ASK=1; [ "${1:-}" = "--yes" ] && ASK=""; [ -t 0 ] || ASK=""
ask() { if [ -n "$ASK" ]; then printf "%s " "$1"; read -r REPLY || REPLY=""; [ -z "$REPLY" ] && REPLY="$2"; else REPLY="$2"; fi; }

if [ -f "$BIN/coot0" ] && grep -q "^$MARK" "$BIN/coot0"; then
  cur="$(sed -n 's/^COOT0_HOME="\(.*\)"$/\1/p' "$BIN/coot0" | head -1)"
  cur_real="$(cd "$cur" 2>/dev/null && pwd -P)"
  if [ "$cur_real" = "$HERE" ] || [ ! -d "$cur" ]; then rm -f "$BIN/coot0"; echo "removed $BIN/coot0"
  else echo "$BIN/coot0 points to another version ($cur): left as it is"; fi
fi
[ -f "$BIN/coot0.before-coot0-install" ] && [ ! -e "$BIN/coot0" ] && mv "$BIN/coot0.before-coot0-install" "$BIN/coot0" && echo "restored your own $BIN/coot0"

if [ ! -e "$BIN/coot0" ]; then
  for f in "$HOME/.zshrc" "$HOME/.bash_profile" "$HOME/.bashrc"; do
    [ -f "$f" ] && grep -q "^$MARK" "$f" || continue
    cp -p "$f" "$f.before-coot0-uninstall"
    # drop each marker line, the PATH line after it, and the empty line before it
    awk -v m="$MARK" '
      { lines[NR] = $0 }
      END { skip = 0
        for (i = 1; i <= NR; i++) {
          if (index(lines[i], m) == 1) { skip = 1; continue }
          if (skip == 1) { skip = 0; if (lines[i] ~ /^export PATH="\$HOME\/\.local\/bin:\$PATH"$/) continue }
          if (lines[i] == "" && i < NR && index(lines[i+1], m) == 1) continue
          print lines[i] } }' "$f.before-coot0-uninstall" > "$f"
    echo "removed the coot0 PATH line from $f (previous version: $f.before-coot0-uninstall)"
  done
fi

if [ -f "$HERE/.coot0-installed" ]; then
  ask "Delete this installed copy, $HERE ?  [Y/n]" "y"
  case "$REPLY" in y|Y|yes) cd / && rm -rf "$HERE" && echo "deleted $HERE";; *) echo "kept $HERE";; esac
fi
if [ -d "$STATE" ]; then
  ask "Also delete your Coot preferences and logs, $STATE ?  [y/N]" "n"
  case "$REPLY" in y|Y|yes) rm -rf "$STATE" && echo "deleted $STATE";; *) echo "kept $STATE";; esac
fi
echo "coot0 is uninstalled."
