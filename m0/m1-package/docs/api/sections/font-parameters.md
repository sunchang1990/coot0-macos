# Font Parameters

[Scripting reference](../README.md) > Font Parameters (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_font_size

Python: `get_font_size()`  
Scheme: `(get-font-size)`

return the font size

 Returns 1 (small) 2 (medium, default) 3 (large)

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_font_size()` | ran, returned `2` |
| Scheme | `(get-font-size)` | ran, returned `2` |

Python and Scheme gave the same answer.

### set_font_colour

Python: `set_font_colour(red, green, blue)`  
Scheme: `(set-font-colour red green blue)`

set the colour of the atom label font - the arguments are
 in the range 0->1

Arguments: red (a number), green (a number), blue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_font_colour(0.5, 0.5, 0.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-font-colour 0.5 0.5 0.5)` | ran (no return value, nothing visible changed) |

### set_font_size

Python: `set_font_size(i)`  
Scheme: `(set-font-size i)`

set the font size

 @param i 1 (small) 2 (medium, default) 3 (large)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_font_size(1)` | ran (no return value); changed: get_font_size(): 2 -> 1 |
| Scheme | `(set-font-size 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: get_font_size was 2, set to 0, read back 0; Scheme: get-font-size was 2, set to 0, read back 0.

### set_use_stroke_characters

Python: `set_use_stroke_characters(state)`  
Scheme: `(set-use-stroke-characters state)`

set use stroke characters

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_use_stroke_characters(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-use-stroke-characters 1)` | ran (no return value, nothing visible changed) |

