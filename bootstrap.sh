#!/bin/bash
# bootstrap.sh [--make-envs]  -- prepare a fresh clone of coot0 for building.  Idempotent; deletes nothing of yours.
#   1. checks the command line tools
#   2. the two conda build environments in envs/ (made from the pinned lists in env/ with --make-envs: micromamba or Miniforge)
#   3. the GNOME canvas libraries in canvas/prefix (built from download.gnome.org sources, checksums in canvas/build-scripts/src)
#   4. the Coot 0.9.8.96 release tarball (downloaded from Paul Emsley's site and checked, unless COOT_PRISTINE names an
#      unpacked copy) and m0/coot-src = that source + the numbered patches in m0/patches
# Then build:  m0/tools/build_all.sh   (see BUILDING.md)
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
COOT_URL="https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/source/releases/coot-0.9.8.96.tar.gz"
COOT_SHA256="c43fb6d76ded82da8fa51b35b6ff857d85bb84240b1331029fc50ce06a1cd4f2"

case "$HERE" in *" "*)
  echo "This folder's path contains a space: $HERE"
  echo "The build tools (conda's scripts, the autotools builds of the canvas libraries) cannot work there."
  echo "Clone or move the repository to a path without spaces (for example ~/src/coot0-macos) and run bootstrap.sh again."
  exit 1;; esac
echo "== 1. tools"
miss=""
for t in git rsync clang clang++ codesign install_name_tool otool curl shasum tar make perl; do command -v $t >/dev/null || { echo "   MISSING: $t"; miss=1; }; done
[ -n "$miss" ] && { echo "   install Apple's command line tools first:  xcode-select --install"; exit 1; }
echo "   ok"

echo "== 2. conda build environments (coot-deps: Coot's libraries; coot-rdkit: RDKit 2023.09 + Boost headers)"
ENVS="${COOT0_ENVS:-$HERE/envs}"
MM="$(command -v micromamba || command -v mamba || command -v conda || true)"
if [ -d "$ENVS/coot-deps" ] && [ -d "$ENVS/coot-rdkit" ]; then
  echo "   found $ENVS/{coot-deps,coot-rdkit}"
elif [ "${1:-}" = "--make-envs" ]; then
  [ -n "$MM" ] || { echo "   no micromamba/mamba/conda: install Miniforge (https://github.com/conda-forge/miniforge) and re-run"; exit 1; }
  for e in coot-deps coot-rdkit; do
    echo "   creating $ENVS/$e from env/$e.explicit.txt (exact package URLs; about 1 GB each, a few minutes)"
    "$MM" create -y -p "$ENVS/$e" --file "$HERE/env/$e.explicit.txt"
  done
else
  echo "   not found in $ENVS.  Run  ./bootstrap.sh --make-envs  (needs micromamba, mamba or conda), or set COOT0_ENVS"; exit 1
fi
export CONDA_PREFIX="$ENVS/coot-deps"

echo "== 3. canvas libraries (libart_lgpl, libgnomecanvas, goocanvas) -> canvas/prefix"
if [ -f "$HERE/canvas/prefix/lib/libgoocanvas.3.dylib" ]; then
  echo "   found canvas/prefix"
else
  PATH="$CONDA_PREFIX/bin:$PATH" bash "$HERE/canvas/build-scripts/build_all.sh"
  ln -sfn build-scripts/prefix "$HERE/canvas/prefix"
fi

echo "== 4. Coot 0.9.8.96 source + patches -> m0/coot-src"
if [ -d "$HERE/m0/coot-src/.git" ]; then
  echo "   m0/coot-src exists ($(ls "$HERE"/m0/patches/*.patch | wc -l | tr -d ' ') patches in the series); not touched"
else
  PRISTINE="${COOT_PRISTINE:-}"
  if [ -z "$PRISTINE" ]; then
    DL="$HERE/m0/pristine"; mkdir -p "$DL"
    if [ ! -f "$DL/coot-0.9.8.96.tar.gz" ] || [ "$(/usr/bin/shasum -a 256 "$DL/coot-0.9.8.96.tar.gz" | cut -c1-64)" != "$COOT_SHA256" ]; then
      echo "   downloading $COOT_URL"; curl -fL --retry 2 -o "$DL/coot-0.9.8.96.tar.gz.part" "$COOT_URL" && mv "$DL/coot-0.9.8.96.tar.gz.part" "$DL/coot-0.9.8.96.tar.gz"
    fi
    [ "$(/usr/bin/shasum -a 256 "$DL/coot-0.9.8.96.tar.gz" | cut -c1-64)" = "$COOT_SHA256" ] || { echo "   the Coot tarball does not have the expected checksum"; exit 1; }
    echo "   coot-0.9.8.96.tar.gz: checksum ok"
    [ -d "$DL/coot-0.9.8.96" ] || tar -xzf "$DL/coot-0.9.8.96.tar.gz" -C "$DL"
    PRISTINE="$DL/coot-0.9.8.96"
  fi
  [ -d "$PRISTINE" ] || { echo "   pristine tree not found: $PRISTINE"; exit 1; }
  GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 COOT_PRISTINE="$PRISTINE" bash "$HERE/m0/setup.sh"
fi
echo "== done.  Next:  m0/tools/build_all.sh   (compile, link, assemble the bundle; see BUILDING.md)"
