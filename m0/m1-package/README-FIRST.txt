Coot 0.9.8.96 for Apple Silicon Macs ("coot0")
==============================================
An independent build of Coot 0.9.8.96 (Paul Emsley et al., MRC-LMB) that runs natively on Apple Silicon Macs
without XQuartz.  Menus, look and the Python / Scheme scripting are those of Coot 0.9.8.96.

INSTALL (about 1 minute)
  In Terminal, in this folder:      ./install.sh
  or double-click "Install coot0.command" in Finder (if macOS refuses to open it: right-click > Open).
  The installer checks the Mac, copies Coot to ~/.local/share/coot0/<version> (you can choose another folder),
  creates the command ~/.local/bin/coot0 and adds ~/.local/bin to your PATH (~/.zshrc; also ~/.bash_profile if
  you use bash).  It prints every change it makes.  This folder can be deleted afterwards.

RUN
  Open a new Terminal window, go to your project folder, and type:   coot0
  e.g.   coot0 --pdb model.pdb --auto refine_001.mtz
  Coot writes coot-backup/ and 0-coot-history.py into the folder you start it from.

  RESOLUTION: coot0 draws the 3D view at full Retina resolution (2 pixels per point: sharper atoms, bonds and labels).
  If the view is slow (large maps, an external non-Retina monitor, an older Mac) or looks wrong, start with
      coot0 --legacy
  for the standard resolution (1 pixel per point, enlarged by macOS: softer, but less work for the graphics chip).
  (--retina / --legacy also work with ./run-coot.sh in the unpacked folder, which uses the standard resolution unless
  you give --retina.  The environment variable COOT_RETINA=1 / 0 does the same.)
  Your Coot preferences and logs are kept in ~/Library/Application Support/coot0.

MONOMER LIBRARY (restraint dictionaries: needed to refine, regularise and add ligands)
  Not inside this folder.  With CCP4 installed, coot0 uses CCP4's library: nothing to do.  Without CCP4, install.sh offers
  to download it (about 110 MB from github.com/MonomerLibrary/monomers); later:  coot0 --fetch-monomers
  (or ./fetch-monomers.sh in this folder).  coot0 --fetch-monomers latest gets the newest version instead of the tested one.

OTHER PROGRAMS (optional)
  CCP4 (/Applications/ccp4-*): Run Refmac, Ligand Builder > Apply and SMILES import (acedrg), ProSMART, Privateer ...
  reduce + probe (CCP4 or Phenix): Probe Clashes, Add Hydrogens.   Everything else works without them.
  coot0 --diagnose shows what was found.

LICENCE
  Coot is free software by Paul Emsley et al. (GPL-3.0-or-later).  The coot0 changes for macOS: Copyright (C) 2026
  Chang Sun, GPL-3.0-or-later.  The package as a whole is distributed under GPL-3.0; bundled libraries keep their own licences.
  See LICENSING.md, LICENSE, THIRD_PARTY_LICENSES.md, licenses/ and CORRESPONDING_SOURCE.md (how to get the source).
  coot0 is an independent build based on the Coot 0.9.8.96 source code from Paul Emsley's website.
  Report problems at https://github.com/sunchang1990/coot0-macos/issues.

HELP
  coot0 --legacy        standard (non-Retina) resolution for the 3D view
  coot0 --diagnose      what this Mac has, where the logs are
  coot0 --fetch-monomers  download the monomer library (not needed when CCP4 is installed)
  coot0 --self-test     full self-test (about 15 minutes; send the result if something does not work)
  coot0 --uninstall     remove coot0
  CHANGELOG.md          what changed in each build;  TEST-PROTOCOL.md  the test notes of each build
