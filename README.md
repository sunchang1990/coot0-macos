# coot0: Coot 0.9.8.96 for Apple Silicon Macs

**coot0** is an unofficial build of [Coot](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/) 0.9.8.96, the
macromolecular model-building program by Paul Emsley and colleagues, that runs natively on Apple Silicon Macs
(macOS 26 Tahoe tested) without XQuartz. It aims to be **Coot 0.9 as you know it**: the same menus, dialogs, keyboard
and mouse behaviour, the same Python and Scheme scripting API, so existing scripts, habits and teaching material keep
working. It changes only what has to change for Coot 0.9 to run on a current Mac.

It is not made, endorsed or supported by the Coot developers. Please report problems here.

## What works

- The full Coot 0.9.8.96 interface (GTK 2, drawn natively by macOS), with sharp Retina rendering of the 3D view.
- **Coot's Python scripting and its Python GUI** (Python 3.11): the extension menus and dialogs that Coot 0.9 builds
  in Python (Glyco, NCS, PISA, PDB-REDO, Fit Loop, the various sliders, RCrane for RNA, ...) run as written, on a
  replacement for the old PyGTK 2 library. Your own PyGTK-based Coot 0.9 scripts should work too.
- **Scheme scripting** (Guile 3): Calculate > Scripting > Scheme, `--script file.scm`, start-up scripts. (Coot's
  Scheme *GUI* scripts, written for guile-gtk, are not available; their functions are provided by the Python versions.)
- RDKit-based ligand tools (Lidia, SMILES import), the CCP4 monomer library, reference structures, Ramachandran data.
- CCP4 (refmac5, acedrg, ...) and Phenix/CCP4 reduce + probe are found automatically when installed; they are
  optional.
- 19 automated test suites (about 300 checks) and a real-window audit of every menu entry and toolbar button.

## Changes from the original Coot 0.9.8.96

Besides what it takes to run on a current Mac (native macOS windows instead of X11, Python 3, Retina drawing), coot0 fixes
some things that did not work in the original 0.9.8.96 release. The changes you will notice most:

- **Calculate > All Molecule... > Refine/Improve Ramachandran Plot...** is back in the menu (build 20). The code was in
  Coot 0.9.8.96, but a mis-indented line meant the menu entry was never created. It runs Stepped Refine with Ramachandran
  restraints switched on, residue by residue over the whole molecule.
- **New: Calculate > All Molecule... > Refine/Improve Ramachandran Plot (try peptide flips)...** (build 21). Ramachandran
  restraints alone cannot turn a peptide that is built the wrong way round (it is about 180 degrees away). This entry
  refines every residue twice, once as it is and once with the peptide to the next residue flipped, and keeps the
  flip only if it is better: a better Ramachandran region for the two residues, or the same regions and a clearly
  (at least 10%) better fit to the map. Flips that were kept are reported in the status bar. The original entry is
  unchanged. In the tests, four peptides flipped on purpose were all put back and four correct ones left alone.
- **You can watch whole-molecule refinement** (build 20 for Fit Protein; build 14 for Stepped Refine). Fit Protein, Stepped
  Refine and both Refine/Improve Ramachandran Plot entries now show each residue being refined in Coot's usual refinement style (the
  highlighted "intermediate atoms") for a moment before accepting it, instead of the atoms jumping to their result. The
  map is re-contoured around each residue, the **Stop** button on the toolbar works at any time, and no "Accept
  Refinement?" window is left behind. `COOT_STEPPED_REFINE_SHOW=<seconds>` sets how long each residue is shown (default
  0.6; 0 = the old immediate behaviour).
- Stepped Refine, Refine/Improve Ramachandran Plot and Fit Protein also work on **RNA / DNA** (residues without CA are centred
  on C1'). Fit Protein's rotamer search itself is for protein side chains.

The full list, build by build: [`m0/m1-package/CHANGELOG.md`](m0/m1-package/CHANGELOG.md).

## Install

Download `coot0-<version>-macos-arm64.tar.gz` from [Releases](../../releases), then in Terminal:

```
tar -xzf coot0-<version>-macos-arm64.tar.gz
cd coot0-<version>
./install.sh
```

The installer checks your Mac, installs into `~/.local/share/coot0/<version>` (you can choose another folder), creates
the command `coot0` and tells you how to use it. Then, in a new Terminal window: `coot0 --pdb model.pdb --auto data.mtz`.
Details: `README-FIRST.txt` in the package.

Requirements: an Apple Silicon Mac (M1 or later), macOS 11 or newer (macOS 26 tested), about 1 GB of disk space.
Intel Macs and Linux are not supported.

## How coot0 relates to other Coot versions

| | **Coot 0.9.x** (upstream) | **Coot 1.x** (upstream) | **Bandicoot** | **coot0** (this project) |
|---|---|---|---|---|
| What it is | The original Coot 0.9 series by Paul Emsley et al. (GTK 2, fixed-function OpenGL) | The current Coot, redesigned and actively developed (GTK 4, modern OpenGL) | A fork of Coot 0.9.8.95 by the Fraser lab (UCSF), turned into a separate project with its own new features | Coot 0.9.8.96 kept as it is, ported to run on Apple Silicon |
| On a current Mac | Older builds depend on XQuartz and do not run well on recent macOS | Runs natively (e.g. via CCP4 or Homebrew) | Runs natively (macOS and Linux) | Runs natively (macOS on Apple Silicon only) |
| Interface | Coot 0.9 | New interface | New wxWidgets interface, reorganised menus, many new features | Coot 0.9, unchanged |
| Python / Scheme scripts of Coot 0.9 | Yes (Python 2 era) | New API | Python 3; many Python dialogs rewritten in C++; no Scheme | Python 3 with the Coot 0.9 Python GUI working as written; Scheme scripting |
| When to choose it | | For new work and new features: the version the Coot developers recommend and support | A modernised Coot 0.9 with new features, or Linux | You want Coot 0.9 exactly as you know it on an Apple Silicon Mac, including its scripts and plugins |

coot0 and Bandicoot started from the same problem and solved parts of it in similar ways (GTK 2 on macOS's own
graphics, Retina-aware drawing, Python 3), but independently and with different aims. If you want new features, look at
Coot 1 and Bandicoot first.

## Building from source

The program is built from the Coot 0.9.8.96 release tarball plus the numbered patches in `m0/patches/`
(`m0/setup.sh` applies them). Build and packaging tools are in `m0/tools/`; the technical notes of every build are in
`m0/README-m0.txt`; the build environments are pinned in `env/`. See `CORRESPONDING_SOURCE.md`.

## Licence

Coot itself is licensed by its authors under GPL-3.0-or-later; the coot0 modifications (patches, tools, installer)
are Copyright (C) 2026 Chang Sun under GPL-3.0; the bundled third-party libraries keep their own licences. The package
as a whole is distributed under GPL-3.0. Details: [`LICENSING.md`](LICENSING.md); licence text: [`LICENSE`](LICENSE).

## Credits

Coot: Paul Emsley, Kevin Cowtan, Bernhard Lohkamp and the Coot contributors. RCrane: Kevin Keating. The libraries in
the package are listed in `m0/m1-package/THIRD_PARTY_LICENSES.md`.

The macOS / Apple Silicon port: Chang Sun.

Thanks to the members of Huilin Li's lab for testing coot0 and for their feedback, and to Paul Emsley for supporting
the project.
