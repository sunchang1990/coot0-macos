#!/bin/bash
# Build bin/coot-splash (start-up picture helper, AppKit only).  usage: build_splash.sh <coot-src> <output file>
set -e
SRC=$(cd "$1" && pwd); OUT=$2
clang -O2 -fobjc-arc -arch arm64 -mmacosx-version-min=11.0 -framework Cocoa -o "$OUT" "$SRC/compat/splash/coot-splash.m"
codesign --force -s - "$OUT"
otool -L "$OUT" | tail -n +2 | awk '{print $1}' | grep -v '^/System/\|^/usr/lib/' && { echo "unexpected library"; exit 1; } || true
echo "built $OUT"
