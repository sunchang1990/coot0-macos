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
| Python | `add_action_view("hide-map", "set_map_displayed(1, 0)")` | ran, returned `0`; changed: n_views(): 0 -> 1 |
| Scheme | `(add-action-view "hide-map" "(set-map-displayed 1 0)")` | ran, returned `1`; changed: n_views(): 1 -> 2 |

Example written and checked by hand on the test data. Expected: returns the new view number; the view runs the given command when played.

Note: Playing an action view with go_to_view_number does nothing in 0.9.8.96 (the code has '// do nothing' for action views): map 1 stayed displayed.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_spin_view

Python: `add_spin_view(view_name, n_steps, degrees_total)`  
Scheme: `(add-spin-view view-name n-steps degrees-total)`

Arguments: view_name (text), n_steps (a whole number), degrees_total (a number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_spin_view("spin", 10, 90.0)` | ran, returned `0`; changed: n_views(): 0 -> 1 |
| Scheme | `(add-spin-view "spin" 10 90.0)` | ran, returned `1`; changed: n_views(): 1 -> 2 |

Example written and checked by hand on the test data. Expected: returns the new view number; a view that spins 90 degrees in 10 steps is added.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_view_description

Python: `add_view_description(view_number, description)`  
Scheme: `(add-view-description view-number description)`

Add a view description/annotation to the give view number

Arguments: view_number (a whole number), description (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_description(1, "hello")` | ran (no return value, nothing visible changed) |
| Scheme | `(add-view-description 1 "hello")` | ran (no return value, nothing visible changed) |

### add_view_here

Python: `add_view_here(view_name)`  
Scheme: `(add-view-here view-name)`

return the view number

Arguments: view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_here("my-name")` | ran, returned `0`; changed: n_views(): 0 -> 1 |
| Scheme | `(add-view-here "my-name")` | ran, returned `1`; changed: n_views(): 1 -> 2 |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### add_view_raw

Python: `add_view_raw(rcx, rcy, rcz, quat1, quat2, quat3, quat4, zoom, view_name)`  
Scheme: `(add-view-raw rcx rcy rcz quat1 quat2 quat3 quat4 zoom view-name)`

return the view number

Arguments: rcx (a number), rcy (a number), rcz (a number), quat1 (a number), quat2 (a number), quat3 (a number), quat4 (a number), zoom (a number), view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_view_raw(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 100.0, "my-name")` | ran, returned `2`; changed: n_views(): 2 -> 3 |
| Scheme | `(add-view-raw 1.0 1.0 1.0 1.0 1.0 1.0 1.0 100.0 "my-name")` | ran, returned `3`; changed: n_views(): 3 -> 4 |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### clear_all_views

Python: `clear_all_views()`  
Scheme: `(clear-all-views)`

Clear the view list

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `clear_all_views()` | ran (no return value, nothing visible changed) |
| Scheme | `(clear-all-views)` | ran (no return value, nothing visible changed) |

### go_to_first_view

Python: `go_to_first_view(snap_to_view_flag)`  
Scheme: `(go-to-first-view snap-to-view-flag)`

go to the first view. if snap_to_view_flag, go directly, else
 smooth twisty path.

Arguments: snap_to_view_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `set_rotation_centre(10.0, 10.0, 10.0)`, then `go_to_first_view(1)` | ran, returned `0`; changed: rotation centre moved 31.8 A to (41.6, 8.7, 12.9) |
| Scheme | first `(add-view-here "first")`, then `(set-rotation-centre 10.0 10.0 10.0)`, then `(go-to-first-view 1)` | ran, returned `0`; changed: rotation centre moved 31.8 A to (41.6, 8.7, 12.9) |

Example written and checked by hand on the test data. Expected: jumps (snap flag 1) to the first stored view: the centre goes back to where add_view_here was called.

Python and Scheme gave the same answer.

### go_to_view

Python: `go_to_view(view)`  
Scheme: `(go-to-view view)`

Arguments: view (a list or value). Returns: nothing.
Also available in Python as `go_to_view_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_view([[0.0, 0.0, 0.0, 1.0], [50.0, 5.0, 15.0], 60.0, "my view"])` | ran (no return value); changed: rotation centre moved 38.4 A to (50.0, 5.0, 15.0); zoom: 100.0 -> 60.0 |
| Scheme | `(go-to-view (list (list 0.0 0.0 0.0 1.0) (list 50.0 5.0 15.0) 60.0 "my view"))` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: moves to the view given as [quaternion, centre, zoom, name].

### go_to_view_number

Python: `go_to_view_number(view_number, snap_to_view_flag)`  
Scheme: `(go-to-view-number view-number snap-to-view-flag)`

Arguments: view_number (a whole number), snap_to_view_flag (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `set_rotation_centre(10.0, 10.0, 10.0)`, then `go_to_view_number(0, 1)` | ran, returned `0`; changed: rotation centre moved 31.8 A to (41.6, 8.7, 12.9); zoom: 60.0 -> 100.0 |
| Scheme | first `(add-view-here "first")`, then `(set-rotation-centre 10.0 10.0 10.0)`, then `(go-to-view-number 0 1)` | ran, returned `0`; changed: rotation centre moved 31.8 A to (41.6, 8.7, 12.9) |

Example written and checked by hand on the test data. Expected: jumps to stored view 0 (snap flag 1); returns 0.

Python and Scheme gave the same answer.

### insert_action_view_after_view

Python: `insert_action_view_after_view(view_number, view_name, action_function)`  
Scheme: `(insert-action-view-after-view view-number view-name action-function)`

add an action view after the view of the given view number

 Returns the view number for this (new) view.

Arguments: view_number (a whole number), view_name (text), action_function (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `add_spin_view("spin", 10, 90.0)`, then `insert_action_view_after_view(0, "show-map", "set_map_displayed(1, 1)")` | ran, returned `1`; changed: n_views(): 2 -> 3 |
| Scheme | first `(add-view-here "first")`, then `(add-spin-view "spin" 10 90.0)`, then `(insert-action-view-after-view 0 "show-map" "(set-map-displayed 1 1)")` | ran, returned `1`; changed: n_views(): 5 -> 6 |

Example written and checked by hand on the test data. Expected: returns 1: the action view is inserted after view 0.

Python and Scheme gave the same answer.

### n_views

Python: `n_views()`  
Scheme: `(n-views)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `n_views()` | ran, returned `1` |
| Scheme | first `(add-view-here "first")`, then `(n-views)` | ran, returned `2` |

Example written and checked by hand on the test data. Expected: the number of stored views: 1 after add_view_here.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### play_views

Python: `play_views()`  
Scheme: `(play-views)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `play_views()` | ran (no return value, nothing visible changed) |
| Scheme | `(play-views)` | ran (no return value, nothing visible changed) |

### remove_named_view

Python: `remove_named_view(view_name)`  
Scheme: `(remove-named-view view-name)`

the view with the given name

Arguments: view_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `add_spin_view("spin", 10, 90.0)`, then `remove_named_view("spin")` | ran, returned `0`; changed: n_views(): 2 -> 1 |
| Scheme | first `(add-view-here "first")`, then `(add-spin-view "spin" 10 90.0)`, then `(remove-named-view "spin")` | ran, returned `0`; changed: n_views(): 3 -> 2 |

Example written and checked by hand on the test data. Expected: the view called spin is removed (n_views drops by 1); returns 0.

Python and Scheme gave the same answer.

### remove_this_view

Python: `remove_this_view()`  
Scheme: `(remove-this-view)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_this_view()` | ran (no return value, nothing visible changed) |
| Scheme | `(remove-this-view)` | ran (no return value, nothing visible changed) |

### remove_view

Python: `remove_view(view_number)`  
Scheme: `(remove-view view-number)`

the given view number

Arguments: view_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `remove_view(1)` | ran (no return value); changed: n_views(): 2 -> 1 |
| Scheme | `(remove-view 1)` | ran (no return value, nothing visible changed) |

### save_views

Python: `save_views(view_file_name)`  
Scheme: `(save-views view-file-name)`

save views to view_file_name

Arguments: view_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `save_views("tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(save-views "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### set_views_play_speed

Python: `set_views_play_speed(f)`  
Scheme: `(set-views-play-speed f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_views_play_speed(1.0)` | ran (no return value); changed: views_play_speed(): 10 -> 1 |
| Scheme | `(set-views-play-speed 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: views_play_speed was 10.0, set to 15.5, read back 15.5; Scheme: views-play-speed was 10.0, set to 15.5, read back 15.5.

### view_description

Python: `view_description(view_number)`  
Scheme: `(view-description view-number)`

Arguments: view_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `view_description_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("v0")`, then `add_view_description(0, "start view")`, then `view_description(0)` | ran, returned `'start view'` |
| Scheme | first `(add-view-here "v0")`, then `(add-view-description 0 "start view")`, then `(view-description 0)` | ran, returned `"start view"` |

Example written and checked by hand on the test data. Expected: the description of view 0; False if the view has none or does not exist.

Python and Scheme gave the same answer.

### view_name

Python: `view_name(view_number)`  
Scheme: `(view-name view-number)`

return the name of the given view, if view_number does not
 specify a view return Python value False

Arguments: view_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `view_name_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `add_view_here("first")`, then `add_spin_view("spin", 10, 90.0)`, then `view_name(1)` | ran, returned `'v0'` |
| Scheme | first `(add-view-here "first")`, then `(add-spin-view "spin" 10 90.0)`, then `(view-name 1)` | ran, returned `"v0"` |

Example written and checked by hand on the test data. Expected: the name of view 1; False for a view number that does not exist.

Python and Scheme gave the same answer.

### views_play_speed

Python: `views_play_speed()`  
Scheme: `(views-play-speed)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `views_play_speed()` | ran, returned `10.0` |
| Scheme | `(views-play-speed)` | ran, returned `10.0` |

Python and Scheme gave the same answer.

