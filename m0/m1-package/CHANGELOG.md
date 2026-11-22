# Changelog: Coot 0.9.8.96 for Apple Silicon (macOS, no XQuartz)

Base: Coot 0.9.8.96 (the release tarball), ported to run natively on macOS / Apple Silicon with GTK 2 (Quartz) and the old fixed-function
OpenGL that Coot 0.9 uses; menus, look and Python API are those of 0.9.x.  Every change below is a numbered patch (`patches/00NN-*.patch`,
applied to the pristine tree by `setup.sh`) or a change of the packaged data / scripts / tests; `README-m0.txt` has the technical notes of every
round, `TEST-PROTOCOL.md` has the user-facing explanation and the checks for you (newest round first).  A "build" is one delivered zip.
"Verified" means a headless test (no window server in the build environment); what only a screen can show is marked "on screen: not verified".

## Build 32  (patch 0050 about-dialog-coot0-notice (C++); new `bin/coot-bin`; licence: coot0 changes now GPL-3.0-or-later; source archive)
- Licence (user, 22 Nov): the coot0 changes are now **GPL-3.0-or-later**, the same terms as Coot itself (before: GPL-3.0-only), so
  the Coot developers can take any of them back unchanged. `LICENSING.md` has a notice of modification; the source offer
  (`CORRESPONDING_SOURCE.md`), `README-FIRST.txt` and `LICENSING.md` point to the GitHub Issues for questions and problem reports;
  `THIRD_PARTY_LICENSES.md` carries the credit line that FreeType's licence asks for.
- **Help > About** (Coot's own About window) now says that this is Coot 0.9.8.96 modified for macOS on Apple Silicon by Chang Sun
  (2026), that it is not an official Coot release, where the changes and the source are and that the licence is GPL v3 or later
  (GPL v3 section 5). Coot's own copyright lines and the GPL text are unchanged. On screen: not verified (checked from a test that
  builds the window and reads its texts).
- **Source archive**: each release now has `coot0-<version>-source.tar.gz` next to the Mac package: the exact Coot tree that was
  compiled (release + patches) and the coot0 repository (`m0/tools/make_source_tarball.sh`; checked by `m0/tools/check_source_tarball.py`).
- README rewritten for readers who use Coot rather than build it; the rules of Refine/Improve Ramachandran Plot (try peptide flips)
  moved to `docs/try-peptide-flips.md`.
- Tests: `gui-dialogs` 89 -> 90 (build 31 fails the new About check); source archive check 13 checks (build 31 has no archive).

## Build 31  (patch 0049 scheme-wrappers-write-cif-once (C++); new `bin/coot-bin`; scripting reference: every example checked)
- Scripting reference (docs/api): "ran" was not enough: 812 functions had returned nothing and 253 a failure value (-1, #f), mostly
  because the program-made example used placeholders (`"hello"`, molecule 0 for a map, a PDB file where a dictionary is needed).
  1. Every call is now compared before and after (`tests/api_state.py`): atoms of every model (added, deleted, moved, B-factors,
     occupancies), maps (level, sigma, colour), new or closed molecules, view centre and zoom, and ~100 settings with a getter. Each
     result says what changed, e.g. `changed: molecule 0: deleted 1 residue(s) (A41)`.
  2. 542 examples were written by hand and tried in both languages on the test data (real atoms, the map molecule, files of the right
     type, set-up lines where needed); each page says what a correct result is, and notes what looked wrong. New test files:
     `tutorial-modern.fasta`, `rnasa-sf.cif` (structure factors as mmCIF), `rnasa-sm.cif` / `rnasa-sm-data.cif` (small-molecule CIF).
  3. Every setting with a getter (105) was set to another value, read back and put back: 195 of 210 calls read back.
  Result: Python 1,595 ran (build 30: 1,399), Scheme 1,558 (1,369); 0 stopped Coot (64 / 62: those need the window and are now marked
  so); 595 of 657 comparable answers agree in both languages.
- New tool: `tests/api-try.sh FILE` runs your own Python/Scheme lines without a window on the test data and prints each value and
  what it changed.
- Four bugs of Coot 0.9.8.96 fixed (found by this):
  1. `write_cif_file` wrote the model once more on every call (140, 275, 410 kB; the third file read back with every atom three
     times). It now writes a copy, as Coot's own Save Coordinates does (that menu was not affected).
  2. Scheme `kullback-liebler` always returned #f (the result was never returned); now the two numbers, as in Python.
  3. Scheme `probe-clash-score-from-scm` took the 5th number (wide contacts) from the 4th.
  4. Scheme `register-interesting-positions-list-scm` stopped Coot on any call.
- Noted, not changed (Coot's own code; the pages say so): unfinished functions that always return False (`chain_fragments`,
  `metal_coordination`, `glyco_tree`, `alignment_results`, `residues_torsions_match`, `model_composition_statistics`), return values
  that are wrong although the work is done (`add_alt_conf`, `b_factor_from_map`, `scale_cell`, `copy_residue_range`,
  `watson_crick_pair`, `reset_view`, `save_coordinates` 0 = success), `exchange_chain_ids_for_seg_ids` merges chains when there are no
  segment IDs, `copy_from_ncs_master_to_chains` replaces the whole target chain.
- Tests: `python-api` 21 -> 22, `scheme-api` 30 -> 33, `api-docs` 8 -> 12 (build 30 fails all 8 new checks).

## Build 30  (patch 0048 scheme-list-builders-sanitise-alt-confs (C++ + Python); new `bin/coot-bin`; scripting reference: every function tried)
- Found by running each read-only function in Python and in Scheme on the test data and comparing the answers (20 Nov). Problems 2-5
  are in Coot 0.9.8.96's own C++ source:
  1. `sanitise_alt_confs_active_residue()` (Python) always failed with a TypeError: it took the chain, residue number and insertion
     code all from the same field of the active atom.  The Scheme version was right.
  2. Scheme `map-peaks` gave the peaks lowest first (Python: highest first, as Coot sorts them).  Now highest first in both.
  3. Scheme `map-to-model-correlation-stats-per-residue-range-scm` returned a list nested ~90 levels deep (the two arguments of
     `scm_cons` were swapped).  Now a flat list `((residue-spec (n correlation)) ...)` in residue order, as in Python.
  4. Scheme `ncs-chain-differences` left out the residues (the lines were commented out): `((0.5) (0.283) ...)`.  Now each entry is
     `((resno ins-code) (master-resno ins-code) mean-difference)`, as in Python.
  5. Python `ligand_atom_overlaps` always returned False: its C++ in 0.9.8.96 was unfinished ("FIXME").  Now it returns the overlaps
     as the Scheme version does: `[[atom-spec-1, atom-spec-2, overlap-volume, is-h-bond], ...]`.
- Scripting reference (docs/api): the run that tries every example (`tests/run-api-examples.sh`) stopped after a third of the calls in
  build 26, because an example overwrote the test model and the next Coot could not load it.  The script now copies fresh test data
  before each start.  Now every one of the 3,406 examples (1,717 Python, 1,689 Scheme) has a result: 1,399 Python and 1,369 Scheme
  ran; 18 / 26 gave an error (mostly placeholder values such as `"hello"`); 64 / 62 need the graphics window (stopped Coot without one;
  not tried with one); 7 / 7 gave no answer within 60 s; 229 / 225 were not run on purpose (they quit Coot, use the network or an
  external program, or take a widget).  For the 570 functions where both languages returned a comparable value, Python and Scheme gave
  the same answer for 528; each page says so.  The Python examples now pass True/False for true/false arguments (5 more ran).
- Tests: `python-api` 19 -> 21, `scheme-api` 27 -> 30 (build 29 fails all 5 new checks).

## Build 29  (patch 0047 help-open-and-contact-dots-off; Python only, `bin/coot-bin` as in build 28)
- Fixed (user, 20 Nov, round 28 JJ3): in Help > Search Menus and Docs, **double-click did nothing**: the row arrives from GTK as a
  pointer, not a row number, and was ignored.  **Enter ran, but the document did not open at its heading**: Safari does not follow the
  small forwarding page build 28 used (macOS `open` drops the #heading of a file:// address).  Now Coot serves the documentation pages
  itself on 127.0.0.1 (only this computer; only the docs/html folder; while Coot runs) and the browser opens e.g.
  `http://127.0.0.1:PORT/cookbook/04-refinement.html#43-...`.  Down in the search box moves into the list.
- New (user, 20 Nov): **contact dots off**.  Ctrl-1 (and Ligand > Coot All-Atom Contact Dots) draw the dots, Coot 0.9.8.96 has nothing to
  remove them except Draw > Generic Objects.  New: **Ligand > Coot All-Atom Contact Dots Off** and `coot0_contact_dots_off(imol)`
  (`-1` or nothing: every molecule).  Ctrl-1 again draws them anew.  Keyboard Shortcuts mentions it.
- Tests: `gui-dialogs` 88 -> 89; the search-window check now makes GTK emit the signals itself (`gtk_widget_activate`,
  `gtk_tree_view_row_activated`: build 28 called the Python handler, which hid the double-click bug), and the document checks fetch the
  page from Coot's server and look for the heading (build 28 fails 4).  Real-window test 11 -> 12 (Enter -> page served with its heading).
- On screen: whether Safari opens the served page at the heading is not verified by me (I did not open a browser).

## Build 28  (patch 0046 help-menu-ctrl-key-state (C++ + Python + Scheme); new `bin/coot-bin`; docs as web pages)
- Fixed (user, 20 Nov, round 27 II1): cookbook **6.3 used `o`, which Coot uses itself** (next NCS chain: the terminal showed `(n-chains 2)`
  ...).  The list of Coot's own keys in 6.3 was written from memory and incomplete; it is now taken from Coot's key handler
  (`globjects.cc`): also `c` `p` `s` `O`, Ctrl with C D I L X.  The recipe uses `v` (free also when the template key bindings are installed).
- Fixed (user, 20 Nov, II2): **Ctrl-T still did not run a `"Control_t"` binding.**  Build 27 asked GDK whether Ctrl was held; that could
  not be tested and did not work for you.  Now Coot's C++ key handler passes its own Ctrl state (the one Ctrl-S, Ctrl-Z use) to Scheme's
  key hook, which passes it to Python (`globjects.cc`, `coot-utils.scm`; one C++ line, so a new `bin/coot-bin`, otherwise as build 26/27).
  When a key binding runs, the terminal says so (`INFO:: key Ctrl-116: running key binding "Ctrl test"`).
- Fixed: binding a plain key (e.g. `"k"`) silently **removed a Ctrl binding of the same letter** (`"Control_k"`) in `add_key_binding`
  (Coot 0.9.8.96 bug, found by the new tests).
- New (user, 20 Nov): **Help menu** (Coot's "About" menu, renamed, stays the last menu):
  - **Search Menus and Docs...**: type a few words; it lists matching menu entries (all menus, also those added later, e.g. by Modules;
    entries coot0 removed are left out), cookbook recipes, scripting functions and documentation sections. Double-click or Enter: a menu
    entry runs, a document opens in your web browser at that recipe / function.
  - **Keyboard Shortcuts...**: Coot's own keys (from its key handler) and your key bindings (Python and Scheme); a binding to one of
    Coot's keys is marked "never runs".
  - Cookbook, Scripting Reference, Documentation Overview, coot0 README, What's New (this file), Coot Website (online); then Coot's
    Header/Remarks Browser, Hints, About as before.
  - The documents are web pages in `docs/html/` (made from the Markdown in `docs/` by `m0/tools/gen_docs_html.py`, with a search index).
- Tests: `gui-dialogs` 80 -> 88 (Ctrl state through the key hook; Help menu, last menu, search of menus and documents, opening at the right
  heading, the search window, Keyboard Shortcuts; build 27 fails all 8); `api-docs` 5 -> 8 (a page for every Markdown file, made from its
  current text; no broken link or heading between the pages; search index complete; build 27 fails 2, the links check has nothing to check);
  `cookbook` checks the corrected list of Coot's keys (build 27's 6.3 fails it).  New **real-window test** `tests/run-real-window-checks.sh`
  (opens Coot for ~10 s, sends key presses to the graphics window through GTK, so through Coot's own C++ key handler): plain key, Ctrl-T,
  plain t, Coot's `o`, and the Help menu on the real menus; build 28: 10 / 10, build 27: Ctrl-T fails.
- Test scripts set `COOT0_NO_BROWSER=1` so that the menu sweep / audit do not open web pages.
- On screen: windows opened (the test checks they are mapped), but I did not look at them, and the key presses were synthetic GTK events,
  not your keyboard.

## Build 27  (patch 0045 python-ctrl-key-bindings; cookbook fixes; Python / docs only, `bin/coot-bin` as in build 26)
- Fixed (user, 19 Nov, round 26 HH4): cookbook **6.3** bound F5, which Coot itself uses (F5 opens Model/Fit/Refine), so the binding never
  ran; its tip "Control_r" is Coot's Ctrl-R (rock).  Now the recipe uses `o` and lists the keys Coot keeps for itself, with a note on F-keys
  on a Mac (they need `fn`).
- Fixed (user, 19 Nov, HH5): **refinement recipes left `set_refinement_immediate_replacement(1)` on**, so every refinement made afterwards
  with the mouse or a key had no Accept window and its moving atoms stayed on the screen.  All 8 recipes (4.1-4.4, 4.6, 4.9, 7.1, and 6.7
  where it was a "preference") now switch it off again; chapter 4 says how to get out of it; 6.7/6.8 no longer suggest it as a setting.
- Fixed: **Ctrl key bindings made in Python never ran** in coot0 (and in any Coot 0.9 built with both Guile and Python): Coot hands keys
  it does not use to Scheme's key hook, which passes only the key on to Python, so the Ctrl state was lost.  Python now asks GDK whether
  Ctrl is held (`_coot0_control_pressed` in `coot_utils.py`).
- Docs (user, HH5): the cookbook says plainly that **each recipe stands alone** (it loads its own copy of the test files; several in a row
  give several copies), that recipe 1.1 must run first, and how to use a recipe on your own model and map (molecule numbers instead of the
  loading lines); 6.4 explains why it loads a map.  When the test file is missing, `make_and_draw_map` gives -1 and `set_map_colour(-1, ...)`
  does nothing: in round 26 only the background (white) changed.
- Tests: `cookbook` checks that no recipe binds a key Coot uses and that none leaves immediate replacement on (build 26 docs: 148 / 166);
  `gui-dialogs` 79 -> 80 (Python key bindings, plain and Ctrl, through Scheme's key hook; build 26 fails it).
- On screen: not verified by me (headless only); in particular whether Ctrl reaches the Python binding on macOS (round 27 II2).

## Build 26  (patches 0042 auto-recontour-report, 0043 quiet-scheme-calls (C++), 0044 python-scripting-window; new `bin/coot-bin`)
- **First C++ rebuild since build 13** (only for 0043; all 412 files compiled from the patched tree, same compiler and libraries; `lib/` unchanged).
- Fixed (user, 18 Nov): Coot printed "debug:: g.safe_scheme_command() with command ..." in the terminal for every Scheme call, and the Scheme
  window's own calls were echoed as `(coot0-console-eval "...")`.  Both are gone; ordinary Scheme commands are still shown as before.
  `COOT_DEBUG_SCHEME=1` brings the debug line back.
- New (user, 18 Nov): Cryo-EM > **No Auto-Recontour Map Mode** / **Enable Auto-Recontour Map Mode** said nothing; now they print the new mode
  in the terminal (with the script command) and in the status bar.
- New: the **Python scripting window** (Calculate > Scripting > Python...) works like the Scheme window of build 25: command, printed output
  (before: only in the terminal), result (`=> 'GLU'`), errors with their traceback, Up / Down history, blocks over several lines (a line ending
  in ":" continues and indents, an empty line runs the block), a hint when Scheme is typed into it.  The 0.9.8.96 window stays as
  `coot_gui_classic()` (used by the remote-control socket; `COOT0_CLASSIC_PYTHON_WINDOW=1` makes the menu open it).
- New: **documentation** in `docs/` (also on GitHub): `docs/cookbook/` (85 recipes in 10 topics, Python and Scheme; all run by the new
  `cookbook` suite) and `docs/api/` (the scripting reference: 1,735 functions, 1,717 in Python and 1,689 in Scheme, each with a concrete example
  on the test data and the result of trying it; A-Z list; the functions that exist in only one language).  Made by `m0/tools/gen_api_index.py`
  (SWIG wrappers + headers + the script layers' redefinitions) and `m0/tools/gen_api_docs.py`; `tests/run-api-examples.sh` tries every example
  (about 75 minutes): 1,033 ran, 13 errors (internal functions or placeholder values), 35 stopped Coot without a window (windows, OpenGL),
  6 gave no answer within 60 s, 164 not run on purpose (quit, network, external programs, widgets).
- Found while writing the cookbook (not changed, documented): `set_map_colour` stops Coot when there is no window; `density_score_residue` and
  `residues_distortions` in the script layers take a residue spec (and the latter needs a refinement map); `all_molecule_ramachandran_region`
  exists only in Python; `run-python-command` evaluates one Python expression (use `run-python-script` for several lines).
- Tests: `gui-dialogs` 74 -> 79 (Auto-Recontour messages; no debug line / no echo of the window's calls; the new Python window: results,
  printed output, blocks, definitions, errors, history; unfinished statements; the classic window kept); build 25 fails the 5 new ones.  The
  Stepped Refine check now lets GTK finish what earlier checks queued first (the old Python window used to do that by chance).  New suites
  `api-docs` (5: the reference matches this Coot) and `cookbook` (166: every recipe in both languages).
- `tests/run-api-examples.sh`: when a call hung, only the helper shell was stopped and Coot kept running (found the next morning: six
  such Coot processes at full CPU); it now stops Coot itself.
- On screen: not verified by me (headless only).

## Build 25  (patch 0041 scheme-scripting-window; Python / Scheme only, `bin/coot-bin` and `lib/` as in build 13)
- Fixed (user report 18 Nov): **Calculate > Scripting > Scheme...** opened 0.9.8.96's "simple" Scheme window (C++, used when the guile-gtk Scheme
  GUI is not loaded), which said "For now this is a placeholder only! Don't expect anything to happen here!" and threw the result of every command
  away.  Now the entry opens a new window (Python, `coot_gui.py`: `scheme_scripting_window`) that passes the text unchanged to Coot's Guile
  (`coot0-console-eval` in `python-gui-bridge.scm`) and shows the command, its printed output, its result and errors; Up / Down recall earlier
  commands; Enter with brackets still open waits for the rest of the expression; everything is also written to the terminal.
- Fixed: output printed by Scheme (`display`, `format #t`, also in `--script file.scm`) did not reach the terminal while Coot ran: the launcher
  copies the terminal into `logs/` through a pipe, and Guile then buffered its output (often until Coot quit).  Guile's output is now line-buffered.
  Checked: a script that prints a line and waits: build 24 had not shown the line after 90 s, build 25 showed it after 6 s.
- Known, cosmetic: Coot's C++ echoes every Scheme call it is given ("debug:: g.safe_scheme_command() with command (coot0-console-eval ...)") in
  the terminal; removing that needs a C++ rebuild.
- `README.md` is now in the package; README: the trackpad two-finger click (works as the middle click), the Scheme window.
- Tests: `gui-dialogs` 70 -> 74 (the menu entry opens the new window, the old one is hidden; command / output / result / error / several lines /
  history; line-buffered output; open brackets recognised); build 24 fails all 4.
- On screen: not verified by me (headless only).

## Build 24  (patch 0040 rama-turned-peptides-repaint; Python only, `bin/coot-bin` and `lib/` as in build 13)
- Fixed (user report 17 Nov, EE2 / plain entry): the menu bar also went blank during the plain **Refine/Improve Ramachandran Plot**.  Every shown
  refinement (refine_and_show: Stepped Refine, Fit Protein, both Ramachandran entries) now asks for a redraw of the main window afterwards (build 23
  did this only in the (try peptide flips) entry, where EE2 then passed).
- Clearer (user report 17 Nov, EE3): the user flipped 4 peptides on purpose; all 4 were put back but the report named only 2, because the other 2
  were already turned back by the refinement as it is (try A) and so were not "flipped by the flip try".  The report now compares every peptide
  with the start of the run: a peptide counts as turned when its carbonyl O ends up more than `rama_flip_turn_angle` (90) degrees from where it was,
  round the CA(i) - CA(i+1) axis.  Two lists: "Flipped by the flip try" and "Turned by the refinement itself".  The plain entry lists the peptides
  its refinement turned in the terminal and status bar.  A peptide whose O is shared but whose next residue is split into alt confs is followed too.
- README: how the flip is decided (the formulas: density at the O, the peptide C + O + N, map fit, Ramachandran regions), the limit variables with
  their defaults, and how to change them (Python scripting window or a file in coot0's `.coot-preferences`).
- Tests: `gui-dialogs` 66 -> 70 (redraw in the plain entry; the turned list apart from the flips; the plain-run report; shared O next to a split
  residue); build 23 fails all 4.  Headless on the user's model (local only): the 4 deliberate flips of EE3 all put back, the report lists 1
  flipped by the try and 3 turned by the refinement.
- On screen: not verified by me (headless only).

## Build 23  (patch 0039 rama-flip-map-veto-scratch-molecule; Python only, `bin/coot-bin` and `lib/` as in build 13)
- Fixed (user report 17 Nov): **Refine/Improve Ramachandran Plot (try peptide flips)** kept wrong flips: a flip that moved a residue from allowed to
  favoured was kept although the flipped carbonyl O pointed out of the density (build 22 ranked the Ramachandran regions above the map).  On the
  user's data the three wrong flips took the carbonyl O from 5.3 / 7.3 / 5.6 sigma to 3.7 / -0.8 / 0.1 sigma.  Now the map has a veto: a flip is kept
  only if no Ramachandran region gets worse, the carbonyl O loses at most 0.3 sigma, the peptide C + O + N at most 0.6 sigma (sum), the map fit of
  the two residues at most 2%; and then either a region gets better, or (same regions) the carbonyl O and the peptide each gain >= 1 sigma and the
  map fit gets better (the build-21/22 "10% better map fit" missed a deliberate flip with +4.4 sigma at the O and +6.8% fit).  No map: no flip.
  Checked headless on the user's model (local only): of the 232 peptides of chain A the old rule flipped 3 (the wrong ones), the new rule 0;
  21 peptides flipped on purpose: 21 put back (20 with the 10% rule).  The report and terminal give the carbonyl density before and after.
- Fixed (user report 17 Nov): during a (try peptide flips) run part of the main window (the menu bar) stayed blank until the mouse went over it, and
  the status bar showed "Successfully read coordinates file .../coot-rama-conformer-....pdb. Molecule number N created".  Build 22 read and closed a
  new hidden molecule for every Ramachandran check of a split conformer; now one hidden scratch molecule is reused (refilled with
  clear_and_update_model_molecule_from_file) and closed when the run ends or is stopped, and the main window is redrawn after every residue and at
  the end.  The blank menu bar itself was not reproduced by me (no screen used); whether this cures it: check EE2.
- Tests: `gui-dialogs` 61 -> 66 (map veto with the user's three cases; a deliberate flip with the same regions is put back; carbonyl density in the
  score; one scratch molecule, closed at the end; the main window redrawn); build 22 fails all 5.
- On screen: not verified by me (headless only).

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
