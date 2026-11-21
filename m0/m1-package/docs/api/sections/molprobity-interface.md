# Molprobity Interface

[Scripting reference](../README.md) > Molprobity Interface (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### do_probe_dots_on_rotamers_and_chis_state

Python: `do_probe_dots_on_rotamers_and_chis_state()`  
Scheme: `(do-probe-dots-on-rotamers-and-chis-state)`

return the state of if run molprobity for on edit chi
 angles intermediate atoms?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_probe_dots_on_rotamers_and_chis_state()` | ran, returned `0` |
| Scheme | `(do-probe-dots-on-rotamers-and-chis-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 if probe dots are drawn while changing rotamers/chis, else 0 (default).

Python and Scheme gave the same answer.

### do_probe_dots_post_refine_state

Python: `do_probe_dots_post_refine_state()`  
Scheme: `(do-probe-dots-post-refine-state)`

show the state of shall we run molprobity after a
 refinement has happened?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_probe_dots_post_refine_state()` | ran, returned `0` |
| Scheme | `(do-probe-dots-post-refine-state)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns 1 if probe dots are made after each refinement, else 0 (default).

Python and Scheme gave the same answer.

### handle_read_draw_probe_dots

Python: `handle_read_draw_probe_dots(dots_file)`  
Scheme: `(handle-read-draw-probe-dots dots-file)`

pass a filename that contains molprobity's probe output in XtalView
format

Arguments: dots_file (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("dots.kin", "w").write("# so small overlap)\n47.9 11.9 18.9 48.2 12.0 19.1 yellow\n47.0 11.0 18.0 47.0 11.0 18.0 red\n")`, then `handle_read_draw_probe_dots("dots.kin")` | ran (no return value, nothing visible changed) |
| Scheme | first `(call-with-output-file "dots.kin" (lambda (port) (display "# so small overlap)\n47.9 11.9 18.9 48.2 12.0 19.1 yellow\n47.0 11.0 18.0 47.0 11.0 18.0 red\n" port) ...`, then `(handle-read-draw-probe-dots "dots.kin")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: reads a probe dots file ('# ... small overlap)' headers, then 'x1 y1 z1 x2 y2 z2 colour' lines) into generic objects.

### handle_read_draw_probe_dots_unformatted

Python: `handle_read_draw_probe_dots_unformatted(dots_file, imol, show_clash_gui_flag)`  
Scheme: `(handle-read-draw-probe-dots-unformatted dots-file imol show-clash-gui-flag)`

pass a filename that contains molprobity's probe output in unformatted
format

Arguments: dots_file (text), imol (a whole number), show_clash_gui_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `open("probe-dots.txt", "w").write(":1->1:so: A  41 GLU  C   : A  43 VAL  N   :-0.503:-0.331:45.969:11.365:14.759:0.166:-0.1036:C:N:45.911:11.420:14.613:15.36:14 ...`, then `handle_read_draw_probe_dots_unformatted("probe-dots.txt", 0, 0)` | ran (no return value, nothing visible changed) |
| Scheme | first `(call-with-output-file "probe-dots.txt" (lambda (port) (display ":1->1:so: A  41 GLU  C   : A  43 VAL  N   :-0.503:-0.331:45.969:11.365:14.759:0.166:-0.1036:C:N ...`, then `(handle-read-draw-probe-dots-unformatted "probe-dots.txt" 0 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: reads probe -u output (3 real probe lines for A41/A43 here) and draws them as generic objects per contact type.

Note: the setup lines are 3 lines of real 'probe -u' output for tutorial-modern.pdb residues A41-43

### interactive_probe_dots_molprobity_radius

Python: `interactive_probe_dots_molprobity_radius()`  
Scheme: `(interactive-probe-dots-molprobity-radius)`

return the radius over which we can run interactive probe.

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `interactive_probe_dots_molprobity_radius()` | ran, returned `6.0` |
| Scheme | `(interactive-probe-dots-molprobity-radius)` | ran, returned `6.0` |

Example written and checked by hand on the test data. Expected: returns the radius (A) of the interactive probe dots region (default 6.0).

Python and Scheme gave the same answer.

### set_do_coot_probe_dots_during_refine

Python: `set_do_coot_probe_dots_during_refine(state)`  
Scheme: `(set-do-coot-probe-dots-during-refine state)`

state is 1 for on and 0 for off

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_coot_probe_dots_during_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-do-coot-probe-dots-during-refine 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: turns Coot's own contact dots during refinement on (no getter; seen only in the graphics window).

### set_do_probe_dots_on_rotamers_and_chis

Python: `set_do_probe_dots_on_rotamers_and_chis(state)`  
Scheme: `(set-do-probe-dots-on-rotamers-and-chis state)`

shall we run molprobity for on edit chi angles intermediate atoms?

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_probe_dots_on_rotamers_and_chis(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-do-probe-dots-on-rotamers-and-chis 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: turns probe dots during rotamer/chi changes on; the _state getter then returns 1.

Setting checked (set to another value and read back, then put back): Python: do_probe_dots_on_rotamers_and_chis_state was 0, set to 1, read back 1; Scheme: do-probe-dots-on-rotamers-and-chis-state was 0, set to 1, read back 1.

### set_do_probe_dots_post_refine

Python: `set_do_probe_dots_post_refine(state)`  
Scheme: `(set-do-probe-dots-post-refine state)`

shall we run molprobity after a refinement has happened?

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_probe_dots_post_refine(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-do-probe-dots-post-refine 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: turns probe dots after refinement on; do_probe_dots_post_refine_state() then returns 1.

Setting checked (set to another value and read back, then put back): Python: do_probe_dots_post_refine_state was 0, set to 1, read back 1; Scheme: do-probe-dots-post-refine-state was 0, set to 1, read back 1.

### set_interactive_probe_dots_molprobity_radius

Python: `set_interactive_probe_dots_molprobity_radius(r)`  
Scheme: `(set-interactive-probe-dots-molprobity-radius r)`

set the radius over which we can run interactive probe,
 bigger is better but slower.

 default is 6.0

Arguments: r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_interactive_probe_dots_molprobity_radius(4.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-interactive-probe-dots-molprobity-radius 4.0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the interactive probe dots radius; interactive_probe_dots_molprobity_radius() returns it.

Setting checked (set to another value and read back, then put back): Python: interactive_probe_dots_molprobity_radius was 6.0, set to 9.5, read back 9.5; Scheme: interactive-probe-dots-molprobity-radius was 6.0, set to 9.5, read back 9.5.

### unmangle_hydrogen_name

Python: `unmangle_hydrogen_name(pdb_hydrogen_name)`  
Scheme: `(unmangle-hydrogen-name pdb-hydrogen-name)`

make an attempt to convert pdb hydrogen name to the name
 used in Coot (and the refmac dictionary, perhaps).

Arguments: pdb_hydrogen_name (text). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unmangle_hydrogen_name("my-name")` | ran, returned `'my-name'` |
| Scheme | `(unmangle-hydrogen-name "my-name")` | ran, returned `"my-name"` |

Python and Scheme gave the same answer.

### user_mods

Python: `user_mods(file_name)`  
Scheme: `(user-mods file-name)`

return the parsed user mod fields from the PDB file
 file_name (output by reduce most likely)

Arguments: file_name (text). Returns: a value (see the result of the example).
Also available in Python as `user_mods_py`.
Also available in Scheme as `user-mods-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `user_mods("tutorial-modern.pdb")` | ran, returned `[[], []]` |
| Scheme | `(user-mods "tutorial-modern.pdb")` | ran, returned `(() ())` |

Python and Scheme gave the same answer.

