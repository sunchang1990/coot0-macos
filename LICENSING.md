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

Licensed under the **GNU General Public License, version 3** (GPL-3.0-only). This covers the work of this project:

- the patches in `m0/patches/` (the changes made to Coot's source files, and the new files they add, such as the
  macOS OpenGL view `compat/gl-seam/`, the PyGTK-2 replacement `compat/pygtk2/` and the splash helper);
- the build, packaging and check tools in `m0/tools/` and `m0/setup.sh`;
- the launcher, installer, uninstaller, tests and documents in `m0/m1-package/`.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License version 3 as published by the Free Software Foundation. It is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

## 3. Third-party components in the binary package

GTK 2, Python, Guile, RDKit, Clipper, MMDB2, the CCP4 monomer library and the other bundled libraries and data keep
their own licences, all of which allow distribution together with GPL-3.0 code. The list with versions and licences is
`THIRD_PARTY_LICENSES.md` and the licence texts are in `licenses/` (in the package: next to this file; in the source
repository: in `m0/m1-package/`).

## The binary package as a whole

The program in the package combines parts 1-3 and is distributed under **GPL-3.0**: Coot's "version 3 or later"
permits version 3, the coot0 modifications are version 3, and some bundled libraries (e.g. GNU Readline) are
"version 3 only". The source of everything is available: [`CORRESPONDING_SOURCE.md`](CORRESPONDING_SOURCE.md).

## Not an official Coot release

coot0 is an independent, unofficial build of Coot 0.9.8.96 for Apple Silicon Macs. It is not made by the Coot
developers, and they do not provide support for it: please report problems with coot0 to its author (Chang Sun),
not to the Coot developers. The name "Coot" is used only to say what this program is.
