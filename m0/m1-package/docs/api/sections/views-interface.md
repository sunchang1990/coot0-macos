# Views Interface

[Scripting reference](../README.md) > Views Interface (20 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_action_view

Python: `add_action_view(view_name, action_function)`  
Scheme: `(add-action-view view-name action-function)`

add a view (not add to an existing view) that *does*
 something (e.g. displays or undisplays a molecule) rather than move
 the graphics.

 Returns the view number for this (new) view.

Arguments: view_name (text), action_function (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_action_view("my-name", "hello")` | ran, returned `0` |
| Scheme | `(add-action-view "my-name" "hello")` | ran, returned `1` |

### add_spin_view

Python: `add_spin_view(view_name, n_steps, degrees_total)`  
Scheme: `(add-spin-view view-name n-steps degrees-total)`

Arguments: view_name (text), n_steps (a whole number), degrees_total (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_spin_view("my-name", 1, 1.0)` | ran, returned `0` |
| Scheme | `(add-spin-view "my-name" 1 1.0)` | ran, returned `1` |

### add_view_description

Python: `add_view_description(view_number, description)`  
Scheme: `(add-view-description view-number description)`

Add a view description/annotation to the give view number

Arguments: view_number (a whole number), description (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_description(1, "hello")` | ran (no return value) |
| Scheme | `(add-view-description 1 "hello")` | ran (no return value) |

### add_view_here

Python: `add_view_here(view_name)`  
Scheme: `(add-view-here view-name)`

return the view number

Arguments: view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_here("my-name")` | ran, returned `2` |
| Scheme | `(add-view-here "my-name")` | ran, returned `3` |

### add_view_raw

Python: `add_view_raw(rcx, rcy, rcz, quat1, quat2, quat3, quat4, zoom, view_name)`  
Scheme: `(add-view-raw rcx rcy rcz quat1 quat2 quat3 quat4 zoom view-name)`

return the view number

Arguments: rcx (a number), rcy (a number), rcz (a number), quat1 (a number), quat2 (a number), quat3 (a number), quat4 (a number), zoom (a number), view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_raw(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 100.0, "my-name")` | ran, returned `4` |
| Scheme | `(add-view-raw 1.0 1.0 1.0 1.0 1.0 1.0 1.0 100.0 "my-name")` | ran, returned `5` |

### clear_all_views

Python: `clear_all_views()`  
Scheme: `(clear-all-views)`

Clear the view list

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_all_views()` | ran (no return value) |
| Scheme | `(clear-all-views)` | ran (no return value) |

### go_to_first_view

Python: `go_to_first_view(snap_to_view_flag)`  
Scheme: `(go-to-first-view snap-to-view-flag)`

go to the first view. if snap_to_view_flag, go directly, else
 smooth twisty path.

Arguments: snap_to_view_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_first_view(1)` | ran, returned `0` |
| Scheme | `(go-to-first-view 1)` | ran, returned `0` |

### go_to_view

Python: `go_to_view(view)`  
Scheme: `(go-to-view view)`

Arguments: view (a list or value). Returns: nothing.
Also available in Python as `go_to_view_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### go_to_view_number

Python: `go_to_view_number(view_number, snap_to_view_flag)`  
Scheme: `(go-to-view-number view-number snap-to-view-flag)`

Arguments: view_number (a whole number), snap_to_view_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_view_number(1, 1)` | ran, returned `0` |
| Scheme | `(go-to-view-number 1 1)` | ran, returned `0` |

### insert_action_view_after_view

Python: `insert_action_view_after_view(view_number, view_name, action_function)`  
Scheme: `(insert-action-view-after-view view-number view-name action-function)`

add an action view after the view of the given view number

 Returns the view number for this (new) view.

Arguments: view_number (a whole number), view_name (text), action_function (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `insert_action_view_after_view(1, "my-name", "hello")` | not tried |
| Scheme | `(insert-action-view-after-view 1 "my-name" "hello")` | not tried |

### n_views

Python: `n_views()`  
Scheme: `(n-views)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `n_views()` | not tried |
| Scheme | `(n-views)` | not tried |

### play_views

Python: `play_views()`  
Scheme: `(play-views)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `play_views()` | not tried |
| Scheme | `(play-views)` | not tried |

### remove_named_view

Python: `remove_named_view(view_name)`  
Scheme: `(remove-named-view view-name)`

the view with the given name

Arguments: view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_named_view("my-name")` | not tried |
| Scheme | `(remove-named-view "my-name")` | not tried |

### remove_this_view

Python: `remove_this_view()`  
Scheme: `(remove-this-view)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_this_view()` | not tried |
| Scheme | `(remove-this-view)` | not tried |

### remove_view

Python: `remove_view(view_number)`  
Scheme: `(remove-view view-number)`

the given view number

Arguments: view_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_view(1)` | not tried |
| Scheme | `(remove-view 1)` | not tried |

### save_views

Python: `save_views(view_file_name)`  
Scheme: `(save-views view-file-name)`

save views to view_file_name

Arguments: view_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_views("tutorial-modern.pdb")` | not tried |
| Scheme | `(save-views "tutorial-modern.pdb")` | not tried |

### set_views_play_speed

Python: `set_views_play_speed(f)`  
Scheme: `(set-views-play-speed f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_views_play_speed(1.0)` | not tried |
| Scheme | `(set-views-play-speed 1.0)` | not tried |

### view_description

Python: `view_description(view_number)`  
Scheme: `(view-description view-number)`

Arguments: view_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `view_description_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `view_description(1)` | not tried |
| Scheme | `(view-description 1)` | not tried |

### view_name

Python: `view_name(view_number)`  
Scheme: `(view-name view-number)`

return the name of the given view, if view_number does not
 specify a view return Python value False

Arguments: view_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `view_name_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `view_name(1)` | not tried |
| Scheme | `(view-name 1)` | not tried |

### views_play_speed

Python: `views_play_speed()`  
Scheme: `(views-play-speed)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `views_play_speed()` | not tried |
| Scheme | `(views-play-speed)` | not tried |

