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
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

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
| Python | `protein_db_loops(0, ["A", 41, ""], 1, 1, True)` | error: SystemError: <built-in function protein_db_loops_py> returned a result with an exception set |
| Scheme | `(protein-db-loops 0 (list "A" 41 "") 1 1 1)` | error: In procedure length: Wrong type argument in position 1: "A" |

