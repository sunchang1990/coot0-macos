#!/bin/bash
# Build libart_lgpl + libgnomecanvas + goocanvas 1.x against conda-forge GTK2 (Quartz) on arm64 macOS.
# usage: bash build_canvas.sh <name> <version> [extra configure args]   (run in env coot-deps)
# Fixes needed for these 2005-2010 era tarballs on Apple Silicon:
#  1. their bundled libtool picks "-flat_namespace -undefined suppress" for unknown darwin hosts -> use two-level namespace
#  2. conda 'msgfmt' cannot write .gmo files in this sandbox and translations are irrelevant -> drop po/ demos/ from SUBDIRS
set -u
W=$(cd "$(dirname "$0")" && pwd)
P=$W/prefix
export PKG_CONFIG_PATH=$P/lib/pkgconfig:$CONDA_PREFIX/lib/pkgconfig:$CONDA_PREFIX/share/pkgconfig
export PATH=$W/tools/bin:$CONDA_PREFIX/bin:$PATH
export INTLTOOL_PERL=/usr/bin/perl
export CC=/usr/bin/clang CXX=/usr/bin/clang++
export CFLAGS="-O2 -arch arm64 -Wno-error -Wno-deprecated-declarations -Wno-incompatible-function-pointer-types -Wno-int-conversion -Wno-implicit-function-declaration"
export CPPFLAGS="-I$P/include -I$CONDA_PREFIX/include"
export LDFLAGS="-L$P/lib -L$CONDA_PREFIX/lib -Wl,-rpath,$CONDA_PREFIX/lib"
N=$1; V=$2; shift 2
cd $W/build
rm -rf $N-$V && tar xjf $W/src/$N-$V.tar.bz2 && cd $N-$V
for d in $CONDA_PREFIX/share/automake-*; do
  cp $d/config.guess $d/config.sub . 2>/dev/null
  [ -d build-aux ] && cp $d/config.guess $d/config.sub build-aux/ 2>/dev/null
done
# (1) libtool darwin fix
sed -i.libtoolbak 's/${wl}-flat_namespace ${wl}-undefined ${wl}suppress/${wl}-undefined ${wl}error/g' configure
# (2) no po/demos/docs
for f in Makefile.in; do sed -E -i.subdirsbak 's/^(SUBDIRS = .*) po( |$)/\1\2/; s/^(SUBDIRS = .*) demos( |$)/\1\2/' $f; done
./configure --prefix=$P --disable-gtk-doc --disable-nls "$@" > $W/logs/$N.configure.log 2>&1 || { echo "configure FAILED"; tail -25 $W/logs/$N.configure.log | cut -c1-240; exit 1; }
make -j8 > $W/logs/$N.make.log 2>&1 || { echo "make FAILED"; grep -n "error:\|Error [0-9]\|ld: " $W/logs/$N.make.log | head -30 | cut -c1-240; exit 1; }
make install > $W/logs/$N.install.log 2>&1 || { echo "install FAILED"; tail -20 $W/logs/$N.install.log | cut -c1-240; exit 1; }
echo "$N $V OK"
