#!/bin/bash
# update_tap.sh VERSION  -- after a GitHub release of coot0, update the Homebrew tap (github.com/sunchang1990/homebrew-coot0).
# Needs: the release coot0-VERSION-macos-arm64.tar.gz already on GitHub, Homebrew, current Command Line Tools, the tap
# cloned at $(brew --repository)/Library/Taps/sunchang1990/homebrew-coot0 (brew tap sunchang1990/coot0), and gh.
#   1. points Formula/coot0.rb at the release tarball (url, version, sha256 of the download)
#   2. installs it with --build-bottle, packs the bottle (brew bottle) and labels it arm64_big_sur (coot0 runs on macOS 11+;
#      Homebrew then uses it on every newer arm64 macOS), writes the bottle block into the formula
#   3. uploads the bottle to the same GitHub release, uninstalls, installs again FROM THE BOTTLE, runs brew test
# It does not commit or push the tap: check the formula (git diff in the tap), then commit and push yourself.
# brew bottle switches Homebrew's developer mode on; this script switches it off again.
set -eu
V="${1:?usage: update_tap.sh VERSION   (e.g. 0.9.8.96-b39)}"
REPO=sunchang1990/coot0-macos; TAP=sunchang1990/coot0
export HOMEBREW_NO_AUTO_UPDATE=1 HOMEBREW_NO_INSTALL_CLEANUP=1
TAPDIR="$(brew --repository)/Library/Taps/sunchang1990/homebrew-coot0"; F="$TAPDIR/Formula/coot0.rb"
[ -f "$F" ] || { echo "the tap is not here: $TAPDIR  (brew tap $TAP)"; exit 1; }
URL="https://github.com/$REPO/releases/download/v$V/coot0-$V-macos-arm64.tar.gz"
W="$(mktemp -d)"; trap 'rm -rf "${W:?}"; brew developer off >/dev/null 2>&1 || true' EXIT
echo "== 1. formula -> $URL"
/usr/bin/curl -fsSL -o "$W/pkg.tar.gz" "$URL"
SHA=$(/usr/bin/shasum -a 256 "$W/pkg.tar.gz" | cut -c1-64)
/usr/bin/sed -i '' -E \
  -e "s#^  url \".*\"#  url \"$URL\"#" -e "s#^  version \".*\"#  version \"$V\"#" -e "s#^  sha256 \"[0-9a-f]{64}\"#  sha256 \"$SHA\"#" \
  -e "s#^    root_url \".*\"#    root_url \"https://github.com/$REPO/releases/download/v$V\"#" "$F"
echo "== 2. build the bottle"
brew uninstall coot0 >/dev/null 2>&1 || true
brew install --build-bottle "$TAP/coot0"
( cd "$W" && brew bottle --json --root-url="https://github.com/$REPO/releases/download/v$V" "$TAP/coot0" )
brew developer off >/dev/null 2>&1 || true
# Homebrew downloads "coot0-VERSION.TAG.bottle.tar.gz" (one dash) although brew bottle writes "coot0--VERSION..." locally
B="$W/coot0-$V.arm64_big_sur.bottle.tar.gz"
mv "$W"/coot0--"$V".*.bottle.tar.gz "$B"
BSHA=$(/usr/bin/shasum -a 256 "$B" | cut -c1-64)
/usr/bin/sed -i '' -E "s#arm64_big_sur: \"[0-9a-f]{64}\"#arm64_big_sur: \"$BSHA\"#" "$F"
echo "== 3. upload the bottle to release v$V, then install from it and test"
gh release upload "v$V" "$B" --repo "$REPO" --clobber
brew uninstall coot0
brew install "$TAP/coot0"
/usr/bin/python3 -c "import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if d.get('poured_from_bottle') else 'not installed from the bottle')" \
  "$(brew --cellar)/coot0/$V/INSTALL_RECEIPT.json"
brew test "$TAP/coot0"
echo "== done: tarball sha256 $SHA, bottle sha256 $BSHA"
echo "   next: cd \"$TAPDIR\" && git diff && git commit -am \"coot0 $V\" && git push"
