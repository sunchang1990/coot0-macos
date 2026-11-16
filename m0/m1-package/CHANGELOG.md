# Changelog: Coot 0.9.8.96 for Apple Silicon (macOS, no XQuartz)

Base: Coot 0.9.8.96 (the release tarball), ported to run natively on macOS / Apple Silicon with GTK 2 (Quartz) and the old fixed-function
OpenGL that Coot 0.9 uses; menus, look and Python API are those of 0.9.x.  Every change below is a numbered patch (`patches/00NN-*.patch`,
applied to the pristine tree by `setup.sh`) or a change of the packaged data / scripts / tests; `README-m0.txt` has the technical notes of every
round, `TEST-PROTOCOL.md` has the user-facing explanation and the checks for you (newest round first).  A "build" is one delivered zip.
"Verified" means a headless test (no window server in the build environment); what only a screen can show is marked "on screen: not verified".

## Build 22  (patch 0038 rama-alt-confs-protein-only-report-fill-partial; Python only, `bin/coot-bin` and `lib/` as in build 13)
- Fixed (user report 16 Nov): **Refine/Improve Ramachandran Plot (try peptide flips)** tried no flip when residue i or i+1 had alternate conformations
  (it fell back to a plain refinement of each alt conf).  Now: shared peptide atoms (only side chains split) -> both tries refine every alt conf of the
  zone, one decision; peptide atoms split (CA/C/O of i, N/CA/H of i+1 with alt confs) -> pepflip(i, alt) and the decision per alt conf, scored on that
  conformer alone (Coot does not classify residues with a split main chain, so the conformer is read into a hidden temporary molecule for the
  Ramachandran regions, then closed; map fit = density at that conformer's atoms and the shared ones).
- Changed (user request): both **Refine/Improve Ramachandran Plot** entries touch amino acids only (main-chain N, CA, C; modified ones count).
  Ligands, waters and nucleotides are skipped (non-water ones are named in the terminal), and the refinement zone is i-1..i+1 limited to amino acids
  joined by a peptide bond (C-N < 2.5 A).  Before, Coot's refine_auto_range took i-1..i+1 by number, so a ligand numbered after the last amino acid
  of a chain was refined with it, and ligands themselves were refined.
- New (user request): a **report at the end of a (try peptide flips) run, or when it is stopped**: number of peptides flipped and tried, the list of
  flips, the residues not touched; in the terminal, the status bar and a window.  `interruptible_fit_protein(imol, func, when_done=None)`.
- Changed (user request): **Fill Partial Residues** (Calculate > All Molecule > [Post MR] ..., Calculate > Modelling > ...): the terminal lists each
  residue filled with the atoms added, and the ones not filled (main chain N/CA/C missing); no hydrogens are added (as before); the model chooser
  only appears when more than one model is loaded (the Modelling entry used the molecule at the centre); if several maps are loaded and none is the
  refinement map, the map is asked for first (before: filled, then asked, and the rotamer fit / refinement was skipped).
- Tests: `gui-dialogs` 53 -> 61 (alt confs shared and split; ligand + water untouched by both entries; report at the end and after Stop; Fill Partial
  Residues list and menus); build 21 fails all 8.
- On screen: not verified by me (headless only).

## Build 21  (patch 0037 rama-try-peptide-flips; Python only, `bin/coot-bin` and `lib/` as in build 13)
- New: **Calculate > All Molecule... > Refine/Improve Ramachandran Plot (try peptide flips)...** (user request 16 Nov; the original entry is unchanged).
  For each residue i with a protein residue i+1: try A = refine i-1..i+1 with Ramachandran restraints; restore; try B = pepflip(i) + the same refinement.
  B is kept if the Ramachandran regions of i, i+1 (Coot's own outlier 0 / allowed 1 / favoured 2) sum higher, or are equal and the map fit
  (density_score_residue of i, i+1) is at least 10% better (`rama_flip_density_gain`); otherwise A is restored.  Both tries are shown like Stepped
  Refine; Stop after try A keeps A.  Waters, nucleotides, chain ends, insertion codes and alt confs: refined as in the original entry (no flip tried).
  Kept flips go to the status bar and the log ("INFO:: rama flip"); `rama_flip_log` has every decision.
- Tests: `gui-scripts` 15 -> 16, `gui-dialogs` 48 -> 53 (4 peptides of tutorial-modern flipped on purpose are put back, O within 0.5 A; 4 correct
  ones kept; both tries shown with Ramachandran restraints on; Stop; the decision rule); build 20 fails all 6.
- On screen: not verified by me (headless only).

## Build 20  (patch 0036 fit-protein-rama-shown-refinement; Python only, `bin/coot-bin` and `lib/` as in build 13)
- Fixed: **Calculate > All Molecule... > Refine/Improve Ramachandran Plot...** never appeared: in the 0.9.8.96 source the line that creates the entry is
  indented into the function the entry calls.  Now in the menu (Stepped Refine with Ramachandran restraints on).  Dialog title typo "Ramachanran" fixed.
- Changed: **Fit Protein** shows its refinement like Stepped Refine: after the rotamer search each residue is refined as an ordinary refinement, its atoms
  are drawn in the refinement style for `COOT_STEPPED_REFINE_SHOW` seconds (default 0.6), then accepted; Stop works; Coot's "Accept Refinement?" window
  is hidden.  Before, it used immediate replacement (AutoAccept): nothing drawn, the residue jumped.  Also: centre on C1'/P for residues without CA
  (RNA/DNA), map re-contoured at every residue, 400 minimiser steps per frame during the run (as Stepped Refine; restored afterwards).
  The display code is shared: `refine_and_show()` in fitting.py (Stepped Refine and Refine/Improve Ramachandran Plot use it through `refine_auto_range_and_show`).
- Tests: `gui-scripts` 14 -> 15 (menu entry + opens the molecule chooser; fails on build 19); `gui-dialogs` 45 -> 48 (Fit Protein shown, Fit Protein on
  RNA 1EHZ, Ramachandran refinement shown with restraints on; build 19 fails the first two).  Test fix: `check()` of gui_python_load.py counted any
  returned message as a pass, so its "condition or 'message'" checks could not fail (all of them pass on build 19 with the fix).
- On screen: not verified by me (headless only).

## Build 19  (no patch: package only; the build for the lab)
- New: licence files in the package: `LICENSE` (GPL-3.0), `LICENSING.md` (Coot GPL-3.0-or-later by its authors; the coot0 changes Copyright (C) 2026
  Chang Sun, GPL-3.0; third-party components; the package as a whole GPL-3.0), `CORRESPONDING_SOURCE.md` (source of every part, written offer),
  `THIRD_PARTY_LICENSES.md` + `licenses/` (generated by `m0/tools/gen_licenses.py`; FFTW 2, FreeType and SQLite texts added by hand). README-FIRST: LICENCE section.
- Fixed: `coot0 --self-test` made macOS show its "coot-bin Not Opened" dialog (the installer test started the copy it flags with the download quarantine on purpose).
- Tests: `installer` 22 -> 26 (fails on build 18).

## Build 18  (no patch: package only)
- Changed: **`coot0` uses the Retina (2x) 3D view by default**; new option **`--legacy`** (also for `./run-coot.sh`) for the standard resolution. `COOT_RETINA=0/1` overrides.
  The unpacked folder keeps the standard resolution unless `--retina` is given.  `README-FIRST.txt` and the installer summary explain it.
- Tests: `installer` 19 -> 22 (fails on build 17).

## Build 17  (no patch: package only; `bin/coot-bin`, `lib/` and Coot's scripts as in build 16)
- New: **`install.sh`** (and **Install coot0.command** for Finder): checks the Mac (arm64, macOS, disk, CCP4 / Phenix / reduce / probe with what each is for),
  removes the download quarantine from the installed copy, installs into `~/.local/share/coot0/<version>` (asked; any folder), writes the command
  **`~/.local/bin/coot0`**, adds one marked PATH line to `~/.zshrc` (and `~/.bash_profile` / `~/.bashrc` for bash users) and prints it, runs a 30 s start test.
  `coot0` runs Coot in the current folder; preferences and logs per user in `~/Library/Application Support/coot0`. `coot0 --diagnose / --self-test / --uninstall`; `uninstall.sh`.
- New: distribution as `coot0-<version>-macos-arm64.tar.gz` (top folder `coot0-<version>`), `README-FIRST.txt`, `VERSION`.
- Changed: launcher finds reduce / probe of Phenix 2.x (`bin/`, in /Applications or the home folder); `COOT_STATE_DIR`; the log names the state folder.
- Tests: `installer` (19 checks; fails on build 16).

## Build 16  (patch 0035 round16-lidia-acedrg-env; no C++ change: `bin/coot-bin` and `lib/` are those of build 13)
- Fixed: **Ligand Builder (Lidia) > Apply**, SMILES import and the acedrg link tool: acedrg's environment was built from `CBIN`, which exists only if Coot was started from a
  shell that sourced CCP4's setup (`KeyError: 'CBIN'` otherwise, e.g. started from Finder); PATH was joined with `;` and Coot's own PYTHONPATH went to CCP4's Python.
  acedrg now gets CCP4's variables like refmac5 does.  Test: benzene from a Lidia sketch -> ligand + dictionary with the real acedrg of CCP4 9.  On screen: not verified.
- Changed: Apply with an empty sketch says "Draw a molecule first" instead of starting acedrg (which stopped with a traceback; found by the real-window audit).
- Real-window GUI audit of build 15 on the iMac: 255 ok, 6 known GTK warnings, 0 crashes, 0 hangs, 0 dead entries; the two build-14 errors are gone.

## Build 15  (patch 0034 round15-rna-stepped-refine-pdb-redo-toolbar; no C++ change: `bin/coot-bin` and `lib/` are those of build 13)
- Fixed: **Stepped Refine did nothing on RNA/DNA.** Coot's `refine_auto_range` finds a residue by its C-alpha atom, which nucleotides do not have
  ("Can't get index for resno1" for every residue in your log), and the view was moved to "CA" too.  Residues without CA are now centred on C1'
  (else P, else their first atom) and refined as the zone residue-1 .. residue+1 (the range `refine_auto_range` uses for proteins).  Proteins: unchanged.
  Test: one Stepped Refine step on nucleotide A 22 of tRNA 1EHZ moves that nucleotide and nothing outside 21-23; backbone O3'-P stays 1.60 A.  On screen: not verified.
- Fixed: **File > Fetch PDB & Map using PDB-REDO** saved PDB-REDO's "404 Not Found" HTML page as the model for entries that PDB-REDO serves only as
  mmCIF (your 9E5H: read error, map only), and then ran the HTML "guided tour" as a script ("Unbound variable <html>").  Every download is now checked
  (an HTML page or empty file is not data and is removed), the model falls back to `<id>_final.cif`, the guided tour is run only if it exists, and a message
  says what could not be fetched (no such entry, or no network).  The menu's Scheme function now calls the Python version (its guided tour window exists).
  Checked live against pdb-redo.eu: 9E5H (mmCIF-only) and 1EHZ load model + maps.
- Fixed: **Stop / Cancel / Continue toolbar buttons of Stepped Refine and Fit Protein**: after Stop, starting a new run (or two runs at once) left the old
  buttons on the toolbar, and pressing them raised `AttributeError: 'bool' object has no attribute 'destroy'` (found by the real-window GUI audit).
  A new run now ends the old one and removes its buttons; pressing a button of a finished run is harmless.
- Fixed: a PDB-REDO code that does not exist: PDB-REDO answers with `{"error":"Not Found"}` (JSON), which was kept as `<id>_final.pdb`.  Downloads are now accepted only
  if they look like what they should be (PDB records, mmCIF `data_`, MTZ header).
- Tests: the real-window GUI audit no longer presses hidden buttons (it pressed Lidia's hidden developer "test function" button: `No module named 'recap_wrapper'`;
  that button is not visible to users and is left as upstream has it).
- Fixed: two Gtk-WARNINGs per file dialog about `home/.local/share/recently-used.xbel` (the launcher's private HOME lacked that folder).

## Build 14  (patch 0033; no C++ change: `bin/coot-bin` and `lib/` are those of build 13)
- Fixed: **Alt Conf Occupancy slider, "OK" did nothing.** `set_alt_conf_occ` compared a list with a number (`alt_confs > 1`), which Python 2 accepted and
  Python 3 rejects (TypeError, 58 of them in your log). The same comparison was in `rename_alt_confs` (swap alt confs A and B). Tests: slider -> OK -> occupancies 0.4/0.6 and window closed; swap.
- Fixed: **Stepped Refine left Coot's own "Accept Refinement?" window on the screen**, where its buttons act on a refinement that is already finished.
  It is hidden when it appears and closed after the residue is accepted.  On screen: not verified.
- Fixed: **Stepped Refine: no density around the residue being refined** (a regression of build 13 on your machine; builds 9-12 showed it).  Going to the next residue only moves the view; the map stayed
  contoured around the old centre until the contour level was changed.  The maps are now re-contoured around every residue (test counts the re-contouring events and checks their centres).
  Why builds 9-12 did not need it is not understood.  On screen: not verified.
- Changed: **RCrane** entries are a sub-menu **Calculate > RCrane** that exists from start-up (build 13: an entry "RCrane launch" that was meant to create a top-level menu; on one machine it
  gave neither a menu nor a message, cause not found).  Each entry prints a line in the log when used, the Coot / monomer-library check runs the first time, an exception is printed and shown in a window.
- New: this file.

## Build 13  (patch 0032; **new `bin/coot-bin`**: one C++ change)
- Fixed: Calculate > Fit Loop > **Fit Loop by Database Search** (a 7-element atom spec gave `None`; the candidate buttons all showed the last loop).
- Changed: **Stepped Refine** shows the refinement style (moving atoms) for 0.6 s per residue before accepting (`COOT_STEPPED_REFINE_SHOW`, 0 = old behaviour).
- New: **RCrane** (RNA building) works and is on by default (list view / tree model layer in the PyGTK replacement; Python 3 fixes in `linearInterp`, `finalMoleculeCleanup` (OP3), `removeLastBaseAndPhos`).
  `COOT_DISABLE_RCRANE=1` hides it.
- Changed (C++): a refinement driven by a script, or without a window, stops after `COOT_REFINE_MAX_SECONDS` (default 10 s) instead of waiting for ever for a minimiser that does not converge.
- New tests: `gui-rcrane` (20), `gtk2compat` 12, `gui-dialogs` 39.

## Build 12  (patch 0031; no C++ change)
- New: the 28 **reference structures** (Ca -> Mainchain no longer says COOT_REF_STRUCTS is not defined).
- Fixed: Ligand Metric Sliders (needs an MTZ with observed F; says what is missing; uses the sigma column that belongs to F); Run Refmac environment messages.
- New: **Sphere Refine / Sphere Regularization (+)** on the toolbar from the first start; new **splash** (`bin/coot-splash`, 1160 x 956 px at 580 x 478 pt).
- Fixed: Python scripting window (`gtk.FALSE`), sliders that were dead (`gtk.Adjustment` properties), the menu sweep now includes menus created after start-up.
- Changed: `tests/run-headless-tests.sh` and `collect-results.sh` report the macOS quarantine flag with the command that clears it (instead of printing empty lines).

## Build 11  (patch 0030; no C++ change)
- Fixed: **Glyco** module (missing install data, Python glue, `add_linked_residue` result), **Run Refmac** (the Scheme call-out is bridged to Python; CCP4 environment for child processes only; `FREE=` label bug),
  Ligand Metric Sliders (bytes/str), `popen_command` and friends, and further Python 3 slips found by scanning all scripts.
- New: share/coot data that `make install` copies from other directories (pdb templates, protein database, rama tables, ligand database, ...).

## Build 10  (patch 0029)
- Fixed: Stepped Refine **Stop** / Continue / Cancel (string callbacks), middle-click picking after "Go to next ligand" (GL matrix state), unreadable ligand labels.

## Build 9  (patch 0028)
- Fixed: **crash on Map Tools > Make a Smoother Copy** for space groups with screw axes (grid incompatible with the space group; upstream 0.9.8 has the same fault); contouring errors no longer terminate Coot.
- Changed: GL view placed as a subview of the NSView that GDK keeps for the drawing area (picking offset, displaced view).  (Middle-click picking was reported working in your build-9 report.)

## Build 8  (patch 0027)
- Fixed: **crashes in the first real-window GUI audit**: the PyGTK replacement released the Python GIL during GTK calls (ctypes `PyDLL` now); audit tool hardened.

## Build 7  (patches 0023-0026)
- New: Coot's **Python GUI scripts run** (menus, toolbar buttons and dialogs of All Molecule / Modelling / Modules / NCS / PISA / Probe ...) on a PyGTK-2 replacement written over the real GTK 2 (`compat/pygtk2`);
  Python 2 leftovers of the first port fixed in ~60 places; new headless GUI test suites and a menu sweep.

## Build 6  (patches 0021-0022)
- New: **RDKit** "enhanced ligand tools" (Lidia SMILES import, SMILES readout, `residue_to_sdf_file`, ...), RDKit 2023.09 shipped in the bundle.

## Build 5  (patches 0018-0020)
- Changed: scene labels drawn through Pango/cairo textures (GLUT bitmap fonts are gone on macOS); environment distances (H-bonds, bumps) on by default; right-click re-centres (trackpad);
  Draw menu item for the Model/Fit/Refine toolbar; Lidia icons installed.

## Builds 1-4  (patches 0001-0017)
- Build 1: the 0.9.8.96 source compiles for arm64 macOS (macOS GL/GLUT includes, Guile 3 and Python 3 compatibility, Python scripts ported 2 -> 3, crash handler opt-in) and runs headless; first GUI
  window through an NSOpenGLView seam instead of GtkGLExt (0010), Retina scaling behind `COOT_RETINA` (0011).
- Build 2 (0013-0016): Ramachandran-plot crash (accel-group use-after-free), monomer library path handling (link restraints were never loaded), wall-clock animation pacing, Scheme probe fixes.
- Build 3 (0017): external programs (reduce, probe, refmac ...) started through `system()` from Scheme.
- Build 4: **self-contained, relocatable bundle** (all libraries inside the folder, Python and Guile trees, ad hoc signatures, minimum macOS 11).

## Not supported / open
- **Scheme GUI scripts** (105 functions in 27 `.scm` files, e.g. the `(coot-gui)` window) are written against *guile-gtk*, an old Guile 1.x GTK binding that does not exist for Guile 3 on macOS.
  Scheme scripting itself works (Calculate > Scripting > Scheme..., `--script file.scm`, startup scripts); the GUI is provided by the Python scripts.
  A Guile 3 <-> GTK 2 layer for the Scheme GUI scripts (your decision of 3 Nov: keep Scheme including its GUI scripts) is planned after the Python layer and **not started**.
- Things that only a screen can show are checked by you (see TEST-PROTOCOL.md, newest round at the top).
- No native `Coot.app` / DMG yet; licence texts and source offer for the bundled libraries are still to be added.
