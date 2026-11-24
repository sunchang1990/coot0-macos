# Corresponding source for the coot0 binary package

The GPL and LGPL require that anyone who receives the binary package can get the complete source code that was used
to build it. For coot0 that is:

1. **Coot 0.9.8.96**: the release tarball `coot-0.9.8.96.tar.gz` from the Coot developers
   (https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ and https://github.com/pemsley/coot, tag/branch of the 0.9.8 series).
2. **Our changes to it**: the numbered patches in `m0/patches/` of this repository; `m0/setup.sh` applies them to the
   pristine tarball and reproduces the exact source tree that was compiled. Build instructions: `m0/README-m0.txt`.
3. **Build and packaging scripts**: `m0/tools/` (compile, link, relocate, bundle, check), `m0/m1-package/` (launcher,
   installer, tests).
4. **Bundled libraries from conda-forge**: the exact packages (name, version, build) are pinned in
   `env/coot-deps.explicit.txt` and `env/coot-rdkit.explicit.txt`. The source of each conda-forge package is the
   upstream release named in its recipe (https://github.com/conda-forge/<package>-feedstock, file `recipe/meta.yaml`,
   which lists the source URL and checksum).
5. **Libraries we built ourselves**: libart_lgpl 2.3.21, libgnomecanvas 2.30.3, goocanvas 1.0.0 (GNOME release
   tarballs, https://download.gnome.org/sources/), built with `canvas/build-scripts/build_canvas.sh` (source URLs and
   checksums in `canvas/build-scripts/src/sources.json`).
6. **The CCP4 monomer library** (not in the package from build 37; coot0 uses CCP4's, or downloads it with
   `coot0 --fetch-monomers`): https://github.com/MonomerLibrary/monomers (tested commit 0af022bf).

**Written offer.** For at least three years after we distribute a binary package, we will give anyone who asks a copy
of the complete corresponding source code of that package (items 1-6) on a common medium or for download, for no more
than the cost of providing it. Ask by opening an issue at https://github.com/sunchang1990/coot0-macos/issues. The
patches and scripts (items 2, 3 and 5) are in the coot0 source repository, https://github.com/sunchang1990/coot0-macos.
