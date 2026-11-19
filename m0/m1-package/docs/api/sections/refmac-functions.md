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
| Python | `get_refmac_sad_atom_info()` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-refmac-sad-atom-info)` | not run: not run automatically (refmac: exits, uses the network, an external program, files or a screen) |

### keep_map_colour_after_refmac_state

Python: `keep_map_colour_after_refmac_state()`  
Scheme: `(keep-map-colour-after-refmac-state)`

the keep-map-colour-after-refmac internal state

 Returns 1 for "yes", 0 for "no"

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `keep_map_colour_after_refmac_state()` | not tried |
| Scheme | `(keep-map-colour-after-refmac-state)` | not tried |

### refmac_runs_with_nolabels

Python: `refmac_runs_with_nolabels()`  
Scheme: `(refmac-runs-with-nolabels)`

refmac vresion testing, returns 1 for new refmac (>5.3) otherwise 0

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `refmac_runs_with_nolabels()` | not tried |
| Scheme | `(refmac-runs-with-nolabels)` | not tried |

### set_keep_map_colour_after_refmac

Python: `set_keep_map_colour_after_refmac(istate)`  
Scheme: `(set-keep-map-colour-after-refmac istate)`

flag to enable above

call this with istate=1

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_keep_map_colour_after_refmac(1)` | not tried |
| Scheme | `(set-keep-map-colour-after-refmac 1)` | not tried |

### set_refmac_counter

Python: `set_refmac_counter(imol, refmac_count)`  
Scheme: `(set-refmac-counter imol refmac-count)`

set counter for runs of refmac so that this can be used to
 construct a unique filename for new output

Arguments: imol (a whole number), refmac_count (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_refmac_counter(0, 1)` | not tried |
| Scheme | `(set-refmac-counter 0 1)` | not tried |

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
| Python | `swap_map_colours(0, 0)` | not tried |
| Scheme | `(swap-map-colours 0 0)` | not tried |

