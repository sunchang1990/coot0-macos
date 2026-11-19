# Least-Squares matching

[Scripting reference](../README.md) > Least-Squares matching (10 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_lsq_atom_pair

Python: `add_lsq_atom_pair(atom_spec_ref, atom_spec_moving)`  
Scheme: `(add-lsq-atom-pair atom-spec-ref atom-spec-moving)`

Arguments: atom_spec_ref (a list or value), atom_spec_moving (a list or value). Returns: nothing.
Also available in Python as `add_lsq_atom_pair_py`.
Also available in Scheme as `add-lsq-atom-pair-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_lsq_atom_pair(["A", 41, "", " CA ", ""], ["A", 41, "", " CA ", ""])` | ran (no return value) |
| Scheme | `(add-lsq-atom-pair (list "A" 41 "" " CA " "") (list "A" 41 "" " CA " ""))` | ran (no return value) |

### add_lsq_match

Python: `add_lsq_match(reference_resno_start, reference_resno_end, chain_id_reference, moving_resno_start, moving_resno_end, chain_id_moving, match_type)`  
Scheme: `(add-lsq-match reference-resno-start reference-resno-end chain-id-reference moving-resno-start moving-resno-end chain-id-moving match-type)`

Arguments: reference_resno_start (a whole number), reference_resno_end (a whole number), chain_id_reference (text), moving_resno_start (a whole number), moving_resno_end (a whole number), chain_id_moving (text), match_type (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_lsq_match(41, 45, "A", 41, 45, "A", 1)` | ran (no return value) |
| Scheme | `(add-lsq-match 41 45 "A" 41 45 "A" 1)` | ran (no return value) |

### apply_lsq_matches

Python: `apply_lsq_matches(imol_reference, imol_moving)`  
Scheme: `(apply-lsq-matches imol-reference imol-moving)`

Return an rtop pair (proper list) on good match, else False

Arguments: imol_reference (a whole number), imol_moving (a whole number). Returns: a value (see the result of the example).
Also available in Python as `apply_lsq_matches_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_lsq_matches(0, 0)` | ran, returned `False` |
| Scheme | `(apply-lsq-matches 0 0)` | ran, returned `#f` |

### apply_lsq_matches_simple

Python: `apply_lsq_matches_simple(imol_reference, imol_moving)`  
Scheme: `(apply-lsq-matches-simple imol-reference imol-moving)`

poor old python programmers...

Arguments: imol_reference (a whole number), imol_moving (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_lsq_matches_simple(0, 0)` | ran, returned `0` |
| Scheme | `(apply-lsq-matches-simple 0 0)` | ran, returned `0` |

### clear_lsq_matches

Python: `clear_lsq_matches()`  
Scheme: `(clear-lsq-matches)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_lsq_matches()` | ran (no return value) |
| Scheme | `(clear-lsq-matches)` | ran (no return value) |

### get_lsq_matrix

Python: `get_lsq_matrix(imol_reference, imol_moving)`  
Scheme: `(get-lsq-matrix imol-reference imol-moving)`

Arguments: imol_reference (a whole number), imol_moving (a whole number). Returns: a value (see the result of the example).
Also available in Python as `get_lsq_matrix_py`.
Also available in Scheme as `get-lsq-matrix-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_lsq_matrix(0, 0)` | ran, returned `False` |
| Scheme | `(get-lsq-matrix 0 0)` | ran, returned `#f` |

### remove_last_lsq_plane_atom

Python: `remove_last_lsq_plane_atom()`  
Scheme: `(remove-last-lsq-plane-atom)`

callback from destroy of widget

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_last_lsq_plane_atom()` | not tried |
| Scheme | `(remove-last-lsq-plane-atom)` | not tried |

### setup_lsq_deviation

Python: `setup_lsq_deviation(state)`  
Scheme: `(setup-lsq-deviation state)`

section Least-Squares plane interface

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_lsq_deviation(1)` | not tried |
| Scheme | `(setup-lsq-deviation 1)` | not tried |

### setup_lsq_plane_define

Python: `setup_lsq_plane_define(state)`  
Scheme: `(setup-lsq-plane-define state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_lsq_plane_define(1)` | not tried |
| Scheme | `(setup-lsq-plane-define 1)` | not tried |

### unset_lsq_plane_dialog

Python: `unset_lsq_plane_dialog()`  
Scheme: `(unset-lsq-plane-dialog)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unset_lsq_plane_dialog()` | not tried |
| Scheme | `(unset-lsq-plane-dialog)` | not tried |

