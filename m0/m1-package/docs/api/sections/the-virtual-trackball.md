# The Virtual Trackball

[Scripting reference](../README.md) > The Virtual Trackball (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### vt_surface

Python: `vt_surface(mode)`  
Scheme: `(vt-surface mode)`

How should the mouse move the view?

mode=1 for "Flat", mode=2 for "Spherical Surface"

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `vt_surface(1)` | not tried |
| Scheme | `(vt-surface 1)` | not tried |

### vt_surface_status

Python: `vt_surface_status()`  
Scheme: `(vt-surface-status)`

return the mouse view status mode

mode=1 for "Flat", mode=2 for "Spherical Surface"

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `vt_surface_status()` | not tried |
| Scheme | `(vt-surface-status)` | not tried |

