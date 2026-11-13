#!/bin/bash
# bootstrap.sh [--make-envs]  -- prepare this folder for work.  Idempotent; deletes nothing.
#   1. checks the command line tools      2. looks for the two conda build environments (or makes them with --make-envs)
#   3. unpacks the canvas libraries       4. rebuilds m0/coot-src = pristine 0.9.8.96 + the numbered patches (git repo)
# Needs the pristine Coot 0.9.8.96 source tree (the release tarball, unpacked): COOT_PRISTINE=/path (default ~/Downloads/coot-0.9.8.96).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
PRISTINE="${COOT_PRISTINE:-$HOME/Downloads/coot-0.9.8.96}"
echo "== 1. tools"
for t in git rsync clang clang++ codesign install_name_tool otool ditto zip unzip; do command -v $t >/dev/null || echo "   MISSING: $t   (xcode-select --install)"; done
echo "== 2. conda build environments (coot-deps = Coot's dependency stack, coot-rdkit = RDKit 2023.09 + Boost 1.84 headers)"
CS="$HOME/.claude-science/conda"
MM="$(command -v micromamba || true)"; [ -z "$MM" ] && [ -x "$CS/bin/micromamba" ] && MM="$CS/bin/micromamba"
if [ -d "$HERE/envs/coot-deps" ] && [ -d "$HERE/envs/coot-rdkit" ]; then
  echo "   found $HERE/envs/{coot-deps,coot-rdkit}"
elif [ -d "$CS/envs/coot-deps" ] && [ -d "$CS/envs/coot-rdkit" ]; then
  echo "   found $CS/envs/{coot-deps,coot-rdkit} (made by the earlier Claude Science sessions; works, but lives in that tool's folder)"
elif [ "$1" = "--make-envs" ]; then
  [ -n "$MM" ] || { echo "   no micromamba: install Miniforge (https://github.com/conda-forge/miniforge) and re-run"; exit 1; }
  for e in coot-deps coot-rdkit; do
    echo "   creating $HERE/envs/$e from env/$e.explicit.txt (exact package URLs + md5; several GB, a few minutes)"
    "$MM" create -y -p "$HERE/envs/$e" -f "$HERE/env/$e.explicit.txt"
  done
else
  echo "   not found.  Run  ./bootstrap.sh --make-envs  (needs micromamba or Miniforge)."
fi
echo "== 3. canvas libraries (libart_lgpl, libgnomecanvas, goocanvas) -> canvas/prefix"
if [ ! -d "$HERE/canvas/canvas-prefix" ]; then tar -xzf "$HERE/canvas/coot-canvas-libs-arm64-prefix.tar.gz" -C "$HERE/canvas"; fi
ln -sfn canvas-prefix "$HERE/canvas/prefix"
echo "   NOTE: the dylibs carry the install name of the machine they were built on:"
otool -D "$HERE/canvas/prefix/lib/libgoocanvas.3.dylib" | tail -1 | sed 's/^/   /'
echo "   pass the directory of that path as CANVAS_PREFIX_LIB to m0/tools/relocate_coot_bin.sh (CLAUDE.md, 'C++ rebuild')"
echo "== 4. source tree"
if [ -d "$HERE/m0/coot-src/.git" ]; then echo "   m0/coot-src exists ($(ls "$HERE"/m0/patches/*.patch | wc -l | tr -d ' ') patches in the series); not touched"
elif [ -d "$PRISTINE" ]; then GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 COOT_PRISTINE="$PRISTINE" bash "$HERE/m0/setup.sh"
else echo "   pristine tree not found: $PRISTINE   (unpack the Coot 0.9.8.96 release tarball and set COOT_PRISTINE)"; fi
echo "== done.  Next: read CLAUDE.md ('Working loop')."
