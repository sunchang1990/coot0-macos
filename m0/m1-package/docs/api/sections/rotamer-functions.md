# Rotamer Functions

[Scripting reference](../README.md) > Rotamer Functions (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### auto_fit_best_rotamer

Python: `auto_fit_best_rotamer(resno, altloc, insertion_code, chain_id, imol_coords, imol_map, clash_flag, lowest_probability)`  
Scheme: `(auto-fit-best-rotamer resno altloc insertion-code chain-id imol-coords imol-map clash-flag lowest-probability)`

auto fit by rotamer search.

 return the score, for some not very good reason. clash_flag
 determines if we use clashes with other residues in the score for
 this rotamer (or not). It would be cool to call this from a script
 that went residue by residue along a (newly-built) chain (now available).

Arguments: resno (a whole number), altloc (text), insertion_code (text), chain_id (text), imol_coords (a whole number), imol_map (a whole number), clash_flag (a whole number), lowest_probability (a number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `auto_fit_best_rotamer(41, "", "", "A", 0, 1, 1, 1.0)` | ran, returned `5.950581073760986` |
| Scheme | `(auto-fit-best-rotamer 41 "" "" "A" 0 1 1 1.0)` | ran, returned `5.950581073760986` |

Python and Scheme gave the same answer.

### do_rotamers

Python: `do_rotamers(atom_index, imol)`  
Scheme: `(do-rotamers atom-index imol)`

moving_atoms_asc

Arguments: atom_index (a whole number), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_rotamers(0, 0)` | ran (no return value) |
| Scheme | `(do-rotamers 0 0)` | ran (no return value) |

### fill_partial_residue

Python: `fill_partial_residue(imol, chain_id, resno, inscode)`  
Scheme: `(fill-partial-residue imol chain-id resno inscode)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `fill_partial_residue(0, "A", 41, "")` | ran (no return value) |
| Scheme | `(fill-partial-residue 0 "A" 41 "")` | ran (no return value) |

### de_chainsaw

Python: `de_chainsaw(imol)`  
Scheme: `(fill-partial-residues imol)`

fill all the residues of molecule number imol that have
 missing atoms.

To be used to remove the effects of chainsaw.

Arguments: imol (a whole number). Returns: nothing.
Also available in Python as `fill_partial_residues`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `de_chainsaw(0)` | ran (no return value) |
| Scheme | `(fill-partial-residues 0)` | ran (no return value) |

### get_rotamer_name

Python: `get_rotamer_name(imol, chain_id, resno, ins_code)`  
Scheme: `(get-rotamer-name imol chain-id resno ins-code)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a value (see the result of the example).
Also available in Python as `get_rotamer_name_py`.
Also available in Scheme as `get-rotamer-name-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_rotamer_name(0, "A", 41, "")` | ran, returned `''` |
| Scheme | `(get-rotamer-name 0 "A" 41 "")` | ran, returned `""` |

Python and Scheme gave the same answer.

### missing_atom_info

Python: `missing_atom_info(imol)`  
Scheme: `(missing-atom-info imol)`

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `missing_atom_info_py`.
Also available in Scheme as `missing-atom-info-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `missing_atom_info(0)` | ran, returned `[['A', 72, '']]` |
| Scheme | `(missing-atom-info 0)` | ran, returned `(("A" 72 ""))` |

Python and Scheme gave the same answer.

### n_rotamers

Python: `n_rotamers(imol, chain_id, resno, ins_code)`  
Scheme: `(n-rotamers imol chain-id resno ins-code)`

return the number of rotamers for this residue - return -1
 on no residue found.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_rotamers(0, "A", 41, "")` | ran, returned `8` |
| Scheme | `(n-rotamers 0 "A" 41 "")` | ran, returned `8` |

Python and Scheme gave the same answer.

### rotamer_graphs

Python: `rotamer_graphs(imol)`  
Scheme: `(rotamer-graphs imol)`

Activate rotamer graph analysis for molecule number imol.

Return rotamer info - function used in testing.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `rotamer_graphs_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotamer_graphs(0)` | ran, returned `[['A', 1, '', 2.0856404304504395, 'ASP'], ['A', 2, '', 49.393089294433594, 'VAL'], ['A', 3, '', 48.683773040771484, 'SER ...` |
| Scheme | `(rotamer-graphs 0)` | ran, returned `(("A" 1 "" 2.0856404304504395 "ASP") ("A" 2 "" 49.393089294433594 "VAL") ("A" 3 "" 48.683773040771484 "SER") ("A" 5 "" 2 ...` |

Python and Scheme gave the same answer.

### rotamer_score

Python: `rotamer_score(imol, chain_id, res_no, insertion_code, alt_conf)`  
Scheme: `(rotamer-score imol chain-id res-no insertion-code alt-conf)`

currently stub function only

Arguments: imol (a whole number), chain_id (text), res_no (a whole number), insertion_code (text), alt_conf (text). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotamer_score(0, "A", 41, "", "")` | ran, returned `1.4432990550994873` |
| Scheme | `(rotamer-score 0 "A" 41 "" "")` | ran, returned `1.4432990550994873` |

Python and Scheme gave the same answer.

### rotamer_search_mode_state

Python: `rotamer_search_mode_state()`  
Scheme: `(rotamer-search-mode-state)`

\ brief get the mode of rotamer search

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotamer_search_mode_state()` | ran, returned `0` |
| Scheme | `(rotamer-search-mode-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_auto_fit_best_rotamer_clash_flag

Python: `set_auto_fit_best_rotamer_clash_flag(i)`  
Scheme: `(set-auto-fit-best-rotamer-clash-flag i)`

set the clash flag for rotamer search

 And this functions for [pre-setting] the variables for
 auto_fit_best_rotamer called interactively (using a graphics_info_t
 function). 0 off, 1 on.

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_auto_fit_best_rotamer_clash_flag(1)` | ran (no return value) |
| Scheme | `(set-auto-fit-best-rotamer-clash-flag 1)` | ran (no return value) |

### set_residue_to_rotamer_name

Python: `set_residue_to_rotamer_name(imol, chain_id, resno, ins_code, alt_conf, rotamer_name)`  
Scheme: `(set-residue-to-rotamer-name imol chain-id resno ins-code alt-conf rotamer-name)`

set the residue specified to the rotamer name specified.

(rotamer names are the Richardson rotamer names.)

return value is 0 if atoms were not moved (e.g. because rotamer-name was not know)

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), alt_conf (text), rotamer_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_to_rotamer_name(0, "A", 41, "", "", "my-name")` | ran, returned `0` |
| Scheme | `(set-residue-to-rotamer-name 0 "A" 41 "" "" "my-name")` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_residue_to_rotamer_number

Python: `set_residue_to_rotamer_number(imol, chain_id, resno, ins_code, alt_conf, rotamer_number)`  
Scheme: `(set-residue-to-rotamer-number imol chain-id resno ins-code alt-conf rotamer-number)`

set the residue specified to the rotamer number specifed.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), alt_conf (text), rotamer_number (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_residue_to_rotamer_number(0, "A", 41, "", "", 1)` | ran, returned `0` |
| Scheme | `(set-residue-to-rotamer-number 0 "A" 41 "" "" 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### set_rotamer_check_clashes

Python: `set_rotamer_check_clashes(i)`  
Scheme: `(set-rotamer-check-clashes i)`

set a flag: 0 is off, 1 is on

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotamer_check_clashes(1)` | ran (no return value) |
| Scheme | `(set-rotamer-check-clashes 1)` | ran (no return value) |

### set_rotamer_lowest_probability

Python: `set_rotamer_lowest_probability(f)`  
Scheme: `(set-rotamer-lowest-probability f)`

For Dunbrack rotamers, set the lowest probability to be
 considered. Set as a percentage i.e. 1.00 is quite low. For
 Richardson Rotamers, this has no effect.

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotamer_lowest_probability(1.0)` | ran (no return value) |
| Scheme | `(set-rotamer-lowest-probability 1.0)` | ran (no return value) |

### set_rotamer_search_mode

Python: `set_rotamer_search_mode(mode)`  
Scheme: `(set-rotamer-search-mode mode)`

set the mode of rotamer search, options are (ROTAMERSEARCHAUTOMATIC),
 (ROTAMERSEARCHLOWRES) (aka. "backrub rotamers"),
 (ROTAMERSEARCHHIGHRES) (with rigid body fitting)

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotamer_search_mode(1)` | ran (no return value) |
| Scheme | `(set-rotamer-search-mode 1)` | ran (no return value) |

### setup_auto_fit_rotamer

Python: `setup_auto_fit_rotamer(state)`  
Scheme: `(setup-auto-fit-rotamer state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_auto_fit_rotamer(1)` | ran (no return value) |
| Scheme | `(setup-auto-fit-rotamer 1)` | ran (no return value) |

### setup_rotamers

Python: `setup_rotamers(state)`  
Scheme: `(setup-rotamers state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_rotamers(1)` | ran (no return value) |
| Scheme | `(setup-rotamers 1)` | ran (no return value) |

### show_rotamers_dialog

Python: `show_rotamers_dialog(imol, chain_id, resno, ins_code, altconf)`  
Scheme: `(show-rotamers-dialog imol chain-id resno ins-code altconf)`

Arguments: imol (a whole number), chain_id (text), resno (a whole number), ins_code (text), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_rotamers_dialog(0, "A", 41, "", "")` | ran (no return value) |
| Scheme | `(show-rotamers-dialog 0 "A" 41 "" "")` | ran (no return value) |

### simple_fill_partial_residues

Python: `simple_fill_partial_residues(imol)`  
Scheme: `(simple-fill-partial-residues imol)`

Fill amino acid residues

do backrub rotamer search for residues, but don't do refinement

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `simple_fill_partial_residues(0)` | ran (no return value) |
| Scheme | `(simple-fill-partial-residues 0)` | ran (no return value) |

