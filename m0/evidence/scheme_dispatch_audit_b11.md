# C++ -> Scheme dispatch audit (build 11)

Coot 0.9.8.96 is built with Guile (scripting) and Python. It has no guile-gtk (no `gtk-*` procedures), so the scripted GUI is Python.
Where C++ decides between the two languages there are four cases:

| mechanism | sites | status in build 11 |
|---|---|---|
| `#if defined USE_GUILE && !defined COOT_GUI_VIA_PYTHON` (patch 0023) | 16 (mutate sequence, fit loop, copy molecule/fragment, merge, multi-refine toolbar, post-ligand-fit, ...) | Python GUI; tests in gui-dialogs |
| runtime `prefer_python` (default 1 in this build: `USE_GUILE` without `USE_GUILE_GTK`, with `USE_PYTHON`; checked `coot.prefer_python() == 1`) | `click-protein-db-loop-gui` (Fit Loop by DB search), `place-strand-here-gui`, `reduce-on-pdb-file-no-flip`, drug lookup, NCS skip keys | Python |
| `#ifdef USE_GUILE` only, Scheme function without guile-gtk need | `(get-refmac-version)`, `fit-chain`, `(get-pdb-redo ...)`, `(get-ebi-pdb-and-sfs ...)`, `(get-ccp4srs-monomer-and-overlay ...)`, key-press hooks | Scheme, works (`get-ebi-pdb`: the `.ent` URL is stale (404), the `.cif` fallback works, tested with network) |
| `#ifdef USE_GUILE` only, Scheme function needs guile-gtk | `run-refmac-by-filename` (Calculate > Run Refmac), `interesting-things-with-fix-maybe` (Validate > GLN and ASN B-factor Outliers) | **bridged to Python in build 11** (`scheme/python-gui-bridge.scm`) |
| same, not reachable from the GUI or not available | `open-coot-listener-socket-with-timeout` (remote control, command line `--port` only), `(render-image)` / `(raytrace ...)` (external Raster3D/povray), `get-eds-pdb-and-mtz` (EDS server), `molecule-chooser-gui` in `junk.cc` (dead code: the Undo Molecule chooser is a Glade dialog) | not changed; listed as known gaps |

Scheme procedures that C++ can ask for and that are unbound in this build (checked with `(defined? 'name)`): `place-strand-here-gui`, `smiles-gui`, `molecule-chooser-gui`,
`interesting-things-with-fix-maybe` (now defined by the bridge), `interesting-things-gui`, `coot-gui`, `gtk-timeout-add`, `gtk-idle-add`, `coot-menubar-menu`, `add-simple-coot-menu-menuitem`.
Compile-level fix for a later rebuild: add `&& !defined COOT_GUI_VIA_PYTHON` to the remaining `#ifdef USE_GUILE` GUI sites in `c-interface-refmac.cc` (execute_refmac_real) and
`c-interface-validate.cc` (gln_asn_b_factor_outliers); the bridge makes that unnecessary.
