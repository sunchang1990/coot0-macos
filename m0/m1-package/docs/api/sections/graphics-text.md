# Graphics Text

[Scripting reference](../README.md) > Graphics Text (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### edit_text

Python: `edit_text(text_handle, new_text)`  
Scheme: `(edit-text text-handle new-text)`

Arguments: text_handle (a whole number), new_text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `edit_text(1, "hello")` | ran (no return value) |
| Scheme | `(edit-text 1 "hello")` | ran (no return value) |

### place_text

Python: `place_text(text, x, y, z, size)`  
Scheme: `(place-text text x y z size)`

Put text at x,y,z

Returns a text handle

size variable is currently ignored.

Arguments: text (text), x (a number), y (a number), z (a number), size (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `place_text("hello", 54.5, 9.4, 12.3, 10)` | not tried |
| Scheme | `(place-text "hello" 54.5 9.4 12.3 10)` | not tried |

### remove_text

Python: `remove_text(text_handle)`  
Scheme: `(remove-text text-handle)`

Remove "3d" text item

Arguments: text_handle (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_text(1)` | not tried |
| Scheme | `(remove-text 1)` | not tried |

### text_index_near_position

Python: `text_index_near_position(x, y, z, r)`  
Scheme: `(text-index-near-position x y z r)`

return the closest text that is with r A of the given
 position. If no text item is close, then return -1

Arguments: x (a number), y (a number), z (a number), r (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `text_index_near_position(54.5, 9.4, 12.3, 0.5)` | not tried |
| Scheme | `(text-index-near-position 54.5 9.4 12.3 0.5)` | not tried |

