# New Molecule by Section Interface

[Scripting reference](../README.md) > New Molecule by Section Interface (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### set_axis_orientation_matrix

Python: `set_axis_orientation_matrix(m11, m12, m13, m21, m22, m23, m31, m32, m33)`  
Scheme: `(set-axis-orientation-matrix m11 m12 m13 m21 m22 m23 m31 m32 m33)`

section Miguel's orientation axes matrix

Arguments: m11 (a number), m12 (a number), m13 (a number), m21 (a number), m22 (a number), m23 (a number), m31 (a number), m32 (a number), m33 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_axis_orientation_matrix(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | not tried |
| Scheme | `(set-axis-orientation-matrix 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | not tried |

### set_axis_orientation_matrix_usage

Python: `set_axis_orientation_matrix_usage(state)`  
Scheme: `(set-axis-orientation-matrix-usage state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_axis_orientation_matrix_usage(1)` | not tried |
| Scheme | `(set-axis-orientation-matrix-usage 1)` | not tried |

