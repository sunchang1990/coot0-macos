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
| Python | `ideal_nucleic_acid("hello", "hello", 1, "ACDEFGHIKLMNPQRSTVWY")` | ran, returned `-1` |
| Scheme | `(ideal-nucleic-acid "hello" "hello" 1 "ACDEFGHIKLMNPQRSTVWY")` | ran, returned `-1` |

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
| Python | `pucker_info(0, ["A", 41, ""], 1)` | ran, returned `False` |
| Scheme | `(pucker-info 0 (list "A" 41 "") 1)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### setup_base_pairing

Python: `setup_base_pairing(state)`  
Scheme: `(setup-base-pairing state)`

not for user level

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_base_pairing(1)` | ran (no return value) |
| Scheme | `(setup-base-pairing 1)` | ran (no return value) |

### watson_crick_pair

Python: `watson_crick_pair(imol, chain_id, resno)`  
Scheme: `(watson-crick-pair imol chain-id resno)`

Return a molecule that contains a residue that is the WC pair
 partner of the clicked/picked/selected residue

Arguments: imol (a whole number), chain_id (text), resno (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `watson_crick_pair(0, "A", 41)` | ran, returned `-1` |
| Scheme | `(watson-crick-pair 0 "A" 41)` | ran, returned `-1` |

Python and Scheme gave the same answer.

### watson_crick_pair_for_residue_range

Python: `watson_crick_pair_for_residue_range(imol, chain_id, resno_start, resno_end)`  
Scheme: `(watson-crick-pair-for-residue-range imol chain-id resno-start resno-end)`

add base pairs for the given residue range, modify molecule imol by creating a new chain

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `watson_crick_pair_for_residue_range(0, "A", 41, 45)` | ran, returned `0` |
| Scheme | `(watson-crick-pair-for-residue-range 0 "A" 41 45)` | ran, returned `0` |

Python and Scheme gave the same answer.

