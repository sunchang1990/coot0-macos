# Extra Ligand Functions

[Scripting reference](../README.md) > Extra Ligand Functions (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_animated_ligand_interaction

Python: `add_animated_ligand_interaction(imol, lb)`  
Scheme: `(add-animated-ligand-interaction imol lb)`

Arguments: imol (a whole number), lb (`coot::fle_ligand_bond_t`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### cootaneer_internal

Python: `cootaneer_internal(imol_map, imol_model, atom_spec)`  
Scheme: `(cootaneer-internal imol-map imol-model atom-spec)`

Arguments: imol_map (a whole number), imol_model (a whole number), atom_spec (`coot::atom_spec_t`). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### ligand_search_make_conformers

Python: `ligand_search_make_conformers()`  
Scheme: `(ligand-search-make-conformers)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `ligand_search_make_conformers_py`.
Also available in Scheme as `ligand-search-make-conformers-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ligand_search_make_conformers()` | ran, returned `[]` |
| Scheme | `(ligand-search-make-conformers)` | ran, returned `()` |

Python and Scheme gave the same answer.

### ligand_search_make_conformers_internal

Python: `ligand_search_make_conformers_internal()`  
Scheme: `(ligand-search-make-conformers-internal)`

Arguments: none. Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ligand_search_make_conformers_internal()` | ran, returned `()` |
| Scheme | `(ligand-search-make-conformers-internal)` | ran, returned `#()` |

Python and Scheme gave the same answer.

