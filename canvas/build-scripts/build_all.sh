#!/bin/bash
# build_all.sh  (build 37) -- download, check and build the three GNOME canvas libraries Coot 0.9 links against
# (libart_lgpl 2.3.21, libgnomecanvas 2.30.3, goocanvas 1.0.0; plus intltool 0.40.6, a build tool) into canvas/build-scripts/prefix.
# Run with the coot-deps conda environment active (CONDA_PREFIX), as bootstrap.sh does.  Sources: download.gnome.org, checked
# against the sha256 sums in src/sources.json.  Takes a few minutes.  Re-running rebuilds.
set -eu
W="$(cd "$(dirname "$0")" && pwd)"
: "${CONDA_PREFIX:?activate the coot-deps environment first (bootstrap.sh does this)}"
export MACOSX_DEPLOYMENT_TARGET="${COOT_MIN_MACOS:-11.0}"       # the oldest macOS coot0 supports (bundle_check.py checks it)
mkdir -p "$W/src" "$W/build" "$W/logs"
fetch() {  # fetch NAME VERSION URL
  local name=$1 ver=$2 url=$3 f="$W/src/$1-$2.tar.bz2"
  local want; want=$(/usr/bin/python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))[sys.argv[2]]["sha256"])' "$W/src/sources.json" "$name")
  if [ ! -f "$f" ] || [ "$(/usr/bin/shasum -a 256 "$f" | cut -c1-64)" != "$want" ]; then
    echo "  downloading $name $ver"; /usr/bin/curl -fsSL --retry 2 -o "$f.part" "$url" && mv "$f.part" "$f"
  fi
  [ "$(/usr/bin/shasum -a 256 "$f" | cut -c1-64)" = "$want" ] || { echo "  $name: checksum does not match src/sources.json"; exit 1; }
  echo "  $name $ver: checksum ok"
}
fetch intltool       0.40.6 https://download.gnome.org/sources/intltool/0.40/intltool-0.40.6.tar.bz2
fetch libart_lgpl    2.3.21 https://download.gnome.org/sources/libart_lgpl/2.3/libart_lgpl-2.3.21.tar.bz2
fetch libgnomecanvas 2.30.3 https://download.gnome.org/sources/libgnomecanvas/2.30/libgnomecanvas-2.30.3.tar.bz2
fetch goocanvas      1.0.0  https://download.gnome.org/sources/goocanvas/1.0/goocanvas-1.0.0.tar.bz2
rm -rf "${W:?}/prefix"
bash "$W/build_intltool.sh"
bash "$W/build_canvas.sh" libart_lgpl 2.3.21
bash "$W/build_canvas.sh" libgnomecanvas 2.30.3
bash "$W/build_canvas.sh" goocanvas 1.0.0
for l in libart_lgpl_2.2 libgnomecanvas-2.0 libgoocanvas.3; do
  [ -f "$W/prefix/lib/$l.dylib" ] || { echo "  missing $W/prefix/lib/$l.dylib"; exit 1; }
done
echo "canvas libraries ready in $W/prefix (minimum macOS $MACOSX_DEPLOYMENT_TARGET)"
