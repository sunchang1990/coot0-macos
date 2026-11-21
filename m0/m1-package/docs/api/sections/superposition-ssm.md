# Superposition (SSM)

[Scripting reference](../README.md) > Superposition (SSM) (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### superpose

Python: `superpose(imol1, imol2, move_imol2_flag)`  
Scheme: `(superpose imol1 imol2 move-imol2-flag)`

simple interface to superposition.

Superpose all residues of imol2 onto imol1. imol1 is reference, we
can either move imol2 or copy it to generate a new molecule depending
on the vaule of move_imol2_flag (1 for copy 0 for move).

Arguments: imol1 (a whole number), imol2 (a whole number), move_imol2_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `superpose(0, 0, 0)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...); first_molecule_with_symmetry_displayed(): 0 -> -1; get_symmetry(0): ['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z -> []; n_symops(0): 4 -> -1 |
| Scheme | `(superpose 0 0 0)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...); first_molecule_with_symmetry_displayed(): 0 -> -1; get_symmetry(0): ['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z -> []; n_symops(0): 4 -> -1 |

### superpose_with_atom_selection

Python: `superpose_with_atom_selection(imol1, imol2, mmdb_atom_sel_str_1, mmdb_atom_sel_str_2, move_imol2_copy_flag)`  
Scheme: `(superpose-with-atom-selection imol1 imol2 mmdb-atom-sel-str-1 mmdb-atom-sel-str-2 move-imol2-copy-flag)`

detailed interface to superposition.

Superpose the given atom selection (specified by the mmdb atom
selection strings) of imol2 onto imol1. imol1 is reference, we can
either move imol2 or copy it to generate a new molecule depending on
the vaule of move_imol2_flag (1 for move 0 for copy).

Returns the index of the superposed molecule - which could either be a
new molecule (if move_imol2_flag was 1) or the imol2 or -1 (signifying
failure to do the SMM superposition).

Arguments: imol1 (a whole number), imol2 (a whole number), mmdb_atom_sel_str_1 (text), mmdb_atom_sel_str_2 (text), move_imol2_copy_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `imol2 = read_pdb("tutorial-modern.pdb")`, then `superpose_with_atom_selection(0, imol2, "//A/10-60", "//B/10-60", 1)` | ran, returned `4`; changed: new molecule 4 (model, Copy_of_tutorial-modern.pdb); graphics_n_molecules(): 4 -> 5 |
| Scheme | first `(define imol2 (read-pdb "tutorial-modern.pdb"))`, then `(superpose-with-atom-selection 0 imol2 "//A/10-60" "//B/10-60" 1)` | ran, returned `4`; changed: new molecule 4 (model, Copy_of_tutorial-modern.pdb); graphics_n_molecules(): 4 -> 5 |

Example written and checked by hand on the test data. Expected: returns the molecule number of the superposed copy (move flag 1 = copy here, despite the doc's wording); -1 on failure.

Python and Scheme gave the same answer.

### superpose_with_chain_selection

Python: `superpose_with_chain_selection(imol1, imol2, chain_imol1, chain_imol2, chain_used_flag_imol1, chain_used_flag_imol2, move_imol2_copy_flag)`  
Scheme: `(superpose-with-chain-selection imol1 imol2 chain-imol1 chain-imol2 chain-used-flag-imol1 chain-used-flag-imol2 move-imol2-copy-flag)`

chain-based interface to superposition.

Superpose the given chains of imol2 onto imol1. imol1 is reference,
we can either move imol2 or copy it to generate a new molecule
depending on the vaule of move_imol2_flag (1 for move 0 for copy).

Arguments: imol1 (a whole number), imol2 (a whole number), chain_imol1 (text), chain_imol2 (text), chain_used_flag_imol1 (a whole number), chain_used_flag_imol2 (a whole number), move_imol2_copy_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `superpose_with_chain_selection(0, 0, "A", "B", 0, 0, 0)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...); first_molecule_with_symmetry_displayed(): 0 -> -1; get_symmetry(0): ['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z -> []; n_symops(0): 4 -> -1 |
| Scheme | `(superpose-with-chain-selection 0 0 "A" "B" 0 0 0)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...); first_molecule_with_symmetry_displayed(): 0 -> -1; get_symmetry(0): ['x,y,z', '-x+1/2,-y,z+1/2', 'x+1/2,-y+1/2,-z', '-x,y+1/2,-z -> []; n_symops(0): 4 -> -1 |

