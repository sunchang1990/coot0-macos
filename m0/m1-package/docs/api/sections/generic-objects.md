# Generic Objects

[Scripting reference](../README.md) > Generic Objects (21 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### attach_generic_object_to_molecule

Python: `attach_generic_object_to_molecule(obj_number, imol)`  
Scheme: `(attach-generic-object-to-molecule obj-number imol)`

attach the generic object to a particular molecule 

one might do this if the generic object is specific to a molecule.

Arguments: obj_number (a whole number), imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `attach_generic_object_to_molecule(1, 0)` | ran (no return value, nothing visible changed) |
| Scheme | `(attach-generic-object-to-molecule 1 0)` | ran (no return value, nothing visible changed) |

### close_generic_object

Python: `close_generic_object(object_number)`  
Scheme: `(close-generic-object object-number)`

close generic object, clear the lines/points etc, not
 available for buttons/displaying etc

Arguments: object_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `close_generic_object(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(close-generic-object 1)` | ran (no return value, nothing visible changed) |

### generic_object_clear

Python: `generic_object_clear(object_number)`  
Scheme: `(generic-object-clear object-number)`

clear out the lines and points from object_number, but keep
 it displayable (not closed).

Arguments: object_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_object_clear(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(generic-object-clear 1)` | ran (no return value, nothing visible changed) |

### generic_object_has_objects_p

Python: `generic_object_has_objects_p(obj_no)`  
Scheme: `(generic-object-has-objects-p obj-no)`

does generic display object number obj_no have things to
 display? (predicate name)

Returns 0 for no things, 1 for things.

Arguments: obj_no (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_object_has_objects_p(1)` | ran, returned `0` |
| Scheme | `(generic-object-has-objects-p 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### generic_object_index

Python: `generic_object_index(name)`  
Scheme: `(generic-object-index name)`

return the index of the object with name name, if not, return -1;

Arguments: name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `new_generic_object_number("my-object")`, then `generic_object_index("my-object")` | ran, returned `0` |
| Scheme | first `(new-generic-object-number "my-object")`, then `(generic-object-index "my-object")` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the index of the generic object with that name, -1 if there is none.

Python and Scheme gave the same answer.

### generic_object_info

Python: `generic_object_info()`  
Scheme: `(generic-object-info)`

print to the console the name and display status of the
 generic display objects

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_object_info()` | ran (no return value, nothing visible changed) |
| Scheme | `(generic-object-info)` | ran (no return value, nothing visible changed) |

### generic_object_is_displayed_p

Python: `generic_object_is_displayed_p(object_number)`  
Scheme: `(generic-object-is-displayed-p object-number)`

is generic display object displayed?

 Returns 1 for yes, otherwise 0

Arguments: object_number (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `generic_object_is_displayed_p(1)` | ran, returned `0` |
| Scheme | `(generic-object-is-displayed-p 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### generic_object_name

Python: `generic_object_name(obj_number)`  
Scheme: `(generic-object-name obj-number)`

Arguments: obj_number (a whole number). Returns: a value (see the result of the example).
Also available in Python as `generic_object_name_py`.
Also available in Scheme as `generic-object-name-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `new_generic_object_number("my-object")`, then `generic_object_name(0)` | ran, returned `'my-object'` |
| Scheme | first `(new-generic-object-number "my-object")`, then `(generic-object-name 0)` | ran, returned `"my-object"` |

Example written and checked by hand on the test data. Expected: returns the name of generic object number 0; False/#f if there is no such object.

Python and Scheme gave the same answer.

### get_generic_object_py

Python: `get_generic_object_py(obj_number)`

Arguments: obj_number (a whole number). Returns: a value (see the result of the example).
**Python only** (see [one-language-only](../one-language-only.md)).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `new_generic_object_number("my-object")`, then `get_generic_object_py(0)` | ran, returned `{'name': 'my-object', 'imol': -1, 'is_displayed_flag': 0, 'is_solid_flag': 0}` |

Example written and checked by hand on the test data. Expected: returns a dict describing the generic object (name, attached molecule, displayed/solid flags); False if no such object.

### is_closed_generic_object_p

Python: `is_closed_generic_object_p(object_number)`  
Scheme: `(is-closed-generic-object-p object-number)`

has the generic object been closed? 

 Returns 1 for yes, 0 othersize

Arguments: object_number (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `is_closed_generic_object_p(1)` | ran, returned `0` |
| Scheme | `(is-closed-generic-object-p 1)` | ran, returned `0` |

Python and Scheme gave the same answer.

### number_of_generic_objects

Python: `number_of_generic_objects()`  
Scheme: `(number-of-generic-objects)`

return the number of generic display objects

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `new_generic_object_number("my-object")`, then `number_of_generic_objects()` | ran, returned `1` |
| Scheme | first `(new-generic-object-number "my-object")`, then `(number-of-generic-objects)` | ran, returned `2` |

Example written and checked by hand on the test data. Expected: returns how many generic display objects exist (0 at start).

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### set_display_generic_object

Python: `set_display_generic_object(object_number, istate)`  
Scheme: `(set-display-generic-object object-number istate)`

set the display status of object number object_number, 

 when they are created, by default objects are not displayed, so we
 generally need this function.

Arguments: object_number (a whole number), istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_generic_object(1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-generic-object 1 1)` | ran (no return value, nothing visible changed) |

### set_display_generic_object_simple

Python: `set_display_generic_object_simple(object_number, istate)`  
Scheme: `(set-display-generic-object-simple object-number istate)`

set the display status of object number object_number, 

 set the state of a generic object to be drawn, but no redraw. 
 Use when enabling multiple generic objects.

Arguments: object_number (a whole number), istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_generic_object_simple(1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-generic-object-simple 1 1)` | ran (no return value, nothing visible changed) |

### set_display_generic_objects_as_solid

Python: `set_display_generic_objects_as_solid(state)`  
Scheme: `(set-display-generic-objects-as-solid state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_display_generic_objects_as_solid(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-display-generic-objects-as-solid 1)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_arc

Python: `to_generic_object_add_arc(object_number, colour, radius, radius_inner, from_angle, to_angle, start_point_x, start_point_y, start_point_z, start_dir_x, start_dir_y, start_dir_z, normal_x1, normal_y1, normal_z1)`  
Scheme: `(to-generic-object-add-arc object-number colour radius radius-inner from-angle to-angle start-point-x start-point-y start-point-z start-dir-x start-dir-y start-dir-z normal-x1 normal-y1 normal-z1)`

add point to generic object object_number

Arguments: object_number (a whole number), colour (text), radius (a number), radius_inner (a number), from_angle (a number), to_angle (a number), start_point_x (a number), start_point_y (a number), start_point_z (a number), start_dir_x (a number), start_dir_y (a number), start_dir_z (a number), normal_x1 (a number), normal_y1 (a number), normal_z1 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_arc(1, "hello", 5.0, 5.0, 10.0, 10.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-arc 1 "hello" 5.0 5.0 10.0 10.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_dashed_line

Python: `to_generic_object_add_dashed_line(object_number, colour, line_width, dash_density, from_x1, from_y1, from_z1, to_x2, to_y2, to_z2)`  
Scheme: `(to-generic-object-add-dashed-line object-number colour line-width dash-density from-x1 from-y1 from-z1 to-x2 to-y2 to-z2)`

add a dashed line to generic object object_number 

dash_density is number of dashes per Angstrom.

Arguments: object_number (a whole number), colour (text), line_width (a whole number), dash_density (a number), from_x1 (a number), from_y1 (a number), from_z1 (a number), to_x2 (a number), to_y2 (a number), to_z2 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_dashed_line(1, "hello", 2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-dashed-line 1 "hello" 2 1.0 1.0 1.0 1.0 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_display_list_handle

Python: `to_generic_object_add_display_list_handle(object_number, display_list_id)`  
Scheme: `(to-generic-object-add-display-list-handle object-number display-list-id)`

add a display list handle generic object

Arguments: object_number (a whole number), display_list_id (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_display_list_handle(1, 1)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-display-list-handle 1 1)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_dodecahedron

Python: `to_generic_object_add_dodecahedron(object_number, colour, radius, x, y, z)`  
Scheme: `(to-generic-object-add-dodecahedron object-number colour radius x y z)`

Arguments: object_number (a whole number), colour (text), radius (a number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_dodecahedron(1, "hello", 5.0, 54.5, 9.4, 12.3)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-dodecahedron 1 "hello" 5.0 54.5 9.4 12.3)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_line

Python: `to_generic_object_add_line(object_number, colour, line_width, from_x1, from_y1, from_z1, to_x2, to_y2, to_z2)`  
Scheme: `(to-generic-object-add-line object-number colour line-width from-x1 from-y1 from-z1 to-x2 to-y2 to-z2)`

add line to generic object object_number

Arguments: object_number (a whole number), colour (text), line_width (a whole number), from_x1 (a number), from_y1 (a number), from_z1 (a number), to_x2 (a number), to_y2 (a number), to_z2 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_line(1, "hello", 2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-line 1 "hello" 2 1.0 1.0 1.0 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_pentakis_dodecahedron

Python: `to_generic_object_add_pentakis_dodecahedron(object_number, colour, stellation_factor, radius_factor, x, y, z)`  
Scheme: `(to-generic-object-add-pentakis-dodecahedron object-number colour stellation-factor radius-factor x y z)`

Arguments: object_number (a whole number), colour (text), stellation_factor (a number), radius_factor (a number), x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_pentakis_dodecahedron(1, "hello", 1.0, 5.0, 54.5, 9.4, 12.3)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-pentakis-dodecahedron 1 "hello" 1.0 5.0 54.5 9.4 12.3)` | ran (no return value, nothing visible changed) |

### to_generic_object_add_point

Python: `to_generic_object_add_point(object_number, colour, point_width, from_x1, from_y1, from_z1)`  
Scheme: `(to-generic-object-add-point object-number colour point-width from-x1 from-y1 from-z1)`

add point to generic object object_number

Arguments: object_number (a whole number), colour (text), point_width (a whole number), from_x1 (a number), from_y1 (a number), from_z1 (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `to_generic_object_add_point(1, "hello", 2, 1.0, 1.0, 1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(to-generic-object-add-point 1 "hello" 2 1.0 1.0 1.0)` | ran (no return value, nothing visible changed) |

