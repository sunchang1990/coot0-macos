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
| Python | `do_probe_dots_on_rotamers_and_chis_state()` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(do-probe-dots-on-rotamers-and-chis-state)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### do_probe_dots_post_refine_state

Python: `do_probe_dots_post_refine_state()`  
Scheme: `(do-probe-dots-post-refine-state)`

show the state of shall we run molprobity after a
 refinement has happened?

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_probe_dots_post_refine_state()` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(do-probe-dots-post-refine-state)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### handle_read_draw_probe_dots

Python: `handle_read_draw_probe_dots(dots_file)`  
Scheme: `(handle-read-draw-probe-dots dots-file)`

pass a filename that contains molprobity's probe output in XtalView
format

Arguments: dots_file (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_probe_dots("tutorial-modern.pdb")` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(handle-read-draw-probe-dots "tutorial-modern.pdb")` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### handle_read_draw_probe_dots_unformatted

Python: `handle_read_draw_probe_dots_unformatted(dots_file, imol, show_clash_gui_flag)`  
Scheme: `(handle-read-draw-probe-dots-unformatted dots-file imol show-clash-gui-flag)`

pass a filename that contains molprobity's probe output in unformatted
format

Arguments: dots_file (text), imol (a whole number), show_clash_gui_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `handle_read_draw_probe_dots_unformatted("tutorial-modern.pdb", 0, 1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(handle-read-draw-probe-dots-unformatted "tutorial-modern.pdb" 0 1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### interactive_probe_dots_molprobity_radius

Python: `interactive_probe_dots_molprobity_radius()`  
Scheme: `(interactive-probe-dots-molprobity-radius)`

return the radius over which we can run interactive probe.

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `interactive_probe_dots_molprobity_radius()` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(interactive-probe-dots-molprobity-radius)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### set_do_coot_probe_dots_during_refine

Python: `set_do_coot_probe_dots_during_refine(state)`  
Scheme: `(set-do-coot-probe-dots-during-refine state)`

state is 1 for on and 0 for off

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_coot_probe_dots_during_refine(1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-do-coot-probe-dots-during-refine 1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### set_do_probe_dots_on_rotamers_and_chis

Python: `set_do_probe_dots_on_rotamers_and_chis(state)`  
Scheme: `(set-do-probe-dots-on-rotamers-and-chis state)`

shall we run molprobity for on edit chi angles intermediate atoms?

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_probe_dots_on_rotamers_and_chis(1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-do-probe-dots-on-rotamers-and-chis 1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### set_do_probe_dots_post_refine

Python: `set_do_probe_dots_post_refine(state)`  
Scheme: `(set-do-probe-dots-post-refine state)`

shall we run molprobity after a refinement has happened?

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_do_probe_dots_post_refine(1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-do-probe-dots-post-refine 1)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

### set_interactive_probe_dots_molprobity_radius

Python: `set_interactive_probe_dots_molprobity_radius(r)`  
Scheme: `(set-interactive-probe-dots-molprobity-radius r)`

set the radius over which we can run interactive probe,
 bigger is better but slower.

 default is 6.0

Arguments: r (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_interactive_probe_dots_molprobity_radius(0.5)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-interactive-probe-dots-molprobity-radius 0.5)` | not run: not run automatically (probe: exits, uses the network, an external program, files or a screen) |

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

