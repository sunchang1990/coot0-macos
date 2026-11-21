# Experimental

[Scripting reference](../README.md) > Experimental (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_ligand_builder_menu_item_maybe

Python: `add_ligand_builder_menu_item_maybe()`  
Scheme: `(add-ligand-builder-menu-item-maybe)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_builder_menu_item_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(add-ligand-builder-menu-item-maybe)` | ran (no return value, nothing visible changed) |

### all_molecule_ramachandran_region

Python: `all_molecule_ramachandran_region(imol)`

a stub currently

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `all_molecule_ramachandran_region_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_molecule_ramachandran_region(0)` | ran, returned `[([True, 'A', 2, ''], 2), ([True, 'A', 3, ''], 1), ([True, 'A', 4, ''], 2), ([True, 'A', 5, ''], 2), ([True, 'A', 6, ''] ...` |

### all_molecule_ramachandran_score

Python: `all_molecule_ramachandran_score(imol)`  
Scheme: `(all-molecule-ramachandran-score imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `all_molecule_ramachandran_score_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_molecule_ramachandran_score(0)` | ran, returned `[-281.4500914078069, 183, -235.4046792835865, 123, 0, [[[-80.1338765510191, 130.8971531422487], [True, 'A', 2, ''], 0.21 ...` |
| Scheme | `(all-molecule-ramachandran-score 0)` | ran, returned `(-281.4500914078069 183 -235.4046792835865 123 0 (((-80.1338765510191 130.8971531422487) (#t "A" 2 "") 0.215748766869011 ...` |

Python and Scheme gave the same answer.

### all_molecule_rotamer_score

Python: `all_molecule_rotamer_score(imol)`  
Scheme: `(all-molecule-rotamer-score imol)`

a stub currently

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `all_molecule_rotamer_score_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_molecule_rotamer_score(0)` | ran, returned `[-195.6084282377372, 159]` |
| Scheme | `(all-molecule-rotamer-score 0)` | ran, returned `(-195.6084282377372 159)` |

Python and Scheme gave the same answer.

### fetch_and_superpose_alphafold_models_using_active_molecule

Python: `fetch_and_superpose_alphafold_models_using_active_molecule()`  
Scheme: `(fetch-and-superpose-alphafold-models-using-active-molecule)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_and_superpose_alphafold_models_using_active_molecule()` | not run: uses the network |
| Scheme | `(fetch-and-superpose-alphafold-models-using-active-molecule)` | not run: uses the network |

Example written and checked by hand on the test data. Expected: downloads AlphaFold models for the active molecule's sequence and superposes them.

### full_screen

Python: `full_screen(mode)`  
Scheme: `(full-screen mode)`

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `full_screen(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(full-screen 1)` | ran (no return value, nothing visible changed) |

### globularize

Python: `globularize(imol)`  
Scheme: `(globularize imol)`

globularize the molecule.

This is not guaranteed to generate the correct biological entity, but will bring together
molecules (chains/domains) that are dispersed throughout the unit cell.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `globularize(0)` | ran (no return value); changed: molecule 0: coordinates of 76 residue(s) (A5, A6, A7, A8 ...) |
| Scheme | `(globularize 0)` | ran (no return value); changed: molecule 0: coordinates of 76 residue(s) (A5, A6, A7, A8 ...) |

### start_ligand_builder_gui

Python: `start_ligand_builder_gui()`  
Scheme: `(start-ligand-builder-gui)`

display the ligand builder dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `start_ligand_builder_gui()` | ran (no return value, nothing visible changed) |
| Scheme | `(start-ligand-builder-gui)` | ran (no return value, nothing visible changed) |

### user_defined_click

Python: `user_defined_click(n_clicks, func)`  
Scheme: `(user-defined-click n-clicks func)`

Arguments: n_clicks (a whole number), func (a list or value). Returns: nothing.
Also available in Python as `user_defined_click_py`.
Also available in Scheme as `user-defined-click-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `user_defined_click(1, lambda *args: print("clicked", args))` | ran (no return value, nothing visible changed) |
| Scheme | `(user-defined-click 1 (lambda args (display args)))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: the function is called with the clicked atom specs after n_clicks clicks; nothing happens until atoms are clicked.

Note: Only arming verified headless; the callback itself needs clicks in the graphics window.

