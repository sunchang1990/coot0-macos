# 180 Flip Side chain

[Scripting reference](../README.md) > 180 Flip Side chain (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_180_degree_side_chain_flip

Python: `do_180_degree_side_chain_flip(imol, chain_id, resno, inscode, altconf)`  
Scheme: `(do-180-degree-side-chain-flip imol chain-id resno inscode altconf)`

rotate 180 degrees around the last chi angle

Arguments: imol (a whole number), chain_id (text), resno (a whole number), inscode (text), altconf (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_180_degree_side_chain_flip(0, "A", 41, "", "")` | ran (no return value); changed: molecule 0: coordinates of 1 residue(s) (A41) |
| Scheme | `(do-180-degree-side-chain-flip 0 "A" 41 "" "")` | ran (no return value); changed: molecule 0: coordinates of 1 residue(s) (A41) |

### setup_180_degree_flip

Python: `setup_180_degree_flip(state)`  
Scheme: `(setup-180-degree-flip state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_180_degree_flip(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-180-degree-flip 1)` | ran (no return value, nothing visible changed) |

### side_chain_flip_180_intermediate_atoms

Python: `side_chain_flip_180_intermediate_atoms()`  
Scheme: `(side-chain-flip-180-intermediate-atoms)`

! side-chain 180 flip the terminal chi angle of the residue of the active atom

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `refine_zone(0, "A", 41, 41, "")`, then `side_chain_flip_180_intermediate_atoms()` | ran, returned `1` |
| Scheme | first `(refine-zone 0 "A" 41 41 "")`, then `(side-chain-flip-180-intermediate-atoms)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns 1 when intermediate (moving) atoms exist and the active residue's last chi was flipped; 0 when no refinement is in progress.

Note: Works only while a refinement's intermediate atoms exist (run in the same step as the refinement in a headless test).

Python and Scheme gave the same answer.

