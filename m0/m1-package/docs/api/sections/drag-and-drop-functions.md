# Drag and Drop Functions

[Scripting reference](../README.md) > Drag and Drop Functions (1 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### handle_drag_and_drop_string

Python: `handle_drag_and_drop_string(uri)`  
Scheme: `(handle-drag-and-drop-string uri)`

Arguments: uri (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_drag_and_drop_string("hello")` | ran, returned `0` |
| Scheme | `(handle-drag-and-drop-string "hello")` | ran, returned `0` |

