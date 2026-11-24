#!/bin/bash
# Coot 0.9.8.96 for Apple Silicon -- launcher (build 12).
# Usage:  ./run-coot.sh [--retina | --legacy] [coot arguments...]
#   --retina    request the high-resolution (2x) GL surface (COOT_RETINA=1); the default for a copy installed by install.sh (coot0)
#   --legacy    standard resolution instead (COOT_RETINA=0): 1 GL pixel per point, macOS upscales (the default of the unpacked folder)
# Two layouts are supported:
#   self-contained bundle  (lib/libgtk-quartz-2.0.0.dylib is in this folder): nothing outside this folder is needed;
#   conda mode             (older test package): the GTK2/Python/Guile runtime comes from the conda environment
#                          $COOT_DEPS_ENV (default ~/.claude-science/conda/envs/coot-deps).
# Everything written to the terminal is also saved in logs/coot-<time>.log
# Optional environment switches (set before starting, e.g.  COOT_LABEL_SCALE=2 ./run-coot.sh):
#   COOT_LABEL_SCALE=<x>        size factor for atom/distance labels in the 3D view (default 1.4; 1.0 = original size)
#   COOT_BITMAP_LABELS=1        use the original fixed-size bitmap label fonts instead
#   COOT_RIGHT_CLICK_CENTRE=0   a still right-click (two-finger click) no longer re-centres like a middle-click
#   COOT_RETINA=1 / --retina    high-resolution GL surface;  COOT_RETINA=0 / --legacy  standard resolution
#   COOT_NO_SPLASH=1            no start-up picture
HERE="$(cd "$(dirname "$0")" && pwd -P)"
REAL_HOME="$HOME"

if [ -f "$HERE/lib/libgtk-quartz-2.0.0.dylib" ]; then
  BUNDLED=1; ENV="$HERE"
else
  BUNDLED=""; ENV="${COOT_DEPS_ENV:-$HOME/.claude-science/conda/envs/coot-deps}"
  if [ ! -d "$ENV/lib" ]; then echo "ERROR: dependency environment not found at $ENV (set COOT_DEPS_ENV)"; exit 1; fi
fi

# Files downloaded with a browser or AirDrop carry a quarantine flag; macOS then refuses to load our (ad-hoc signed) libraries.
if [ -n "$BUNDLED" ] && [ -z "$COOT_IGNORE_QUARANTINE" ] && xattr -p com.apple.quarantine "$HERE/bin/coot-bin" >/dev/null 2>&1; then
  echo "This folder still has the macOS download quarantine flag, so macOS may block Coot."
  echo "If you trust this copy, clear the flag once and start again:"
  echo "    xattr -dr com.apple.quarantine \"$HERE\""
  echo "(set COOT_IGNORE_QUARANTINE=1 to try anyway)"
  exit 3
fi

# State (logs, work files, private home with the preferences, caches): COOT_STATE_DIR if set; for a copy installed by install.sh
# (marker file .coot0-installed) ~/Library/Application Support/coot0, per user; else this folder if writable, else Application Support.
if [ -n "$COOT_STATE_DIR" ]; then STATE="$COOT_STATE_DIR"                                    # (build 17) explicit
elif [ -f "$HERE/.coot0-installed" ]; then STATE="$REAL_HOME/Library/Application Support/coot0"   # installed by install.sh: per user
elif [ -w "$HERE" ]; then STATE="$HERE"; else STATE="$REAL_HOME/Library/Application Support/Coot-0.9.8.96"; fi
mkdir -p "$STATE/logs" "$STATE/.cache" "$STATE/work"
LOG="$STATE/logs/coot-$(date +%Y%m%d-%H%M%S).log"
exec > >(tee -a "$LOG") 2>&1

# Coot writes coot-backup/ and 0-coot-history.{py,scm} into the current directory: run from work/ (set COOT_KEEP_CWD=1 to stay put).
# Existing relative file arguments are made absolute first so they still resolve.
args=()
for a in "$@"; do
  if [ "$a" = "--retina" ]; then export COOT_RETINA=1
  elif [ "$a" = "--legacy" ]; then export COOT_RETINA=0          # (build 18) standard resolution (1 GL pixel per point; macOS upscales)
  elif [ -e "$a" ] && [ "${a#/}" = "$a" ]; then args+=("$(cd "$(dirname "$a")" && pwd)/$(basename "$a")")
  else args+=("$a"); fi
done
if [ -z "$COOT_KEEP_CWD" ]; then cd "$STATE/work"; fi
# (build 18) a copy installed by install.sh (the coot0 command) uses the Retina (2x) GL surface by default; --legacy or COOT_RETINA=0 turns it off
if [ -f "$HERE/.coot0-installed" ] && [ -z "$COOT_RETINA" ]; then export COOT_RETINA=1; fi

# Isolation: by default Coot uses a private HOME inside the state folder, so your own ~/.coot, ~/.coot.py and ~/.coot-preferences
# (possibly from another Coot version, possibly Python 2 syntax) are NOT read.  COOT_USE_HOME=1 uses your real home instead.
if [ -n "$COOT_HOME_OVERRIDE" ]; then export HOME="$COOT_HOME_OVERRIDE"; mkdir -p "$HOME"      # (used by tests/run-gui-audit.sh: a throw-away home)
elif [ -z "$COOT_USE_HOME" ]; then export HOME="$STATE/home"; mkdir -p "$HOME"; export COOT_DEFAULT_TOOLBAR=1   # (private home: the default toolbar buttons are installed there once, see python/coot_toolbuttons.py)
fi
# (build 15) GTK keeps the "recently used files" list in $HOME/.local/share; without that folder every file dialog printed two Gtk-WARNINGs
[ -z "$COOT_USE_HOME" ] && mkdir -p "$HOME/.local/share" 2>/dev/null

export COOT_PREFIX="$HERE"
export PYTHONUNBUFFERED=1      # Python print() output reaches the log immediately (a crash used to lose the buffered tail)
export COOT_DATA_DIR="$HERE/share/coot"
export SYMINFO="$COOT_DATA_DIR/syminfo.lib"
export COOT_STANDARD_RESIDUES="$COOT_DATA_DIR/standard-residues.pdb"
export COOT_PIXMAPS_DIR="$COOT_DATA_DIR/pixmaps"
export COOT_RESOURCES_FILE="$COOT_DATA_DIR/cootrc"
export COOT_SCHEME_DIR="$COOT_DATA_DIR/scheme"
export COOT_PYTHON_DIR="$COOT_DATA_DIR/python"
# Environment hygiene: a shell that has sourced the CCP4 / Phenix setup scripts exports variables that would redirect
# Coot to other libraries, dictionaries or Python/Guile installations.  (COOT_KEEP_ENV=1 keeps everything.)
if [ -z "$COOT_KEEP_ENV" ]; then
  unset DYLD_LIBRARY_PATH DYLD_FALLBACK_LIBRARY_PATH DYLD_INSERT_LIBRARIES DYLD_FRAMEWORK_PATH
  unset GUILE_LOAD_COMPILED_PATH GUILE_AUTO_COMPILE PYTHONSTARTUP PYTHONUSERBASE PYTHONEXECUTABLE
  unset COOT_REFMAC_LIB_DIR COOT_CCP4_LIB_DIR CLIB
fi
# Reference structures for Ca -> Mainchain / strand building (the same directory `make install` creates under share/coot)
for _rs in "$COOT_DATA_DIR/reference-structures" "$HERE/reference-structures"; do
  if [ -d "$_rs" ]; then export COOT_REF_STRUCTS="$_rs"; break; fi
done

export PYTHONHOME="$ENV"
export PYTHONPATH="$COOT_PYTHON_DIR"
export GUILE_LOAD_PATH="$COOT_SCHEME_DIR"
export GUILE_WARN_DEPRECATED=no
export XDG_CACHE_HOME="$STATE/.cache"                      # Guile's compiled scheme (.go) cache and the fontconfig cache
export GSETTINGS_SCHEMA_DIR="$ENV/share/glib-2.0/schemas"
export XDG_DATA_DIRS="$ENV/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
export FONTCONFIG_FILE="$ENV/etc/fonts/fonts.conf"
if [ -n "$BUNDLED" ]; then
  # Every library hard-codes the prefix it was built under; point each one at this folder instead.
  export GTK_EXE_PREFIX="$HERE" GTK_DATA_PREFIX="$HERE" GTK_PATH="$HERE/lib/gtk-2.0"
  export GTK_IM_MODULE_FILE=/dev/null                      # no input-method modules (as in the conda layout)
  export PANGO_LIBDIR="$HERE/lib" PANGO_SYSCONFDIR="$HERE/etc"
  export FONTCONFIG_PATH="$HERE/etc/fonts"
  export GIO_MODULE_DIR="$HERE/lib/gio/modules"
  export GUILE_SYSTEM_PATH="$HERE/share/guile/3.0"
  export GUILE_SYSTEM_COMPILED_PATH="$HERE/lib/guile/3.0/ccache"
  export GUILE_SYSTEM_EXTENSIONS_PATH="$HERE/lib/guile/3.0/extensions"
  # Guile treats a compiled module (.go) as stale when its source (.scm) looks newer.  A copy of this folder made without
  # timestamps (cp -R, some sync/backup tools) makes every system module look stale and Guile then tries to recompile its own
  # library at start-up (very slow, and it fails).  Refresh the compiled files' timestamps once if that is the case.
  if [ "$HERE/share/guile/3.0/ice-9/regex.scm" -nt "$HERE/lib/guile/3.0/ccache/ice-9/regex.go" ]; then
    echo "note: the compiled Guile modules look older than their sources (this folder was copied without file dates); refreshing them"
    find "$HERE/lib/guile/3.0/ccache" -name '*.go' -exec touch {} + 2>/dev/null || {
      echo "note: could not refresh them (read-only folder?); Guile auto-compile is switched off for this run"; export GUILE_AUTO_COMPILE=0; }
  fi
  export SSL_CERT_FILE="$HERE/ssl/cacert.pem" CURL_CA_BUNDLE="$HERE/ssl/cacert.pem"
  # gdk-pixbuf's loader list needs absolute paths: generate it for this location (it includes the SVG loader: the toolbar icons are SVG)
  PIXCACHE="$STATE/.cache/gdk-pixbuf-loaders.cache"
  if [ ! -s "$PIXCACHE" ] || [ "$HERE/lib/gdk-pixbuf-loaders.cache.in" -nt "$PIXCACHE" ] || ! grep -qF "\"$HERE/lib/gdk-pixbuf-2.0/" "$PIXCACHE"; then
    tmpl="$(cat "$HERE/lib/gdk-pixbuf-loaders.cache.in")"
    printf '%s\n\n' "${tmpl//@BUNDLE@/$HERE}" > "$PIXCACHE"      # (every block, the last too, must end with a blank line)
  fi
  export GDK_PIXBUF_MODULE_FILE="$PIXCACHE"
else
  export GDK_PIXBUF_MODULE_FILE="$HERE/lib/gdk-pixbuf-loaders.cache"
fi
# locale: UTF-8 for text, "C" for numbers (Coot parses and prints numbers with '.')
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LC_NUMERIC=C

# Programs Coot starts for some functions: reduce + probe ("Probe clashes"), refmac5, acedrg.  If one is not on PATH, the
# directory of a CCP4 / Phenix installation that has it is appended to the END of PATH (Coot's own libraries are never
# taken from there).  COOT_NO_AUTO_PATH=1 turns this off.
if [ -z "$COOT_NO_AUTO_PATH" ]; then
  for tool in reduce probe refmac5 acedrg; do
    if ! command -v "$tool" >/dev/null 2>&1; then
      # newest first: CCP4; Phenix 1.x (build/<tool>/exe); Phenix 2.x (bin/, in /Applications or the home folder); Homebrew
      _dirs=()
      while IFS= read -r _d; do _dirs+=("$_d"); done < <(
        { _apps="${COOT_APPS_DIR:-/Applications}"          # (COOT_APPS_DIR: another applications folder; used by tests/installer_test.sh)
          ls -d "$_apps"/ccp4-*/bin 2>/dev/null | sort -r
          ls -d "$_apps"/phenix-*/build/$tool/exe 2>/dev/null | sort -r
          ls -d "$_apps"/phenix-*/bin "$REAL_HOME"/phenix-*/bin 2>/dev/null | sort -r
          echo /opt/homebrew/bin; echo /usr/local/bin; } )
      for d in "${_dirs[@]}"; do
        if [ -f "$d/$tool" ] && [ -x "$d/$tool" ]; then PATH="$PATH:$d"; break; fi
      done
    fi
  done
fi
export PATH
# The CCP4 installation whose programs Coot starts (refmac5 ...): python/coot_utils.py ccp4_child_env() adds CCP4's variables
# (CCP4, CINCL, CCP4_SCR, ...) to the environment of those programs only; refmac5 stops with "Cannot open environ.def" without them.
if [ -z "$CCP4" ] && [ -z "$COOT_CCP4_HOME" ]; then
  _rm=$(command -v refmac5 2>/dev/null)
  if [ -n "$_rm" ]; then
    _d=$(cd "$(dirname "$_rm")/.." 2>/dev/null && pwd)
    [ -n "$_d" ] && [ -f "$_d/include/environ.def" ] && export COOT_CCP4_HOME="$_d"
  fi
fi

# (build 37) The CCP4 monomer library (restraint dictionaries) is no longer inside the package.  First found wins:
#   COOT0_MONOMERS (a folder you name) > monomers/ in this folder (older packages, development copies) >
#   the copy fetched by `coot0 --fetch-monomers` (~/Library/Application Support/coot0/monomers) > CCP4's (lib/data/monomers).
# COOT0_MONOMERS_IGNORE_CCP4=1 skips CCP4's (tests).  Programs started from Coot get the same folder (CLIBD_MON).
MONOMERS_FROM=""
_ccp4_mon=""
if [ -z "$COOT0_MONOMERS_IGNORE_CCP4" ]; then
  for _c in "$COOT_CCP4_HOME" "$CCP4" $(ls -d /Applications/ccp4-* 2>/dev/null | sort -r); do
    [ -n "$_c" ] && [ -f "$_c/lib/data/monomers/list/mon_lib_list.cif" ] && { _ccp4_mon="$_c/lib/data/monomers"; break; }
  done
fi
for _m in "${COOT0_MONOMERS:-}|your folder (COOT0_MONOMERS)" "$HERE/monomers|this folder" \
          "$REAL_HOME/Library/Application Support/coot0/monomers|coot0 --fetch-monomers" "$_ccp4_mon|CCP4"; do
  _dir="${_m%%|*}"
  if [ -n "$_dir" ] && [ -f "$_dir/list/mon_lib_list.cif" ]; then
    export CLIBD_MON="$_dir/" COOT_MONOMER_LIB_DIR="$_dir"; MONOMERS_FROM="${_m#*|}"; break
  fi
done
unset _m _dir _c _ccp4_mon
if [ -z "$MONOMERS_FROM" ]; then
  echo "coot0: NO MONOMER LIBRARY: refinement and ligands need it.  Get it once with:  coot0 --fetch-monomers"
  echo "       (about 110 MB from github.com/MonomerLibrary/monomers; or install CCP4, whose library coot0 then uses)"
fi

echo "== Coot launch $(date) | $([ -n "$BUNDLED" ] && echo 'self-contained bundle' || echo "conda environment $ENV") =="
echo "macOS $(sw_vers -productVersion) $(uname -m) | retina=${COOT_RETINA:-0} | monomer library: ${CLIBD_MON:-NOT FOUND}${MONOMERS_FROM:+ ($MONOMERS_FROM)} | cwd: $(pwd) | state: $STATE"
echo "external tools: $(for t in reduce probe refmac5 acedrg; do printf '%s=%s  ' $t "$(command -v $t || echo none)"; done)"
[ -n "$COOT_CCP4_HOME" ] && echo "CCP4 for child programs: $COOT_CCP4_HOME"
echo "animation: COOT_ANIM_MS_PER_STEP=${COOT_ANIM_MS_PER_STEP:-default(16.7)}"
echo "labels: COOT_LABEL_SCALE=${COOT_LABEL_SCALE:-default(1.4)} COOT_BITMAP_LABELS=${COOT_BITMAP_LABELS:-0} right-click-centre: ${COOT_RIGHT_CLICK_CENTRE:-1}"
# Start-up picture: bin/coot-splash (AppKit) shows the 2x picture at full Retina resolution until Coot's main window is up, then closes
# itself.  COOT_NO_SPLASH=1 skips it; without the helper (or with --splash-screen FILE) Coot's own start-up window is used.
if [ -z "$COOT_NO_SPLASH" ] && [ -x "$HERE/bin/coot-splash" ] && [ -f "$COOT_DATA_DIR/pixmaps/coot-splash@2x.png" ]; then
  _show_splash=1
  for _a in "${args[@]}"; do
    case "$_a" in --no-graphics|--no-splash-screen|--splash-screen|--splash-screen=*|--version|--help|-h) _show_splash="";; esac
  done
  if [ -n "$_show_splash" ]; then
    "$HERE/bin/coot-splash" "$COOT_DATA_DIR/pixmaps/coot-splash@2x.png" --pid $$ >/dev/null 2>&1 &
    args+=(--no-splash-screen)
  fi
fi
[ -n "$COOT_DYLD_DEBUG" ] && export DYLD_PRINT_LIBRARIES=1   # diagnostics: print every library the process loads
if [ -n "$COOT_STRICT" ]; then
  # Diagnostic: deny this process read access to conda, Homebrew, MacPorts and XQuartz, so that a hidden dependency on any of them
  # fails loudly instead of silently working on a Mac that happens to have them (macOS sandbox-exec; not tested by the packager).
  SB='(version 1)(allow default)(deny file-read* (subpath "'"$REAL_HOME"'/.claude-science/conda") (subpath "/opt/homebrew") (subpath "/opt/local") (subpath "/opt/X11") (subpath "/usr/local/Cellar"))'
  echo "STRICT mode: reads from conda, Homebrew, MacPorts and XQuartz are denied for this run"
  exec /usr/bin/sandbox-exec -p "$SB" "${COOT_BIN:-$HERE/bin/coot-bin}" "${args[@]}"
fi
exec "${COOT_BIN:-$HERE/bin/coot-bin}" "${args[@]}"
