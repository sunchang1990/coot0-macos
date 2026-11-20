# Coot's Hole implementation

[Scripting reference](../README.md) > Coot's Hole implementation (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### hole

Python: `hole(imol, start_x, start_y, start_z, end_x, end_y, end_z, colour_map_multiplier, colour_map_offset, n_runs, show_probe_radius_graph_flag, export_surface_dots_file_name)`  
Scheme: `(hole imol start-x start-y start-z end-x end-y end-z colour-map-multiplier colour-map-offset n-runs show-probe-radius-graph-flag export-surface-dots-file-name)`

starting piont and end point, colour map multiplier and
 shall the probe radius graph be shown (dummy value currently).

if export_dots_file_name string length is zero, then don't try to
export the surface dots.

Arguments: imol (a whole number), start_x (a number), start_y (a number), start_z (a number), end_x (a number), end_y (a number), end_z (a number), colour_map_multiplier (a number), colour_map_offset (a number), n_runs (a whole number), show_probe_radius_graph_flag (true or false), export_surface_dots_file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `hole(0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1, True, "tutorial-modern.pdb")` | ran (no return value) |
| Scheme | `(hole 0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1 1 "tutorial-modern.pdb")` | ran (no return value) |

### link_info

Python: `link_info(imol)`  
Scheme: `(link-info imol)`

return a list of the links in the given molecule.
will return an empty list for non-valid (i.e. non-model) molecules

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `link_info_py`.
Also available in Scheme as `link-info-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `link_info(0)` | ran, returned `[]` |
| Scheme | `(link-info 0)` | ran, returned `()` |

Python and Scheme gave the same answer.

### make_link

Python: `make_link(imol, spec_1, spec_2, link_name, length)`  
Scheme: `(make-link imol spec-1 spec-2 link-name length)`

make a link between the specified atoms

Arguments: imol (a whole number), spec_1 (a list or value), spec_2 (a list or value), link_name (text), length (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_link(0, ["A", 41, ""], ["A", 41, ""], "my-name", 1.0)` | ran (no return value) |
| Scheme | `(make-link 0 (list "A" 41 "") (list "A" 41 "") "my-name" 1.0)` | ran (no return value) |

### probe_radius_graph_close_callback

Python: `probe_radius_graph_close_callback(button, dialog)`  
Scheme: `(probe-radius-graph-close-callback button dialog)`

GUI stuff

Arguments: button (`GtkWidget *`), dialog (`GtkWidget *`). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### show_hole_probe_radius_graph

Python: `show_hole_probe_radius_graph(hole_path, path_length)`  
Scheme: `(show-hole-probe-radius-graph hole-path path-length)`

Arguments: hole_path (a list), path_length (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### show_hole_probe_radius_graph_basic

Python: `show_hole_probe_radius_graph_basic(hole_path, path_length)`  
Scheme: `(show-hole-probe-radius-graph-basic hole-path path-length)`

Arguments: hole_path (a list), path_length (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

### show_hole_probe_radius_graph_goocanvas

Python: `show_hole_probe_radius_graph_goocanvas(hole_path, path_length)`  
Scheme: `(show-hole-probe-radius-graph-goocanvas hole-path path-length)`

Arguments: hole_path (a list), path_length (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |
| Scheme | (no automatic example) | not run: no automatic example (it takes a list, a widget or an object) |

