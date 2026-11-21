# Pointer Position Function

[Scripting reference](../README.md) > Pointer Position Function (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_pointer_position_frac

Python: `get_pointer_position_frac()`

return the [x,y] position of the pointer in fractional coordinates.

the origin is top-left.
may return false if pointer is not available

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `get_pointer_position_frac_py`.
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_pointer_position_frac()` | ran, returned `False` |

Example written and checked by hand on the test data. Expected: with a window: [x, y] of the mouse as fractions of the window; False without a pointer (correct here).

