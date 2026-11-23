# coot0: Coot 0.9 for Apple Silicon Macs

**Coot 0.9, exactly as you know it, running natively on today's Macs.**

[Coot](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/), by Paul Emsley and colleagues, is one of the most widely
used programs for building and fixing protein and nucleic-acid models in X-ray and cryo-EM maps. Many labs still work
in, and teach with, its 0.9 series: the menus people know by heart, the keyboard and mouse habits, and years of lab
scripts and plug-ins written for its Python and Scheme interface.

The Mac builds of Coot 0.9 draw their windows through XQuartz, the X11 server for macOS. At the time of writing
(November 2026), XQuartz was disrupted by the macOS 26 Tahoe update, and its developers are working to restore it.
Coot 1 runs natively, but it is a redesign with a new interface and a new scripting interface; moving to it means
retraining people and rewriting scripts.

**coot0 does not need XQuartz.** It is Coot 0.9.8.96 rebuilt for Apple Silicon (M1 and later), and it draws its
windows by calling macOS's own Quartz graphics directly, so it works whatever the state of XQuartz. It also uses the
full Retina resolution of a modern Mac for the 3D view. The interface, the menus and the scripting functions are those
of Coot 0.9, so a lab can keep its workflows, scripts and teaching material, and new members learn from the same
material.

coot0 is an independent build based on the Coot 0.9.8.96 source code from
[Paul Emsley's website](https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/). Please report problems with coot0 in
this repository's [Issues](../../issues).

## What it gives you

- **No new interface to learn.** Coot 0.9.8.96's own windows, menus, dialogs, keys and mouse actions, drawn by macOS
  itself, with Retina rendering of the 3D view. A trackpad two-finger click stands in for the middle mouse button.
- **Your scripts keep working.** Python 3 and Scheme (Guile 3) scripting with Coot 0.9's function names. The extension
  menus and dialogs that Coot 0.9 builds in Python run as written: Glyco, NCS, PISA, PDB-REDO, Fit Loop, RCrane for RNA
  and the others.
- **Scripting you can look up.** All of Coot 0.9's roughly 1,700 Python and Scheme functions are documented, with an
  example for each one that was run on test data and a note of what it actually did. There is also a cookbook of 85
  everyday recipes in both languages, and you can search menus and documentation from the Help menu.
- **Some things work better than in the original 0.9.8.96.** Several features that were broken in the released 0.9.8.96
  now work, and a few were added for Ramachandran clean-up and for watching whole-molecule refinement (see below).
- **Your other programs are found.** CCP4 (refmac5, acedrg, ...) and the reduce and probe tools of CCP4 or Phenix are
  picked up automatically when installed. RDKit ligand tools (Lidia, SMILES import) and the CCP4 monomer library are
  included.
- **Tested.** Every menu entry and toolbar button has been tried in a real window, about 530 automated checks run
  against every release, and members of a structural biology lab have tested each release on their own data.

## What is different from the original Coot 0.9.8.96

coot0 changes as little as possible. Besides what it takes to run on a current Mac, the changes you will notice most
are these:

- **Refine/Improve Ramachandran Plot is back** (Calculate > All Molecule...). The code was in 0.9.8.96, but the menu
  entry was never created.
- **New: Refine/Improve Ramachandran Plot (try peptide flips).** It tries flipping each peptide and keeps a flip only
  when the map supports it. At the end it reports which peptides turned. How it decides:
  [docs/try-peptide-flips.md](m0/m1-package/docs/try-peptide-flips.md).
- **You can watch whole-molecule refinement.** Fit Protein, Stepped Refine and both Ramachandran entries show each
  residue being refined, re-contour the map as they go, and stop when you press Stop. They also work on RNA and DNA.
- **The Python and Scheme scripting windows show results.** Each window shows the command, what it printed, its result
  and any error, and keeps a history. In 0.9.8.96 the Scheme window showed nothing.
- **Bugs found while testing every function are fixed.** For example, mmCIF files written from a script no longer
  repeat the model, and several Scheme functions now return what their Python versions return.

The full list, build by build, is in [CHANGELOG.md](m0/m1-package/CHANGELOG.md).

## Install

Requirements: an Apple Silicon Mac (M1 or later), macOS 11 or newer, and about 1 GB of disk space. It has been tested on
macOS 26. Intel Macs and Linux are not supported.

Download `coot0-<version>-macos-arm64.tar.gz` from [Releases](../../releases), then in Terminal:

```
tar -xzf coot0-<version>-macos-arm64.tar.gz
cd coot0-<version>
./install.sh
```

The installer checks your Mac, installs coot0 into `~/.local/share/coot0/<version>` (you can choose another folder) and
creates the command `coot0`. Then, in a new Terminal window:

```
coot0 --pdb model.pdb --auto data.mtz
```

More details are in `README-FIRST.txt` in the download.

## Which Coot should I use?

| | **coot0** (this project) | **Coot 1.x** | **Bandicoot** |
|---|---|---|---|
| What it is | Coot 0.9.8.96 kept as it is, rebuilt for Apple Silicon | The current Coot, redesigned and actively developed by the Coot team | A fork of Coot 0.9.8.95 by the Fraser lab (UCSF), with a new interface and new features |
| Interface | Coot 0.9, unchanged | New | New (wxWidgets) |
| Coot 0.9 scripts and plug-ins | Python and Scheme, as written | New scripting interface | Python 3; no Scheme |
| Platforms | macOS on Apple Silicon | macOS and Linux (and others) | macOS, Linux |
| Choose it if | You want Coot 0.9 exactly as you know it on a current Mac | You want the newest features and the version the Coot developers support | You want a modernised Coot 0.9 with new features, or Linux |

## Building from source

coot0 is built from the Coot 0.9.8.96 release tarball plus the numbered patches in `m0/patches/`, which `m0/setup.sh`
applies. The build and packaging tools are in `m0/tools/`, the notes for every build are in `m0/README-m0.txt`, and the
build environments are pinned in `env/`. Where to get every part of the source:
[CORRESPONDING_SOURCE.md](CORRESPONDING_SOURCE.md).

## Licence

coot0 is free software under the GNU General Public License, version 3. Coot itself is licensed by its authors under
GPL-3.0-or-later. The coot0 changes (patches, tools and installer) are Copyright (C) 2026 Chang Sun, under the same
licence, GPL-3.0-or-later.
The bundled third-party libraries keep their own licences. Details are in [LICENSING.md](LICENSING.md), and the licence
text is in [LICENSE](LICENSE).

## Credits

Coot: Paul Emsley, Kevin Cowtan, Bernhard Lohkamp and the Coot contributors. RCrane: Kevin Keating. The bundled
libraries are listed in [THIRD_PARTY_LICENSES.md](m0/m1-package/THIRD_PARTY_LICENSES.md).

Port to macOS and Apple Silicon: Chang Sun.

Thanks to the members of Huilin Li's lab for testing coot0 and for their feedback, and to Paul Emsley for supporting
the project.
