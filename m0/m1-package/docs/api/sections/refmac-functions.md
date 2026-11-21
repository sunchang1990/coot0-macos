# Refmac Functions

[Scripting reference](../README.md) > Refmac Functions (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_refmac_sad_atom_info

Python: `get_refmac_sad_atom_info()`  
Scheme: `(get-refmac-sad-atom-info)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `get_refmac_sad_atom_info_py`.
Also available in Scheme as `get-refmac-sad-atom-info-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_refmac_sad_atom("SE", -8.0, 3.0, 0.98)`, then `get_refmac_sad_atom_info()` | ran, returned `[['SE', -8.0, 3.0, 0.9800000190734863]]` |
| Scheme | first `(add-refmac-sad-atom "SE" -8.0 3.0 0.98)`, then `(get-refmac-sad-atom-info)` | ran, returned `(("SE" -8.0 3.0 0.9800000190734863))` |

Example written and checked by hand on the test data. Expected: returns the SAD atoms set for Refmac: [atom name, f', f'', wavelength] each; empty by default.

Python and Scheme gave the same answer.

### keep_map_colour_after_refmac_state

Python: `keep_map_colour_after_refmac_state()`  
Scheme: `(keep-map-colour-after-refmac-state)`

the keep-map-colour-after-refmac internal state

 Returns 1 for "yes", 0 for "no"

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `keep_map_colour_after_refmac_state()` | ran, returned `0` |
| Scheme | `(keep-map-colour-after-refmac-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 if the map colour is kept after a Refmac run, 0 (default) if not.

Python and Scheme gave the same answer.

### refmac_runs_with_nolabels

Python: `refmac_runs_with_nolabels()`  
Scheme: `(refmac-runs-with-nolabels)`

refmac vresion testing, returns 1 for new refmac (>5.3) otherwise 0

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_runs_with_nolabels()` | ran, returned `2` |
| Scheme | `(refmac-runs-with-nolabels)` | ran, returned `2` |

Example written and checked by hand on the test data. Expected: returns 0 for old Refmac, 1 for >= 5.4, 2 for >= 5.5 (SAD/twin support).

Note: the doc says 1 or 0 but the code returns 2 for any modern Refmac; it runs refmac to read its version (needs CCP4)

Python and Scheme gave the same answer.

### set_keep_map_colour_after_refmac

Python: `set_keep_map_colour_after_refmac(istate)`  
Scheme: `(set-keep-map-colour-after-refmac istate)`

flag to enable above

call this with istate=1

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_keep_map_colour_after_refmac(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-keep-map-colour-after-refmac 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: keeps the map colour after Refmac; the _state getter returns 1.

Setting checked (set to another value and read back, then put back): Python: keep_map_colour_after_refmac_state was 0, set to 1, read back 1; Scheme: keep-map-colour-after-refmac-state was 0, set to 1, read back 1.

### set_refmac_counter

Python: `set_refmac_counter(imol, refmac_count)`  
Scheme: `(set-refmac-counter imol refmac-count)`

set counter for runs of refmac so that this can be used to
 construct a unique filename for new output

Arguments: imol (a whole number), refmac_count (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_counter(0, 5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-refmac-counter 0 5)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the Refmac run counter of molecule 0, used in the next output file names.

### swap_map_colours

Python: `swap_map_colours(imol1, imol2)`  
Scheme: `(swap-map-colours imol1 imol2)`

swap the colours of maps

 swap the colour of maps imol1 and imol2. Useful to some after
 running refmac, so that the map to be build into is always the same
 colour

Arguments: imol1 (a whole number), imol2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `swap_map_colours(0, 0)` | ran (no return value, nothing visible changed) |
| Scheme | `(swap-map-colours 0 0)` | ran (no return value, nothing visible changed) |

