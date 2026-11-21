# Pep-flip Interface

[Scripting reference](../README.md) > Pep-flip Interface (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_pepflip

Python: `do_pepflip(state)`  
Scheme: `(do-pepflip state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_pepflip(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-pepflip 1)` | ran (no return value, nothing visible changed) |

### pepflip

Python: `pepflip(imol, chain_id, resno, inscode, altconf)`  
Scheme: `(pepflip imol chain-id resno inscode altconf)`

the residue with CO, for scripting interface.

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pepflip(0, "A", 41, "", "")` | ran (no return value); changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |
| Scheme | `(pepflip 0 "A" 41 "" "")` | ran (no return value); changed: molecule 0: coordinates of 2 residue(s) (A41, A42) |

### pepflip_intermediate_atoms

Python: `pepflip_intermediate_atoms()`  
Scheme: `(pepflip-intermediate-atoms)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `(refine_zone(0, "A", 41, 43, ""), pepflip_intermediate_atoms())[1]` | ran, returned `1` |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (pepflip-intermediate-atoms))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: flips the peptide at the intermediate-atom pointer during a refinement and returns 1; 0 when there are no moving atoms.

Note: needs moving atoms: the example starts a refinement in the same expression (headless Coot keeps them until cleared)

Python and Scheme gave the same answer.

### pepflip_intermediate_atoms_other_peptide

Python: `pepflip_intermediate_atoms_other_peptide()`  
Scheme: `(pepflip-intermediate-atoms-other-peptide)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `(refine_zone(0, "A", 41, 43, ""), pepflip_intermediate_atoms_other_peptide())[1]` | ran, returned `1` |
| Scheme | `(begin (refine-zone 0 "A" 41 43 "") (pepflip-intermediate-atoms-other-peptide))` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: flips the other peptide of the residue during a refinement; 1 if done, 0 when there are no moving atoms.

Python and Scheme gave the same answer.

### pepflip_using_difference_map

Python: `pepflip_using_difference_map(imol_coords, imol_difference_map, n_sigma)`  
Scheme: `(pepflip-using-difference-map-scm imol-coords imol-difference-map n-sigma)`

Arguments: imol_coords (a whole number), imol_difference_map (a whole number), n_sigma (a number). Returns: a value (see the result of the example).
Also available in Python as `pepflip_using_difference_map_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `pepflip_using_difference_map(0, 1, 1.5)` | ran, returned `[]` |
| Scheme | `(pepflip-using-difference-map-scm 0 1 1.5)` | ran, returned `()` |

Python and Scheme gave the same answer.

