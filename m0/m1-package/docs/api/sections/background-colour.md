# Background Colour

[Scripting reference](../README.md) > Background Colour (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### background_is_black_p

Python: `background_is_black_p()`  
Scheme: `(background-is-black-p)`

is the background black (or nearly black)?

Returns 1 if the background is black (or nearly black),
else return 0.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `background_is_black_p()` | ran, returned `1` |
| Scheme | `(background-is-black-p)` | ran, returned `1` |

Python and Scheme gave the same answer.

### redraw_background

Python: `redraw_background()`  
Scheme: `(redraw-background)`

re draw the background colour when switching between mono and stereo

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `redraw_background()` | ran (no return value) |
| Scheme | `(redraw-background)` | ran (no return value) |

### set_background_colour

Python: `set_background_colour(red, green, blue)`  
Scheme: `(set-background-colour red green blue)`

set the background colour

 red, green and blue are numbers between 0.0 and 1.0

Arguments: red (a number), green (a number), blue (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_background_colour(0.5, 0.5, 0.5)` | ran (no return value) |
| Scheme | `(set-background-colour 0.5 0.5 0.5)` | ran (no return value) |

