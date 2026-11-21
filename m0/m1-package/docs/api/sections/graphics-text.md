# Graphics Text

[Scripting reference](../README.md) > Graphics Text (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### edit_text

Python: `edit_text(text_handle, new_text)`  
Scheme: `(edit-text text-handle new-text)`

Arguments: text_handle (a whole number), new_text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `edit_text(1, "hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(edit-text 1 "hello")` | ran (no return value, nothing visible changed) |

### place_text

Python: `place_text(text, x, y, z, size)`  
Scheme: `(place-text text x y z size)`

Put text at x,y,z

Returns a text handle

size variable is currently ignored.

Arguments: text (text), x (a number), y (a number), z (a number), size (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_text("Glu A41", 47.1, 10.6, 17.4, 1)` | ran, returned `0` |
| Scheme | `(place-text "Glu A41" 47.1 10.6 17.4 1)` | ran, returned `1` |

Example written and checked by hand on the test data. Expected: returns the handle (index) of the new text label placed at (x, y, z).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### remove_text

Python: `remove_text(text_handle)`  
Scheme: `(remove-text text-handle)`

Remove "3d" text item

Arguments: text_handle (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_text(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(remove-text 1)` | ran (no return value, nothing visible changed) |

### text_index_near_position

Python: `text_index_near_position(x, y, z, r)`  
Scheme: `(text-index-near-position x y z r)`

return the closest text that is with r A of the given
 position. If no text item is close, then return -1

Arguments: x (a number), y (a number), z (a number), r (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `place_text("Glu A41", 47.1, 10.6, 17.4, 1)`, then `text_index_near_position(47.0, 10.0, 17.0, 2.0)` | ran, returned `0` |
| Scheme | first `(place-text "Glu A41" 47.1 10.6 17.4 1)`, then `(text-index-near-position 47.0 10.0 17.0 2.0)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the index of the closest text label within r A of the point, -1 if none.

Python and Scheme gave the same answer.

