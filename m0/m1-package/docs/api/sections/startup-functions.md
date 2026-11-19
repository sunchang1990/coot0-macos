# Startup Functions

[Scripting reference](../README.md) > Startup Functions (2 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### prefer_python

Python: `prefer_python()`  
Scheme: `(prefer-python)`

the python-prefered mode.

This is available so that the scripting functions know whether on not
to put themselves onto in as menu items.

If you consider using this, consider in preference use_gui_qm == 2,
which is used elsewhere to stop python functions adding to the gui,
when guile-gtk functions have alread done so. We should clean up this
(rather obscure) interface at some stage.

return 1 for python is prefered, 0 for not.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `prefer_python()` | not tried |
| Scheme | `(prefer-python)` | not tried |

### set_prefer_python

Python: `set_prefer_python()`  
Scheme: `(set-prefer-python)`

tell coot that you prefer to run python scripts if/when
 there is an option to do so.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_prefer_python()` | not tried |
| Scheme | `(set-prefer-python)` | not tried |

