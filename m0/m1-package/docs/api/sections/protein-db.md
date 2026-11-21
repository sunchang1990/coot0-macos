# protein-db

[Scripting reference](../README.md) > protein-db (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### protein_db_loop_specs_to_atom_selection_string

Python: `protein_db_loop_specs_to_atom_selection_string(specs)`  
Scheme: `(protein-db-loop-specs-to-atom-selection-string specs)`

so that we can create a "original loop" molecule from the atom
specs picked (i.e. the atom selection string should extend over the
range from the smallest residue number to the largest (in the same
chain)).

Arguments: specs (a list). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `protein_db_loop_specs_to_atom_selection_string(residue_records_list_py_to_residue_specs([{"seq_num": "40", "ins_code": ""}, {"seq_num": "45", "ins_code": ""}], "A"))` | ran, returned `'//A/40-45'` |
| Scheme | first `(define mk (record-constructor (make-record-type 'residue-rec '(seq-num ins-code))))`, then `(protein-db-loop-specs-to-atom-selection-string (residue-records-list-scm-to-residue-specs (list (mk "40" "") (mk "45" "")) "A"))` | ran, returned `"//A/40-45"` |

Example written and checked by hand on the test data. Expected: the mmdb atom selection covering the residue range: '//A/40-45'. The argument is a C++ vector of residue specs (plain lists give a TypeError).

Python and Scheme gave the same answer.

### protein_db_loops

Python: `protein_db_loops(imol_coords, residues_specs, imol_map, nfrags, preserve_residue_names)`  
Scheme: `(protein-db-loops imol-coords residues-specs imol-map nfrags preserve-residue-names)`

return in the first pair, the imol of the new molecule generated
from an atom selection of the imol_coords for the residue selection
of the loop and the molecule number of the consolidated solutions
(displayed in purple). and the second of the outer pair, there is
vector of molecule indices for each of the candidate loops.
return -1 in the first of the pair on failure

Arguments: imol_coords (a whole number), residues_specs (a list or value), imol_map (a whole number), nfrags (a whole number), preserve_residue_names (true or false). Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `protein_db_loops(0, [[True, "A", 40, ""], [True, "A", 41, ""], [True, "A", 42, ""], [True, "A", 43, ""]], 1, 10, False)` | ran, returned `[[14, 13], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]`; changed: new molecule 10 (model, Loop candidate #7); new molecule 11 (model, Loop candidate #8); new molecule 12 (model, Loop candidate #9); new molecule 13 (model, All Loop candidates ) ... |
| Scheme | `(protein-db-loops 0 (list (list #t "A" 40 "") (list #t "A" 41 "") (list #t "A" 42 "") (list #t "A" 43 "")) 1 10 #f)` | ran, returned `((14 13) (3 4 5 6 7 8 9 10 11 12))`; changed: new molecule 10 (model, Loop candidate #7); new molecule 11 (model, Loop candidate #8); new molecule 12 (model, Loop candidate #9); new molecule 13 (model, All Loop candidates ) ... |

Example written and checked by hand on the test data. Expected: [[original-loop molecule, all-candidates molecule], [candidate molecules]] for 10 database loops fitting residues A40-43.

Python and Scheme gave the same answer.

