# Spin Search Functions

[Scripting reference](../README.md) > Spin Search Functions (9 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### CG_spin_search_py

Python: `CG_spin_search_py(imol_model, imol_map)`  
Scheme: `(CG-spin-search imol-model imol-map)`

Spin search the density based on possible positions of CG of a side-chain

Arguments: imol_model (a whole number), imol_map (a whole number). Returns: a value (see the result of the example).
Also available in Scheme as `CG-spin-search-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `CG_spin_search_py(0, 1)` | ran, returned `[[-24.0, [True, 'A', 1, '']], [9.0, [True, 'A', 8, '']], [-3.0, [True, 'A', 11, '']], [3.0, [True, 'A', 14, '']], [3.0,  ...` |
| Scheme | `(CG-spin-search 0 1)` | ran, returned `(((#t "A" 1 "") -24.0) ((#t "A" 8 "") 9.0) ((#t "A" 11 "") -3.0) ((#t "A" 14 "") 3.0) ((#t "A" 17 "") 3.0) ((#t "A" 19 " ...` |

### monomer_lib_3_letter_codes_matching

Python: `monomer_lib_3_letter_codes_matching(search_string, allow_minimal_descriptions_flag)`  
Scheme: `(monomer-lib-3-letter-codes-matching search-string allow-minimal-descriptions-flag)`

Arguments: search_string (text), allow_minimal_descriptions_flag (a whole number). Returns: a list.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `monomer_lib_3_letter_codes_matching("hello", 1)` | not tried |
| Scheme | `(monomer-lib-3-letter-codes-matching "hello" 1)` | not tried |

### mutate_internal

Python: `mutate_internal(ires, chain_id, imol, target_res_type)`  
Scheme: `(mutate-internal ires chain-id imol target-res-type)`

Arguments: ires (a whole number), chain_id (text), imol (a whole number), target_res_type (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mutate_internal(41, "A", 0, "ALA")` | not tried |
| Scheme | `(mutate-internal 41 "A" 0 "ALA")` | not tried |

### on_monomer_lib_sbase_molecule_button_press

Python: `on_monomer_lib_sbase_molecule_button_press(button, user_data)`  
Scheme: `(on-monomer-lib-sbase-molecule-button-press button user-data)`

Arguments: button (`GtkButton *`), user_data (`gpointer`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### on_monomer_lib_search_results_button_press

Python: `on_monomer_lib_search_results_button_press(button, user_data)`  
Scheme: `(on-monomer-lib-search-results-button-press button user-data)`

Arguments: button (`GtkButton *`), user_data (`gpointer`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### overlap_ligands_internal

Python: `overlap_ligands_internal(imol_ligand, imol_ref, chain_id_ref, resno_ref, apply_rtop_flag)`  
Scheme: `(overlap-ligands-internal imol-ligand imol-ref chain-id-ref resno-ref apply-rtop-flag)`

Arguments: imol_ligand (a whole number), imol_ref (a whole number), chain_id_ref (text), resno_ref (a whole number), apply_rtop_flag (true or false). Returns: `coot::graph_match_info_t`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `overlap_ligands_internal(0, 0, "A", 41, 1)` | not tried |
| Scheme | `(overlap-ligands-internal 0 0 "A" 41 1)` | not tried |

### spin_N

Python: `spin_N(imol, residue_spec, angle)`  
Scheme: `(spin-N-scm imol residue-spec-scm angle)`

Spin N and CB (and the rest of the side chain if extant)
 Sometime on N-terminal addition, then N ends up pointing the wrong way.
 The allows us to (more or less) interchange the positions of the CB and the N.
 angle is in degrees.

Arguments: imol (a whole number), residue_spec (a list or value), angle (a number). Returns: nothing.
Also available in Python as `spin_N_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `spin_N(0, ["A", 41, ""], 10.0)` | not tried |
| Scheme | `(spin-N-scm 0 (list "A" 41 "") 10.0)` | not tried |

### spin_search

Python: `spin_search(imol_map, imol, chain_id, resno, ins_code, direction_atoms_list, moving_atoms_list)`  
Scheme: `(spin-search imol-map imol chain-id resno ins-code direction-atoms-list moving-atoms-list)`

for the given residue, spin the atoms in moving_atom_list...
 around the bond defined by direction_atoms_list looking for the best
 fit to density of imom_map map of the first atom in
 moving_atom_list. Works (only) with atoms in altconf ""

Arguments: imol_map (a whole number), imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), direction_atoms_list (a list or value), moving_atoms_list (a list or value). Returns: nothing.
Also available in Python as `spin_search_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not tried |
| Scheme | (no automatic example) | not tried |

### spin_search_by_atom_vectors

Python: `spin_search_by_atom_vectors(imol_map, imol, chain_id, resno, ins_code, direction_atoms_list, moving_atoms_list)`  
Scheme: `(spin-search-by-atom-vectors imol-map imol chain-id resno ins-code direction-atoms-list moving-atoms-list)`

Arguments: imol_map (a whole number), imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), direction_atoms_list (text), moving_atoms_list (a list). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `spin_search_by_atom_vectors(1, 0, "A", 41, "", ".", "hello")` | not tried |
| Scheme | `(spin-search-by-atom-vectors 1 0 "A" 41 "" "." "hello")` | not tried |

