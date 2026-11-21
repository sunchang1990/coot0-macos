# Surface Interface

[Scripting reference](../README.md) > Surface Interface (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_clipped_surface

Python: `do_clipped_surface(imol, residue_specs)`  
Scheme: `(do-clipped-surface imol residue-specs)`

draw the surface of the imolth molecule clipped to the
 residues given by residue_specs

Arguments: imol (a whole number), residue_specs (a list or value). Returns: nothing.
Also available in Python as `do_clipped_surface_py`.
Also available in Scheme as `do-clipped-surface-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_clipped_surface(0, [["A", 41, ""], ["A", 42, ""]])` | ran (no return value, nothing visible changed) |
| Scheme | `(do-clipped-surface 0 (list (list "A" 41 "") (list "A" 42 "")))` | ran (no return value, nothing visible changed) |

### do_surface

Python: `do_surface(imol, istate)`  
Scheme: `(do-surface imol istate)`

draw surface of molecule number imol

if state = 1 draw the surface (normal representation goes away)

if state = 0 don't draw surface

Arguments: imol (a whole number), istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_surface(0, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(do-surface 0 1)` | ran (no return value, nothing visible changed) |

### get_electrostatic_surface_charge_range

Python: `get_electrostatic_surface_charge_range()`  
Scheme: `(get-electrostatic-surface-charge-range)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_electrostatic_surface_charge_range()` | ran, returned `0.5` |
| Scheme | `(get-electrostatic-surface-charge-range)` | ran, returned `0.5` |

Python and Scheme gave the same answer.

### get_electrostatic_surface_opacity

Python: `get_electrostatic_surface_opacity(imol)`  
Scheme: `(get-electrostatic-surface-opacity imol)`

return 1.0 for non transparent and 0.5 if screendoor
 transparency has been turned on.

Arguments: imol (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_electrostatic_surface_opacity(0)` | ran, returned `1.0` |
| Scheme | `(get-electrostatic-surface-opacity 0)` | ran, returned `1.0` |

Python and Scheme gave the same answer.

### molecule_is_drawn_as_surface_int

Python: `molecule_is_drawn_as_surface_int(imol)`  
Scheme: `(molecule-is-drawn-as-surface-int imol)`

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_is_drawn_as_surface_int(0)` | ran, returned `1` |
| Scheme | `(molecule-is-drawn-as-surface-int 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### set_electrostatic_surface_charge_range

Python: `set_electrostatic_surface_charge_range(v)`  
Scheme: `(set-electrostatic-surface-charge-range v)`

Arguments: v (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_electrostatic_surface_charge_range(1.0)` | ran (no return value); changed: get_electrostatic_surface_charge_range(): 0.5 -> 1 |
| Scheme | `(set-electrostatic-surface-charge-range 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_electrostatic_surface_charge_range was 0.5, set to 1.25, read back 1.25; Scheme: get-electrostatic-surface-charge-range was 0.5, set to 1.25, read back 1.25.

### set_transparent_electrostatic_surface

Python: `set_transparent_electrostatic_surface(imol, opacity)`  
Scheme: `(set-transparent-electrostatic-surface imol opacity)`

simple on/off screendoor transparency at the moment, an
 opacity > 0.0 will turn on screendoor transparency (stippling).

Arguments: imol (a whole number), opacity (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_transparent_electrostatic_surface(0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-transparent-electrostatic-surface 0 1.0)` | ran (no return value, nothing visible changed) |

