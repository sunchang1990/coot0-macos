# Coot 0.9.8.96 on Apple Silicon: test round 35 (build 35 = build 34 + a command log you can replay)

**From you** (23 Nov): PP1 passes (self-test all N / N). The qtRView toolbar is CCP4's own (same outside coot0). Updating Maps printed
`(calculate-maps-and-stats 3 1 1 2)`, which is not a function: you asked that the terminal output can be replayed, in Python by default.

1. **Every command line Coot writes can be run again**: real names (`calculate_maps_and_stats_py(3, 1, 1, 2)`), quoted text, and a
   comment where a command does not exist in that language. 12 wrong names and 26 unquoted arguments in Coot's source corrected.
2. **The terminal shows Python** by default; `coot0_set_command_echo("scheme")` switches to Scheme.
3. `0-coot-history.py` and `0-coot-history.scm` (written when Coot quits, in the folder you started it from) replay.

**Verified without a window only**: a session (model, two maps, settings, a delete, calculate_maps_and_stats_py) was replayed from
both files in fresh Coots to the same result. The Updating Maps menu itself was not clicked.

## QQ. Round 35 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| QQ1 | Install build 35, open a model and its MTZ (`coot0 --pdb model.pdb --auto data.mtz`), Calculate > Updating Maps... and start it. | The terminal shows `calculate_maps_and_stats_py(…)` (no brackets around the whole line, underscores). |
| QQ2 | Copy that line into Calculate > Scripting > Python... and press Enter. | The maps are recalculated again, no error. |
| QQ3 | Quit Coot, then in the same Terminal folder: `coot0 --script 0-coot-history.py` | Coot opens with the model and maps as you left them (the history replays). Optional: the same with `0-coot-history.scm`. |

# Earlier round (PP1 confirmed 23 Nov): Coot 0.9.8.96 on Apple Silicon: test round 34 (build 34 = build 33 + two self-test checks corrected)

**From you** (23 Nov): OO1, OO2 pass; OO3: Credits without the port line (done). Your `coot0 --self-test` had two FAILs.

1. **Both FAILs were mistakes in the tests**, not in coot0, and showed only from an installed copy (my tests of each build ran from
   the unpacked folder): `bundle-python` wanted a small cache file (the list of image loaders) inside the coot0 folder, but an
   installed copy keeps it in `~/Library/Application Support/coot0` on purpose; `installer` made a copy to play an unpacked download,
   but from an installed copy the copy took the install marker along and believed it was installed. Both corrected; reproduced
   before and after on a copy marked as installed (`evidence/checks_b33_vs_b34.txt`).
2. Each build is now also tested as `coot0 --self-test` from a fresh install.

## PP. Round 34 checks (about 20 minutes, mostly waiting)

| # | Do | Expected |
|---|---|---|
| PP1 | Install build 34 (`./install.sh` in the unpacked folder), then in Terminal: `coot0 --self-test` | 21 lines, every one N / N (installer 26 / 26, bundle-python 19 / 19). |

# Earlier round (OO1-OO3 confirmed 23 Nov): Coot 0.9.8.96 on Apple Silicon: test round 33 (build 33 = build 32 + a smaller Help > About notice + README wording)

**From you** (23 Nov): build 32's About window had too much coot0 text; the README's XQuartz sentence should hold whether or not
XQuartz works again; drop the sentences about the Coot developers' support and say that coot0 is an independent build based on
the Coot 0.9.8.96 source code from Paul Emsley's website.

1. **Help > About** (new `bin/coot-bin`): Coot's own window, with one small line at the end of the copyright lines,
   "macOS / Apple Silicon changes (coot0): Copyright (C) 2026 Chang Sun", where **coot0** is a link to the GitHub repository.
2. **README**: the XQuartz paragraph is dated (November 2026) and says what coot0 does instead (Quartz directly, Retina).
3. **"Independent build"**: README, LICENSING.md, README-FIRST.txt and the GitHub description say it in those words; the sentences about support are gone.

**Verified without a window only**: the About texts, the link and its handler were read in a test; the window was not seen and
the link was not clicked.

## OO. Round 33 checks (about 2 minutes)

| # | Do | Expected |
|---|---|---|
| OO1 | Install build 33, start `coot0`, Help > About... | Like Coot's own window: "Coot 0.9.8.96", "Marina Bay", the copyright lines, and last "macOS / Apple Silicon changes (coot0): Copyright (C) 2026 Chang Sun" in the same small font, with **coot0** underlined as a link. |
| OO2 | Click **coot0** in that line. | Your web browser opens the coot0 GitHub page (you need to be signed in to GitHub while the repository is private). |
| OO3 | (On GitHub) README, LICENSING.md, CORRESPONDING_SOURCE.md. | The XQuartz paragraph and "independent build" wording read well; nothing private. |

# Earlier round (NN1 replaced by OO1 after your remark of 23 Nov): Coot 0.9.8.96 on Apple Silicon: test round 32 (build 32 = build 31 + licence notices: GPL v3 or later, Help > About, source archive)

**From you** (22 Nov): MM1-MM4 pass (after installing build 31). VAI: fine to publish coot0 publicly as your own project, following the
GNU licences. You chose GPL v3 **or later** for the coot0 changes, the README rewrite and the new GitHub description; the repository
stays private until you have looked at it.

1. **Licence**: the coot0 changes are GPL-3.0-or-later, like Coot. `LICENSING.md` says that coot0 is a modified Coot and by whom;
   questions and problems go to the GitHub Issues; FreeType's credit line is in `THIRD_PARTY_LICENSES.md`.
2. **Help > About** says the same inside the program (new `bin/coot-bin`): Coot's copyright, then "macOS / Apple Silicon changes
   (coot0): Copyright (C) 2026 Chang Sun", and under the version: modified by whom and when, not official, where the changes and the
   source are, GPL v3 or later.
3. **Source archive** `coot0-<version>-source.tar.gz` for each release (Coot tree as compiled + the coot0 repository).

**Verified without a window only**: the About texts were read from the window object in a test; how the window looks is not seen.
**New tests**: `gui-dialogs` 89 -> 90; source archive check (build 31 fails both).

## NN. Round 32 checks (about 2 minutes)

| # | Do | Expected |
|---|---|---|
| NN1 | Install build 32 (`./install.sh` in the unpacked folder), start `coot0`, then Help > About... | Under "Coot 0.9.8.96": "Marina Bay", then "coot0: this is Coot 0.9.8.96 modified for macOS on Apple Silicon by Chang Sun (2026)." and the GitHub address. The copyright lines end with "macOS / Apple Silicon changes (coot0): Copyright (C) 2026 Chang Sun". The License button still shows the GPL. |
| NN2 | (Tomorrow, on GitHub) read README, LICENSING.md, CORRESPONDING_SOURCE.md. | Clear to a colleague; nothing private; nothing says "private" any more. |

# Earlier round (MM1-MM4 confirmed 22 Nov): Coot 0.9.8.96 on Apple Silicon: test round 31 (build 31 = build 30 + every scripting example checked + four Coot bugs fixed)

**From you** (20 Nov): LL1, LL2 pass; LL3 failed only because my instructions had a placeholder path (`read-pdb` gave -1); with the real
path it gives `((1 "") (1 "") 0.4996...)` (checked without a window). Asked tonight: check all the Python and Scheme functions with test
data and update the documentation.

1. **What "ran" meant**: in build 30, 812 functions returned nothing and the run never looked at what they did; 253 returned -1 or #f,
   mostly because the generated example used placeholders. Now every call is compared before and after (models, maps, molecules,
   view, ~100 settings), and the reference says what changed. 542 examples were written by hand and tried in both languages; 105
   settings were set to another value and read back.
2. **Four Coot bugs fixed** (new `bin/coot-bin`): `write_cif_file` wrote the model again on every call (third file: every atom three
   times); Scheme `kullback-liebler` always #f; Scheme `probe-clash-score-from-scm` lost the 5th number; Scheme
   `register-interesting-positions-list-scm` stopped Coot. Other odd results of Coot's own code are noted on the function pages.
3. **New tool**: `tests/api-try.sh FILE` tries your own lines without a window and shows what they changed.

**Verified without a window only.** About 120 functions per language need the graphics window, quit Coot, use the network or run an
external program; they were not tried and their pages say why. **New tests**: `python-api` 21 -> 22, `scheme-api` 30 -> 33, `api-docs` 8 -> 12
(build 30 fails all 8). Evidence: `evidence/checks_b30_vs_b31.txt`.

## MM. Round 31 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| MM1 | Help > Scripting Reference (all functions): read "Results of trying the examples". | Three short tables/paragraphs: what ran, what the calls showed (value / changed something / nothing visible), and the settings that were read back (195 of 210). |
| MM2 | First check that `coot0` starts build 31 (title bar or `coot0 --diagnose`; after installing, the `coot0` command points to the new folder). Help > Search Menus and Docs...: type `delete_residue`, double-click it. | On the page that opens, the table row for `delete_residue` has a right-hand column "When tried". It reads `ran (no return value); changed: molecule 0: deleted 1 residue(s) (A41); n_atoms(0): 1465 -> 1456; ...`. Build 30 showed only `ran (no return value)`. |
| MM3 | Open any model, then Calculate > Scripting > Python...: `[ (write_cif_file(0, "/tmp/coot0-twice.cif"), os.path.getsize("/tmp/coot0-twice.cif")) for i in range(3) ]` (use your model's molecule number instead of 0). | Three pairs with the SAME size, e.g. `[(0, 140435), (0, 140435), (0, 140435)]`; build 30 gave a bigger file each time. |
| MM4 | Calculate > Scripting > Scheme...: `(kullback-liebler (list 1.0 1.0 1.0 2.0) (list 1.0 2.0 2.0 2.0))` | `(0.5493061443340548 0.5493061443340548)` (that is ln 3 / 2); build 30 showed `#f` for any input. Coot sorts the numbers into bins 0.05 wide and only counts bins both lists use, so lists with no shared values give `(0.0 0.0)`. |

# Earlier round (LL1, LL2 confirmed 20 Nov; LL3 = placeholder path, fine with the real path): Coot 0.9.8.96 on Apple Silicon: test round 30 (build 30 = build 29 + five scripting functions fixed + every scripting function tried)

**From you** (20 Nov): KK1, KK2 pass. Asked: check the Python and Scheme functions with the test data and update the documentation
(most functions showed "not tried").

1. **Python against Scheme**: I ran the read-only functions in both languages on the same data and compared the answers. Four were wrong:
   `sanitise_alt_confs_active_residue()` (Python) always failed; Scheme `map-peaks` gave the weakest peak first;
   Scheme `map-to-model-correlation-stats-per-residue-range-scm` returned a deeply nested list; Scheme `ncs-chain-differences` left out
   the residue numbers. A fifth: Python `ligand_atom_overlaps` always returned False (unfinished in Coot's C++). The last four are in
   Coot 0.9.8.96's own C++; all five are fixed (new `bin/coot-bin`).
2. **Scripting reference**: the run that tries every example had stopped after a third of the functions (an example overwrote the test
   model). Now all 3,406 examples have a result: 1,399 Python and 1,369 Scheme ran on the test data; about 125 need the graphics window and
   were not tried with one; about 450 were not run on purpose (they quit Coot, use the network or an external program). Where both
   languages returned a comparable value (570 functions), they agreed for 528; each page says whether they agreed.

**Verified without a window only** (test data, no screen): functions marked "stopped Coot (no window)" need the graphics window and were not
tried with one. **New tests**: `python-api` 19 -> 21, `scheme-api` 27 -> 30 (build 29 fails all 5). Evidence: `evidence/checks_b29_vs_b30.txt`.

## LL. Round 30 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| LL1 | Help > Search Menus and Docs...: type `map_peaks`, double-click the `map_peaks` line. | The reference opens at `map_peaks`: both examples have a result ("ran, returned ..."), and a line says whether Python and Scheme agreed. |
| LL2 | Help > Scripting Reference (all functions): look at "Results of trying the examples". | Every function has a result; few or no "not tried". |
| LL3 | Calculate > Scripting > Scheme...: `(define imol (read-pdb "/Users/<you>/.local/share/coot0/0.9.8.96-b30/test-data/tutorial-modern.pdb"))` (the full path written out: `~` and placeholders are not expanded; `imol` must be 0 or more, -1 means the file was not found and the next line then fails with `list-ref ... #f`) then `(list-ref (list-ref (ncs-chain-differences imol "A") 2) 0)` (use the coot0 folder path; in the installed copy: `~/.local/share/coot0/0.9.8.96-b30/test-data/...`). | Shows `((1 "") (1 "") 0.4996705651283264)` (residue, master residue, difference); build 29 showed `(0.5)`. |

# Earlier round (KK1, KK2 confirmed 20 Nov): Coot 0.9.8.96 on Apple Silicon: test round 29 (build 29 = build 28 + Help search opens what you pick + contact dots off)

**From you** (20 Nov): JJ1, JJ2, JJ4, JJ5 pass; JJ3: the search finds things, but double-click / Enter neither ran a menu entry nor opened the
documentation. Asked: is there a function to turn off the dots of Ctrl-1?

1. **Double-click** was ignored (GTK hands over the row as a pointer; my code expected a number; my test called the handler directly and
   missed it). **Enter** did run, but the document was opened through a small forwarding page that Safari does not follow. Now Coot serves
   the documentation pages itself (address `http://127.0.0.1:...`, reachable only from this Mac, only while Coot runs), so the browser opens
   the page at the recipe or function. Down in the search box moves into the list.
2. **Contact dots off**: Coot 0.9.8.96 had only Draw > Generic Objects... for that. New: **Ligand > Coot All-Atom Contact Dots Off**, and
   in scripts `coot0_contact_dots_off()` (all molecules) or `coot0_contact_dots_off(0)` (molecule 0). Ctrl-1 draws them again.

**On screen**: my real-window test (12 / 12) pressed Enter through GTK and fetched the page from Coot's server with its heading; I did not
open a browser or look at the screen. **New tests**: `gui-dialogs` 88 -> 89 (build 28 fails 4). Evidence: `evidence/checks_b28_vs_b29.txt`.

## KK. Round 29 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| KK1 | Help > Search Menus and Docs...: type `sphere refine`, Enter. Then type `refine_zone`, double-click the `refine_zone` line. Then type `brighten`, double-click the menu line. | Safari opens the cookbook at 4.3, then the reference at `refine_zone`; Brighten Maps runs (the search window closes). |
| KK2 | With a model: click an atom, Ctrl-1 (dots), then Ligand > Coot All-Atom Contact Dots Off. Then Ctrl-1 again. | The dots go; Ctrl-1 brings them back. |

# Earlier round (JJ1, JJ2, JJ4, JJ5 confirmed 20 Nov; JJ3 -> build 29): Coot 0.9.8.96 on Apple Silicon: test round 28 (build 28 = build 27 + a Help menu + Ctrl key bindings that work + recipe 6.3 fixed)

**From you** (20 Nov): II1 failed (pressing `o` refined nothing; the terminal showed `(n-chains 2)` ...), II2 failed (neither Ctrl-T nor t did
anything; t printed two "not found" lines, Ctrl-T one), II3 pass, II4 clear. Asked for a Help menu that searches the menus and points to the
documentation, README and cookbook, like Visual Studio Code's Help.

1. **`o` is Coot's own key**: "go to the same residue in the next NCS chain" (that is what `(n-chains 2)` ... was). My list of Coot's keys
   was incomplete; it now comes from Coot's key handler itself. Recipe 6.3 uses `v`.
2. **Ctrl-T**: your log shows the key reached Python but build 27 decided the Ctrl state by asking macOS separately, and that did not work
   for you. Now Coot's own Ctrl state (the one Ctrl-S and Ctrl-Z use) is handed through. When a binding runs, the terminal prints
   `INFO:: key Ctrl-116: running key binding "Ctrl test"`, so you can see it even if the action itself is quiet.
   Also fixed: binding plain `k` after `Control_k` silently removed the Ctrl-K binding (an old Coot bug).
3. **Help menu** (the old "About" menu, now "Help", always the last menu): Search Menus and Docs..., Keyboard Shortcuts..., the Cookbook,
   the Scripting Reference, the documentation overview, the coot0 README, What's New, Coot's website; then Coot's own Header/Remarks
   Browser, Hints and About. Documents open in your web browser.

**On screen**: I ran Coot in a real window myself (about 10 s, `tests/run-real-window-checks.sh`): key presses sent through GTK to the
graphics window ran the bindings (v, Ctrl-T, not t, not o), Help was the last menu, the search window and Keyboard Shortcuts opened. I did
not look at the screen (no screenshot), and the key presses were synthetic, not your keyboard. **New tests**: `gui-dialogs` 80 -> 88,
`api-docs` 5 -> 8, the cookbook key list; build 27 fails them. Evidence: `evidence/checks_b27_vs_b28.txt`.

## JJ. Round 28 checks (about 10 minutes)

| # | Do | Expected |
|---|---|---|
| JJ1 | Python window: `add_key_binding("Ctrl test", "Control_t", lambda: info_dialog("Ctrl-T works"))`. Click in the graphics window, press Ctrl-T; then plain `t`. | Ctrl-T: a small window "Ctrl-T works" and the terminal line `running key binding "Ctrl test"`. Plain `t`: no window. |
| JJ2 | With a model and map: paste recipe 6.3 (Python) into the Python window, click in the graphics window, press `v` near a residue. | 7 residues refine, Accept window as usual. |
| JJ3 | Help > Search Menus and Docs...; type `brighten`, double-click the menu line; type `sphere refine`, double-click the Cookbook line; type `refine_zone`, Enter. | Brighten Maps runs; the browser opens the cookbook at 4.3; then the reference at `refine_zone` (or the first function line). |
| JJ4 | Help > Keyboard Shortcuts... (after JJ1). | Coot's keys, and "Ctrl test" under your bindings. |
| JJ5 | Help > Cookbook, Scripting Reference, coot0 README, What's New. Then: is the menu what you had in mind? What would you add (e.g. a keyboard shortcut for the search)? | Each opens a readable page in the browser. Your opinion. |

# Earlier round (II3, II4 confirmed 20 Nov; II1, II2 -> build 28): Coot 0.9.8.96 on Apple Silicon: test round 27 (build 27 = build 26 + cookbook fixes + Ctrl key bindings from Python)

**From you** (19 Nov): HH1, HH2, HH3 pass; HH4: 6.1 ok, 6.3 F5 did nothing (fn+F5 opened Model/Fit/Refine), 6.4 did not load the map and
"changed another map"; HH5 useful, but the recipes repeat the loading lines (following them in order loads many copies), and after recipe 4.1
the next refinement had no Accept window and the view stayed in a strange state.

1. **F5 belongs to Coot** (Model/Fit/Refine); a binding of a key Coot uses is made but never runs. Recipe 6.3 now uses `o` and lists Coot's own
   keys; on a Mac, F-keys need `fn`. Its old tip `Control_r` is Coot's Ctrl-R (rock) and is gone too.
2. **Ctrl keys from Python now work** (they never did in coot0: the key reached Python without the Ctrl state). Not seen on a screen yet.
3. **The refinement recipes switched off the Accept window and left it off** (`set_refinement_immediate_replacement(1)`). Then your sphere
   refine had nothing to accept it, and its moving atoms stayed on the screen. Every recipe now switches it back with
   `set_refinement_immediate_replacement(0)`; to get out of that state in an open Coot: `accept_regularizement()` (or `clear_up_moving_atoms()`),
   then `set_refinement_immediate_replacement(0)`.
4. **6.4** could not find the test map because recipe 1.1 (which copies the test files) had not run: `make_and_draw_map` gave -1 and
   `set_map_colour(-1, ...)` did nothing; what you saw change was the white background from the same recipe. The cookbook now says at the top
   of every chapter that each recipe stands alone, to run 1.1 first, and how to use your own model and map (`imol = 0`, `imol_map = 1`).
5. "Refine here" (6.1) is like Coot's Sphere Refine: the residue at the centre plus every residue within 4 A (Coot's own uses 4.5 A and also
   handles alternate conformations).

**On screen: not verified by me** (headless only). **New tests**: `cookbook` (no recipe binds a key Coot uses; none leaves immediate
replacement on; the build 26 cookbook fails 18 of 166), `gui-dialogs` 79 -> 80 (build 26 fails the new one). Evidence: `evidence/checks_b26_vs_b27.txt`.

## II. Round 27 checks (about 10 minutes)

| # | Do | Expected |
|---|---|---|
| II1 | With a model and map loaded: paste the Python of recipe 6.3 into the Python window, close it, click in the graphics window, press `o` near a residue. | The 7 residues around the centre refine (Accept window as usual). |
| II2 | Python window: `add_key_binding("Ctrl test", "Control_t", lambda: add_status_bar_text("Ctrl-T works"))`; then Ctrl-T in the graphics window. Then plain `t`. | Ctrl-T: "Ctrl-T works" in the status bar. Plain `t`: nothing from this binding. |
| II3 | Run recipe 4.1 (after 1.1), then sphere refine (R key or toolbar) somewhere. | The usual Accept window appears; the view is normal after Accept. |
| II4 | Read the top of `docs/cookbook/README.md` ("How to use a recipe") and one chapter's first lines. | Clear that recipes stand alone and how to use your own data? |

# Coot 0.9.8.96 on Apple Silicon: test round 26 (build 26 = build 25 + a new Python window, a quiet terminal, the scripting documentation)

**From you** (18 Nov): GG1-GG4 confirmed (you liked the new Scheme window); Cryo-EM > Align and Mutate using ClustalW2 opens fine on screen. Asked for: the Auto-Recontour entries to say something in the terminal; the debug line for each Scheme command to go; the documentation of the functions and the cookbook.

1. **Python window.** Calculate > Scripting > Python... now looks and works like the Scheme window: the command (green), what it printed (black; before, `print` went to the terminal only), its result (blue, `=> 'GLU'`), errors with their traceback (red); Up / Down; Clear. Several lines as at the Python prompt: after a line ending in `:` the prompt shows `...` and the next line is indented for you; an empty line runs the block. If you type Scheme into it, it says so.
2. **Quiet terminal.** The "debug:: g.safe_scheme_command() with command ..." line is gone (this needed the first C++ rebuild since build 13; everything else in `bin/coot-bin` is unchanged). Commands you type into the Scheme window appear once in the terminal (`scheme> ...` and `=> ...`).
3. **Auto-Recontour.** Cryo-EM > No / Enable Auto-Recontour Map Mode print e.g. "Auto-recontour map mode: OFF. Maps keep their current contours ..." in the terminal and the status bar.
4. **Documentation** in the package folder `docs/` (start at `docs/README.md`; on GitHub under `m0/m1-package/docs/`):
   - `docs/cookbook/`: 85 recipes in 10 topics (files and maps, view, selections, refinement, editing, customizing toolbar / menus / keys / colours / preferences, batch scripts and hooks, validation, NCS, ligands), each in Python and Scheme. The test suite runs every recipe in both languages (83 of them; 6.4 map colour and 7.6 timer need the window).
   - `docs/api/`: every scripting function (1,735), with a concrete example on the test data (`residue_name(0, "A", 41, "")`, molecule 0 = tutorial-modern.pdb, molecule 1 = its map) and what happened when it was tried without a window. `docs/api/one-language-only.md` is the list of functions that exist only in Python or only in Scheme, with their counterparts.

**On screen: not verified by me** (all headless). In particular: the Python window, the status-bar text, and the cookbook recipes that make buttons, menus and keys (6.1-6.3) or set the map colour (6.4).

**New tests** (`gui-dialogs` 74 -> 79, build 25 fails the 5 new ones; new suites `api-docs` 5 and `cookbook` 166). Evidence: `evidence/checks_b25_vs_b26.txt`, `evidence/verify_b26.txt`.

## HH. Round 26 checks (about 15 minutes)

| # | Do | Expected |
|---|---|---|
| HH1 | Calculate > Scripting > Python...; load a model; type `residue_name(0, "A", 41, "")` (your molecule / chain / residue), then `print("hello")`, then `for i in range(3):` Enter, `print(i)` Enter, Enter; then `1/0`; then Up a few times. | `=> '...'`; `hello`; `0 1 2`; a red error with the traceback; earlier commands come back. The same in the terminal. |
| HH2 | Calculate > Scripting > Scheme...; type `(+ 1 2)`. Look at the terminal. | `scheme> (+ 1 2)` and `=> 3`; no "debug:: g.safe_scheme_command" line. |
| HH3 | Cryo-EM > No Auto-Recontour Map Mode, then Enable Auto-Recontour Map Mode (the Cryo-EM menu appears after Calculate > Modules... > Cryo-EM). | A line "Auto-recontour map mode: OFF/ON ..." in the terminal each time, and the same in the status bar. |
| HH4 | Cookbook 6.1 (toolbar button "Refine here"), 6.3 (F5 key) and 6.4 (map colour): paste the Python of each into the Python window, with a model and its map loaded; press the new button / F5 near a residue. | The button and the key refine around the centre; the map turns light blue. |
| HH5 | Open `docs/README.md` (or on GitHub) and look at a recipe or a function you know. | Readable and useful? Tell me what is missing or wrong. |

---

# Earlier round (GG1-GG4 confirmed 18 Nov): Coot 0.9.8.96 on Apple Silicon: test round 25 (build 25 = build 24 + a working Scheme scripting window)

**From you** (18 Nov): FF1 (A 117 was flipped back by the flip try), FF2, FF3 confirmed; README.md was not in the package; add the two-finger click to the README. The Scheme window said "For now this is a placeholder only!" and nothing appeared in it or in the terminal (only `set-graphics-window-size` worked, and its message comes from the C++ code).

1. **Scheme window.** Calculate > Scripting > Scheme... now opens a new window, "Coot Scheme Scripting". It does not translate anything: your text goes unchanged to Coot's Scheme (Guile), and the window shows the command (green), what it printed (black), its result (blue, `=> "HIS"`) and errors (red). Up / Down bring back earlier commands; an expression over several lines works (Enter with brackets still open waits for the rest); Clear empties the window. Everything is also written to the terminal.
2. **Terminal output of Scheme.** The launcher copies the terminal into `logs/`, and Guile then held back what Scheme printed, often until Coot quit. Now each line appears at once (checked with a script that prints and waits: build 24 had not shown it after 90 s, build 25 after 6 s). Cosmetic: Coot also prints a long "debug:: g.safe_scheme_command() with command (coot0-console-eval ...)" line for each command; that is in the C++ code and goes at the next C++ rebuild.
3. `README.md` is in the package; the two-finger click is in its "Changes" list.

**On screen: not verified by me** (the window was tested headless: menu entry, commands, output, results, errors, several lines, history).

**New tests** (`gui-dialogs` 70 -> 74; build 24 fails all 4). Evidence: `evidence/checks_b24_vs_b25.txt`, `evidence/verify_b25.txt`.

## GG. Round 25 checks (about 10 minutes): GG1-GG4 confirmed 18 Nov (ClustalW2 entry opens on screen)

| # | Do | Expected |
|---|---|---|
| GG1 | Calculate > Scripting > Scheme... | A window "Coot Scheme Scripting" with a short help text; no "placeholder" message. |
| GG2 | Load a model, type `(residue-name 0 "A" 41 "")` (your molecule number / chain / residue), Enter; then `(display "hello") (newline) (+ 1 2)`; then `(car 1)`. | The command, then `=> "..."`; then `hello` and `=> 3`; then a red error. The same in the terminal. |
| GG3 | Type `(+ 1` Enter, then `2)` Enter; then press Up twice. | `=> 3`; Up brings back earlier commands. |
| GG4 | Something you use, e.g. `(set-graphics-window-size 800 600)` or a function from your own scripts. | It runs; nothing missing in the window or the terminal. |

---

# Earlier round (FF1-FF3 confirmed 18 Nov): Coot 0.9.8.96 on Apple Silicon: test round 24 (build 24 = build 23 + a clear list of turned peptides, no blank menu bar in the plain entry)

**From you** (17 Nov): EE1, EE2 confirmed. EE3: of 4 peptides flipped on purpose, all were put back, but the report named only 2; the plain entry turned back 2 of them; the menu bar went blank in the plain entry. Asked for: the limits visible in the README, an explanation of "the carbonyl O left the density" with equations, and a clear definition of a flipped peptide.

1. **What counts as flipped.** A badly flipped peptide is often put back by the ordinary refinement (try A) already; then the flip try (B) is worse and is not kept, so build 23 did not count it. Now the report compares every peptide with the start of the run: a peptide has **turned** when its carbonyl O ends up more than 90 degrees from where it was (round the CA(i) - CA(i+1) axis). The report lists them in two groups: "Flipped by the flip try" and "Turned by the refinement itself". The plain entry lists the peptides it turned in the terminal and the status bar.
2. **Blank menu bar in the plain entry.** The redraw that cured EE2 in the (try peptide flips) entry now follows every shown refinement (also Stepped Refine and Fit Protein).
3. **README**: the formulas and the limit variables, with how to change them (section "How (try peptide flips) decides").

**Tested headless on your model** (local, not in git): your 4 deliberate flips (EE3): all put back; the report lists 1 flipped by the flip try and 3 turned by the refinement itself (in a run over residues around them only, so the split between the two lists can differ from a whole-model run). **On screen: not verified by me.**

**New tests** (`gui-dialogs` 66 -> 70; build 23 fails all 4). Evidence: `evidence/checks_b23_vs_b24.txt`, `evidence/verify_b24.txt`.

## FF. Round 24 checks (about 15 minutes, on a copy of your model)

| # | Do | Expected |
|---|---|---|
| FF1 | Pep-flip 3-4 good peptides on purpose, run "(try peptide flips)" over the model. | The report lists every one of them, either under "Flipped by the flip try" or "Turned by the refinement itself"; nothing else turned that should not. |
| FF2 | The same with the plain "Refine/Improve Ramachandran Plot..." and watch the menu bar. | The menu bar stays drawn; at the end the terminal / status bar say which peptides turned. |
| FF3 | Read the README section "How (try peptide flips) decides". | Clear enough; tell me if a limit should change. |

---

# Earlier round (EE1, EE2 confirmed 17 Nov; EE3 led to round 24): Coot 0.9.8.96 on Apple Silicon: test round 23 (build 23 = build 22 + the map decides peptide flips, no blank menu bar)

**From you** (17 Nov): DD1-DD5 confirmed. Found: (1) part of the window (the menu bar) went blank during a run until the mouse went over it; (2) "(try peptide flips)" kept flips that were clearly wrong but gave a slightly better Ramachandran plot (two screenshots).

1. **Wrong flips.** Build 22 ranked the Ramachandran regions above the map: a flip that moved a residue from allowed to favoured was kept whatever the density said. On your model there were three such flips (the residue numbers are in chat): the flipped carbonyl O went from 5.3 / 7.3 / 5.6 sigma to 3.7 / -0.8 / 0.1 sigma. Now **the map has a veto**. A flip is kept only if
   - no residue moves to a worse Ramachandran region, and the carbonyl O does not lose density (at most 0.3 sigma), nor the peptide C, O, N together (0.6 sigma), nor the two residues as a whole (2%);
   - and then either a Ramachandran region gets better, or (same regions) the carbonyl O and the peptide each gain at least 1 sigma.
   The report and the terminal now give the carbonyl density before and after each flip ("Peptide A 43-44 flipped (Ramachandran 2 -> 4, carbonyl O -0.6 -> 4.2 sigma, ...)"). The limits are variables (`rama_flip_max_o_loss` etc. in `fitting.py`) if they need tuning.
2. **Blank menu bar.** Not reproduced by me (I did not use your screen). The likely cause: build 22 opened and closed a hidden molecule for every Ramachandran check of a split conformer (your status bar showed "Successfully read coordinates file .../coot-rama-conformer-....pdb. Molecule number 10 created"), and each time Coot updated its molecule lists. Now one hidden scratch molecule is reused and closed when the run ends, and the window is redrawn after every residue.

**Tested headless on your model** (local, not in git): all 232 peptides of chain A scored both ways: the old rule flips 3 (the wrong ones), the new rule none. 21 peptides flipped on purpose (every 11th, A 15-235): all 21 put back (the old 10% map rule missed one). On the tutorial model the earlier flip checks still pass. **On screen: not verified by me.**

**New tests** (`gui-dialogs` 61 -> 66; build 22 fails all 5). Evidence: `evidence/checks_b22_vs_b23.txt`, `evidence/verify_b23.txt`.

## EE. Round 23 checks (about 20 minutes, on a copy of your model)

| # | Do | Expected |
|---|---|---|
| EE1 | Run "(try peptide flips)" over the three residues that were wrongly flipped last time (or the whole model). | None of the three is flipped; the report lists only flips whose carbonyl density went up. |
| EE2 | During that run (residues with alternate conformations included), watch the menu bar and the status bar. | The menu bar stays drawn; no "coot-rama-conformer" message; the Display Manager has no extra molecule after the run. |
| EE3 | Pep-flip two or three good peptides on purpose, then run "(try peptide flips)" over them. | They are flipped back; the report shows the carbonyl density going up. |

---

# Earlier round (DD1-DD5 confirmed 17 Nov): Coot 0.9.8.96 on Apple Silicon: test round 22 (build 22 = build 21 + peptide flips with alternate conformations, amino acids only, flip report, Fill Partial Residues list)

**From you** (16 Nov): CC1-CC3 and CC5 confirmed (the new entry is there, both orientations are tried, correct peptides are kept, Fill Partial Residues rebuilt the deleted side chain). Asked for: flips also for residues with alternate conformations; no ligands / non-protein residues touched by either Ramachandran entry; a final report of the flips; a list of the residues Fill Partial Residues fixed; the model asked for only when there is a choice; the active map; no hydrogens.

1. **Alternate conformations** (you were right: build 21 tried no flip at all next to alt confs, it only refined each conformer). Now, if only side chains are split (the peptide atoms are shared), both tries refine every conformer and one decision is made for the shared peptide. If the peptide itself is split (C, O / N in conformers A and B), the flip is tried for each conformer separately and judged on that conformer alone.
2. **Amino acids only**, in both Refine/Improve Ramachandran Plot entries: ligands, waters and nucleotides are not refined, and they are not part of the zone around an amino acid either (before, a ligand numbered right after the last residue of a chain was refined with it). Skipped ligands are named in the terminal.
3. **Report** (try peptide flips): when the run finishes, or when you press Stop, a window (and the terminal and status bar) says "... finished: N peptides flipped (M peptides tried)" with the list of flips. After Continue you get another report at the end.
4. **Fill Partial Residues**: the terminal lists each residue filled ("filled ARG A 40: added CG CD NE CZ NH1 NH2") and those it could not fill (when N, CA or C is missing). With one model loaded it does not ask; with several, the chooser opens (also for Calculate > Modelling... > Fill Partial Residues, which used the molecule at the centre). The map is the refinement map (Coot's "active" map; picked automatically when only one map is loaded); with several maps and none chosen it asks for the map first. No hydrogens are added (that was already so).

**Tested headless** on the tutorial model: the peptide B 71-72 next to Cys B 72 (side-chain alt confs) flipped on purpose was put back; with residues A 43-44 split into conformers A / B and only B flipped on purpose, B was flipped back and A kept; a sulfate numbered after the last amino acid and a water were not moved by either entry; the report after a finished and a stopped run; the Fill Partial Residues list. **On screen: not verified by me.**

**New tests** (`gui-dialogs` 53 -> 61; build 21 fails all 8). Evidence: `evidence/checks_b21_vs_b22.txt`, `evidence/verify_b22.txt`.

## DD. Round 22 checks (about 15 minutes, on a copy of your model)

| # | Do | Expected |
|---|---|---|
| DD1 | A residue with alternate conformations: Pep-flip the peptide before or after it, run "(try peptide flips)", Stop after that residue. | The flip is tried and the peptide is back; the report window appears after Stop. |
| DD2 | (if your model has a ligand or glycan) Run either Ramachandran entry over the residues around it. | The ligand does not move; the terminal says it was not touched. |
| DD3 | Let "(try peptide flips)" finish (or Stop it). | A report window: number of peptides flipped and tried, the list. |
| DD4 | Delete a side chain, Calculate > All Molecule... > [Post MR] Fill Partial Residues... (one model loaded). | No chooser; side chain rebuilt; terminal lists "filled <RES> <chain> <no>: added ...". |
| DD5 | (optional) Load a second model and repeat DD4. | The chooser opens first. |

---

# Earlier round (CC1-CC3, CC5 confirmed 16 Nov): Coot 0.9.8.96 on Apple Silicon: test round 21 (build 21 = build 20 + Refine/Improve Ramachandran Plot (try peptide flips))

**From you** (16 Nov): BB1-BB4 confirmed (Fit Protein and Refine/Improve Ramachandran Plot show the refinement like Stepped Refine; the menu entries are there). Asked for peptide flips in the Ramachandran refinement as a new entry next to the original (your choice (a)). Fill Partial Residues: question answered in chat, your details pending (CC5).

1. **New entry Calculate > All Molecule... > Refine/Improve Ramachandran Plot (try peptide flips)...** For every residue it refines twice: as it is, and with the peptide to the next residue flipped (Coot's Pep-flip). It keeps the flip only if it is better: a better Ramachandran region for the two residues (outlier < allowed < favoured, Coot's own classification), or the same regions and at least 10% better fit to the map. Otherwise the first result is kept. Both tries are shown like Stepped Refine (so a residue takes about twice as long). Kept flips are reported in the status bar ("Peptide A 43-44 flipped ...") and in the terminal log ("INFO:: rama flip").
2. Residues where no flip is tried (refined as in the original entry): waters, nucleotides, the last residue of a chain, residues with insertion codes or alternate conformations.
3. The original **Refine/Improve Ramachandran Plot...** is unchanged.

**Tested headless** on the tutorial model: 4 peptides flipped on purpose (A 20, 43, 60, 85) were all flipped back (carbonyl O within 0.15 A of the deposited position); 4 correct ones (A 30, 50, 70, 90) were left alone. A 60 was decided by the map fit (both orientations in the same Ramachandran regions). **On screen: not verified by me.**

**New tests** (`gui-scripts` 15 -> 16, `gui-dialogs` 48 -> 53; build 20 fails all 6). Evidence: `evidence/checks_b20_vs_b21.txt`, `evidence/verify_b21.txt`.

## CC. Round 21 checks (about 15 minutes)

| # | Do | Expected |
|---|---|---|
| CC1 | Install build 21, Calculate > All Molecule... | Five entries; the new one is "Refine/Improve Ramachandran Plot (try peptide flips)...". |
| CC2 | On a copy of your model, flip one peptide on purpose (Pep-flip button), then run the new entry; Stop after that residue has been done. | Both tries are shown; the status bar says that peptide was flipped; it is back in its original orientation. |
| CC3 | Let it run over 20-30 correct residues. | No flips reported (or only ones you agree with). |
| CC4 | (optional) The original entry on the same deliberately flipped peptide. | It does not fix it (as before). |
| CC5 | Fill Partial Residues: tell me how you removed the atoms, how many models were loaded (and which one the chooser showed), whether a "select map" window appeared, whether the model has hydrogens. | Your answers. |

---

# Earlier round (BB1-BB4 confirmed 16 Nov): Coot 0.9.8.96 on Apple Silicon: test round 20 (build 20 = build 19 + Refine/Improve Ramachandran Plot in the menu + Fit Protein shows its refinement)

**From you** (16 Nov): asked for the Ramachandran entry, a README note, and the same refinement highlight in Fit Protein and Refine/Improve Ramachandran Plot as in Stepped Refine. AA1-AA4 (round 19) are still open.

1. **Calculate > All Molecule... > Refine/Improve Ramachandran Plot...** is now in the menu. It was in the Coot 0.9.8.96 code but never appeared (one line indented into the wrong function, the same in the original source). It does what Stepped Refine does, with Ramachandran restraints on during each residue's refinement (your own setting is restored afterwards).
2. **Fit Protein shows its refinement.** For each residue it still does the rotamer search first (protein residues), then refines the residue; that refinement is now drawn in Coot's refinement style (the highlighted intermediate atoms) for 0.6 s and then accepted, exactly as in Stepped Refine. Before, the residue just jumped. The map is re-contoured around each residue, Stop works, no "Accept Refinement?" window. On RNA it now centres on C1' (before: the view did not move).
3. Refine/Improve Ramachandran Plot uses the Stepped Refine code, so it has the same display.
4. `README.md` (GitHub page) has a new section "Changes from the original Coot 0.9.8.96".

**On screen: not verified by me.** The headless tests check that the refinement runs as an ordinary (displayed) refinement and stays displayed until it is accepted, the map follows, the menu entry exists and opens its molecule chooser. Whether it looks the same as Stepped Refine is for you to see (BB2, BB3).

**New tests** (`gui-scripts` 14 -> 15, `gui-dialogs` 45 -> 48; build 19 fails 3 of them). Evidence: `evidence/checks_b19_vs_b20.txt`, `evidence/verify_b20.txt`.

## BB. Round 20 checks (about 10 minutes)

| # | Do | Expected |
|---|---|---|
| BB1 | Install build 20 (`./install.sh` in the unpacked `coot0-0.9.8.96-b20`), `coot0 --pdb <model> --auto <mtz>`. Calculate > All Molecule... | Four entries: [Post MR] Fill Partial Residues..., Fit Protein..., Stepped Refine..., Refine/Improve Ramachandran Plot... |
| BB2 | Refine/Improve Ramachandran Plot..., choose the model. Let it do 10-20 residues, then Stop. | Each residue shown in the refinement style for a moment, the view and the density follow; Stop ends it; Cancel / Continue then work as in Stepped Refine. |
| BB3 | Fit Protein..., choose the model (a copy: it changes side chains). 10-20 residues, Stop. | Same display as Stepped Refine after each rotamer fit; no residue jumps without being shown. |
| BB4 | (optional) Stepped Refine... as before. | Unchanged from build 19. |

---

# Earlier round (AA1-AA4 still open): Coot 0.9.8.96 on Apple Silicon: test round 19 (build 19 = build 18 + licences; the build for the lab)

**From you** (13 Nov): build 18 works (Retina view by default, `--legacy`). Licensing decided: Coot keeps its own licence (GPL-3.0-or-later, its authors); the coot0 changes are Copyright (C) 2026 Chang Sun under GPL-3.0, stated separately; the package as a whole is GPL-3.0. **No change to Coot itself.**

1. **The package carries its licences**: `LICENSE` (GPL-3.0 text, as shipped with Coot), `LICENSING.md` (Coot, the coot0 changes and the third-party libraries, each with its own copyright and licence), `CORRESPONDING_SOURCE.md` (where the source of every part comes from, and the written offer the GPL requires), `THIRD_PARTY_LICENSES.md` (60 bundled packages + 7 other components with version and licence) and `licenses/` (the licence texts of each of the 60 packages). `README-FIRST.txt` has a short LICENCE section.
2. **Fixed: the self-test showed macOS's "coot-bin Not Opened" dialog.** The installer test flags a copy of the package with the download quarantine on purpose (to check that the installer removes it); a check added in build 18 then started Coot from that flagged copy. That was the dialog you saw on 13 Nov (12:25 and about 14:00, during my test runs), not a problem of your installation. The test now removes the flag before starting that copy and checks that Coot really started. In build 18 `coot0 --self-test` would still show it once.

**New tests** (`installer` 23 -> 26; build 18 fails 3): the licence files are in the installed copy, every package of the list has its licence text, README-FIRST mentions the licence. Evidence: `evidence/checks_b18_vs_b19.txt`, `evidence/verify_b19.txt`.

## AA. Round 19 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| AA1 | `tar -xzf ~/Desktop/test/coot0-0.9.8.96-b19-macos-arm64.tar.gz`, `cd coot0-0.9.8.96-b19`, `./install.sh` (Enter). | Installed into `~/.local/share/coot0/0.9.8.96-b19`; `coot0` starts build 19 (Retina view). |
| AA2 | Read `README-FIRST.txt` and `LICENSING.md` as a lab member would. | Clear what coot0 is, how to install and run it, who wrote what, whom to ask. |
| AA3 | (optional) `coot0 --self-test` | 19 lines `N / N` (installer 26), no macOS dialog. |
| AA4 | **The first lab member** who installs it: `coot0 --self-test` on their Mac, send the 19 lines. | All `N / N`. Why: some libraries contain the folders of the build machine (a conda folder in the build account's home, e.g. GLib's and GTK's default data folders). The launcher points all of them into the package, but on your Macs those folders exist, so only a Mac without them proves that nothing falls back to them. |

---

# Earlier round (confirmed 13 Nov: build 18 works): Coot 0.9.8.96 on Apple Silicon: test round 18 (build 18 = build 17 + Retina view by default for coot0)

**From you** (13 Nov): build 17 installed and `coot0` works; the Gatekeeper dialog seen once at 12:25 could not be reproduced (paused; notes in the answer of 13 Nov). **No change to Coot itself**: the launcher, installer, tests and documents changed.

1. **`coot0` draws the 3D view at full Retina resolution by default** (2 GL pixels per point, as `--retina` did; your earlier sessions used it 14 times). **`coot0 --legacy`** gives the standard resolution (1 pixel per point, enlarged by macOS: softer, less work for the graphics chip; useful for large maps, an external non-Retina monitor or an older Mac). `COOT_RETINA=0` / `1` in the environment does the same and wins over the default. The unpacked folder (`./run-coot.sh`) keeps the standard resolution unless you give `--retina`; `--legacy` works there too. `--legacy` is not passed on to Coot (Coot does not know it).
2. `README-FIRST.txt` explains the two resolutions; the installer's final summary mentions `coot0 --legacy`.
3. The installer suite checks the default (retina=1), `--legacy` (retina=0, Coot starts) and the unpacked folder (retina=0): 22 checks; build 17 fails 2 of them.

**On screen: not verified by me** (the Retina view itself was used by you in builds 9-16 with `--retina`).

## Z. Round 18 checks (about 5 minutes)

| # | Do | Expected |
|---|---|---|
| Z1 | `tar -xzf ~/Desktop/test/coot0-0.9.8.96-b18-macos-arm64.tar.gz` (e.g. in ~/Downloads), `cd coot0-0.9.8.96-b18`, `./install.sh` (Enter). | Installed into `~/.local/share/coot0/0.9.8.96-b18` (b17 stays), summary mentions `coot0 --legacy`. |
| Z2 | New Terminal window, a data folder: `coot0 --pdb <model> --auto <mtz>`. | Sharp (Retina) atoms, bonds, labels; picking (middle/right-click centre, click on atom) hits the atom under the pointer. The log line 2 says `retina=1`. |
| Z3 | Quit, `coot0 --legacy` with the same files. | Softer view, same picking; log `retina=0`. |
| Z4 | Anything slow or wrong with the Retina view (large map, rotate)? | Your impression. |

---

# Earlier round (Y1-Y5 still open): Coot 0.9.8.96 on Apple Silicon: test round 17 (build 17 = build 16 + installer and `coot0` command)

**From you** (13 Nov): X1, X2, W2, W3, W5 confirmed; the MacBook Pro M2 Pro passes all 18 headless suites on build 16 (your `m1-results-20261113-112209.txt`; the `ERROR:: ... torsion gradients` / `Null link_p` lines in it are Coot's own messages while the tests refine deliberately distorted test data, the same on the iMac). W6: I ran collect-results myself (no errors in your 13 Nov session). Rounds 13-16 are closed. **No C++ change, no change to Coot's scripts**: only the package (installer, launcher, tests, documents).

**New: install and run with one command.** The download is now `coot0-0.9.8.96-b17-macos-arm64.tar.gz` (tar keeps file times and links). In Terminal: `tar -xzf coot0-...tar.gz`, `cd coot0-0.9.8.96-b17`, `./install.sh` (or double-click **Install coot0.command** in Finder). The installer:
1. checks the Mac (Apple Silicon, macOS version, disk space) and says what CCP4 / Phenix / reduce / probe it finds and what each is needed for;
2. removes the download flag (quarantine) from the installed copy;
3. asks where to install (Enter = `~/.local/share/coot0/0.9.8.96-b17`; type another folder to change it). An older copy of the same version is moved aside, not deleted; other versions stay. On the same disk the copy is an APFS clone (seconds, no extra space);
4. writes the command `~/.local/bin/coot0`;
5. adds one marked line `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc` (zsh is the macOS default), and also to `~/.bash_profile` if bash is your login shell or that file exists, and to `~/.bashrc` if it exists; it prints every change (a file that already has `.local/bin` is not changed);
6. starts Coot once without a window (about 30 s; Python, Scheme, a model and a map);
7. tells you how to run it.

`coot0` starts Coot **in the folder you type it in** (coot-backup/, 0-coot-history.py there, like Coot 0.9 on Linux), with all Coot options (`coot0 --pdb x.pdb --auto x.mtz`). Your preferences and logs are per user in `~/Library/Application Support/coot0` (private, so CCP4's Coot 1 settings are never read). `coot0 --diagnose`, `coot0 --self-test` (all suites), `coot0 --uninstall` (removes the command, the PATH lines - a copy of each file is kept - and, if you say so, the installed copy and your preferences). The unpacked folder itself still runs with `./run-coot.sh` as before (logs then stay in the folder).

Also: the launcher now finds reduce / probe of **Phenix 2.x** (`~/phenix-*/bin` or `/Applications/phenix-*/bin`; it only knew the Phenix 1.x layout). Harmless on your Macs (CCP4 has them), useful on a Mac with only Phenix.

**New test** (fails on build 16: 3 / 19; with only the build-16 launcher: 15 / 19): `installer` 19 (in `run-headless-tests.sh`; throw-away home folders, a copy with the download flag set on purpose and spaces in the paths; zsh and bash users; install twice; coot0 from a project folder; uninstall). Evidence: `evidence/checks_b16_vs_b17.txt`.

## Y. Round 17 checks (about 10 minutes)

| # | Do | Expected |
|---|---|---|
| Y1 | Download/copy `coot0-0.9.8.96-b17-macos-arm64.tar.gz` to `~/Downloads`; in Terminal: `cd ~/Downloads; tar -xzf coot0-0.9.8.96-b17-macos-arm64.tar.gz; cd coot0-0.9.8.96-b17; ./install.sh`; press Enter at the folder question. | Short check lines (ok / note), "removed the download flag" if Safari flagged it, the PATH line it added to `~/.zshrc`, "ok Coot starts: ...", the summary. |
| Y2 | Open a **new** Terminal window, `cd` to a folder with your data, `coot0 --pdb <model> --auto <mtz>` (or just `coot0`). | Coot opens as before (your preferences start fresh: the per-user folder is new); `coot-backup/` appears in that folder when you edit. |
| Y3 | `coot0 --diagnose` | CCP4 and Phenix found, the installed version listed. |
| Y4 | (MacBook, optional) the same as Y1, then `coot0 --self-test`. | 19 lines `N / N` (18 + installer). |
| Y5 | Your opinion: is anything in the installer output unclear for a lab member? | |

---

# Earlier round (all checks confirmed 13 Nov): Coot 0.9.8.96 on Apple Silicon: test round 16 (build 16 = build 15 + one fix found by the real-window audit)

**From you** (11 Nov): W1 (Stepped Refine on RNA) and W4 (RCrane with the test data) confirmed. You allowed on-screen tests on the iMac after 17:00, so I ran the full real-window audit on build 15 at 17:05. **Build 16 has no C++ change** (`bin/coot-bin` and `lib/` as in builds 13-15); one Python file, one test and the documents changed (patch 0035).

1. **Real-window GUI audit of build 15** (every menu entry and toolbar button, about 18 minutes, in a throw-away folder): **255 ok, 0 crashes, 0 hangs, 0 dead entries.** Both errors of the build-14 audit are gone on the screen: the Stop / Cancel / Continue toolbar buttons (round 15, item 4) and Lidia's hidden developer button. The 6 warnings are the same GTK messages as in build 14 (file chooser, a window closed twice by the audit's clicking, a combo box in LSQ Superpose that the audit closes while it is being filled); they do not change what you see.
2. **Fixed: Ligand Builder (Lidia) > Apply could fail before acedrg was started.** The audit pressed Apply on an empty sketch; acedrg (CCP4) stopped with a Python traceback. Looking at why, I found a real fault in the same path. Coot builds acedrg's environment from the variable `CBIN`, which exists only when Coot is started from a Terminal that has sourced CCP4's setup. If you start Coot from Finder or a plain shell, Apply raised `KeyError: 'CBIN'` and nothing happened. The same code joined PATH with `;` (Windows) and passed Coot's own Python 3.11 path to CCP4's Python 3.9. This affected the SMILES import and the acedrg link tool too. Now acedrg gets CCP4's variables the way refmac5 does (the CCP4 folder that the launcher found). An empty sketch gives a message ("Draw a molecule first") instead of starting acedrg. Test: a benzene drawn as Lidia writes it is turned into a ligand + dictionary by the real acedrg of CCP4 9, with no CCP4 variables in Coot's environment; it fails on build 15. The repeated real-window audit of Calculate > Ligand Builder gives ok. **On screen: not verified** (what the imported ligand looks like).

**New tests** (fail on build 15, pass on build 16): `refmac-run` 8 -> 11 (acedrg environment without a CCP4 shell, empty sketch, Lidia -> acedrg -> ligand). Evidence: `evidence/checks_b15_vs_b16.txt`, `evidence/gui_audit_claude_b15_iMac.txt`, `evidence/gui_audit_claude_b16_lidia_iMac.txt`.

## X. Round 16 checks (about 5 minutes; W2, W3, W5 and W6 of round 15 are still open)

| # | Do | Expected |
|---|---|---|
| X1 | Calculate > **Ligand Builder**: draw a small molecule (e.g. a benzene ring from the ring buttons), then **Apply** (or File > Apply in Lidia). Best: start Coot by double-clicking `run-coot.sh` / from a Terminal that has *not* sourced CCP4. | After some seconds (acedrg runs) a new ligand molecule appears at the screen centre and its dictionary is read; no `KeyError` in the terminal. |
| X2 | Ligand Builder with nothing drawn: **Apply**. | A message "Nothing to import ... Draw a molecule first"; no traceback in the terminal. |

---

# Earlier round, still valid (W2, W3, W5, W6 are still open): Coot 0.9.8.96 on Apple Silicon: test round 15 (build 15 = build 14 + answers to your round-14 report)

**From your report on build 14** (thank you; confirmed: the occupancy slider, Stepped Refine on proteins, the Calculate > RCrane sub-menu, Scheme scripting; the MacBook tests are postponed to the end). **Build 15 has no C++ change** (`bin/coot-bin` and `lib/` as in builds 13-14); Python/Scheme scripts, the launcher, tests and documents changed (patch 0034).

1. **Stepped Refine on RNA did nothing - fixed (it was a limit of Coot 0.9.8.96 itself, not of the port).** Coot's `refine_auto_range` (the per-residue refinement that Stepped Refine uses) finds the residue by its C-alpha atom; nucleotides have none, so your 9E5H run logged `refine_auto_range: Can't get index for resno1` for every residue and nothing moved; the view was sent to "CA" too, so it did not move either. Now a residue without CA is centred on C1' (else P, else its first atom) and refined as the zone residue-1 .. residue+1, the same range Coot uses for proteins. Protein residues go through the unchanged path. Test: one step on nucleotide A 22 of tRNA 1EHZ moves it, nothing outside 21-23 moves, the O3'-P links stay 1.60 A; it fails on build 14. **On screen: not verified.**
2. **PDB-REDO: where the "HTML error page" note came from.** Your fetch of 1FFT and 9E5H is in the log. 1FFT: the network timed out (curl status 28), nothing to do with Coot. 9E5H: PDB-REDO has it, but **only as mmCIF**; asking for `9e5h_final.pdb` returns "404 Not Found" as a small HTML page, and Coot saved that page as `9e5h_final.pdb` (read error, so you got the map without the model), then saved the missing "guided tour" the same way and ran it as Scheme (`Unbound variable <html>`). Entries that still have a PDB-format file (older ones) worked, which matches what you saw. Fixed: every download is checked (an HTML page or an empty file is removed, not read), the model falls back to `<id>_final.cif`, the guided tour runs only if PDB-REDO has one (it is the Python window "PDB_REDO results"; the Scheme version needed the guile-gtk window this build lacks), and a message window says what could not be fetched. Checked live against pdb-redo.eu: 9E5H and 1EHZ load model + maps. Offline tests (a fake server) fail on build 14.
3. **The Scheme window shows no result** (your item 4): right, upstream's simple Scheme window evaluates what you type but never prints the value. Showing it needs a C++ change; noted for the next C++ rebuild.
4. **Real-window GUI audit (you asked me to run it):** done on this iMac on build 14 (every menu entry and toolbar button, about 18 minutes): **254 ok, 0 crashes, 0 hangs, 0 dead entries** (build 7, your last audit: 18 crashes, 6 dead entries). It found one real fault: the **Stop / Cancel / Continue** buttons that Stepped Refine and Fit Protein put on the toolbar. After Stop, a new run left the old buttons behind and pressing them gave `AttributeError: 'bool' object has no attribute 'destroy'`. Fixed (a new run ends the old one and removes its buttons; a button of a finished run does nothing). The second error was the audit pressing Lidia's hidden developer "test function" button (upstream shows it only with `COOT_LBG_TEST_FUNCTION` set); you cannot reach it, the audit no longer presses hidden buttons. The 6 warnings are GTK messages of the file chooser and of windows closed twice by the audit's clicking (known since build 7, harmless). I did **not** repeat the full audit on build 15: it takes over the screen for ~18 minutes and you were working at the Mac; the changed code is covered by the tests below. Say if you want it run at a time that suits you.
   **What I checked on the screen myself** (a scripted session in a real window; I read Coot's own window list; screenshots did not help because your other windows were in front of Coot): Stepped Refine on 1EHZ centred on C1' of each nucleotide and refined it; PDB-REDO 1EHZ opened the window "PDB_REDO results" (81 entries, it was mapped on the screen); 9E5H loaded model + maps; a code that does not exist gave the message window. **Not seen by me:** what any of this looks like.
5. Small: the two `Gtk-WARNING ... recently-used.xbel` lines after every file dialog are gone (the private `home/` lacked `.local/share`).

**New tests** (fail on build 14, pass on build 15): `refine-zone` 4 -> 7 (RNA Stepped Refine step), `data-and-maps` 32 -> 39 (PDB-REDO: mmCIF-only entry, no HTML/JSON error page left, missing entry, the menu's Scheme path, guided tour), `gui-dialogs` 44 -> 45 (Stop, then a new run), `bundle-python` 18 -> 19 (private HOME). Evidence: `evidence/checks_b14_vs_b15.txt`.

## W. Round 15 checks (about 10 minutes)

| # | Do | Expected |
|---|---|---|
| W1 | Open `test-data/1ehz.pdb` and `test-data/1ehz_map.mtz` (FWT/PHWT), make the map the refinement map, Calculate > All Molecule... > **Stepped Refine...** (or your own RNA). | The view goes to each nucleotide (its C1'), the nucleotides move in the refinement style; the log says `centering on A 1 C1'`, no `Can't get index`. |
| W2 | The same on your protein. | As in build 14. |
| W3 | File > **Fetch PDB & Map using PDB-REDO...**: `9E5H`, then `1EHZ`, then `0XYZ`. | 9E5H: model and maps (no `9e5h_final.pdb` in `work/`). 1EHZ: model, maps, and a window "PDB_REDO results". 0XYZ: a message that it could not be fetched (and no `0xyz_final.*` file in `work/`). |
| W4 | (Still open from round 13: U6-U8) RCrane > Rotamerize existing structure on 1EHZ. | The review window as described in U6. |
| W5 | Stepped Refine on a few residues, **Stop**, then start Stepped Refine again; then let it finish (or Stop + Cancel). | One Stop button during the second run; no Cancel/Continue left over; no error in the log. |
| W6 | Quit with File > Exit; run `./collect-results.sh` and tell me. | |

---

# Earlier round, still valid (V5, the MacBook tests, is postponed): Coot 0.9.8.96 on Apple Silicon: test round 14 (build 14 = build 13 + answers to your round-13 report)

**From your report on build 13** (thank you; confirmed: the Python scripting window, Nudge Residues, Fit Loop by Database Search, Place Helix Here, and Stepped Refine now shows the refinement style). Your open points, in order. **Build 14 has no C++ change:** `bin/coot-bin` and `lib/` are the files of build 13; Python scripts, tests and documents changed (patch 0033).

1. **Alt Conf Occupancy slider: "OK" did nothing - fixed.** Your log shows the cause 58 times: `TypeError: '>' not supported between instances of 'list' and 'int'` in `set_alt_conf_occ` (`coot_utils.py`). The code asks `alt_confs > 1` where `alt_confs` is a *list*; Python 2 answered "true" for any list, Python 3 refuses. Replaced by `len(alt_confs) > 1`. The same comparison was in `rename_alt_confs` (the "swap alt confs A and B" helper), so that one failed too and is fixed. I looked for the same pattern elsewhere and found no other instance (a search for `alt_confs >`; a general search for every list-versus-number comparison is not possible by text search, so I cannot promise there is none). The test opens the slider on Cys B 72 of the tutorial model (SG A 0.7 / SG B 0.3), sets 0.4, presses OK and checks 0.4 / 0.6 and that the window closed; it fails on build 13 with your exact TypeError.
2. **Stepped Refine - the "Accept Refinement?" window on the side.** Coot opens that window for every ordinary refinement; since build 13 Stepped Refine runs ordinary refinements and accepts each residue itself, so the window's buttons act on a refinement that is already finished (that is why it did nothing). It is now **hidden the moment it appears** and **closed after the residue is accepted** (closing it after the accept is what its own Accept button does; closing it before would reject, which is why the order matters). The test builds a window with that title, runs one residue and checks the order *hide - accept - close* and that no such window is left. **What I cannot see:** whether the window flickers for a moment before it is hidden (GTK shows it, my code hides it at the next opportunity, a few milliseconds). Tell me.
3. **Stepped Refine - no density around the refined residues.** Your screenshot shows it clearly: contours only around the *previous* position (lower right), none around the residue in focus (upper left). What I found in the code: "go to the next residue" (`set_go_to_atom_chain_residue_atom_name_full`) only moves the view and redraws; nothing re-contours the maps (that happens when you drag the view with the mouse or change the contour level, which is why changing the level repaired it). **A point I cannot explain:** in your reports on builds 9-12 the density *did* follow during Stepped Refine. In my headless probe neither the old path (build 12) nor the new one re-contours the maps by itself, so I do not know what re-contoured them in the old path on your machine; my guess (a guess, not a finding) is that the old "immediate replacement" path did something the ordinary refinement of build 13 does not. The fix does not depend on that guess: `update_maps()` now runs after every move to the next residue. The test counts the maps' re-contouring events (`COOT_DEBUG_MAPS=1` prints each with its centre) during a two-residue Stepped Refine: none without the call, one per residue with it, each centred within 1 A of the residue's C-alpha. **On screen: not verified** (I cannot look at a drawing). Not touched: symmetry atoms and the skeleton are updated by a different call; if you use "Show Symmetry" during Stepped Refine and see them lag, tell me.
4. **RCrane launch did nothing - not reproduced; the entry is replaced by a menu that exists from the start.** The log of your session contains no RCrane line and no traceback, so the click either did not reach my code or ended silently; in the headless test the same call creates the menu with its 6 entries (all 20 RCrane checks passed). I could not find why it differs on your screen. So I removed the step that could fail silently: **Calculate > RCrane** is now a sub-menu with the 6 entries (New trace 5'->3'..., New trace 3'->5'..., Extend chain..., Rotamerize existing structure..., Rotamerize without density..., About RCrane...) **built at start-up**. Every entry writes a line to the terminal / log when used (`INFO:: RCrane: "New trace 5'->3'" selected`), the pre-launch check (Coot version, monomer library) runs the first time an entry is used and says so when it fails, and an exception in any RCrane handler is printed with its traceback and shown in a message window. At start-up the log has `INFO:: RCrane: menu "Calculate > RCrane" is ready (6 entries)`. **If you still do not see the sub-menu or nothing happens when you use an entry, please send the lines of the log that contain "RCrane"** (`./collect-results.sh` does that): with the new lines I can tell which of the two it is. The new tests: the sub-menu is in the Calculate menu with its 6 entries, the check runs once, a failing check blocks the entry, a failing handler is printed (not lost).
5. **Your question: why is Scheme scripting "not supported"?** It is supported; what is not supported is Scheme *GUI* code. Calculate > Scripting > **Scheme...** opens a plain Scheme window (you used it: `(set-graphics-window-size 600 800)` worked), `--script file.scm`, `~/.coot` Scheme start-up files and the 27 Scheme files of Coot's own library work (tests `scheme-api` 27, `bundle-scheme` 6, `rdkit-scheme` 3, `process-helpers` 10 run on Guile 3.0.10 inside the program). The line in your log - *COOT_SCHEME_DIR was defined ... but loading of scripting window scheme code failed. Nevertheless you will get a simple scripting window* - is Coot telling you that the *rich* Scheme console (the one from `(coot-gui)` with history and completion buttons) could not be loaded, and that it falls back to the plain one. The reason: Coot 0.9's Scheme GUI code (105 functions in 27 `.scm` files: dialogs, sliders, the rich console) is written for **guile-gtk**, an old binding between Guile 1.x and GTK 2 (`USE_GUILE_GTK`). I know of no guile-gtk for Guile 3 on macOS, and this build uses Guile 3. The menus, dialogs and sliders you use are therefore provided by Coot's **Python** scripts (on a replacement for PyGTK 2 that I wrote, `compat/pygtk2`), and for the few places where the C++ program asks for a Scheme GUI function (Run Refmac, the GLN/ASN B-factor window) there is a bridge to the Python version (`scheme/python-gui-bridge.scm`). **This is a gap against what you decided at the start** (3 Nov: keep Scheme *including* the GUI scripts, plus Python; and you left the order to me). My order was: bundle first, then the Python GUI layer (done in build 7), then a Guile GUI layer. The third step is **not started**; it is owed, not dropped. What it would be: a binding of Guile 3 to GTK 2 that offers the guile-gtk function names the 27 `.scm` files call (105 distinct functions; my earlier count said 23 of them cover 80% of the roughly 2,200 call sites), plus the C++ glue that registers them (one file in the upstream design). It is a real piece of work (a second layer next to the PyGTK one, a rebuild of `coot-bin`, and tests that drive every Scheme dialog), but it is not blocked by anything I know of. I have not checked how upstream's own current packages deal with this. **Tell me if you want it as the next item**; until then every menu entry and dialog you can reach in this build is the Python version, and Scheme scripts that only compute (no windows) run unchanged.
6. **Your question: is there a change log?** Until now there was none as a single file; the records were spread over `README-m0.txt` (technical notes of every round, in the source tarball), the protocol (this file: your-facing explanation, newest round on top), the numbered patch series (33 patches) and the evidence files. **`CHANGELOG.md` in the folder is new** and lists builds 1-14 in one place, with what is verified and what only your screen can show; it will be extended with every build.

**New tests** (fail on build 13, pass on build 14; `evidence/checks_b13_vs_b14.txt`): `gui-dialogs` 44 (accept window, maps re-contoured, occupancy slider OK, swap alt confs, no list>number comparison, RCrane sub-menu), `gui-rcrane` 21 (RCrane entry guard). The other 16 suites are unchanged.
**What no test can show:** the Stepped Refine screen (items 2 and 3), the new RCrane sub-menu on your screen. Those are the checks below.

## V. Round 14 checks (about 15 minutes; the RCrane windows U6-U8 of round 13 are still open)

| # | Do | Expected |
|---|---|---|
| V1 | Toolbar button **Change Alt Conf Occ** (right-click the toolbar > Manage Buttons if it is not there), click an atom of a residue with exactly two alt confs; move the slider; press **OK**. Look at the occupancies (Measures > Residue Info..., or Label). | The window closes; the two conformers have occupancy x and 1-x (x = the slider value); the terminal shows `BL INFO:: setting new occupancy ...` and no TypeError. |
| V2 | Calculate > **All Molecule...** > **Stepped Refine...**, 5-10 residues, refinement map set (as U3). | For each residue the refinement style is visible, **no "Accept Refinement?" window appears** (not even for a moment, tell me if it flickers), and **the density is contoured around the residue being refined** (the map follows the focus without touching the contour level). Stop still works. |
| V3 | Calculate menu: is there an entry **RCrane** with a sub-menu of 6 entries? Open **About RCrane...**; then (with `test-data/1ehz.pdb`, its map, refinement map set) **Rotamerize existing structure...** (U6-U8 of round 13). | The sub-menu; the terminal/log shows `INFO:: RCrane: "..." selected` for each use. If nothing happens: send the log lines containing "RCrane". |
| V4 | Calculate > **Scripting** > **Scheme...**: type `(+ 1 2)` and `(graphics-n-molecules)`. | 3 and a number. The log line about the "simple scripting window" is expected, not an error. |
| V5 | MacBook: `xattr -dr com.apple.quarantine "<folder>"`, then `./tests/run-headless-tests.sh` (about 20-25 min), paste the lines (section A). | 18 lines, each `N / N`. |
| V6 | Quit with File > Exit; run `./collect-results.sh` and tell me. | I look for `Traceback`, `ERROR::` and `Unbound variable`. |

---

# Earlier round, still valid (U5-U9 are still open): Coot 0.9.8.96 on Apple Silicon: test round 13 (build 13 = build 12 + answers to your round-12 report)

**From your report on build 12** (thank you: Ca Zone -> Mainchain, the ligand metric sliders, the refmac message, the four sphere buttons and the splash are confirmed; the sharpening and clipping sliders and Place Helix Here work): your to-do list, answered in order. The MacBook file you attached shows the **build 11 folder** (it prints "No reference-structures"): the 15 suites of that folder that print a result line all pass on the M2 Pro (the 16th, `ondemand-make`, prints none by design), which is good news, but build 13 still has to be run there once.

1. **Python scripting window.** It was fixed in build 12 (the code returns `gtk.FALSE`, which the replacement lacked); the log of your iMac session shows no use of it, so it is probably not yet tested. Note how it works upstream: `print(2+2)` writes to the *Terminal*, only the *value of an expression* (`2+2`, `graphics_n_molecules()`) appears in the window. Check T8 again, please.
2. **Where the sliders are.** *Interactive Nudge Residues*: Calculate > **Modules...** > **Cryo-EM** (a menu **Cryo-EM** appears) > **Interactive Nudge Residues...**; it needs a residue at the screen centre. *Occupancy slider*: it is the optional toolbar button **Change Alt Conf Occ** (right-click the toolbar > Manage Buttons > Refinement group); click it, then click an atom of a residue that has exactly two alternative conformations. I did not add it to the default buttons (say so if you want it there with the four sphere buttons). Two more sliders exist only as Python functions without a menu entry: `nudge_screen_centre_extra_gui()` and `map_sharpening_gui()` (you used the sharpening slider, so you have found it already).
3. **Fit Loop by Database Search: you were right, it did not work.** Cause: the loop picker hands Python a 7-element atom spec (`[model-number, imol, chain, resno, ins, atom, alt]`) and `atom_spec_to_residue_spec` in `coot_utils.py` only knew 6 elements, so it returned `None` and the database search received `[None, None]` (your log: "no specs in object", then a `SystemError`). Second fault in the same code: the candidate buttons all showed the *last* loop (a late-bound variable). Both are fixed and a test now drives the whole dialog (pick two atoms -> "Loop Candidates" window with the original loop, "Toggle All Candidate Loops" and one button per candidate). **I kept the menu item** because the cause was small; if you still prefer to remove it, it is one line (`extensions.py` / the C++ menu entry) - tell me.
4. **Place Helix Here** works (your report): nothing to do.
5. **Stepped Refine had no refinement style.** In 0.9.8.96 a refinement that must be accepted automatically (`refinement_immediate_replacement`) blocks the main thread until it is finished and never draws the moving atoms, which is where the thick grey-yellow "refinement style" bonds come from. Stepped Refine used exactly that. It now starts an ordinary (non-immediate) refinement per residue, keeps the GTK main loop running for 0.6 s so that the moving atoms are drawn in the refinement style, and then accepts. Change the time with `COOT_STEPPED_REFINE_SHOW=<seconds>` (0 = the old, invisible way). Stop in the dialog still works (it interrupts the wait). **Please check it on screen** (T3): possible side effects are a flicker of the accept/reject dialog and a slower run (0.6 s per residue).
6. **RCrane - I made it work, and it is on again (Calculate > RCrane launch).** What was wrong, in the order I met it: (a) the review window needs a list view (`gtk.TreeView`, `TreeViewColumn`, `TreeSelection`, cell renderers with colour properties, `ListStore` with GType names, `Style.bg`): added to the PyGTK replacement (a new `gtk2compat` test case); (b) `linearInterp.py` compared a number with text (Python 2 allowed it, so it never fired); (c) `Accept` raised `KeyError: 'OP3'` for a 5' terminal OP3 (PDB 1EHZ has one; upstream has the same fault); (d) *Previous Nt* of a 5'->3' trace raised an IndexError in upstream too (off by one) and left the trace inconsistent; (e) **some refinements never ended** - the minimiser neither converges nor fails (start geometries with a 5.5 A P-O5' bond), the main thread waits for it, Coot freezes. That one needed a change in the C++ program (`graphics-info-modelling.cc`): a refinement that is driven by a script (or has no window) is now stopped after `COOT_REFINE_MAX_SECONDS` (default 10 s, 0 = no limit) with a line "WARNING:: refinement stopped after ... seconds". Interactive refinement (you can press Esc / Return) is not limited. So **build 13 contains a rebuilt `bin/coot-bin`** (same sources, same libraries, same flags; the only code difference is that limit). The 18 suites below run on it.
   What the new test `gui-rcrane` does with tRNA **1EHZ** (test-data/1ehz.pdb, its 2mFo-DFc map 1ehz_map.mtz): opens RCrane from the menu; Rotamerize existing structure (click 2 nucleotides) -> review window (52 conformers in a list, overview of the suites) -> Next/Previous Conformer, Next/Previous Suite, Accept; Rotamerize without density -> Restore Original Coordinates (coordinates identical) and -> Accept; New trace 5'->3' and 3'->5' (starting phosphate, Next/Previous, Accept, Accept Nt, Next/Previous Phos and C1', Anti/Syn Flip, Previous Nt, Manually Adjust dialog, Build Backbone, Done); Extend chain (delete nucleotides 21-76, click 20, build 3 nucleotides). Rotamerizing nucleotides 3-6 of 1EHZ with the default conformers and accepting moved the 1652 atoms by 0.02 A on average (0.26 A mean over nucleotides 2-7, 1.19 A at most): RCrane reproduces the deposited RNA (`ROUND-TRIP` line in `evidence/rcrane_headless_b13.txt`). In that test run 8 refinements hit the 10 s limit; they are the reason why a rotamerize/trace step sometimes takes 10 s longer.
   **What I could not test, and you should look at:** how the windows look (the list sizes are computed from font metrics), the colours of the cells, a mouse click on a column of the overview strip (the list must be on screen), and the three sliders of "Manually Adjust" (they need the screen vectors of a real drawing area). **Quality of the trace:** I did not change RCrane's scoring. On the 1EHZ map the geometric terms favour the true next phosphate, but the density term (weight 15 on the logarithm of the summed density) is so strong that the true phosphate was the top candidate in only 1 of 9 steps (it was within the first ten in 8 of 9). So with "New trace" you will use **Next Phos / Previous Phos** often; I do not know if that is different in Coot 0.8, where RCrane was written. Your RNA is the judge; if RCrane stays unusable for you it can be switched off with `COOT_DISABLE_RCRANE=1` or removed.

**New tests** (fail on build 12, pass on build 13): `gui-dialogs` 39 (stepped-refine display, Stop, `seconds=0`, Fit Loop by Database Search end-to-end), `gtk2compat` 12 (`tree_views`), `gui-rcrane` 20 (new). Evidence: `evidence/checks_b12_vs_b13.txt`, `evidence/rcrane_headless_b13.txt`, `evidence/refinement_stall_b12_vs_b13.txt`.
**What no test can show:** the refinement style while Stepped Refine runs, the look of the RCrane windows. Those are your checks below.

## U. Round 13 checks (about 20 minutes)

| # | Do | Expected |
|---|---|---|
| U1 | Calculate > **Scripting** > **Python...**: type `2+2`, then `graphics_n_molecules()`, then `1/0` (and `print(2+2)`, which goes to the Terminal). | 4, a number and an error message in the window. |
| U2 | Load your model and map. Calculate > **Fit Loop** > **Fit Loop by Database Search...**, click two C-alpha atoms about 6-8 residues apart (a gap that has a few residues between them). | A window "Loop Candidates" with "Original loop", "Toggle All Candidate Loops" and one button per candidate; each candidate button shows *its* loop. (If the database finds no loop for your gap you get the message that it found none: try another gap.) |
| U3 | Calculate > **All Molecule...** > **Stepped Refine...**, a range of 5-10 residues, refinement map set. | For each residue the **refinement style** (thick grey-yellow bonds and balls of the moving atoms) is visible for about half a second before the residue is accepted; the residues move; Stop interrupts. Tell me if the accept dialog flickers or it feels too slow/fast (`COOT_STEPPED_REFINE_SHOW=1.2` or `0.3` before `./run-coot.sh`). |
| U4 | Calculate > **Modules...** > **Cryo-EM** > **Interactive Nudge Residues...** (residue at the centre) and the toolbar button **Change Alt Conf Occ** (Manage Buttons) on a residue with two alt confs. | The two sliders you asked about; both move something. |
| U5 | File > Open Coordinates `test-data/1ehz.pdb`; File > Open MTZ (or Auto-open) `test-data/1ehz_map.mtz` (columns FWT / PHWT); make it the refinement map. Calculate > **RCrane launch**. | A new top-level menu **RCrane** with 6 entries. About RCrane... shows the logo and the licence. |
| U6 | RCrane > **Rotamerize existing structure...**: click an atom of nucleotide 10, then an atom of nucleotide 13. | After a few seconds the RCrane window: an *Overview* strip (one column per suite, coloured red/orange/yellow where RCrane is unsure), a **list of conformers** (Rank, Conformer, Score, Leading and Ending Pucker; the selected row highlighted), the buttons Previous/Next Conformer, Previous/Next Suite, "Display old coordinates", "Accept New Coordinates", "Restore Original Coordinates". The window must show the whole list without being cut off. |
| U7 | In that window: Next Conformer a few times (each takes a second or two), Next Suite, click a column of the overview, tick/untick "Display old coordinates", then **Accept New Coordinates**. | The structure follows; accepting leaves a RNA close to where it was (this is a good model). Restore Original Coordinates gives the original back. If Coot stops answering for more than ~15 s tell me (the limit should prevent that). |
| U8 | RCrane > **New trace 5'->3'...** with the 1EHZ map; centre on a phosphate of the stem (e.g. nucleotide 10) first. Accept the starting phosphate, then **Accept Nt** a few times; use **Next Phos** if the highlighted phosphate is wrong; **Build Backbone**; **Done**. | A new molecule "RCrane-molecule-1" with the traced nucleotides; the windows must fit on the screen. |
| U9 | MacBook: `xattr -dr com.apple.quarantine "<folder>"`, then `./tests/run-headless-tests.sh` (about 20-25 min) and paste the lines (section A). | 18 lines, each `N / N`. |
| U10 | Quit with File > Exit; run `./collect-results.sh` and tell me. | I look for `Traceback`, `ERROR::` and `Unbound variable`. |

---

# Earlier round, still valid: Coot 0.9.8.96 on Apple Silicon: test round 12 (build 12 = build 11 + fixes for your round-11 report)

**From your report on build 11** (thank you: Glyco, the outliers window and Run Refmac are confirmed; the trackpad double-click as middle-click works): six items from your report (items 1-6; the splash is your request, the MacBook result I could not use) and four more that I found while looking for their causes (items 7-10).

1. **Ca Zone -> Mainchain: "COOT_REF_STRUCTS is not defined".** Coot builds the main chain by matching your C-alpha trace against 28 reference structures (`reference-structures/*.pdb`). The 0.9.8.96 release tarball does not contain them (Coot's git repository does), so every click ended with that message. Build 12 ships them in `share/coot/reference-structures` (10.8 MB, taken from github.com/pemsley/coot, each file checked against its git checksum; list and checksums in `SOURCE.txt` there) and `run-coot.sh` points `COOT_REF_STRUCTS` at them; the start-up warning "No reference-structures found" is gone. **One click is enough in this version:** a click on any C-alpha of the trace builds the whole connected fragment forwards and backwards (two new molecules, "mainchain-forwards" and "mainchain-backwards"). The terminal text "click on 2 atoms" is an old message that upstream never updated; the program does not wait for a second click.
2. **Ligand Metric Sliders: `NameError: name 'imol_map' is not defined`.** The error was in the code that reports a problem; the problem itself is that the refinement map was the EDS map of 8G4N/8G4O (`coot-download/..._map.mtz`), which holds map coefficients only. The sliders need the MTZ with the **observed** F, sigF and R-free flags (refmac5 is run on it). Now: no exception, and a window says which file was looked at and what is missing (also for a map that was read from a `.map` file). With your own MTZ it works as before. While in there: Phenix MTZ files list `SIGI-obs` before `SIGF-obs-filtered`, and the code took the first sigma column; it now takes the one that belongs to F (the density correlation of A 301 changes from 0.689 to 0.729 because refmac now gets the right sigmas). The slider window stays: it is not dropped from the menu.
3. **Run Refmac printed "environment variable ... not set !".** Those lines were a leftover diagnostic that looked at Coot's own environment, where CCP4's variables are deliberately absent (they go to refmac5 only). The log now shows the environment refmac5 actually gets (`INFO: environment for refmac5: SYMINFO=..., CLIBD=..., CCP4=...`).
4. **Sphere Refine, Sphere Refine +, Sphere Regularization and Sphere Regularization + are on the toolbar from the first start.** They were optional buttons (right-click the toolbar > Manage Buttons). The first start in the private home writes them into `home/.coot-preferences/coot_toolbuttons.py`; "Remove a Button" is permanent (a marker file keeps them from coming back), "Manage Buttons" brings one back. Also fixed: removing "Sphere Refine" used to delete the line of "Sphere Refine +" too. I ran all four on the tutorial model: each moves the residues around the centred residue (the "+" versions also the neighbours in sequence).
5. **Splash screen.** New tagline "Good to see you, Old Coot" (capitalised like the old one; say if you want it in lower case). GTK 2 draws one picture pixel as one point, so on a Retina screen the old picture was enlarged 2x and looked soft. A small helper, `bin/coot-splash` (AppKit only, 75 KB), now shows a **1160 x 956 pixel picture at 580 x 478 points**, i.e. every pixel is a screen pixel, and closes when Coot's main window is up. The painting itself only has 580 x 478 pixels of detail: the picture is a clean 2x enlargement, and the three lines of lettering are redrawn crisp. A bigger original of the artwork would give a sharper result (`tools/make_splash.py`). If the helper does not work for you: `COOT_NO_SPLASH=1 ./run-coot.sh` uses Coot's own window with the new text.
6. **MacBook test results.** Every suite file in the zip you attached contains only the launcher's refusal: the folder was in `~/Downloads` and still had the macOS download-quarantine flag, so nothing ran (it is the same for the audit and for Coot itself). Run `xattr -dr com.apple.quarantine "<path of the folder>"` once; `./tests/run-headless-tests.sh` now says so in one clear message instead of printing empty lines, and `collect-results.sh` reports the flag.

**Found while looking (not reported by you):**

7. **The Python scripting window (Calculate > Scripting > Python...) showed no result for anything you typed.** The code returns `gtk.FALSE`, which my PyGTK replacement lacked. Fixed; typing `1+1`, a Coot function, or an error now shows the answer.
8. **Sliders that move something did nothing.** PyGTK gives `gtk.Adjustment` the attributes `value`, `lower`, `upper`, ... The replacement had none, so every move of the zoom/clipping slider (Nudge Screen Centre with Extras), the map-sharpening slider, the occupancy slider (Change Alt Conf Occ) and the Interactive Nudge Residues slider raised an AttributeError. Fixed (`value`, `lower`, `upper`, `step_increment`, `page_increment`, `page_size`).
9. **About 95 menu items had never been swept.** The menus Glyco, CCP4, Cryo-EM, Restraints, Refine, PDBe, ProSMART, SHELX and RCrane only exist after their entry under Calculate > Modules... (or "RCrane launch") has been used, and my headless sweep only knew the menus present at start-up. It now creates them first (252 entries instead of ~160). Three faults came out: **Restraints > Generate Local Self Restraints 6** built a malformed residue list (SystemError); **Cryo-EM > Multi-sharpen using Refmac...** raised a TypeError when refmac5 is not found (now says so); and the RCrane items below.
10. **RCrane is switched off in this build.** "About RCrane..." failed (no `gtk.AboutDialog`; added), and then "New trace" stops at its start with `'<=' not supported between instances of 'float' and 'str'`: RCrane's Python 2 code compares numbers with text (and the review window needs a TreeView that the replacement does not have yet). A real fix needs a careful port with RNA data to compare against, and I would rather hide the entry than give you a menu that fails. `COOT_ENABLE_RCRANE=1 ./run-coot.sh` brings "Calculate > RCrane launch" back for anyone who wants to help port it. Tell me if you use RCrane: it becomes the next item.

**New tests** (they fail on build 11, pass on build 12): `data-and-maps` (reference structures present; `db_mainchain` on a C-alpha-only fragment builds N, CA, C, O); `gui-glyco` (metric sliders with a `.map` map and with a map-coefficient MTZ give the explanation; the sigma chosen for F; the MTZ finder); `refmac-run` (no "not set !", environment shown); `gui-toolbar` (new suite: installation, the buttons Coot's preference script creates, the four clicks, exact removal, permanence); `gui-dialogs` (scripting window, Adjustment members, zoom/clipping, sharpening and nudge sliders, the new widget classes); `bundle-python` (splash pictures and helper: it loads the 2x picture, draws it into a 1160 x 956 bitmap and writes it back; links only system libraries); the menu sweep covers the dynamically created menus.
**What no test can show** (nothing can be drawn without a screen): that the splash window appears, is centred, looks sharp and goes away at the right moment; where the four buttons sit on your toolbar; how the sliders window looks. Those are your checks below.

## T. Round 12 checks (about 15 minutes)

| # | Do | Expected |
|---|---|---|
| T1 | `./run-coot.sh --retina` from Terminal. | A picture of the coot (580 x 478 points, centred) is visible during the start, sharper than before (look at the letters of "Version 0.9.8.96" and of "Good to see you, Old Coot" with your eyes close to the screen), and goes away when the main window has opened. Tell me if it never appears, stays, flickers, or sits in the wrong place. |
| T2 | In the first lines of the terminal. | No line "WARNING:: No reference-structures found". Then the main toolbar (top) ends with **Sphere Refine, Sphere Refine +, Sphere Regularization, Sphere Regularization +**. |
| T3 | Edit > **Copy Fragment...**, molecule = your model, selection `//A/10-40/CA`. Calculate > **Model/Fit/Refine...** > **Ca Zone -> Mainchain**, click **one** C-alpha of the new C-alpha-only molecule. | After a few seconds two new molecules, mainchain-forwards and mainchain-backwards, with N, C, O and CB added; no "COOT_REF_STRUCTS" message. (One reference file prints an "ERROR 42 READ ... Duplicate sequence number" line; that is in the reference data and harmless.) |
| T4 | Centre on a residue (Go To Atom) and press each of the four new toolbar buttons (undo with Edit > Undo if you wish). | Sphere Refine / Sphere Regularization: the residues within 4.5 A of the centred one are refined / regularized (accept or reject in the dialog); the "+" versions also take one residue before and after each of them. |
| T5 | Right-click the toolbar > **Remove a Button**, type `Sphere Refine +` and press **Remove**. Quit and start again. | The button is gone and stays gone; "Sphere Refine" is still there. (Manage Buttons can bring it back.) |
| T6 | Make the map of **your own data** the refinement map; centre on A 301; Ligand > **Ligand Metric Sliders**. Then make one of the EDS maps (8G4N) the refinement map and try again. | First: the slider window (needs CCP4 for refmac5). Second: a dialog that explains that the observed F, sigF and R-free are needed, naming the file that was tried; no traceback in the terminal. |
| T7 | Calculate > **Run Refmac...**, 1 cycle. | No "not set !" lines; one line "INFO: environment for refmac5: ..." |
| T8 | Calculate > **Scripting** > **Python...**: type `print(2+2)`, then `graphics_n_molecules()`, then `1/0`. | 4, a number, and an error message in the window. |
| T9 | Calculate > **Modules...** > **Cryo-EM** (a menu Cryo-EM appears) > **Interactive Nudge Residues...** with a residue at the centre; move the slider. | A new molecule with the nudged residues appears for each position of the slider. |
| T10 | Calculate > **Model/Fit/Refine...** > **Fit Loop** and Place Helix Here (as S7 in the old table below; you have not tried them yet). | See S7. |
| T11 | MacBook: `xattr -dr com.apple.quarantine "<folder>"`, then `./tests/run-headless-tests.sh` and paste the lines (section A). | (superseded by U9: 18 lines in build 13.) |
| T12 | Quit with File > Exit; run `./collect-results.sh` and tell me. | I look for `Traceback`, `ERROR::` and `Unbound variable`. |

---

# Earlier round, still valid: Coot 0.9.8.96 on Apple Silicon: test round 11 (build 11 = build 10 + fixes for your round-10 report)

**From your report on build 10:** Go to next ligand no longer breaks middle-click, the ligand atom letters are readable and Stepped Refine works; thank you. You then found two problems (the Glyco module and the Ligand Metric Sliders). Looking for their causes turned up three more things of the same kind, so build 11 fixes five groups of problems. **Only the Python and Scheme scripts and data files changed: the program file `bin/coot-bin` and all libraries are byte-for-byte the ones of build 10** (this is why the display, picking and refinement you checked cannot have changed).

1. **Glyco: "missing template files".** The folder `share/coot` was incomplete. A normal `make install` of Coot copies about 40 files into it from other source directories (the `pdb-templates` folder with the link templates `link-by-torsion-to-...tab`, `*-decorations.tab`, `ASN-NAG-via-NAG-ASN.pdb`; the protein database `protein_db/protein.db`; the Cootaneer table; the Nautilus library; the Zo Ramachandran tables, which sat in the wrong sub-folder; the ligand database `ligands-2016.db`; the side-chain grid file; fonts) and my package builder did not. Adding the first NAG to an ASN printed `ERROR:: file not found ...link-by-torsion-to-pyranose-core-NAG-ASN.tab` and added nothing. They are all in now (about 10 MB). The same missing files would have stopped **Fit Loop by database search**, **Cootaneer / assign sequence from the map**, **Nautilus**, **Place Helix Here** and the Ligand Metric Sliders percentiles. (One set is still missing, the `reference-structures` used by *Ca to Mainchain*; that entry stays a known gap, see the end.)
   Once the files were there, four more faults in the Glyco code itself showed up and are fixed: (a) the "N-linked Glycan Addition" dialog enables only the buttons that make sense for the residue at the screen centre, and that code iterated over a `gtk.Table`, which my PyGTK replacement could not do (`TypeError: 'Table' object is not iterable` on every move of the centre); (b) the C++ call `add_linked_residue` returns the new residue only when "fit and refine for link addition" is on, and the dialog switches that off, so a NAG added from the dialog was never given its extra restraints or refined, and **"N-link add NAG, NAG, BMA" and every tree builder (High Mannose, Hybrid, Complex) stopped after the first sugar**; (c) the branch that deletes a badly fitting residue again called `delete_residue_by_spec` with the wrong arguments (this bug is in the original script, it ends the whole tree); (d) the dialog now leaves "fit and refine" on afterwards.
2. **Ligand Metric Sliders: `TypeError: a bytes-like object is required, not 'str'`.** The error was in `popen_command` of `coot_utils.py`, the helper that starts an external program (here refmac5, to compute the density correlation of the ligand) and sends it lines of text. In Python 2 a pipe takes text; in Python 3 it takes bytes unless it is opened in text mode, and the script was never converted. It is also the helper of acedrg, libcheck, probe, reduce, prosmart, mapman, ... so all of them were affected; it is fixed (text mode) together with its sibling `run_concurrently`, which also never closed the program's input. Two more Python 3 slips followed in the same flow and are fixed: `write_reduce_het_dict` (the "bad contacts" count: a binary file copied into a text file) and the colour bars of the sliders window (a `str` of `chr()` values was passed as a pixel buffer: the gradient would have been drawn with garbage colours; the same slip was in the PDBe validation sliders).
   **refmac5 needs CCP4's environment variables.** Started from a plain shell it stops with `Cannot open environ.def`. Coot now hands CCP4's variables (CCP4, CINCL, CLIBD, CCP4_SCR, ...) **to the programs it starts and to nothing else** (exporting `CCP4`/`CLIB` into Coot itself changes where Coot looks for its dictionaries). The launcher finds the CCP4 folder from `CCP4`, from refmac5 in `PATH`, or in `/Applications/ccp4-*` and prints `CCP4 for child programs: ...`.
3. **Calculate > Run Refmac did nothing visible (found while testing the above).** With Guile compiled in, Coot's C++ asks the *Scheme* function `run-refmac-by-filename`, which starts refmac and then waits with `gtk-timeout-add`, a procedure of guile-gtk that this port does not have; so refmac ran (in the old build: stopped at `Cannot open environ.def`) and the result was never read in. The Scheme function now forwards to the Python runner (new file `scheme/python-gui-bridge.scm`), which polls with a GLib timer. I also had to fix the Python runner itself: it always sent `FREE=` with an empty label to refmac (it dropped the R-free column and tested `[] != ""`, which is always true) and it assumed the toolbar was not empty.
4. **Validate > GLN and ASN B-factor Outliers** had the same kind of problem (C++ asked for a Scheme GUI function that does not exist here); the bridge hands it to the Python window.
5. **Other Python 3 slips found by scanning every script** (they were not reported but each is a menu item that would have failed): `getiterator()` (removed in Python 3.9) in the PISA parser and the Wikipedia drug lookup; `_thread.start()` on a variable in "Recent PDBe structures"; `str + bytes` in the C-beta deviant buttons (two scripts); a `loop_len/2` that is a float in Python 3 (Fit Loop by DB search for loops of 6 or more residues); downloaded bytes used as text in the update check and the news line.

**New tests** (all fail on build 10, pass on build 11): `data-and-maps` now has 30 checks (templates present, NAG added, dialog flow, N-link add, tree builder incl. the bad-fit branch, Fit Loop by Database Search, Place Helix Here, `popen_command`, `run_concurrently`, CCP4 environment, reduce dictionary, no known Python 2 leftovers); new suites `gui-glyco` (the dialog logic, its button states, the Glyco menu, the colour-bar drawing code with a stand-in window) and `refmac-run` (the Scheme bridge, and a real refmac5 run from Scheme to new model and maps, with and without an R-free column).
**What no test can show** (nothing can be drawn without a screen): that the Glyco dialog looks right, that the sliders window is drawn correctly, and what refmac5's own graphs (logview) look like. Those are your checks below.

## S. Round 11 checks (about 15 minutes)

Start `./run-coot.sh --retina`, load your model and map (your own data is fine).

| # | Do | Expected |
|---|---|---|
| S1 | Calculate > **Modules...** > **Carbohydrate** (a new menu **Glyco** appears). Centre on an ASN (Go To Atom, e.g. A 42, atom CA). Glyco > **N-linked Glycan Addition...** and press **Add a NAG-ASN NAG**. | A NAG appears next to the ASN (new residue number after your last one) and is refined; no "missing template" message in the window or the terminal. **If a message still appears, paste its text** (the first report I had did not contain it). |
| S2 | In that dialog the buttons should follow the centre: centred on the new NAG only **Add a BETA1-4 NAG** is enabled (under *High Mannose*); add it, then **Add a BETA1-4 BMA**. Close the dialog. | Each press adds one residue next to the right atom of the previous one. |
| S3 | Glyco > **Delete All Carbohydrate**, centre on an ASN again, Glyco > **N-link add NAG, NAG, BMA**. | Three residues appear (this used to stop after one). A tree (Glyco > Add High Mannose ...) on a real glycosylated ASN with density builds as far as the density supports it: a sugar whose density correlation is below 0.5 (or that clashes with a symmetry mate) is removed again by design. |
| S4 | **Ligand Metric Sliders**: centre on a ligand (A 301 PEG) and use Ligand > **Ligand Metric Sliders**. Needs CCP4 (refmac5); reduce and probe are used for the bad-contacts line (from CCP4 or Phenix; the launcher looks in `PATH` and in `/Applications/ccp4-*/bin`). | A window "Ligand Validation Report" with four bars with a colour gradient (red to blue) and a black marker each, and the values on the right. With your own data, the terminal printed density correlation 0.69 and a percentile near 9 in my headless run. If the window is blank or the colours look like noise, tell me. |
| S5 | Calculate > **Run Refmac...**: pick the model, the MTZ and the columns, 5 cycles, run. | A **Kill refmac** button appears in the toolbar and the status bar says "Running refmac"; after about 10-60 s "Refmac finished": a new model and new maps are loaded; the log is in `coot-refmac/`. (refmac 5.8.0431 needs ~9 s for 1 cycle on your own data.) |
| S6 | Validate > **GLN and ASN B-factor Outliers** > your molecule. | A window with a list (or the message that there are none). |
| S7 | Calculate > **Fit Loop** > **Fit Loop by Database Search...**: choose the model, a chain and a stretch of 3-7 residues of the protein (the residues may be in place: Coot rebuilds them; give the first and last residue number), OK. Then Calculate > **Other Modelling Tools...** > **Place Helix Here** (centre on some density first). | Loop candidates are built with buttons "Loop A / Loop B"; the helix is placed in the density. (They need `protein_db/protein.db` and `theor-helix-70.pdb`, both missing in build 10.) Tell me what happens, including if nothing does. |
| S8 | Quit with File > Exit; run `./collect-results.sh` and send the result. | I look for `Traceback`, `ERROR::` and `Unbound variable` lines. |

**From your report on build 9:** the density now follows the centre during Stepped Refine, and middle-click picking works (except right after "Go to next ligand"). Three problems remained. I found a cause for each in the code; none of them can be tried on a screen on my side, so section R asks you to confirm.

1. **Stop button on the toolbar did nothing, and no Continue button appeared.** "Stepped Refine..." is the one that runs residue by residue from Coot's idle loop (the other "Stepped Refine" function I tested earlier is not what the menu calls). Its Stop / Continue / Cancel buttons store their action as a string, and my Python 3 port of the scripts had turned Python 2's `types.StringType` into `bytes`, so every such string was rejected with "cannot evaluate or call function". Fixed in `coot_gui.py` (the toolbar-button and the combo-box helper) and in four other places with the same slip (button names and tooltips in `dialog_box_of_buttons`, chain skipping in the NCS tools, the value text of the two validation-slider windows). New tests: a string callback runs; Stop makes **Cancel** and **Continue** appear; Cancel removes them; no `bytes` type tests remain in the scripts. (The tests fail on build 9 and pass on build 10.) How it behaves: Stop greys the Stop button at once, the residue being refined finishes (a second or two), the loop pauses; **Continue** resumes with the next residue, **Cancel** ends it and removes the buttons.
2. **Middle-click fails after "Go to next ligand" until you use Go To Atom.** Cause (found by reading the code; I cannot watch the screen): my label drawing code (added in an earlier build) switches OpenGL to the model-view matrix when it is done. The ligand view in the lower-left corner is drawn in the projection matrix and expects to pop that stack afterwards; it popped the wrong one, so the picture of each frame was fine but the projection left behind was the identity matrix, and picking (which read whatever the last frame left) could not find any atom. The same thing happened for a moment whenever the density-level text was shown. Go To Atom on a normal residue switches the ligand view off, which is why it cured it. Fixes: the label routine now restores the caller's matrix mode; the ligand view sets the mode explicitly; and **picking no longer depends on the leftover state at all**, it uses the scene's own matrices captured when the scene is drawn. If any drawing routine ever leaves an extra matrix on a stack, the next frame removes it and prints `WARNING:: GL ... stack depth` once in the log (tell me if you see it).
3. **Ligand label at the lower left illegible (pink blobs).** Cause: the ligand picture is stored as an OpenGL display list and my text routine was called while the list was being recorded; it asks OpenGL for the current text position, colour and viewport, and those answers are not recorded, so the letters came out at old positions in the colour of the rotation-centre cube (pink). The labels are now collected and drawn each frame in immediate mode, in the colour of the element.

## R. Round 10 checks (already confirmed by you on build 10; keep for regression)

Start `./run-coot.sh --retina`, load your model and map.

| # | Do | Expected |
|---|---|---|
| R1 | Click the toolbar button **Go to next ligand** (or Ctrl+L), then middle-click atoms of the protein near it **without** using Go To Atom. | Each click re-centres. The line printed for the pick ends with the ray distance, mostly below 0.25. |
| R2 | Look at the lower-left corner while the ligand (PGE, for example) is centred. | A flat drawing with readable atom letters (O, N, ...), coloured by element. Tell me if the letters are too small or too large (`COOT_LABEL_SCALE=2 ./run-coot.sh ...` makes all scene text larger). |
| R3 | Calculate > All Molecule... > **Stepped Refine...**, then press **Stop** after a few residues. | Stop greys out; after the current residue the refinement pauses; **Cancel** and **Continue** appear on the toolbar. **Continue** resumes with the next residue, **Cancel** ends it; the three buttons disappear when it ends. |
| R4 | Change the contour level (scroll wheel on the map or the Draw > Map... slider) and middle-click an atom straight afterwards. | The pick works. |
| R5 | Quit with File > Exit and send the newest file in `logs/` (or run `./collect-results.sh`). | I look for `WARNING:: GL ... stack depth`, `coot-gl-seam:` and `DEBUG-MAPS::` lines. |

## M. Manual checks (the real clicks; about 10 minutes; please do these first)

Start `./run-coot.sh`, Calculate > **Load Tutorial Model and Data** (this is M1), then:

| # | Do | Expected |
|---|---|---|
| M1 | Calculate > **Load Tutorial Model and Data** | The tutorial model and map load and display. (Crashed in the audit.) |
| M2 | Edit > **Copy Molecule...**, pick the model, OK. Then Edit > **Copy Fragment...** (selection `//A/1-10`), OK. | A copy appears in the Display Manager each time, no crash. (Both crashed in the audit.) |
| M3 | Calculate > **Ligand Builder** | Lidia opens. (Crashed in the audit.) |
| M4 | Calculate > **Scripting > Python...** and type `print(2+2)` + Enter. | A Python window opens and prints 4. (Crashed in the audit.) |
| M5 | Double-click two different atoms, then Draw > **Undo Last Navigation**. | The view returns to the first atom. (Crashed in the audit.) |
| M6 | Calculate > **Fit Loop > Fit Loop by Database Search...**; Calculate > **Updating Maps...**; Calculate > **Run Script...** (pick any small .py file). | Dialogs open and act, no crash. (All crashed in the audit.) |

If any of M1-M6 crashes, send me the newest `~/Library/Logs/DiagnosticReports/coot-bin-*.ips` (or tell me and I will read it; I have access) and the line of M-number.

## What changed

1. Coot's GUI scripts (`coot_gui.py`, `extensions.py`, `coot_toolbuttons.py`, ... about 27 files) were written for PyGTK 2, which does not exist for Python 3 or macOS. Build 7 ships a small PyGTK 2 replacement (folder `share/coot/python/gtk`, `gobject.py`, `pango.py`) that talks directly to the GTK 2 that is already inside the folder. The scripts themselves are unchanged apart from fixes.
2. Menus: Calculate > **All Molecule...**, **Modelling...**, **Modules...**, **NCS Tools...**, **PISA...**, the Validate / Ligand / Draw / Extensions entries that the scripts add (the Ligand menu has the SMILES entries). About 160 menu entries that were absent are now there.
3. **Sphere Refine** and **Sphere Regularization** (and the other optional toolbar buttons): right-click the main toolbar > **Manage Buttons**, tick them in the Refinement group. The choice is saved in `~/.coot-preferences/coot_toolbuttons.py`.
4. Bugs in the upstream scripts that would have made buttons fail on Python 3 were fixed (e.g. `dialog_box_of_buttons` raised `NameError`; "Save dialog positions", "Atom Overlaps Dialog" and "Pepflips from Difference Map" called functions that did not exist: the last two are now ported from the Scheme versions; RCrane was ported to Python 3).
5. A headless sweep that activates every one of those menu entries and clicks every button of the dialogs they open found no Python error. **That does not prove the buttons work in a real window** (nothing can be drawn headlessly), which is why section B exists.

## A. Install and headless self-test (2 minutes, iMac and MacBook)

Replace the folder with the new `Coot-0.9.8.96-arm64` (zip or folder). **If it came by AirDrop, a browser or `~/Downloads`, clear the macOS download-quarantine flag first** (otherwise the launcher refuses to start, and so does the test): `xattr -dr com.apple.quarantine "<path of the folder>"`. Then `./tests/run-headless-tests.sh`.
Expected (18 lines, all `N / N`): `python-api 19`, `scheme-api 27`, `data-and-maps 32`, `ondemand-read 3`, `refine-zone 4`, `process-helpers 10`, `bundle-python 18`, `bundle-scheme 6`, `rdkit-python 10`, `rdkit-scheme 3`, `gtk2compat 12`, `gui-scripts 14`, `gui-dialogs 44`, `gui-glyco 14`, `gui-toolbar 13`, `gui-rcrane 21`, `refmac-run 8`, `startup-dictionaries 1`. (`refmac-run` really runs refmac5 for about 20 s if CCP4 is installed; without CCP4 it reports "skipped" and counts as passed. The first run on a new folder takes several minutes more because Guile compiles its libraries once.)
If the folder is still quarantined the script prints "headless tests NOT RUN" with the command above instead of lines.
(I still have no MacBook result for any build; please run it once and send the lines.)

## B. The one-command GUI audit (run it again; iMac, then MacBook; about 10-15 minutes, no clicking)

In Terminal, in the Coot folder: `./tests/run-gui-audit.sh`. A stalled Coot is now killed by a separate watchdog after 5 minutes (`COOT_AUDIT_HANG=120` for 2 minutes) and noted as HANG.

Coot opens, loads the tutorial model and map, and **works through every menu entry and every main-toolbar button by itself**: it activates the entry, waits for windows to be drawn, clicks every button inside the dialogs that opened, closes them, and writes one line per entry. If an entry crashes Coot, the script notes it and restarts Coot after that entry. Please do not touch the mouse or keyboard while it runs; windows will flicker. It skips Exit, full-screen/stereo, and entries that fetch from the internet (listed as SKIP, try those by hand: section C).

At the end it prints a summary and writes `results/gui-audit-<time>.txt`. Send me that file (or `./collect-results.sh`, which gathers it). Each line says one of:

| status | meaning |
|---|---|
| `ok` | handler present, no error, no GTK warning |
| `WARN` | GTK printed a CRITICAL/WARNING while the entry ran (usually a widget that is missing: I will look) |
| `ERR` | a Python exception, shown in the line |
| `NO-HANDLER` | the menu entry is connected to nothing: a dead entry, I will hide or fix it |
| `CRASH` / `HANG` | Coot died or stopped responding while this entry ran (four entries crash headless because there is no OpenGL context / no screen to show a window on; in the real window they should not) |
| `SKIP` | not run on purpose |

This audit is new and has only been tested without a display (it runs, finds windows and clicks buttons there). If it misbehaves on your Mac (hangs at start, closes the wrong thing), `COOT_AUDIT_BUTTONS=0 ./tests/run-gui-audit.sh` runs it without clicking dialog buttons, and `COOT_AUDIT_ONLY="Calculate" ./tests/run-gui-audit.sh` restricts it to menu paths matching a pattern. Tell me what happened.

Smaller smoke test that shows a few scripted dialogs for a moment and closes them: `./run-coot.sh --script tests/gui_python_smoke.py` (writes `results/gui-smoke-<time>.txt`).

## C. Things the audit cannot judge (iMac and/or MacBook; PASS / FAIL / PARTIAL and a few words in `results/answers.txt`)

| # | Do | Expected |
|---|---|---|
| G1 | `./run-coot.sh test-data/tutorial-modern.pdb`. Calculate > **All Molecule...**, **Modelling...**, **Modules...** | Each opens a submenu with entries (about 3, 40 and 8). Pick two or three that make sense (e.g. Modelling > Fit Protein..., Add Hydrogens) and tell me what they do. |
| G2 | Right-click the main toolbar > **Manage Buttons**; tick **Sphere Refine** and **Sphere Regularization** (Refinement group); close the dialog. Load the tutorial map (Calculate > Load Tutorial Model and Data), centre on a residue, click **Sphere Refine**. | Both buttons are in the toolbar; Sphere Refine refines the residues around the centre. Quit and restart: the buttons are still there. |
| G3 | Edit > **Copy Molecule...**; Edit > **Copy Fragment...** (selection `//A/1-10`). | A new molecule appears in the Display Manager each time. |
| G4 | Calculate > **NCS Tools...** (tutorial-modern.pdb has chains A and B): NCS Jumping, NCS Ghosts, copy NCS. | Dialogs open and act on the chosen molecule. |
| G5 | Calculate > **PISA...** > PISA Interfaces... / Assemblies... (needs CCP4's `pisa` in the path; the launcher looks in `/Applications/ccp4-*/bin`). | Either results appear, or a clear message that `pisa` was not found: not a silent nothing. |
| G6 | Calculate > Map Tools > **Map Density Histogram...**; Ligand > **Ligand Metric Sliders**; one Validate graph (e.g. Validate > Ramachandran Plot) for comparison. | The histogram and the sliders are drawn: they use PyGTK drawing calls that I could not test without a display, so a blank window = FAIL. |
| G7 | Ligand > **Quick Ligand Validate**, **Isolated Molprobity Dots for this Ligand** with a ligand centred (needs Reduce/Probe: they are found in CCP4 and Phenix). | A dialog / dots; without Reduce/Probe an INFO line in the Terminal. |
| G8 | Ligand menu (new: **SMILES -> 2D**, **SMILES -> simple 3D**, **Residue -> 2D**, **FLEV this residue**, **Show Chemical Features**). | Dialogs open; SMILES -> simple 3D with `CCO` makes a small molecule; SMILES -> 2D opens Lidia with the drawing. |
| G9 | RCrane: Calculate > **RCrane launch** (RNA tool; see U5-U8 in section U with the tRNA in test-data). | Its menu appears. |
| G10 | Quit with File > Exit. | Coot closes at once (no hang, no extra dialog). |

## D. Still open from builds 5 and 6 (nothing heard yet)

| # | Do | Expected |
|---|---|---|
| L1 | Centre on an atom (double-click) in tutorial-modern.pdb. | Dashed environment distances with numbers appear without turning anything on; text clearly larger than in round 4. |
| L2 | Draw > Label Neighbours (or Label Atoms in Residue, Centre Atom Label...). | Same font as the distance numbers, clean edges. |
| L3 | `./run-coot.sh --retina test-data/tutorial-modern.pdb`. | Same physical size as L1, sharper. |
| L4 | `COOT_LABEL_SCALE=2 ./run-coot.sh ...` (1.0 = old size). | Tell me the value you like and I will make it the default. |
| L5 | Trackpad: two-finger click (without moving) on an atom. | Centres on it like a middle click; two-finger drag still zooms. |
| L6 | Draw > **Model/Fit/Refine Toolbar**: untick, tick. | Toolbar disappears and returns. |
| N1-N5 | Calculate > Ligand Builder (Lidia): toolbar icons; Import from SMILES... `CC(=O)Oc1ccccc1C(=O)O` (aspirin) and penicillin G `CC1([C@@H](N2[C@H](S1)[C@@H](C2=O)NC(=O)CC3=CC=CC=C3)C(=O)O)C`; toolbar button SMILES; a broken string `C1CC(`. | Drawings appear with icons and wedge bonds; the broken string gives a warning, no crash. |

## E. Known limits (not worth reporting)

The GUI language is Python: Scheme scripts that build GTK windows (`(molecule-chooser-gui ...)` and similar, in your own `.coot` Scheme files) do not work yet; the same functions exist in Python. QED bars in Lidia stay hidden. No reference-structures set (Ca -> Mainchain). The splash screen is not confirmed. A few entries (Calculate > Map Tools > Brighten Maps, Draw > Representation Tools > Ball & Stick..., Highlight Interesting Site, and the Edit Chi Angles key-binding button) crash only when there is no graphics window, i.e. in the headless sweep; the audit reports whether they behave in the real window.

## F. Send me the results

`results/gui-audit-*.txt`, `results/answers.txt`, the 14 lines of section A. Or run `./collect-results.sh`. I can read `logs/` in the iMac folder directly; the MacBook needs `collect-results.sh` or pasted text.
