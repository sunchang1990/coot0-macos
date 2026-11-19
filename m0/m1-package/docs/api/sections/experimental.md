# Experimental

[Scripting reference](../README.md) > Experimental (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_ligand_builder_menu_item_maybe

Python: `add_ligand_builder_menu_item_maybe()`  
Scheme: `(add-ligand-builder-menu-item-maybe)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_builder_menu_item_maybe()` | ran (no return value) |
| Scheme | `(add-ligand-builder-menu-item-maybe)` | ran (no return value) |

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

### all_molecule_rotamer_score

Python: `all_molecule_rotamer_score(imol)`  
Scheme: `(all-molecule-rotamer-score imol)`

a stub currently

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `all_molecule_rotamer_score_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `all_molecule_rotamer_score(0)` | ran, returned `[-197.50514814092332, 160]` |
| Scheme | `(all-molecule-rotamer-score 0)` | ran, returned `(-197.50514814092332 160)` |

### fetch_and_superpose_alphafold_models_using_active_molecule

Python: `fetch_and_superpose_alphafold_models_using_active_molecule()`  
Scheme: `(fetch-and-superpose-alphafold-models-using-active-molecule)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fetch_and_superpose_alphafold_models_using_active_molecule()` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |
| Scheme | `(fetch-and-superpose-alphafold-models-using-active-molecule)` | not run: not run automatically (fetch: exits, uses the network, an external program, files or a screen) |

### full_screen

Python: `full_screen(mode)`  
Scheme: `(full-screen mode)`

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `full_screen(1)` | ran (no return value) |
| Scheme | `(full-screen 1)` | ran (no return value) |

### globularize

Python: `globularize(imol)`  
Scheme: `(globularize imol)`

globularize the molecule.

This is not guaranteed to generate the correct biological entity, but will bring together
molecules (chains/domains) that are dispersed throughout the unit cell.

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `globularize(0)` | ran (no return value) |
| Scheme | `(globularize 0)` | ran (no return value) |

### start_ligand_builder_gui

Python: `start_ligand_builder_gui()`  
Scheme: `(start-ligand-builder-gui)`

display the ligand builder dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `start_ligand_builder_gui()` | not tried |
| Scheme | `(start-ligand-builder-gui)` | not tried |

### user_defined_click

Python: `user_defined_click(n_clicks, func)`  
Scheme: `(user-defined-click n-clicks func)`

Arguments: n_clicks (a whole number), func (a list or value). Returns: nothing.
Also available in Python as `user_defined_click_py`.
Also available in Scheme as `user-defined-click-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

