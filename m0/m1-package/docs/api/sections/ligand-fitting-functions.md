# Ligand Fitting Functions

[Scripting reference](../README.md) > Ligand Fitting Functions (26 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_ligand_clear_ligands

Python: `add_ligand_clear_ligands()`  
Scheme: `(add-ligand-clear-ligands)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_clear_ligands()` | ran (no return value) |
| Scheme | `(add-ligand-clear-ligands)` | ran (no return value) |

### add_ligand_search_ligand_molecule

Python: `add_ligand_search_ligand_molecule(imol_ligand)`  
Scheme: `(add-ligand-search-ligand-molecule imol-ligand)`

add a rigid ligand molecule to the list of ligands to search for
 in ligand searching

Arguments: imol_ligand (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_search_ligand_molecule(0)` | ran (no return value) |
| Scheme | `(add-ligand-search-ligand-molecule 0)` | ran (no return value) |

### add_ligand_search_wiggly_ligand_molecule

Python: `add_ligand_search_wiggly_ligand_molecule(imol_ligand)`  
Scheme: `(add-ligand-search-wiggly-ligand-molecule imol-ligand)`

add a flexible ligand molecule to the list of ligands to search for
 in ligand searching

Arguments: imol_ligand (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_ligand_search_wiggly_ligand_molecule(0)` | ran (no return value) |
| Scheme | `(add-ligand-search-wiggly-ligand-molecule 0)` | ran (no return value) |

### analyse_ligand_differences

Python: `analyse_ligand_differences(imol_ligand, imol_ref, chain_id_ref, resno_ref)`  
Scheme: `(analyse-ligand-differences imol-ligand imol-ref chain-id-ref resno-ref)`

Arguments: imol_ligand (a whole number), imol_ref (a whole number), chain_id_ref (text), resno_ref (a whole number). Returns: a value (see the result of the example).
Also available in Python as `analyse_ligand_differences_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `analyse_ligand_differences(0, 0, "A", 41)` | ran, returned `[[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [78.85041640521314, 7]]` |
| Scheme | `(analyse-ligand-differences 0 0 "A" 41)` | ran, returned `(((0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0) (0.0 0.0 0.0)) (78.85041640521314 7))` |

### compare_ligand_atom_types_py

Python: `compare_ligand_atom_types_py(imol_ligand, imol_ref, chain_id_ref, resno_ref)`  
Scheme: `(compare-ligand-atom-types-scm imol-ligand imol-ref chain-id-ref resno-ref)`

Arguments: imol_ligand (a whole number), imol_ref (a whole number), chain_id_ref (text), resno_ref (a whole number). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `compare_ligand_atom_types_py(0, 0, "A", 41)` | ran, returned `2` |
| Scheme | `(compare-ligand-atom-types-scm 0 0 "A" 41)` | ran, returned `2` |

### do_find_ligands_dialog

Python: `do_find_ligands_dialog()`  
Scheme: `(do-find-ligands-dialog)`

display the find ligands dialog

 if maps, coords and ligands are available, that is.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_find_ligands_dialog()` | ran (no return value) |
| Scheme | `(do-find-ligands-dialog)` | ran (no return value) |

### exchange_ligand

Python: `exchange_ligand(imol_lig, chain_id_lig, resno_lig, ins_code_lig)`  
Scheme: `(exchange-ligand imol-lig chain-id-lig resno-lig ins-code-lig)`

Just pondering - just a stub currently.

 For use with exporting ligands from the 2D sketcher to the main
 coot window. It should find the residue that this residue is
 sitting on top of that is in a molecule that has lot of atoms
 (i.e. is a protein) and create a new molecule that is a copy of the
 molecule without the residue/ligand that this (given) ligand
 overlays - and a copy of this given ligand.

Arguments: imol_lig (a whole number), chain_id_lig (text), resno_lig (a whole number), ins_code_lig (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `exchange_ligand(0, "A", 41, "")` | ran, returned `-1` |
| Scheme | `(exchange-ligand 0 "A" 41 "")` | ran, returned `-1` |

### execute_ligand_search

Python: `execute_ligand_search()`  
Scheme: `(execute-ligand-search)`

Arguments: none. Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_ligand_search()` | ran, returned `[]` |
| Scheme | `(execute-ligand-search)` | ran (no return value) |

### flip_ligand

Python: `flip_ligand(imol, chain_id, resno)`  
Scheme: `(flip-ligand imol chain-id resno)`

flip the ligand (usually active residue) around its eigen vectors
 to the next flip number. Immediate replacement (like flip
 peptide).

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `flip_ligand(0, "A", 41)` | ran (no return value) |
| Scheme | `(flip-ligand 0 "A" 41)` | ran (no return value) |

### jed_flip

Python: `jed_flip(imol, chain_id, res_no, ins_code, atom_name, alt_conf, invert_selection)`  
Scheme: `(jed-flip imol chain-id res-no ins-code atom-name alt-conf invert-selection)`

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), ins_code (text), atom_name (text), alt_conf (text), invert_selection (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `jed_flip(0, "A", 41, "", " CA ", "", 1)` | not tried |
| Scheme | `(jed-flip 0 "A" 41 "" " CA " "" 1)` | not tried |

### ligand_expert

Python: `ligand_expert()`  
Scheme: `(ligand-expert)`

this sets the flag to have expert option ligand entries in
 the Ligand Searching dialog

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ligand_expert()` | not tried |
| Scheme | `(ligand-expert)` | not tried |

### match_ligand_atom_names

Python: `match_ligand_atom_names(imol_ligand, chain_id_ligand, resno_ligand, ins_code_ligand, imol_reference, chain_id_reference, resno_reference, ins_code_reference)`  
Scheme: `(match-ligand-atom-names imol-ligand chain-id-ligand resno-ligand ins-code-ligand imol-reference chain-id-reference resno-reference ins-code-reference)`

Match ligand atom names

 By using graph matching, make the names of the atoms of the
 given ligand/residue match those of the reference residue/ligand as
 closely as possible - where there would be an atom name clash, invent
 a new atom name.

Arguments: imol_ligand (a whole number), chain_id_ligand (text), resno_ligand (a whole number), ins_code_ligand (text), imol_reference (a whole number), chain_id_reference (text), resno_reference (a whole number), ins_code_reference (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `match_ligand_atom_names(0, "A", 41, "", 0, "A", 41, "")` | not tried |
| Scheme | `(match-ligand-atom-names 0 "A" 41 "" 0 "A" 41 "")` | not tried |

### match_ligand_atom_names_to_comp_id

Python: `match_ligand_atom_names_to_comp_id(imol_ligand, chain_id_ligand, resno_ligand, ins_code_ligand, comp_id_ref)`  
Scheme: `(match-ligand-atom-names-to-comp-id imol-ligand chain-id-ligand resno-ligand ins-code-ligand comp-id-ref)`

Match ligand atom names to a reference ligand type (comp_id)

 By using graph matching, make the names of the atoms of the
 given ligand/residue match those of the reference ligand from the
 geometry store as closely as possible. Where there would be an
 atom name clash, invent a new atom name.

 This doesn't create a new dictionary for the selected ligand -
 and that's a big problem (see match_residue_and_dictionary).

Arguments: imol_ligand (a whole number), chain_id_ligand (text), resno_ligand (a whole number), ins_code_ligand (text), comp_id_ref (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `match_ligand_atom_names_to_comp_id(0, "A", 41, "", "hello")` | not tried |
| Scheme | `(match-ligand-atom-names-to-comp-id 0 "A" 41 "" "hello")` | not tried |

### match_ligand_torsions

Python: `match_ligand_torsions(imol_ligand, imol_ref, chain_id_ref, resno_ref)`  
Scheme: `(match-ligand-torsions imol-ligand imol-ref chain-id-ref resno-ref)`

Arguments: imol_ligand (a whole number), imol_ref (a whole number), chain_id_ref (text), resno_ref (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `match_ligand_torsions(0, 0, "A", 41)` | not tried |
| Scheme | `(match-ligand-torsions 0 0 "A" 41)` | not tried |

### overlap_ligands

Python: `overlap_ligands(imol_ligand, imol_ref, chain_id_ref, resno_ref)`  
Scheme: `(overlap-ligands imol-ligand imol-ref chain-id-ref resno-ref)`

Overlap residue with "template"-based matching.

 Overlap the first residue in
 imol_ligand onto the residue specified by the reference parameters.
 Use graph matching, not atom names.

Returns success status, False = failed to find residue in either
imol_ligand or imo_ref. If success, return the RT operator.

Arguments: imol_ligand (a whole number), imol_ref (a whole number), chain_id_ref (text), resno_ref (a whole number). Returns: a value (see the result of the example).
Also available in Python as `overlap_ligands_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `overlap_ligands(0, 0, "A", 41)` | not tried |
| Scheme | `(overlap-ligands 0 0 "A" 41)` | not tried |

### set_find_ligand_do_real_space_refinement

Python: `set_find_ligand_do_real_space_refinement(state)`  
Scheme: `(set-find-ligand-do-real-space-refinement state)`

fit the top n ligands,
 not all of them, default
 10.

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_ligand_do_real_space_refinement(1)` | not tried |
| Scheme | `(set-find-ligand-do-real-space-refinement 1)` | not tried |

### set_find_ligand_here_cluster

Python: `set_find_ligand_here_cluster(state)`  
Scheme: `(set-find-ligand-here-cluster state)`

Allow the user a scripting means to find ligand at the rotation centre

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_ligand_here_cluster(1)` | not tried |
| Scheme | `(set-find-ligand-here-cluster 1)` | not tried |

### set_find_ligand_mask_waters

Python: `set_find_ligand_mask_waters(istate)`  
Scheme: `(set-find-ligand-mask-waters istate)`

how shall we treat the waters during ligand fitting?

 pass with istate=1 for waters to mask the map in the same way that
 protein atoms do.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_ligand_mask_waters(1)` | not tried |
| Scheme | `(set-find-ligand-mask-waters 1)` | not tried |

### set_find_ligand_multi_solutions_per_cluster

Python: `set_find_ligand_multi_solutions_per_cluster(lim_1, lim_2)`  
Scheme: `(set-find-ligand-multi-solutions-per-cluster lim-1 lim-2)`

allow multiple ligand solutions per cluster.

The first limit is the fraction of the top scored positions that go on
to correlation scoring (closer to 1 means less and faster - default
0.7).

The second limit is the fraction of the top correlation score that is
considered interesting. Limits the number of solutions displayed to
user. Default 0.9.

There is currently no chi-angle set redundancy filtering - I suspect
that there should be.

Nino-mode.

Arguments: lim_1 (a number), lim_2 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_ligand_multi_solutions_per_cluster(1.0, 1.0)` | not tried |
| Scheme | `(set-find-ligand-multi-solutions-per-cluster 1.0 1.0)` | not tried |

### set_find_ligand_n_top_ligands

Python: `set_find_ligand_n_top_ligands(n)`  
Scheme: `(set-find-ligand-n-top-ligands n)`

search the top n sites for ligands.

 Default 10.

Arguments: n (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_find_ligand_n_top_ligands(1)` | not tried |
| Scheme | `(set-find-ligand-n-top-ligands 1)` | not tried |

### set_ligand_acceptable_fit_fraction

Python: `set_ligand_acceptable_fit_fraction(f)`  
Scheme: `(set-ligand-acceptable-fit-fraction f)`

set the fraction of atoms which must be in positive density
 after a ligand fit

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_acceptable_fit_fraction(1.0)` | not tried |
| Scheme | `(set-ligand-acceptable-fit-fraction 1.0)` | not tried |

### set_ligand_cluster_sigma_level

Python: `set_ligand_cluster_sigma_level(f)`  
Scheme: `(set-ligand-cluster-sigma-level f)`

set the default sigma level that the map is searched to
 find potential ligand sites

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_cluster_sigma_level(1.0)` | not tried |
| Scheme | `(set-ligand-cluster-sigma-level 1.0)` | not tried |

### set_ligand_flexible_ligand_n_samples

Python: `set_ligand_flexible_ligand_n_samples(i)`  
Scheme: `(set-ligand-flexible-ligand-n-samples i)`

set the number of conformation samples

 big ligands require more samples. Default 10.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_flexible_ligand_n_samples(1)` | not tried |
| Scheme | `(set-ligand-flexible-ligand-n-samples 1)` | not tried |

### set_ligand_search_map_molecule

Python: `set_ligand_search_map_molecule(imol_map)`  
Scheme: `(set-ligand-search-map-molecule imol-map)`

set the map molecule for ligand searching

Arguments: imol_map (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_search_map_molecule(1)` | not tried |
| Scheme | `(set-ligand-search-map-molecule 1)` | not tried |

### set_ligand_search_protein_molecule

Python: `set_ligand_search_protein_molecule(imol)`  
Scheme: `(set-ligand-search-protein-molecule imol)`

set the protein molecule for ligand searching

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_search_protein_molecule(0)` | not tried |
| Scheme | `(set-ligand-search-protein-molecule 0)` | not tried |

### set_ligand_verbose_reporting

Python: `set_ligand_verbose_reporting(i)`  
Scheme: `(set-ligand-verbose-reporting i)`

default 50: Really?

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ligand_verbose_reporting(1)` | not tried |
| Scheme | `(set-ligand-verbose-reporting 1)` | not tried |

