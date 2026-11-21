# RNA/DNA

[Scripting reference](../README.md) > RNA/DNA (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### ideal_nucleic_acid

Python: `ideal_nucleic_acid(RNA_or_DNA, form, single_stranged_flag, sequence)`  
Scheme: `(ideal-nucleic-acid RNA-or-DNA form single-stranged-flag sequence)`

create a molecule of idea nucleotides

use the given sequence (single letter code)

RNA_or_DNA is either "RNA" or "DNA"

form is either "A" or "B"

Returns the new molecule number or -1 if a problem

Arguments: RNA_or_DNA (text), form (text), single_stranged_flag (a whole number), sequence (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ideal_nucleic_acid("RNA", "A", 0, "GAGCUC")` | ran, returned `3`; changed: new molecule 3 (model, A-form-RNA); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |
| Scheme | `(ideal-nucleic-acid "DNA" "B" 1 "ACGT")` | ran, returned `3`; changed: new molecule 3 (model, B-form-DNA); first_small_coords_imol(): -1 -> 3; graphics_n_molecules(): 3 -> 4 |

Example written and checked by hand on the test data. Expected: returns the new molecule number of an ideal nucleic acid with the sequence (RNA/DNA, form A/B, single-stranded flag).

Python and Scheme gave the same answer.

### pucker_info

Python: `pucker_info(imol, residue_spec, do_pukka_pucker_check)`  
Scheme: `(pucker-info imol residue-spec do-pukka-pucker-check)`

return False if residue not found, otherwise
 [[phosphate_distance, puckered_atom, out_of_plane_distance, plane_distortion], chain_id, resno, ins_code]

 (where plane_distortion is for the other 4 atoms in the plane (I think)).

 and if there is no following residue, then the phosphate distance
 cannot be calculated, so the (inner) list is null (not filled).

Arguments: imol (a whole number), residue_spec (a list or value), do_pukka_pucker_check (a whole number). Returns: a value (see the result of the example).
Also available in Python as `pucker_info_py`.
Also available in Scheme as `pucker-info-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_rna = read_pdb("1ehz.pdb")`, then `pucker_info(imol_rna, ["A", 10, ""], 1)` | ran, returned `[4.813389301300049, " C3'", 0.5553739070892334, 0.03498387709259987]` |
| Scheme | first `(define imol-rna (read-pdb "1ehz.pdb"))`, then `(pucker-info imol-rna (list "A" 10 "") 1)` | ran, returned `(4.813389301300049 " C3'" 0.5553739070892334 0.03498387709259987)` |

Example written and checked by hand on the test data. Expected: for an RNA/DNA residue returns [phosphate distance, puckered atom (C3' or C2'), out-of-plane distance, plane distortion]; False if not found.

Python and Scheme gave the same answer.

### setup_base_pairing

Python: `setup_base_pairing(state)`  
Scheme: `(setup-base-pairing state)`

not for user level

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_base_pairing(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-base-pairing 1)` | ran (no return value, nothing visible changed) |

### watson_crick_pair

Python: `watson_crick_pair(imol, chain_id, resno)`  
Scheme: `(watson-crick-pair imol chain-id resno)`

Return a molecule that contains a residue that is the WC pair
 partner of the clicked/picked/selected residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_ss = ideal_nucleic_acid("RNA", "A", 1, "GAGCUC")`, then `watson_crick_pair(imol_ss, "A", 2)` | ran, returned `-1`; changed: new molecule 4 (model, WC partner); graphics_n_molecules(): 4 -> 5 |
| Scheme | first `(define imol-ss (ideal-nucleic-acid "RNA" "A" 1 "GAGCUC"))`, then `(watson-crick-pair imol-ss "A" 2)` | ran, returned `-1`; changed: new molecule 4 (model, WC partner); graphics_n_molecules(): 4 -> 5 |

Example written and checked by hand on the test data. Expected: should return the new molecule number holding the base-paired partner of A2.

Note: In Coot 0.9.8.96: watson_crick_pair never sets its return value (c-interface-nucleotides.cc:294), so it returns -1 even when the partner molecule is created

Python and Scheme gave the same answer.

### watson_crick_pair_for_residue_range

Python: `watson_crick_pair_for_residue_range(imol, chain_id, resno_start, resno_end)`  
Scheme: `(watson-crick-pair-for-residue-range imol chain-id resno-start resno-end)`

add base pairs for the given residue range, modify molecule imol by creating a new chain

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol_ss = ideal_nucleic_acid("RNA", "A", 1, "GAGCUC")`, then `watson_crick_pair_for_residue_range(imol_ss, "A", 1, 6)` | ran, returned `1`; changed: molecule 3: added 6 residue(s) (B6, B5, B4, B3 ...) |
| Scheme | first `(define imol-ss (ideal-nucleic-acid "RNA" "A" 1 "GAGCUC"))`, then `(watson-crick-pair-for-residue-range imol-ss "A" 1 3)` | ran, returned `1`; changed: molecule 3: added 3 residue(s) (B3, B2, B1) |

Example written and checked by hand on the test data. Expected: returns 1 and adds a new chain with Watson-Crick partners for the residue range.

Python and Scheme gave the same answer.

