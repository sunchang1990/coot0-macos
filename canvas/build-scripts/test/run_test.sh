#!/bin/bash
set -u
W=$(cd "$(dirname "$0")/.." && pwd)
P=$W/prefix
export PKG_CONFIG_PATH=$P/lib/pkgconfig:$CONDA_PREFIX/lib/pkgconfig:$CONDA_PREFIX/share/pkgconfig
CF=$(pkg-config --cflags libgnomecanvas-2.0 goocanvas gtk+-2.0)
LF=$(pkg-config --libs libgnomecanvas-2.0 goocanvas gtk+-2.0)
/usr/bin/clang -arch arm64 -O1 -Wno-deprecated-declarations $CF -I$P/include/libart-2.0 $W/test/canvas_headless_test.c -o $W/test/canvas_test $LF -lart_lgpl_2 -L$P/lib -Wl,-rpath,$P/lib -Wl,-rpath,$CONDA_PREFIX/lib 2>&1 | head -20
echo "--- link ---"; otool -hv $W/test/canvas_test | tail -1; file $W/test/canvas_test | cut -d: -f2
echo "--- run ---"; $W/test/canvas_test
echo "exit=$?"
