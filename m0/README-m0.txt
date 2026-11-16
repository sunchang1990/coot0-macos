Coot 0.9.8.96 -> Apple Silicon: M0 patch series and tools
=========================================================
Layout (extract into a directory called m0/ next to a checkout of canvas/ built by coot-canvas-build-scripts.tar.gz):
  setup.sh            copies the pristine tree (path set inside) to coot-src/ and applies patches/*.patch with git apply
  newpatch.sh NAME    records current edits in coot-src/ as patches/NAME.patch
  patches/0001..0033  the patch series (0001-0009: see coot-macos-m0-report.md; 0010 GL shim, 0011 Retina scaling, 0012 crash-handler opt-in: see coot-macos-m1-report.md;
                      0013-0017: round-2/3 fixes, see "Round 2" below; 0018-0020: round-5 UI fixes, see "Round 5" below; 0021-0022: RDKit, see "Round 6" below)
  tools/m0_build.py   syntax|compile driver for src/ lbg/ tw/ goograph/ (+ --with-libs for the 21 library dirs); same flags for all TUs
  tools/m0_link.py    links coot-bin from the objects; writes <out>.undef.txt (unresolved symbols) and <out>.link.log
  tools/port_python_scripts.py   mechanical Python 2 -> 3 port of python/, python-tests/, rcrane/, lbg/, pyrogen/ (re-creates patch 0007)
  tools/analyze.py, gen_ninja.py, syntax_check.py, stubs-*   earlier baseline tooling (stubs-gtkglext = the GtkGLExt API inventory)
  glseam/gl_seam_stub.c          10 GtkGLExt entry points; link-time placeholder that WP2 replaces
  stage/rt_test.py rt_test.scm run_rt.sh run_rt_scm.sh read_all.scm goosh_in.txt   headless runtime tests (need standard-residues.pdb copied to stage/test.pdb)
  evidence/           result JSON/logs behind the report
Environment: conda env 'coot-deps' (conda-forge: gtk2 2.24.33 quartz, clipper 2.1, mmdb2, libccp4, ssm, gsl, guile 3.0.10, python 3.11, boost, cairo, ...)
plus the canvas prefix (libart_lgpl 2.3.21, libgnomecanvas 2.30.3, goocanvas 1.0.0).
Typical run (from the directory containing m0/ and canvas/):
  export PKG_CONFIG_PATH=$CONDA_PREFIX/lib/pkgconfig:$CONDA_PREFIX/share/pkgconfig
  bash m0/setup.sh
  python m0/tools/m0_build.py compile m0/compile_all.json --stubs gtkglext --prefix $PWD/canvas/prefix --with-libs --objdir m0/obj_link
  python m0/tools/m0_link.py m0/compile_all.json m0/obj_link m0/bin/coot-bin --prefix $PWD/canvas/prefix --seam m0/coot-src/compat/gl-seam/coot-gl-seam.mm
Note: the compile/link harness only exists because the GUI cannot be run in the build sandbox; it is not the final build system.

M1 additions
  tools/m0_link.py --seam *.mm        compiles the Objective-C++ GL shim and links Cocoa (glseam/gl_seam_stub.c is the superseded M0 stub)
  tools/assemble_m1_data.sh           builds share/coot (the make-install layout) from the source tree + syminfo.lib from libccp4
  tools/assemble_m1_package.sh        copies the package, relocates the canvas libraries to @rpath, re-signs ad hoc, verifies with codesign
  m1-package/                         run-coot.sh, collect-results.sh, TEST-PROTOCOL.md, tests/ (headless self-tests), results/answers.txt
  stage/mk_pixbuf_cache.py            gdk-pixbuf loader cache including librsvg's .dylib loader (the toolbar icons are SVG)
  stage/pixbuf_test.c                 loads every pixmap through that cache (153/153 load)
The monomer library (MonomerLibrary/monomers commit 0af022bf, sha256 in coot-macos-m1-report.md) is downloaded, not stored here.

Deployment target (user decision: macOS 11 / Big Sur)
  All builds pin the minimum macOS: tools/m0_build.py and tools/m0_link.py add -mmacosx-version-min=$COOT_MIN_MACOS (default 11.0) and
  canvas/build_canvas.sh exports MACOSX_DEPLOYMENT_TARGET.  Without this the binaries inherit the SDK's 15.5.  Check with:
  otool -l <file> | awk '/LC_BUILD_VERSION/{f=1} f&&/minos/{print $2; exit}'

Round 2 (fixes after the first GUI test; details in coot-macos-m1-report.md section "Round 2")
  0013 rama-plot-accel-group-use-after-free   src/rama_plot.cc: walk a copy of the window's accel-group list (Ramachandran plot SIGSEGV)
  0014 monomer-lib-dir-env-handling           geometry/cif-parse.cc: COOT_MONOMER_LIB_DIR alone no longer gets "/data/monomers/" appended
                                              (mon_lib_list.cif link restraints and ener_lib.cif were never loaded: 0 link bond/angle restraints
                                              -> real-space refinement tore zones away from their neighbours)
  0015 wallclock-animation-pacing-and-timed-spin   src/coot-animation.hh (new): paces the synchronous animation loops (smooth centring, view
                                              interpolation, go-to-ligand, rotate_*_scene) at 1/60 s per step (COOT_ANIM_MS_PER_STEP);
                                              spin is a 16 ms timer and time-based; default idle_function_rotate_angle 1.0 -> 0.15
  0016 scheme-probe-checks-and-command-in-path   scheme/: probe checks reduce's exit status/output, GUI helpers optional; command-in-path? needs an executable regular file
  m1-package/tests/refine_python.py + run-headless-tests.sh: refinement geometry and clean-dictionary-startup regression tests
  tools/assemble_m1_data.sh: cootrc gets gtk-icon-theme-name "Adwaita"; m1-package/run-coot.sh: env hygiene, CCP4/Phenix tool discovery, COOT_BIN override
  evidence/refine_old_vs_new.txt, evidence/probe_paths.txt: the measurements behind 0014 and 0016
Incremental rebuild of changed files:  python m0/tools/m0_build.py compile out.json --stubs gtkglext --prefix $PWD/canvas/prefix --with-libs --objdir m0/obj_m11 --src m0/coot-src --only '<regex>'
  then relink with m0_link.py (its <out> argument is the output FILE, e.g. m0/bin_m11/coot-bin).

Round 3
  0017 scheme-external-programs-via-system   scheme/guile-compat.scm + coot-utils.scm: external programs (goosh-command, run-command/strings,
                                              goosh-command-with-file-input, run, run-concurrently) go through the C library's system() with shell
                                              redirections.  Guile's fork+exec spawn() children exited with status 127 without running the program
                                              (no message) inside the Cocoa GUI process: reduce/probe never ran there although they work headless.
                                              The root cause inside the GUI process is NOT established; this removes the dependency on spawn().
  m1-package/tests/process_scheme.scm         10 checks of the new helpers (quoting, stdin data, exit status, missing command, failing exec)
  evidence/probe_round3.txt                   probe with Phenix 2.2.1, CCP4 9 and a failing reduce

Round 4: self-contained bundle (milestone M2a)
  tools/bundle_inventory.py   dependency closure + run-time loaded modules + files with the build prefix baked in (-> evidence/bundle_inventory*.{json,md})
  tools/assemble_bundle.py    builds the relocatable bundle: flat lib/ (@rpath names), bundle-relative rpaths, Python stdlib (no tests/tk/curses), Guile trees,
                              pixbuf-loader cache template (@BUNDLE@ placeholder), fontconfig data, CA file, icons; every Mach-O re-signed ad hoc
                              usage: assemble_bundle.py --coot-bin m0/bin_m11/coot-bin --canvas-lib canvas/prefix/lib --env <conda env> --stage m1pkg/coot-m1 --out b/coot-bundle
  tools/bundle_check.py       fails on any dependency/rpath/install name outside the bundle, minos > 11.0, bad signature, dangling symlink
  m1-package/run-coot.sh      dual-mode launcher (bundle or conda env); env vars neutralise every baked prefix; per-user pixbuf cache; COOT_DYLD_DEBUG, COOT_STRICT
  m1-package/tests/bundle_python.py, bundle_scheme.scm   run only in a bundle: modules, CA file, 153 pixmaps incl. SVG, fontconfig, Guile paths
  evidence/bundle_relocation.txt   relocated copy under env -i: 9 suites pass, 0 libraries loaded from outside bundle/system
Build + verify:  python m0/tools/assemble_bundle.py ...; python m0/tools/bundle_check.py b/coot-bundle; copy to another path; env -i ... tests/run-headless-tests.sh

Round 5: UI fixes after the first MacBook/iMac GUI tests (build 5)
  0018 scene-text-pango-labels      compat/gl-seam/coot-label-raster.h (Pango/cairo -> A8 bitmap, no GL, offline-testable: tools/label_raster_test.cc) +
                                    coot_gl_draw_text_at_raster_pos() in coot-gl-seam.mm (cached alpha textures, drawn at GL_CURRENT_RASTER_POSITION);
                                    graphics-info.cc printString_internal / draw_generic_text and graphics-ligand-view.cc call it instead of glutBitmapCharacter.
                                    Size = nominal GLUT font size x COOT_LABEL_SCALE (default 1.4) x Retina factor.  COOT_BITMAP_LABELS=1 restores the old fonts.
                                    The GL half can only be verified on a real display (the sandbox has no window server).
  0019 env-distances-default-on-right-click-centre   globjects.cc: environment_show_distances=1, environment_distance_label_atom=1 (H-bonds, bumps, 0-3.2 A were already on);
                                    still right-click (<10 px movement) re-centres like a middle click (trackpad); COOT_RIGHT_CLICK_CENTRE=0 disables.
  0020 model-toolbar-menu-toggle    Draw menu check item "Model/Fit/Refine Toolbar" (gtk2-interface.c, callbacks.c/.h); c-interface-gui.cc keeps it in sync with the popup "Hide".
  tools/assemble_m1_data.sh         now copies lbg/*.svg (23 Lidia icons) into share/coot/pixmaps (they were missing: broken-image placeholders in the ligand builder)
  m1-package/run-coot.sh (build 5)  documents the env switches; repairs Guile .go timestamps after a copy without file dates (cp -R) instead of recompiling the Guile library
  m1-package/collect-results.sh     no word-splitting on folder names with spaces
  m1-package/tests/bundle_python.py 13 checks (adds: lbg.glade icons installed, environment distances on by default, toolbar show/hide API)
  Finding: Lidia SMILES import (lbg.cc import_mol_from_smiles_string) and the SMILES button (babel fallback) need RDKit ("enhanced ligand tools", MAKE_ENHANCED_LIGAND_TOOLS); not built.

Round 6: RDKit "enhanced ligand tools" (build 6)  -- Lidia SMILES import / SMILES readout, residue_to_sdf_file, import_rdkit_mol_from_smiles
  Environment: a separate conda env "coot-rdkit" = conda-forge rdkit=2023.09.* (C++ headers + libs, RDKit 2023.09.6) + libboost-headers=1.84.*.
               (conda-forge has no librdkit-dev for 2023.09; newer RDKit versions were not tried.)  The working env (coot-deps, Boost 1.92) is untouched.
  tools/m0_build.py --rdkit <env>   -DMAKE_ENHANCED_LIGAND_TOOLS -DRDKIT_HAS_CAIRO_SUPPORT; RDKit's Boost 1.84 headers BEFORE the working env's Boost for every TU
                                    (one Boost version in the whole binary); full rebuild of all 412 TUs takes about 3 minutes (objects in m0/obj_m13)
  tools/m0_link.py  --rdkit <env>   adds the 30 libRDKit* libraries of Coot's configure.ac (coordgenlib is called coordgen in 2023.09), -lboost_serialization, -lboost_python311
  0021 rdkit-exception-what         lbg/lbg.cc, coot-utils/lidia-core-functions.cc: RDKit::BadFileException / FileParseException have no message(); use what()
  0022 rdkit-make-residue-atom-names   lidia-core/rdkit-interface.cc make_residue(): atoms without a name were all called ZZZZ; name them from element + running number
                                    (the comment at the top of the function says that is the intent)
  tools/rdkit_smoke.cc              C++ check of the RDKit env: SMILES -> 2D -> Kekulize -> WedgeMolBonds -> molblock -> SMILES (the calls Lidia makes after a SMILES import)
  m1-package/tests/rdkit_python.py (10 checks), rdkit_scheme.scm (3 checks)   run only when lib/libRDKitGraphMol.1.dylib exists
  Result: the bundle gains 40 Mach-O files (30 RDKit + 8 Boost + 2), lib/ 195.8 -> 211.3 MB; 11 suites pass from a path with spaces under env -i;
          dyld: 759 images = 120 bundle + 639 macOS, none from anywhere else.  Python's rdkit module is NOT shipped: Lidia then hides its QED bars by itself.
  Not testable without a window: Lidia's own SMILES import dialog and the SMILES toolbar button (only the RDKit calls behind them are tested).

Round 7: scripted GUI on a PyGTK-2 compatibility layer (build 7)  -- Coot's Python GUI scripts (27 files) run on the real GTK2-Quartz main window
  Why: coot_load_modules.py loads the GUI scripts only if "import pygtk; import gtk" works.  PyGTK 2 does not exist for Python 3 / Apple Silicon, so every menu entry,
       toolbar button and dialog that the scripts create (All Molecule/Modelling/Modules, NCS tools, PISA, Probe dialogs, Sphere Refine buttons, ...) was absent.
  0023 scripted-gui-via-python      USE_PYGTK + COOT_GUI_VIA_PYTHON: GUI call-outs in the C++ code (c-interface-build-gui.cc, toolbar multi-refine, post-ligand-fit, ...) choose the
                                    Python functions when there is no guile-gtk; native module _coot_python_native (coot-setup-python.cc) hands the main menubar / statusbar / toolbar /
                                    hbox to Python as raw GtkWidget pointers (the 4 functions of the `coot_python` module); gtk_widget_set_flags mapped to GTK 2.24 API.
                                    m0_build.py --pygtk adds -DUSE_PYGTK -DCOOT_GUI_VIA_PYTHON.
  0024 pygtk2-compat-layer          compat/pygtk2/: ctypes bindings over the real GTK 2.24 libraries (no C extension, nothing to compile):
                                    _gtk2core.py        generic method dispatch by C function name from clang-generated tables (_gtk2_protos.json: 9439 prototypes with type codes;
                                                        _gtk2_consts.json: 5826 constants), GError** / GList / GSList / out-parameter conversion, signal trampolines (CALLBACK_ERRORS), timeouts/idles, GValue helpers
                                    gtk/__init__.py, gtk/gdk.py, gtk/keysyms.py, gobject.py, pango.py, pygtk.py, coot_python.py
                                    tools/gen_gtk_protos.py, gen_gtk_consts.py, gen_menu_structure.py (rebuilds the main menubar from gtk2-interface.c -> tests/menubar.json)
                                    surface actually used by the scripts (ast scan, evidence/pygtk_surface.md): 79 gtk names (1001 uses), 13 gdk, 4 keysyms, 4 gobject, 5 pango, 14 signal names
                                    Rule: variadic C functions are never called with extra arguments (arm64 Apple ABI: segfault); they raise TypeError instead.
  0025 python3-leftovers-in-gui-scripts-ported-dialogs-rcrane
                                    python/*.py: Python-2 leftovers of the earlier port that only show when the GUI runs: types.StringType/ListType/IntType (NameError/ImportError in
                                    dialog_box_of_buttons and ~60 other places), apply(), file(), operator.isNumberType; name typos (chain_n_iresidues, residue_name_by_spec,
                                    handle_chelx_fcf_file, save_dialog_positions_to_preferences_file, mol_no_ls); save_dialog_positions wrote comment lines without newlines (the
                                    position lines were swallowed into the comment); command_in_path_qm(False) raised TypeError when probe was not found.
                                    Ported from Scheme (the Python scripts called them but never defined them): pepflips_by_difference_map_gui, molecule_atom_overlaps_gui.
                                    rcrane/ (RNA tool, 12.5 k lines): 2to3 (implicit relative imports, print, dict views) + fixes: py2 comparison float<=str in smoothProb, `raise "text"`,
                                    missing imports on error paths, wrong parameter name in getPhosCoordsFromIndex.  installRCrane.py is not shipped.
  Tests (all headless, on real GTK widgets; the build sandbox has no window server):
    gtk2compat_python.py / gtk2compat_selftest.py (11)   the layer against real GTK: widgets, signals, lists, GError, timeouts, pixbufs, FileChooser emulation
    gui_python_load.py (14)       the real scripts load on a menubar rebuilt from gtk2-interface.c: menu items 139 -> 311 (All Molecule 3, Modelling 40, Modules 8)
    gui_python_dialogs.py (20)    Manage Buttons offers Sphere Refine/Regularization, dialog_box_of_buttons runs string/list/function callbacks, the two ported dialogs, no py2 names (ast scan),
                                  save_dialog_positions, RCrane menu, no exception in any signal handler
    gui_menu_sweep.py + run-gui-sweep.sh   activates all 163 menu entries the scripts add, clicks every button of the dialogs they open: 159 ok, 0 errors, 4 entries crash
                                  only because there is no OpenGL context / no screen (Brighten Maps -> compile_density_map_display_list; Ball & Stick; Highlight Interesting Site;
                                  the key-bindings dialog's Edit Chi Angles button -> gtk_window_realize of a C-built window)
    gui_harness.py                shared loader; gui_python_smoke.py (real window, shows a few dialogs), gui_audit.py + run-gui-audit.sh (real window: every menu entry and main-toolbar
                                  button, auto-closes dialogs, clicks their buttons, restarts after a crash; self-tested headless, NOT yet run on a display)
  How the findings were made: pyflakes over python/*.py (1005 unique names, 33 not defined at run time after loading) + regex scan for py2 idioms + the sweep.
  Not testable without a window: drawing (Widget.window / gtk.gdk drawing calls in ligand_validation_sliders.py, pdbe_validation_data.py, map density histogram), real dialog sizes.
  Scheme: GUI scripts written with guile-gtk (105 functions in 27 .scm files) do not work (USE_GUILE_GTK is not defined); the Python equivalents do.
  Result: 14 suites pass from a path with spaces under env -i; dyld: 784 images = 145 bundle + 639 macOS, none from anywhere else; bundle_check OK (210 Mach-O, minos 11.0).
Build:   PKG_CONFIG_PATH=$CONDA_PREFIX/lib/pkgconfig:$CONDA_PREFIX/share/pkgconfig python m0/tools/m0_build.py compile out.json --stubs gtkglext --prefix $PWD/canvas/prefix --with-libs --objdir m0/obj_m13 --src m0/coot-src --rdkit <coot-rdkit env> --pygtk
         python m0/tools/m0_link.py out.json m0/obj_m13 m0/bin_m14/coot-bin --prefix $PWD/canvas/prefix --seam m0/coot-src/compat/gl-seam/coot-gl-seam.mm --rdkit <coot-rdkit env>
         bash m0/tools/assemble_m1_data.sh m0/coot-src m1pkg/coot-m1 ; python m0/tools/assemble_bundle.py --coot-bin m0/bin_m14/coot-bin ... ; python m0/tools/bundle_check.py <bundle>

Round 8: findings of the first real-window GUI audit (build 7, iMac, 270 entries) -> build 8
  Evidence: the user's results/gui-audit-20261104-163931.txt (216 ok, 17 WARN, 2 ERR, 6 NO-HANDLER, 18 CRASH) + 9 macOS crash reports (.ips) of that run.
  Root cause of most crashes: _gtk2core opened the GTK libraries with ctypes.CDLL, which releases the GIL during every foreign call.  Python driving GTK (item.activate() ->
        g_signal_emit) ran Coot's own C callbacks synchronously (on_edit_copy_molecule1_activate -> do_edit_copy_molecule -> PyRun_SimpleString) WITHOUT the GIL: SIGSEGV in
        PyImport_AddModule/import_add_module (7 of 9 reports: Curlew install, Copy Molecule/Fragment, Replace Residue/Fragment, Fit Loop DB, Undo Last Navigation).
        Reproduced headlessly (ctypes.CDLL(None).do_edit_copy_molecule() -> exit -11; PyDLL -> runs).  Fix: ctypes.PyDLL (GIL kept; Python trampolines re-acquire it harmlessly).
        A real mouse click comes from GTK's main loop and never went through ctypes, so real clicks should not have been affected: manual checks M1-M6 in the protocol test this.
  0027 pygtk2-keep-gil-log-filter-surface-guard   compat/pygtk2/_gtk2core.py: PyDLL; log filter for two harmless GTK2/GLib messages (GFileInfo ... is-hidden, shortcuts_add_bookmark_from_file);
        python/extensions.py: surface_func1 (Clipped/Full Surface Around Here) says "no residue centred" instead of TypeError.
  Audit fixes (tests/gui_audit.py, run-gui-audit.sh): reload model+map before every entry (an early entry deleted them, so later entries printed "No such molecule as 0"); --no-state-script
        on restarts; no clicks inside GTK file choosers (one crash = GtkPathBar scroll arrow, GTK's own); no Install/Upgrade/Get buttons; handler detection per instance type
        (tool buttons have their own "clicked" signal, check items "toggled": the 6 NO-HANDLER were false alarms); no destroy of dialogs that already closed themselves (the gtk_widget_destroy
        criticals); external watchdog (separate process) instead of a Python thread, because a thread cannot run while the GIL is held in a blocking GTK call.
        Escapes: raw-string "\\b" in the skip regexes matched a literal backslash (fixed).
  New test: tests/gui_python_dialogs.py (23 checks): a menu item wired to Coot's C callback is activated from Python (a crash there kills the run: -11 with CDLL, passes with PyDLL); log filter.
  Not reproduced: JED-Flip crash (mmdb SeekContacts/MakeBricks) occurred after the model had been deleted by an earlier audit entry; jed_flip with the model loaded works.
  Open: Draw > Generic Display Objects with no objects -> gtk_table_resize critical (C code, benign).

Round 9: user's second GUI report on build 8 (iMac, own data, P 43 21 2) -> build 9
  1 CRASH "terminating due to uncaught exception of type clipper::Message_fatal" after "Failure to find grid coordinate uvw=(-48,-113,-22)" / "Xmap: Internal map ASU error P 4nw 2abw Nuvw=(225,225,400)".
    Root cause (reproduced headlessly with the user's own mtz, identical uvw numbers, rc 134 in build 8): Calculate > Map Tools... > "Make a Smoother Copy..." = smooth_map(imol, 1.25) ->
    coot::util::reinterp_map multiplied the grid 180x180x320 by 1.25 = 225x225x400; odd nu/nv is not allowed with the 2_1/4_3 axes of P 43 21 2, so clipper throws Message_fatal from
    Xmap lookups; the exception left a std::thread (gensurf_and_add_vecs_threaded_workpackage only caught std::out_of_range) -> std::terminate.  (Upstream Coot 0.9.8 has the same defect.)
    Fix: coot::util::grid_is_compatible_with_spacegroup() (translation parts must be whole grid steps; axis-exchanging rotations need equal dimensions), compatible_grid_sampling()
    (clipper Grid_sampling(spgr,cell,Resolution(2*spacing),1.0), checked), used by reinterp_map; update_map_internal() refuses to contour a map with an incompatible grid (message once);
    the contouring worker catches Message_fatal / std::exception / ... and always releases draw_vector_sets_lock.
    Test: tests/data_python.py (data-and-maps 11 -> 16) writes P 43 21 2 CCP4 map files with stdlib only (36x36x64 good, 45x45x80 bad grid); build 8 aborts on smooth_map(1.25), build 9 passes.
    (A map file with a forbidden grid is refused by clipper's own import, reported, no abort.)
  2 GL view displaced up ~45 screenshot px (22 pt).  Not reproducible without a window server (NSScreen is empty: any NSWindow creation dies in this sandbox).  Change (patch 0028, gl-seam):
    the NSOpenGLView is now a subview of the NSView that GDK keeps for the GtkDrawingArea's GdkWindow (gdk_quartz_window_get_nsview(child) != toplevel view; gdk_window_quartz_move_resize
    sets that view's frame, views are flipped), frame = bounds, autoresizing width+height; no GTK->AppKit arithmetic.  COOT_GL_PARENT=toplevel selects the previous placement.
    Launch log: "coot-gl-seam: GL view parent = ...", "coot-gl-seam: widget-view mode: GL frame ... DISAGREE ..." (cross-check against gdk_window_get_origin).  UNVERIFIED on screen.
  3 "Model atom pick failed" (73 times): successful picks in the log had ray distances 0.30-0.58 A (on target 0-0.2): explained by item 2 (pick unprojects GTK mouse coords against the GL viewport).
  4 Stepped Refine / map not redrawn: not reproduced.  Headless stepped_refine_protein on the user's data: 118 distinct centres, update_map_triangles at each (bbox of the lines = centre +- 16 A).
    Changes: stepped refine skips non-protein chains; first 40 re-contourings logged "DEBUG-MAPS:: ... bbox" (COOT_DEBUG_MAPS=1 all, =0 none).  Python stdout now unbuffered (PYTHONUNBUFFERED=1 in the launcher).
  Audit isolation: tests/run-gui-audit.sh runs in a throw-away HOME and cwd (the build-7 audit had written preferences / state into the user's folder; see the protocol, item 6).
  0028 map-grid-symmetry-contouring-exceptions-gl-view-in-widget-nsview (coot-utils/coot-map-utils.{cc,hh}, src/molecule-class-info-maps.cc, compat/gl-seam/coot-gl-seam.mm, python/fitting.py)
  Verified: build 9 bundle, 14 suites from a path with spaces under env -i (data-and-maps 16/16), sweep 159 ok / 0 err / 4 headless-only crashes, dyld 784 = 145 bundle + 639 macOS + 0 other,
  zip tested after ditto -x -k (14 suites).

Round 10: user's report on build 9 (iMac): density follows during Stepped Refine and middle-click picking works, but (1) toolbar Stop dead and no Continue button, (2) middle-click fails after
  "Go to next ligand" until Go To Atom, (3) ligand label at lower left illegible (screenshot: grey 2D ligand, pink double ellipses where O labels should be) -> build 10
  1 Stop button: "Stepped Refine..." (Calculate > All Molecule...) is extensions.py -> interruptible_fit_protein(imol, fit_protein_stepped_refine_function), run from gobject.idle_add; its
    Stop/Continue/Cancel buttons use coot_toolbar_button(label, "stop_interruptible_fit_protein()", ...) with a STRING callback.  cb_wrapper tested `type(callback_function) is bytes`:
    patch 0007 (2to3) had turned types.StringType into bytes, so every string callback fell to "cannot evaluate or call function" (Stop did nothing, so no Cancel/Continue buttons).
    Same slip fixed in coot_gui.py (combobox cb_wrapper, dialog_box_of_buttons button name/tooltip parsing, 3 sites), ncs.py (skip_to_chain), ligand_validation_sliders.py, pdbe_validation_data.py.
    Tests (gui-dialogs 23 -> 26): string callback runs; Stop -> Cancel+Continue appear, Cancel removes them; no str/bytes type tests left.  They FAIL on build 9 (evidence/dialogs_new_tests_on_build9.txt).
    Note: the earlier headless "stepped_refine_protein" experiment (synchronous loop) is NOT what the menu entry runs.
  2 Pick failure after Go to next ligand: coot_gl_draw_text_at_raster_pos() (seam) ended with glMatrixMode(GL_MODELVIEW).  graphics_info_t::graphics_ligand_view() (draw.cc, in the frame) calls
    render() with glMatrixMode(GL_PROJECTION) active (after push+loadIdentity) and then glPopMatrix(); the replayed display list changed the mode, so the pop hit the model-view stack and the
    projection stayed identity at the end of the frame; unproject_xyz() (atom picking) reads GL_PROJECTION/MODELVIEW/VIEWPORT from whatever the last frame left.  Same mechanism in
    display_density_level_maybe().  Go To Atom on a non-ligand switches the ligand view off, hence the cure.  Fixes: helper restores the caller's matrix mode; graphics_ligand_view() sets
    GL_PROJECTION before its pop; draw_mono() captures the scene viewport/projection/modelview right after the scene matrices are set (coot_scene_matrices_capture) and unproject_xyz() uses
    them outside of drawing; stacks are normalised at frame start (WARNING:: GL ... stack depth is printed at most 3 times).  UNVERIFIED on screen.
  3 Ligand label: generate_display_list() compiled make_text_item() -> text helper inside glNewList; glGet* (raster position valid/current raster position/current colour/viewport) are not
    recorded in lists, so they returned stale values (pink = glColor3f(0.8,0.6,0.7) of the rotation-centre cube).  Labels are now collected in a file-static vector while the list is
    compiled and drawn by render() in immediate mode (glColor3f + glRasterPos3d + helper, or GLUT bitmap when COOT_BITMAP_LABELS=1).  UNVERIFIED on screen.
  0029 ligand-view-labels-gl-matrix-state-scene-matrices-for-picking-py3-str-bytes (src/graphics-ligand-view.cc, src/graphics-info-residues.cc, src/draw.cc, src/pick.{cc,h},
    compat/gl-seam/coot-gl-seam.mm, python/coot_gui.py, ncs.py, ligand_validation_sliders.py, pdbe_validation_data.py)
  Verified: build 10 bundle, 14 suites from a path with spaces under env -i, sweep 160 ok / 0 err / 3 headless-only crashes, dyld 784 = 145 bundle + 639 macOS + 0 other, zip tested after ditto -x -k.

Round 11: user's report on build 10 (iMac): Go to next ligand/middle-click OK, ligand labels readable, Stepped Refine OK; new: (1) Glyco module, "missing template files" when adding a NAG to an ASN
  (the pasted text did not arrive; reproduced), (2) Ligand > Ligand Metric Sliders raises TypeError (pasted twice: a traceback at coot_utils.py popen_command) -> build 11.  NO C++ OR LIBRARY CHANGE:
  bin/coot-bin and lib/ are byte-identical to build 10 (diff -rq); only share/coot (data, python, scheme), launcher, tests and protocol changed.
  1 Missing install data.  Makefile.am audit: `make install` copies into share/coot from other directories: pdb-templates/* (6 .pdb, 16 link-by-torsion .tab, 8 *-decorations.tab, theor-helix-70.pdb),
    protein_db/protein.db, cootaneer/cootaneer-llk-2.40.dat, cootilus/nautilus_lib.pdb, fonts/*, data/rama-coeffs/{all-non-pre-pro.tab,coeffsolution.dat} -> data/rama/zo-tables/ (was in the wrong place),
    ligand/ligands-2016.db -> data/, ligand/useable-grid-points-nstep=5,box_radius=5.0-charybdis.data -> data/assign-side-chains/ (~10 MB).  tools/assemble_m1_data.sh copies them now.
    Effects in build 10: add_linked_residue printed "ERROR:: file not found ...link-by-torsion-to-pyranose-core-NAG-ASN.tab" / "No file ...NAG-decorations.tab" and added nothing; protein_db_loops gave
    [[-1,-1],[]] (Fit Loop by Database Search found nothing); place_helix_here returned -1; Ligand Metric Sliders percentile = -1 (no ligands-2016.db).  Still missing: reference-structures (Ca -> Mainchain).
    Note: the Python flavour of add_linked_residue(...) is add_linked_residue_py (redefine_functions.py); the C int version always returns 0 -> tests count residues.
  2 Glyco Python glue (python/add_linked_cho.py, compat/pygtk2/gtk/__init__.py): (a) gui_add_linked_cho_dialog_vbox_set_rotation_centre_hook iterates a gtk.Table: PyGTK 2 Container.__iter__ added to
    the compat layer (TypeError 'Table' object is not iterable on every centre change); (b) add_linked_residue_py returns the new residue spec only when linked_residue_fit_and_refine_state is true
    (the scheme flavour uses the `mode` argument, the python flavour ignores it), and the dialog switches it off for good -> new add_linked_residue_and_get_spec() finds the residue that appeared next to the
    parent when the C++ call returns False; tree builders and multi_add_linked_residue set the state to 1, the dialog function restores 1; (c) delete_residue_by_spec(*spec) -> (imol, spec) (upstream
    bug; the scheme version is right); Tests: data-and-maps (5 checks), gui-glyco (dialog, buttons, menu items, Extract this Tree).
  3 popen_command / run_concurrently / shell_command_to_string (python/coot_utils.py): Python 3 pipes are bytes unless universal_newlines=True; run_concurrently never closed stdin.
    ccp4_child_env(): CCP4, CBIN, CLIB, CLIBD, CETC, CINCL, MMCIFDIC, CCP4_SCR, CCP4_OPEN, GFORTRAN_UNBUFFERED_PRECONNECTED given to CHILD processes only (refmac5 stops with "Cannot open environ.def" without
    CINCL); CLIB/CCP4 must not be exported into Coot itself (Coot would look for dictionaries there / read SRS).  Launcher: COOT_CCP4_HOME (dir above refmac5's bin if it has include/environ.def)
    and the line "CCP4 for child programs: ...".  Scheme programs: scheme/guile-compat.scm %command-line starts external programs through /usr/bin/env VAR=... (same variables, only those unset).
    Other Python 3 slips in the same flow: generic_objects.write_reduce_het_dict (copyfileobj binary -> text), ligand_validation_sliders / pdbe_validation_data colour bar (str of chr() -> bytes buffer;
    pointer arguments of the compat layer take bytes, a str would be passed as wchar_t*).  End-to-end on the user's data: METRICS density correlation 0.689, percentile 9.07.
  4 Calculate > Run Refmac: C++ (c-interface-refmac.cc execute_refmac_real) chooses the SCHEME function run-refmac-by-filename whenever Guile is compiled in (no COOT_GUI_VIA_PYTHON there); it ends with
    (gtk-timeout-add ...) = guile-gtk, unbound here -> refmac ran, the result was never read.  scheme/python-gui-bridge.scm (new, last in coot.scm's list) redefines run-refmac-by-filename to call the Python
    run_refmac_by_filename (GLib timeout), and defines interesting-things-with-fix-maybe (Validate > GLN and ASN B-factor Outliers, C++ asks for it; Python window) by translating the Scheme list.
    python/refmac.py: wrapper passed r_free_col="" (dropped the column) and `[] != ""` is always true -> LABIN ... FREE= (refmac: "Error in label assignments"); fixed; toolbar separator on an empty toolbar fixed.
    Real run on user data: refmac5 5.8.0431, 1 cycle 9 s, R 0.2025 -> 0.1987, new model + 2 maps read in.  Test: refmac-run suite (also runs without an R-free column).
    Audit of C++ -> Scheme dispatch: evidence/scheme_dispatch_audit_b11.md.
  5 Python 3 slips found by AST scans of all shipped scripts (getiterator x9, _thread.start on a Thread variable, str + bytes (u212B) x2, loop_len/2 float, urlopen().read() bytes x3): fixed; test
    "shipped Python scripts have none of the known Python 2 leftovers" (data-and-maps).  gap.py also has `imol_copy` undefined in the no-pygtk branch (never taken in the GUI; left).
  Verified: build 11 bundle (overlay on build 10), 16 suites from a path with spaces under env -i (python-api 19, scheme-api 27, data-and-maps 30, ..., gui-dialogs 26, gui-glyco 9, refmac-run 7), the new checks FAIL on build 10
  (evidence/glyco_refmac_checks_b10_vs_b11.txt).
  0030 glyco-ligand-sliders-refmac-bridge-ccp4-env-py3 (python/{add_linked_cho,refmac,coot_utils,generic_objects,gap,...}.py, scheme/{python-gui-bridge,coot,guile-compat}.scm, compat/pygtk2)

Round 12: user's report on build 11 (iMac): Glyco, outliers window, Run Refmac confirmed; trackpad double-click as middle-click works; new: (1) Ca -> Mainchain "COOT_REF_STRUCTS is not defined", (2) Ligand Metric Sliders NameError,
  (3) Run Refmac "environment variable ... not set !" lines, (4) Sphere Refine/Regularize(+) not on the toolbar, (5) new splash (higher resolution, "Good to see you, Old Coot"); MacBook test zip = launcher quarantine refusal only -> build 12.
  NO C++ OR LIBRARY CHANGE: bin/coot-bin and lib/ are byte-identical to build 10/11; changed: share/coot (data, python, scheme), launcher, tests, protocol; new file bin/coot-splash (AppKit helper, 75 KB, source compat/splash/coot-splash.m).
  1 reference-structures (28 PDB files, 10.8 MB, github.com/pemsley/coot reference-structures/, last commit touching the directory 534e73b5, checked against git blob sha1) -> share/coot/reference-structures (+SOURCE.txt);
    tools/reference-structures.manifest + a fetch/verify block in tools/assemble_m1_data.sh; run-coot.sh exports COOT_REF_STRUCTS.  One click on a CA runs execute_db_main_fragment (finds the connected CA fragment with simple_residue_tree,
    builds forwards and backwards); "click on 2 atoms" is stale upstream text.  Test: data-and-maps (28 files; db_mainchain on //A/10-40/CA gives N, CA, C, O).
  2 python/gui_ligand_sliders.py: the NameError was inside the error report (imol_map); the cause is a refinement map without an observed-F MTZ (EDS _map.mtz holds map coefficients).  ligand_metrics_find_mtz() tries refmac_parameters()[0] and
    mtz_file_name(), checks the file and its F / sigF / R-free columns, else info_dialog says what was tried.  Sigma column = the one in the data set of F / named SIG<F> (Phenix lists SIGI-obs first): own data A 301 correlation 0.689 -> 0.729.
    Test data (small, made with gemmi): test-data/map-coefficients-only.mtz, test-data/two-sigma-columns.mtz.  Tests: gui-glyco (+5).
  3 python/refmac.py prints "INFO: environment for refmac5: ..." from ccp4_child_env() instead of "environment variable: ... not set !"; test in refmac-run (the real run's output and a static check).
  4 Toolbar defaults: python/coot_toolbuttons.py install_default_toolbar_buttons() (first start in the private home, COOT_DEFAULT_TOOLBAR=1 from run-coot.sh; marker home/.coot-preferences/.default-toolbar-buttons-v1;
    COOT_NO_DEFAULT_TOOLBAR=1 off); remove_toolbar_line_from_file(): exact label match (the old regex removed "Sphere Refine +" together with "Sphere Refine"); icons refine-1.svg / regularize-1.svg.  New suite gui-toolbar (13 checks).
    C++ order checked in coot-setup-python.cc: coot_load_modules.py, extras dir, then try_load_dot_coot_py_and_python_scripts() (all ~/.coot-preferences/*.py) -> the file written during module loading is read in the same start.
  5 Splash: tools/splash (README), tools/make_splash.py, compat/splash/coot-splash.m + tools/build_splash.sh.  GTK 2 on macOS draws 1 picture pixel as 1 point; the helper shows the 1160x956 picture as 580x478 points through AppKit,
    closes when the process has an on-screen layer-0 window >= 400x300 (CGWindowListCopyWindowInfo) after >= 2.5 s, when the process ends or after 40 s; run-coot.sh passes --no-splash-screen to coot-bin then; COOT_NO_SPLASH=1 skips it.
    Verified without a window server: --selftest draws the picture into a bitmap pixel-exactly; NOT verified: the window itself.
  6 Quarantine: tests/run-headless-tests.sh stops with "headless tests NOT RUN ..." and the xattr command; collect-results.sh reports the flag.
  Found while looking:
  7 gtk.FALSE missing -> every command typed into Calculate > Scripting > Python... raised AttributeError and showed nothing (coot_gui.py scroll_to_end).  gtk.TRUE / gtk.FALSE added.
  8 gtk.Adjustment had no value / lower / upper / step_increment / page_increment / page_size -> zoom/clipping (Nudge Screen Centre with Extras), map-sharpening, occupancy and Interactive Nudge Residues sliders were dead; properties added.
  9 The menu sweep did not know menus created after start (Glyco, CCP4, Cryo-EM, Restraints, Refine, PDBe, ProSMART, SHELX, RCrane): ~95 entries.  Now swept (244 ok / 0 errors / 3 OpenGL-only crashes, as before).  Faults found: gui_prosmart.py
    "Generate Local Self Restraints 6" passed centred_residue + other_residues (flat, malformed) -> [centred_residue] + other_residues; coot_gui.py refmac_multi_sharpen_gui: find_exe returned False and popen_command(False) raised TypeError -> info dialog; find_exe(non-str) returns False.
  10 RCrane: compat layer got Alignment, AboutDialog, HScrollbar, VScrollbar; "New trace" still fails (linearInterp.py compares float with str: Python 2 semantics; reviewSuitesGui.py needs gtk.TreeView / TreeViewColumn / cell_get_size ...).
    Hidden by default (python/rcrane_loader.py; COOT_ENABLE_RCRANE=1 restores "Calculate > RCrane launch").  evidence/rcrane_not_functional_b12.txt.  A real port needs RNA test data with known results (1EHZ + EDS map downloaded for the probe).
  Verified: build 12 bundle (overlay on build 11), 17 suites from a path with spaces under env -i (python-api 19, scheme-api 27, data-and-maps 32, ondemand-read 3, refine-zone 4, process-helpers 10, bundle-python 18, bundle-scheme 6, rdkit-python 10,
  rdkit-scheme 3, gtk2compat 11, gui-scripts 14, gui-dialogs 35, gui-glyco 14, gui-toolbar 13, refmac-run 8, startup-dictionaries 1); the new checks fail on build 11 (evidence/checks_b11_vs_b12.txt); bundle_check OK (211 Mach-O, minos 11.0).
  0031 round12-refstructs-sliders-toolbar-splash-gtkcompat (python/{gui_ligand_sliders,refmac,coot_toolbuttons,coot_gui,coot_utils,gui_prosmart,rcrane_loader}.py, compat/pygtk2/gtk/__init__.py, compat/splash/coot-splash.m)

Round 13: your round-12 report -> build 13  (patch 0032 round13-fit-loop-stepped-refine-rcrane-treeview-refine-cap)
  python/coot_utils.py      atom_spec_to_residue_spec accepts the 7-element spec of user_defined_click ([model number, imol, chain, resno, ins, atom, alt]); it returned None -> "Fit Loop by Database Search" got [None, None]
  python/coot_gui.py        click_protein_db_loop_gui: candidate buttons bound their loop late (all showed the last one) -> default argument
  python/fitting.py         Stepped Refine: refine_auto_range_and_show() = non-immediate refinement, GTK main loop pumped for COOT_STEPPED_REFINE_SHOW seconds (default 0.6; 0 = old behaviour), then accept_regularizement()
  compat/pygtk2/gtk         TreeView, TreeViewColumn (cell_get_size, set_cell_data_func), TreeSelection (get_selected, get_selected_rows), ListStore (GType names, get_path, row_changed/inserted/deleted),
                            Style.bg/fg/..., CellRenderer 'xxx-gdk' colour properties, Widget.size_request/style_get_property, Box.query_child_packing; selftest case tree_views (gtk2compat 12)
  rcrane/                   linearInterp.py float/str comparison; pseudoMolecule.finalMoleculeCleanup unknown atoms (OP3) keep their order; removeLastBaseAndPhos off-by-one + resNumDict entry of the removed residue
  python/rcrane_loader.py   RCrane is on again (COOT_DISABLE_RCRANE=1 switches it off)
  src/graphics-info-modelling.cc   refinement_loop_threaded: a scripted (refinement_immediate_replacement) or windowless refinement is stopped after COOT_REFINE_MAX_SECONDS (default 10; 0 = off).
                            Without it an RCrane rotamerize could wait for ever for a minimiser that neither converges nor fails (probes: evidence/refinement_stall_b12_vs_b13.txt).
  Rebuild:  python m0/tools/m0_build.py compile out.json ... --objdir m0/obj_m13   (412 TUs, ~3.5 min)  +  m0_link.py ... m0/bin_m13/coot-bin  +  tools/relocate_coot_bin.sh (canvas libraries and rpath as in assemble_bundle.py, ad hoc signature).
  LESSON: replacing a signed binary with cp over the old file leaves the old code-signature in the kernel's cache for that inode: the new file is killed with SIGKILL at start (rc 137).  rm the old file first, then cp.
  tests/gui_rcrane.py (+ test-data/1ehz.pdb, 1ehz_map.mtz: PDB 1EHZ and its EDS 2mFo-DFc map): 20 checks, 3-8 minutes; run-headless-tests.sh now prints 18 lines.

Round 14: your round-13 report -> build 14  (patch 0033 round14-occupancy-ok-stepped-refine-dialog-density-rcrane-submenu)
  NO C++ OR LIBRARY CHANGE: bin/coot-bin and lib/ are byte-identical to build 13; changed: python/{coot_utils,fitting,rcrane_loader}.py, rcrane/{menu,__init__}.py, tests, protocol, collect-results.sh, new CHANGELOG.md.
  python/coot_utils.py      set_alt_conf_occ and rename_alt_confs: `if (alt_confs > 1)` compared a LIST with a number (py2: always true; py3: TypeError) -> len(alt_confs) > 1.
                            Symptom: Change Alt Conf Occ slider, OK did nothing (58 TypeErrors in the user's log coot-20261111-084217.log).
  python/fitting.py         Stepped Refine: (1) hide_accept_reject_dialog(): Coot's "Accept Refinement?" window (floating gtk_dialog_new, no widget name; docked variant via
                            set_accept_reject_dialog_docked_show) is hidden right after refine_auto_range and after every main-loop iteration of the dwell, and destroyed after
                            accept_regularizement() (the window's destroy handler does stop_refinement_internal + clear_up_moving_atoms: harmless after the accept, would reject before it);
                            (2) update_maps() after set_go_to_atom_chain_residue_atom_name_full: setRotationCentre(index, imol) / smooth scroll only move the view, nothing re-contours the maps.
                            Open question: builds 9-12 (immediate-replacement path) showed density following on the user's machine; a headless probe re-contours in neither path without update_maps().
  rcrane/menu.py, python/rcrane_loader.py   Calculate > RCrane is a sub-menu built at start-up (createRCraneMenu(); no "RCrane launch" step); handlers wrapped by _guarded(): INFO line on use, the
                            pre-launch check (checkCootAndReportErrors) at first use, exceptions printed with traceback + message window.  Reason: build 13's "RCrane launch" gave neither menu nor
                            message on the user's iMac; the log has no RCrane line and no traceback; headless the same call works (cause NOT found).  COOT_DISABLE_RCRANE=1 unchanged.
  tests                     gui_python_dialogs.py 39 -> 44 (accept window hide/close order via a spy on the GTK calls, map re-contouring events via COOT_DEBUG_MAPS + fd capture, occupancy slider OK
                            (0.4/0.6, window closed), rename_alt_confs swap, no `if (alt_confs > N)` left, RCrane sub-menu); gui_rcrane.py 20 -> 21 (entry guard: check once / failure blocks / traceback printed);
                            gui_menu_sweep.py no longer needs the "RCrane launch" activation.  All new checks FAIL on the build-13 files (evidence/checks_b13_vs_b14.txt).
  collect-results.sh        new section: lines with RCrane / Traceback / ERROR:: / TypeError ... of the last 3 logs (the 150-line tail used to cut the start-up lines off).
  CHANGELOG.md              new: one file with builds 1-14 (user-facing), shipped in the folder.
  Scheme question answered in the protocol (item 5): Scheme scripting works (simple window); what is missing is guile-gtk (Scheme GUI code); Python GUI scripts replace it.
  Lesson: the headless harness makes Widget.show() a no-op and Dialog.run() answer cancel, so a window that is never shown, or never hidden, cannot be detected by looking at "visible";
          spy on the GTK calls (_c.call) instead.  Python-2 "list > int" comparisons are silent in py2 and TypeErrors in py3 only when the line runs.
  Verified: build 14 zip (sha256 2ef5ed6e...3491) extracted with ditto -x -k into a path with spaces, env -i: 18 suites pass (python-api 19, scheme-api 27, data-and-maps 32, ondemand-read 3, refine-zone 4,
  process-helpers 10, bundle-python 18, bundle-scheme 6, rdkit-python 10, rdkit-scheme 3, gtk2compat 12, gui-scripts 14, gui-dialogs 44, gui-glyco 14, gui-toolbar 13, gui-rcrane 21, refmac-run 8,
  startup-dictionaries 1); sweep 248 ok / 0 err / 5 OpenGL-or-screen-only crashes; bundle_check OK (211 Mach-O, minos 11.0); coot-bin cmp-identical to build 13.  Evidence: evidence/*_b14.txt.
  NOT verified: anything on a screen (items 2-4 above).

Round 15: your round-14 report -> build 15  (patch 0034 round15-rna-stepped-refine-pdb-redo-toolbar; first build made in Claude Code on the user's iMac)
  NO C++ OR LIBRARY CHANGE: bin/coot-bin and lib/ are byte-identical to builds 13-14; changed: python/{fitting,get_ebi}.py, scheme/python-gui-bridge.scm, run-coot.sh, tests, docs.
  User report on build 14: V1 occupancy OK, V2 Stepped Refine fully functional (protein), V3 RCrane sub-menu OK, V4 Scheme window gives no visible result (accepted), V5 MacBook postponed to the end.
  python/fitting.py     (1) RNA/DNA Stepped Refine: refine_auto_range (c-interface-refine.cc) looks the residue up by " CA " -> "Can't get index for resno1" for nucleotides (user log, 9E5H).
                        stepped_refine_centre_atom(): CA, else C1', else P, else first atom; refine_auto_range_any(): CA residues -> refine_auto_range, others -> refine_zone(res-1..res+1, existing only).
                        (2) Stop/Cancel/Continue toolbar buttons: globals overwritten by a second run -> orphaned buttons -> AttributeError 'bool'.destroy (real-window audit, Toolbar > GtkButton).
                        Now run ids, a new run removes the old run's buttons, _multi_refine_remove() tolerates missing widgets, stop/continue after the end are no-ops.
  python/get_ebi.py     get_pdb_redo: pdb-redo.eu returns HTTP 404 + HTML for a missing file of an entry (mmCIF-only entries: no _final.pdb, often no .py/.scm) and HTTP 500 + {"error":"Not Found"}
                        for a missing entry; coot_get_url saves the body.  pdb_redo_download_ok(kind) positively checks PDB records / data_ / 'MTZ ' / not HTML-JSON; bad files removed;
                        fallback <id>_final.cif; maps loaded even without a model; guided tour (.py, Python interesting_things_gui, nested gtk.main by upstream design) only if real; info_dialog on failure.
  scheme/python-gui-bridge.scm   (get-pdb-redo) -> Python get_pdb_redo (the C++ menu calls the Scheme name; Scheme version loaded HTML as .scm and needs guile-gtk interesting-things-gui).
  run-coot.sh           mkdir $HOME/.local/share in the private HOME (GTK recently-used.xbel warnings).
  tests                 refine_python 4->7, data_python 32->39 (fake downloader: mmCIF-only, JSON missing entry, Scheme menu path, tour), gui_python_dialogs 44->45 (Stop then new run),
                        bundle_python 18->19; gui_audit.py skips unmapped (hidden) buttons.  All new checks FAIL on build 14 (evidence/checks_b14_vs_b15.txt).
  Real-window audit on build 14 by me (evidence/gui_audit_claude_b14_iMac.txt): 254 ok, 6 WARN (file chooser GIO criticals, windows destroyed twice by the audit's clicking), 2 ERR (toolbar: fixed;
                        Lidia hidden pe_test_function button, shown upstream only with COOT_LBG_TEST_FUNCTION: audit artifact), 0 NO-HANDLER, 0 CRASH, 0 HANG.  Not repeated on build 15 (user at the screen).
  Scheme simple window (post_scheme_scripting_window / guile_window_enter_callback in c-interface-gui.cc) evaluates but discards the value: needs C++ to show it (next C++ rebuild).
  Verified: build 15 zip, ditto -x -k into a path with spaces, env -i: 18 suites pass (python-api 19, scheme-api 27, data-and-maps 39, ondemand-read 3, refine-zone 7, process-helpers 10,
  bundle-python 19, bundle-scheme 6, rdkit-python 10, rdkit-scheme 3, gtk2compat 12, gui-scripts 14, gui-dialogs 45, gui-glyco 14, gui-toolbar 13, gui-rcrane 21, refmac-run 8,
  startup-dictionaries 1); sweep 248 ok / 0 err / 5 OpenGL-only; bundle_check OK; setup.sh from pristine reproduces coot-src (34 patches).  Live pdb-redo.eu: 9E5H (cif) and 1EHZ load.
  Real window (scripted, window list read inside Coot): RNA Stepped Refine centred on C1'; "PDB_REDO results" window mapped (81 entries); 0XYZ info dialog.  NOT seen: any drawing.
  The zip was re-made once after verification with a corrected TEST-PROTOCOL.md (only file different; sha256 878bf4cf...d165).
  User report (11 Nov, afternoon): W1 Stepped Refine on RNA (1EHZ test data) works "pretty nicely"; W4 RCrane with the test data works.  W2, W3, W5 not yet reported.

Round 16: real-window audit of build 15 -> build 16  (patch 0035 round16-lidia-acedrg-env)
  NO C++ OR LIBRARY CHANGE.  Changed: python/3d_generator_import.py, tests/refmac_run_python.py (+3 checks), run-headless-tests.sh (refmac-run timeout 300 -> 480 s), docs.
  Real-window audit of build 15 on the iMac, 11 Nov 17:05 (user allowed on-screen tests after 17:00; evidence/gui_audit_claude_b15_iMac.txt): 255 ok, 6 WARN (same as build 14:
                        Save Dialog Positions / Model-Fit-Refine destroy twice, LSQ Superpose combo model, 3 x file chooser GIO), 1 ERR, 13 SKIP (network/exit/stereo, 1 insensitive), 0 CRASH, 0 HANG.
                        Both build-14 ERRs are gone (toolbar Stop/Cancel, Lidia hidden test button).
  ERR: Calculate > Ligand Builder: the audit pressed Apply (lbg_apply_button -> prodrg_import_function -> scripting_function -> Python import_from_3d_generator_from_mdl)
                        on an empty sketch (coot-lidia.mdl 0 bytes); CCP4 9 acedrg stopped with a traceback on stderr.  Investigating: acedrg_env() did os.environ["CBIN"]
                        (KeyError when Coot is not started from a CCP4-sourced shell; the launcher keeps CCP4 variables for children only), PATH joined with ";",
                        PYTHONHOME="" but Coot's PYTHONPATH (3.11) passed on to CCP4's Python 3.9.  Used by Lidia Apply, new_molecule_by_smiles_string, SMILES via acedrg, acedrg_link.
                        Now acedrg_env() = ccp4_child_env() + CBIN first on PATH (os.pathsep) - PYTHONHOME/PYTHONPATH; mdl_file_has_atoms_qm(): empty sketch -> info_dialog, return False.
  Tests: refmac-run 8 -> 11 (acedrg_env without CBIN; empty sketch: no generator started + message; benzene mdl -> real acedrg (CCP4 9, ~60 s) -> new model + acedrg-LIG.cif).
                        On build 15: 8/11 (KeyError CBIN), build 16: 11/11 (evidence/checks_b15_vs_b16.txt).
  Real window, COOT_AUDIT_ONLY='Ligand Builder' on build 16: ok (history shows the new message, no acedrg run; evidence/gui_audit_claude_b16_lidia_iMac.txt).  NOT seen: a drawn ligand imported on screen.
  Verified: build 16 zip (sha256 eacbc891...0811), path with spaces, env -i: 18 suites pass (refmac-run 11, others as build 15); sweep 248/0/5; bundle_check OK; setup.sh 35 patches identical.

Round 17: installer -> build 17  (no patch: package files only; coot-bin, lib/, share/coot as build 16)
  User report 13 Nov: X1 (Lidia -> acedrg ligand, ~60 s = acedrg's own run time), X2, W2, W3, W5 confirmed; MacBook M2 Pro: 18 suites pass on build 16
  (evidence/macbook_m2pro_b16_results.txt); W6 run by me (results/m1-results-20261113-092308.txt).  Paul Emsley supports sharing; Bandicoot comparison given.
  User decisions (13 Nov): install to ~/.local/share/coot0 (ask, other path allowed); PATH line added to ~/.zshrc and printed (bash: ~/.bash_profile if
  login shell bash or file exists, ~/.bashrc if it exists); preferences per user (~/Library/Application Support/coot0); keep test-data.
  m1-package: install.sh (checks arm64/Rosetta, macOS >= 11 (26 tested), disk, quarantine, CCP4/Phenix/reduce/probe; copy cp -Rc (APFS clone, mtimes kept)
                        else ditto; same version already there -> moved to .replaced-<time>; marker .coot0-installed; ~/.local/bin/coot0 wrapper (marker line
                        "# coot0-install"; COOT_KEEP_CWD=1 if cwd writable; --diagnose/--self-test/--uninstall); rc lines marked; start test tests/install_check.py),
              uninstall.sh (wrapper, marked rc lines with .before-coot0-uninstall copies, the copy [Y/n], preferences [y/N]), "Install coot0.command",
              README-FIRST.txt, VERSION (0.9.8.96-b17).
  run-coot.sh / collect-results.sh / tests/run-{headless-tests,gui-sweep,gui-audit}.sh: state = COOT_STATE_DIR, else ~/Library/Application Support/coot0 if
              .coot0-installed, else folder if writable, else Application Support/Coot-0.9.8.96.  Launcher: tool search also <apps>/phenix-*/bin and
              ~/phenix-*/bin (Phenix 2.x layout; COOT_APPS_DIR overrides /Applications for tests); log line names the state folder.
  tools/dev_sync.sh copies NEW package files too.  Distribution: coot0-0.9.8.96-b17-macos-arm64.tar.gz, top folder coot0-0.9.8.96-b17,
              COPYFILE_DISABLE=1 tar --no-mac-metadata --no-xattrs -czf (no ._ files; mtimes kept).
  Test: tests/installer_test.sh (19; in run-headless-tests.sh as "installer"): build 16 3/19, build-16 launcher only 15/19, build 17 19/19 (evidence/checks_b16_vs_b17.txt).
  Fix before delivery: install path stored as written but uninstall.sh compared with pwd -P -> under a linked folder (/tmp -> /private/tmp) coot0 was not
              removed.  install.sh now stores the real path; uninstall.sh compares real paths; installer_test checks real paths and runs under TMPDIR=/tmp in
              run-headless-tests (env -i).  First b17 tarball: 15/19 under /tmp; fixed: 19/19.  Verified b17 tarball: 19 suites (installer 19/19 after the fix;
              the other 18 as build 16), sweep 248/0/5, bundle_check OK.  sha256 e70f8045...faad.

Round 18: Retina default for coot0 -> build 18  (no patch: package only)
  User request 13 Nov: --retina default for the installed coot0, --legacy to fall back, README note.
  run-coot.sh: --legacy -> COOT_RETINA=0 (not passed to coot-bin); a copy with .coot0-installed sets COOT_RETINA=1 if unset (env wins).  The seam reads
  COOT_RETINA: set and not "0" = on.  Unpacked folder unchanged (standard).  install.sh: wrapper comment + summary line; README-FIRST.txt section RESOLUTION.
  installer_test 19 -> 22 (coot0 default retina=1; --legacy retina=0 + Coot starts; folder retina=0): build 17 20/22, build 18 22/22.
  User 13 Nov: build 18 works.  The Gatekeeper "coot-bin Not Opened" dialog (12:25, again ~14:00) came from MY installer test: the new
  "unpacked folder keeps standard resolution" check started the copy whose files the test flags with com.apple.quarantine on purpose
  (COOT_IGNORE_QUARANTINE=1); the check still passed because it read the launcher's log line written before exec.  Fix: clear the flag
  on that copy first, require INSTALL-CHECK OK, and check that no started copy was flagged (installer 22 -> 23).  Ships with the next build.
  Licensing (user 13 Nov): Coot GPL-3.0-or-later (unchanged, its authors); coot0 modifications Copyright (C) 2026 Chang Sun, GPL-3.0-only,
  stated separately (LICENSING.md); package as a whole GPL-3.0.  Credits: Huilin Li's lab (feedback), Paul Emsley (support).

Round 19: licences in the package -> build 19 (the build for the lab; no patch)
  LICENSE / LICENSING.md / CORRESPONDING_SOURCE.md (repository root) + m1-package/THIRD_PARTY_LICENSES.md + licenses/ are copied to the package top
  level (tools/dev_sync.sh).  gen_licenses.py: 60 conda packages + 7 extra components; FFTW 2 text copied from the clipper package, FreeType 2.14.3
  FTL.TXT/LICENSE.TXT (from its source tag VER-2-14-3) and an SQLite public-domain note in tools/licence-texts/.  LICENSING/CORRESPONDING_SOURCE
  point lab members to the author (repository private).  installer_test 23 -> 26 (licence files, a text per package, README-FIRST): b18 23/26, b19 26/26.

Round 20: Refine/Improve Ramachandran Plot menu + Fit Protein shown refinement -> build 20  (patch 0036 fit-protein-rama-shown-refinement; Python only)
  User request 16 Nov.  extensions.py: the add_simple_coot_menu_menuitem for "Refine/Improve Ramachandran Plot..." was indented inside fit_protein_func3
  (also in the pristine 0.9.8.96 source): dedented.  fitting.py: refine_and_show(imol, refine, seconds, force) = the old body of
  refine_auto_range_and_show (ordinary refinement, hide "Accept Refinement?", pump events for stepped_refine_show_seconds, Stop, accept);
  fit_protein_fit_function: refine_zone through refine_and_show (was NoBackups + AutoAccept = immediate replacement), centre atom via
  stepped_refine_centre_atom + set_go_to_atom_chain_residue_atom_name_full + update_maps, steps/frame 400 during the residue.  Rotamer step unchanged.
  Tests: gui_python_load.py check(): only None/True pass (any returned message passed before; all old checks still pass on b19);
  + menu entry in All Molecule and it opens a window.  gui_python_dialogs.py shown_refinement(): spies refine_zone/refine_auto_range (immediate
  replacement state at the call) and accept_regularizement (refinement_already_ongoing_p, time >= 0.4 s later); use_graphics_interface_state forced to 1.
  Note: a first version of the tests passed on b19 (AutoAccept also calls accept_regularizement while the refinement counts as ongoing, and the CA
  go-to re-contours) - the immediate-replacement state is the real difference.  b19: gui-scripts 14/15, gui-dialogs 46/48; b20 15/15, 48/48.
  User 16 Nov: BB1-BB4 confirmed on screen.

Round 21: Refine/Improve Ramachandran Plot (try peptide flips) -> build 21  (patch 0037 rama-try-peptide-flips; Python only)
  User request 16 Nov (option a: new entry, original unchanged).  fitting.py fit_protein_rama_flip_function: per residue i (protein i and i+1, no ins
  code, no alt confs): save coords of i-1..i+1; try A refine_zone(i-1, i+1) via refine_and_show with set_refine_ramachandran_angles(1); score =
  (sum of all_molecule_ramachandran_region_py regions of i, i+1 [rama_plot::RAMA_OUTLIER 0 / ALLOWED 1 / PREFERRED 2], n classified,
  density_score_residue sum); save A; restore original (set_atom_attributes x/y/z); pepflip(i) (flips peptide i/i+1, coot::pepflip on the residue
  with the CO); try B; rama_flip_better(): higher region sum, or equal and density >= +10% (rama_flip_density_gain); else restore A.  Stop
  (continue_multi_refine False) after A: keep A.  Note continue_multi_refine is False at load: tests set it True.  density_score_residue in Python
  takes a residue spec (redefine_functions.py -> density_score_residue_py).  Exploration (tutorial-modern + rnasa map): deliberate flips of
  A 20/43/60/85 put back (O 0.04-0.15 A), A 30/50/70/90 kept; A 60 by density (+25%).  Tests: gui-scripts 16, gui-dialogs 53; b20 15/16, 48/53.
  Fill Partial Residues (user question): works headless (Arg A 40 side chain / + CB removed -> 11 atoms, with and without map); a residue missing
  N/CA/C (tutorial-modern Cys A 72) is listed but not filled (mutate needs the main chain).  User's case pending details (CC5).
