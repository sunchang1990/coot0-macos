#!/bin/bash
# fetch-monomers.sh [latest | COMMIT] [--into DIR] [--force]   (build 37; also: coot0 --fetch-monomers ...)
# Downloads the CCP4 monomer library (restraint dictionaries: Coot needs it to refine, regularise and add ligands) from
# https://github.com/MonomerLibrary/monomers into DIR (default: ~/Library/Application Support/coot0/monomers, shared by every
# installed coot0 version).  Without an argument it fetches the version coot0 was tested with (below); "latest" fetches the
# newest version.  About 110 MB to download, 680 MB unpacked.  Not needed when CCP4 is installed: coot0 then uses CCP4's
# library.  The download replaces the folder only when it is complete, so an interrupted download leaves the old one intact.
# For tests: COOT0_MONOMERS_URL=<url or file:// of a .tar.gz> is used instead of GitHub.
set -u
TESTED=0af022bf6f7c401d59c7bf106e6709fc5f57c3d4      # MonomerLibrary/monomers commit of 26 Oct 2026, used by coot0's tests
REF="$TESTED"; DEST="$HOME/Library/Application Support/coot0/monomers"; FORCE=""
while [ $# -gt 0 ]; do
  case "$1" in
    latest) REF="main";;
    --into) DEST="${2:?--into needs a folder}"; shift;;
    --force) FORCE=1;;
    -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0;;
    -*) echo "fetch-monomers: unknown option $1 (see --help)"; exit 2;;
    *) REF="$1";;
  esac
  shift
done
VFILE="$DEST/.coot0-monomers-version"
if [ -z "$FORCE" ] && [ "$REF" != "main" ] && [ -f "$VFILE" ] && [ "$(cat "$VFILE")" = "$REF" ] && [ -f "$DEST/list/mon_lib_list.cif" ]; then
  echo "monomer library $REF is already in $DEST"; exit 0
fi
URL="${COOT0_MONOMERS_URL:-https://github.com/MonomerLibrary/monomers/archive/$REF.tar.gz}"
PARENT="$(dirname "$DEST")"; mkdir -p "$PARENT" || { echo "fetch-monomers: cannot make $PARENT"; exit 1; }
TMP="$(mktemp -d "$PARENT/.monomers-download.XXXXXX")" || exit 1
trap 'rm -rf "${TMP:?}"' EXIT
echo "Downloading the monomer library ($REF) from ${URL%%\?*}"
echo "  (about 110 MB; it goes to $DEST)"
if ! /usr/bin/curl -fL --retry 2 --progress-bar -o "$TMP/m.tar.gz" "$URL"; then
  echo "fetch-monomers: the download failed.  Check the network and try again: coot0 --fetch-monomers"; exit 1
fi
mkdir "$TMP/x" && /usr/bin/tar -xzf "$TMP/m.tar.gz" -C "$TMP/x" || { echo "fetch-monomers: the download is not a readable .tar.gz"; exit 1; }
TOP="$(find "$TMP/x" -mindepth 1 -maxdepth 1 -type d | head -1)"
[ -n "$TOP" ] && [ -f "$TOP/list/mon_lib_list.cif" ] && [ -f "$TOP/a/ALA.cif" ] || { echo "fetch-monomers: the download does not look like the monomer library (no list/mon_lib_list.cif)"; exit 1; }
if [ "$REF" = "main" ]; then echo "latest ($(date +%Y-%m-%d))" > "$TOP/.coot0-monomers-version"; else echo "$REF" > "$TOP/.coot0-monomers-version"; fi
# swap in the complete copy; the previous one is removed only after the new one is in place
OLD=""
if [ -e "$DEST" ]; then OLD="$TMP/previous"; mv "$DEST" "$OLD" || { echo "fetch-monomers: cannot replace $DEST"; exit 1; }; fi
mv "$TOP" "$DEST" || { [ -n "$OLD" ] && mv "$OLD" "$DEST"; echo "fetch-monomers: cannot move the library into $DEST"; exit 1; }
echo "Monomer library ready: $DEST ($(find "$DEST" -name '*.cif' | wc -l | tr -d ' ') dictionaries)"
