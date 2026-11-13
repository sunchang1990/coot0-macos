#!/bin/bash
# Double-click in Finder: runs install.sh in a Terminal window.
cd "$(dirname "$0")" && ./install.sh
echo; read -r -p "Press Return to close this window. " _
