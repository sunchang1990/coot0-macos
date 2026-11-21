# Graphics Move

[Scripting reference](../README.md) > Graphics Move (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### transform_molecule_by

Python: `transform_molecule_by(imol, m11, m12, m13, m21, m22, m23, m31, m32, m33, x, y, z)`  
Scheme: `(transform-molecule-by imol m11 m12 m13 m21 m22 m23 m31 m32 m33 x y z)`

transform molecule number imol by the given rotation
 matrix, then translate by (x,y,z) in Angstroms

Arguments: imol (a whole number), m11 (a number), m12 (a number), m13 (a number), m21 (a number), m22 (a number), m23 (a number), m31 (a number), m32 (a number), m33 (a number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `transform_molecule_by(0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 54.5, 9.4, 12.3)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(transform-molecule-by 0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 54.5 9.4 12.3)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |

### transform_zone

Python: `transform_zone(imol, chain_id, resno_start, resno_end, ins_code, m11, m12, m13, m21, m22, m23, m31, m32, m33, x, y, z)`  
Scheme: `(transform-zone imol chain-id resno-start resno-end ins-code m11 m12 m13 m21 m22 m23 m31 m32 m33 x y z)`

transform fragment of molecule number imol by the given rotation
 matrix, then translate by (x,y,z) in Angstroms

Arguments: imol (a whole number), chain_id (text), resno_start (a whole number), resno_end (a whole number), ins_code (text), m11 (a number), m12 (a number), m13 (a number), m21 (a number), m22 (a number), m23 (a number), m31 (a number), m32 (a number), m33 (a number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `transform_zone(0, "A", 41, 45, "", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 54.5, 9.4, 12.3)` | ran (no return value); changed: molecule 0: coordinates of 5 residue(s) (A41, A42, A43, A44 ...) |
| Scheme | `(transform-zone 0 "A" 41 45 "" 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 54.5 9.4 12.3)` | ran (no return value); changed: molecule 0: coordinates of 5 residue(s) (A41, A42, A43, A44 ...) |

### translate_molecule_by

Python: `translate_molecule_by(imol, x, y, z)`  
Scheme: `(translate-molecule-by imol x y z)`

translate molecule number imol by (x,y,z) in Angstroms

Arguments: imol (a whole number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `translate_molecule_by(0, 54.5, 9.4, 12.3)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |
| Scheme | `(translate-molecule-by 0 54.5 9.4 12.3)` | ran (no return value); changed: molecule 0: coordinates of 189 residue(s) (A1, A2, A3, A4 ...) |

### undo_last_move

Python: `undo_last_move()`  
Scheme: `(undo-last-move)`

undo last move

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `undo_last_move()` | ran (no return value); changed: rotation centre moved 44.4 A to (0.0, 0.0, 0.0) |
| Scheme | `(undo-last-move)` | ran (no return value); changed: rotation centre moved 44.4 A to (41.6, 8.7, 12.9) |

