# Licensing of coot0

coot0 consists of three separately licensed parts. Each keeps its own copyright and licence; this file states them
side by side. The full text of the GNU General Public License version 3 is in [`LICENSE`](LICENSE).

## 1. Coot 0.9.8.96 (the original program)

Copyright Paul Emsley, Kevin Cowtan, Bernhard Lohkamp and the other Coot authors (see `AUTHORS` in the Coot source).
Licensed by its authors under the **GNU General Public License, version 3 or (at your option) any later version**
(GPL-3.0-or-later); a few files are GPL-2.0-or-later or LGPL. RCrane, shipped with Coot, is Copyright Kevin Keating,
under the Educational Community License 2.0. These licences are unchanged by this project; coot0 does not relicense
any Coot code.

## 2. The coot0 modifications (this project)

Copyright (C) 2026 Chang Sun.

Licensed under the **GNU General Public License, version 3 or (at your option) any later version** (GPL-3.0-or-later),
the same terms as Coot itself. This covers the work of this project:

- the patches in `m0/patches/` (the changes made to Coot's source files, and the new files they add, such as the
  macOS OpenGL view `compat/gl-seam/`, the PyGTK-2 replacement `compat/pygtk2/` and the splash helper);
- the build, packaging and check tools in `m0/tools/` and `m0/setup.sh`;
- the launcher, installer, uninstaller, tests and documents in `m0/m1-package/`.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version. It is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

**Notice of modification.** coot0 is a modified version of Coot 0.9.8.96. It was modified by Chang Sun from November
2026 onwards to run on macOS on Apple Silicon. Every change is one of the numbered patches in `m0/patches/` of the
source repository, whose git history records when each was made. `CHANGELOG.md` lists the changes build by build.

## 3. Third-party components in the binary package

GTK 2, Python, Guile, RDKit, Clipper, MMDB2, the CCP4 monomer library and the other bundled libraries and data keep
their own licences, all of which allow distribution together with GPL-3.0 code. The list with versions and licences is
`THIRD_PARTY_LICENSES.md` and the licence texts are in `licenses/` (in the package: next to this file; in the source
repository: in `m0/m1-package/`).

## The binary package as a whole

The program in the package combines parts 1-3 and is distributed under **GPL-3.0**: Coot's "version 3 or later"
permits version 3, the coot0 modifications are "version 3 or later", and some bundled libraries (e.g. GNU Readline)
are "version 3 only". The coot0 source itself (Coot plus the patches, without those libraries) can be used under
version 3 or any later version. The source of everything is available: [`CORRESPONDING_SOURCE.md`](CORRESPONDING_SOURCE.md).

## An independent build

coot0 is an independent build for Apple Silicon Macs based on the source code of Coot 0.9.8.96 from Paul Emsley's
website (https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/). Please report problems with coot0 in the Issues of
its repository, https://github.com/sunchang1990/coot0-macos/issues. The name "Coot" is used only to say what this program is.
