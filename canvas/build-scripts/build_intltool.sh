#!/bin/bash
set -u
W=$(cd "$(dirname "$0")" && pwd)
T=$W/tools
export PATH=$CONDA_PREFIX/bin:$PATH
cd $W/build && rm -rf intltool-0.40.6 && tar xjf $W/src/intltool-0.40.6.tar.bz2 && cd intltool-0.40.6
PERL=/usr/bin/perl ./configure --prefix=$T > $W/logs/intltool.configure.log 2>&1 || { tail -15 $W/logs/intltool.configure.log; exit 1; }
make -j4 > $W/logs/intltool.make.log 2>&1 && make install > $W/logs/intltool.install.log 2>&1 && echo "intltool OK"
head -1 $T/bin/intltool-update
