# Building coot0 from source

From a clone of this repository to the installer tarball that users download. Apple Silicon Mac only, with macOS 11 or
newer. All steps are scripts. Nothing is installed outside the clone, except the conda package cache of micromamba or
conda.

## What you need

- Apple's command line tools: `xcode-select --install`
- micromamba, mamba or conda (for example [Miniforge](https://github.com/conda-forge/miniforge) or `brew install micromamba`)
- A folder whose path has no spaces (conda's scripts and the autotools builds cannot work in one); `bootstrap.sh`
  stops with a message otherwise. The installed program itself does not mind spaces.
- A network connection the first time. The steps download about 2 GB: the conda packages, the Coot 0.9.8.96 release
  tarball and three GNOME libraries. Everything is checked against pinned versions and checksums.

## Steps

```
git clone https://github.com/sunchang1990/coot0-macos.git
cd coot0-macos
./bootstrap.sh --make-envs                  # 1. prepare (about 15 minutes the first time)
m0/tools/build_all.sh                       # 2. build (about 5 minutes): m0/build/bundle
m0/build/bundle/run-coot.sh                 #    try it
m0/build/bundle/tests/run-headless-tests.sh #    the self-test (about 20 minutes)
m0/tools/make_binary_tarball.sh m0/build/bundle   # 3. the installer: coot0-<version>-macos-arm64.tar.gz
m0/tools/make_source_tarball.sh <version> .       #    the matching source archive (commit first)
```

**1. `bootstrap.sh`** prepares everything the build needs:
- **Conda environments:** creates `envs/coot-deps` (GTK 2 for macOS, Python 3.11, Guile 3, Clipper, MMDB2 and so on) and
  `envs/coot-rdkit` (RDKit). Both are made from the exact package lists in `env/`.
- **Canvas libraries:** builds libart_lgpl, libgnomecanvas and goocanvas from download.gnome.org into `canvas/prefix`
  (`canvas/build-scripts/build_all.sh`).
- **Coot source:** downloads the Coot 0.9.8.96 release tarball from Paul Emsley's site and checks its sha256. It then
  makes `m0/coot-src`: the pristine source plus the numbered patches in `m0/patches`, as a git repository
  (`m0/setup.sh`). To use an unpacked copy you already have, set `COOT_PRISTINE=/path/to/coot-0.9.8.96`.

Running it again skips whatever is already there.

**2. `m0/tools/build_all.sh`** builds the program and the self-contained folder:
- compiles the 412 source files, then links `coot-bin` with the macOS OpenGL view (`m0/coot-src/compat/gl-seam`);
- assembles Coot's data files and the package files (launcher, installer, tests, documents, from `m0/m1-package`);
- copies every library into the bundle with relative paths, signs it ad hoc and checks the result
  (`m0/tools/bundle_check.py`).

The CCP4 monomer library is not part of the package. coot0 uses CCP4's library when CCP4 is installed; otherwise
`coot0 --fetch-monomers` downloads it from github.com/MonomerLibrary/monomers.

**3. `make_binary_tarball.sh`** writes the installer tarball, leaving out everything a test run leaves behind.

## Releasing

1. Create the GitHub release with the installer tarball and the source archive (`make_source_tarball.sh`, after the
   last commit).
2. Update the Homebrew tap (github.com/sunchang1990/homebrew-coot0) with `m0/tools/update_tap.sh <version>`. It points
   the formula at the new tarball and builds the Homebrew bottle from it. It then uploads the bottle to the same
   release, reinstalls from the bottle and runs `brew test`. It needs current Command Line Tools. Check the formula with
   `git diff` in the tap, then commit and push the tap.

## Changing coot0

- **Python, Scheme, data and tests:** edit the files under `m0/coot-src/{python,scheme,rcrane,compat/pygtk2}` and
  `m0/m1-package`. Then `m0/tools/dev_sync.sh m0/build/bundle` copies the changed files into the bundle without a rebuild.
- **C++:** rebuild with `m0/tools/build_all.sh`, which compiles all 412 files again (a few minutes). To compile only
  some, `m0/tools/m0_build.py` has `--only REGEX`; the build notes describe how it was used.
- **Record a change to Coot's source** as a new numbered patch:
  `GIT_CONFIG_GLOBAL=/dev/null bash m0/newpatch.sh 00NN-short-name`. `m0/coot-src` itself is not stored in git.
- **Every fix gets a test** in `m0/m1-package/tests` that fails without the fix. The suites run with
  `tests/run-headless-tests.sh`, and `tests/run-real-window-checks.sh` opens a real window for about 15 seconds.
- **Build notes:** the technical notes of every build are in `m0/README-m0.txt`.

## Licences

See [LICENSING.md](LICENSING.md) and [CORRESPONDING_SOURCE.md](CORRESPONDING_SOURCE.md).
