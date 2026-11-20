# Mouse Buttons

[Scripting reference](../README.md) > Mouse Buttons (6 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### blob_under_pointer_to_screen_centre

Python: `blob_under_pointer_to_screen_centre()`  
Scheme: `(blob-under-pointer-to-screen-centre)`

Put the blob under the cursor to the screen centre. Check only
positive blobs. Useful function if bound to a key.

The refinement map must be set. (We can't check all maps because they
are not (or may not be) on the same scale).

 Returns 1 if successfully found a blob and moved there.
 return 0 if no move.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `blob_under_pointer_to_screen_centre()` | ran, returned `0` |
| Scheme | `(blob-under-pointer-to-screen-centre)` | ran, returned `0` |

Python and Scheme gave the same answer.

### control_key_for_rotate_state

Python: `control_key_for_rotate_state()`  
Scheme: `(control-key-for-rotate-state)`

return the control key rotate state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `control_key_for_rotate_state()` | ran, returned `1` |
| Scheme | `(control-key-for-rotate-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### quanta_buttons

Python: `quanta_buttons()`  
Scheme: `(quanta-buttons)`

quanta-like buttons

Note, when you have set these, there is no way to turn them of
 again (other than restarting).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `quanta_buttons()` | ran (no return value) |
| Scheme | `(quanta-buttons)` | ran (no return value) |

### quanta_like_zoom

Python: `quanta_like_zoom()`  
Scheme: `(quanta-like-zoom)`

quanta-like zoom buttons

Note, when you have set these, there is no way to turn them of
 again (other than restarting).

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `quanta_like_zoom()` | ran (no return value) |
| Scheme | `(quanta-like-zoom)` | ran (no return value) |

### select_atom_under_pointer

Python: `select_atom_under_pointer()`  
Scheme: `(select-atom-under-pointer-scm)`

return Python false or a list of molecule number and an atom spec

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `select_atom_under_pointer_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `select_atom_under_pointer()` | ran, returned `False` |
| Scheme | `(select-atom-under-pointer-scm)` | ran, returned `#f` |

Python and Scheme gave the same answer.

### set_control_key_for_rotate

Python: `set_control_key_for_rotate(state)`  
Scheme: `(set-control-key-for-rotate state)`

Alternate mode for rotation

Prefered by some, including Dirk Kostrewa. I don't think this mode
works properly yet

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_control_key_for_rotate(1)` | ran (no return value) |
| Scheme | `(set-control-key-for-rotate 1)` | ran (no return value) |

