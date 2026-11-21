# Rotation Centre

[Scripting reference](../README.md) > Rotation Centre (11 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_text_for_rotation_centre_cube_size

Python: `get_text_for_rotation_centre_cube_size()`  
Scheme: `(get-text-for-rotation-centre-cube-size)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_rotation_centre_cube_size()` | ran, returned `<Swig Object of type 'gchar *' at 0x10b833840>` |
| Scheme | `(get-text-for-rotation-centre-cube-size)` | ran, returned `#<swig-pointer gchar * 94a4d7db0>` |

### go_to_ligand

Python: `go_to_ligand()`  
Scheme: `(go-to-ligand)`

centre on the ligand of the "active molecule", if we are
 already there, centre on the next hetgroup (etc)

Arguments: none. Returns: a value (see the result of the example).

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `go_to_ligand()` | ran, returned `[0.0, 0.0, 0.0]` |
| Scheme | `(go-to-ligand)` | ran (no return value, nothing visible changed) |

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### recentre_on_read_pdb

Python: `recentre_on_read_pdb()`  
Scheme: `(recentre-on-read-pdb)`

return the recentre-on-pdb state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `recentre_on_read_pdb()` | ran, returned `1` |
| Scheme | `(recentre-on-read-pdb)` | ran, returned `1` |

Python and Scheme gave the same answer.

### rotation_centre_position

Python: `rotation_centre_position(axis)`  
Scheme: `(rotation-centre-position axis)`

Arguments: axis (a whole number). Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotation_centre_position(1)` | ran, returned `8.686544418334961` |
| Scheme | `(rotation-centre-position 1)` | ran, returned `8.686544418334961` |

Python and Scheme gave the same answer.

### set_go_to_ligand_n_atoms_limit

Python: `set_go_to_ligand_n_atoms_limit(n_atom_min)`  
Scheme: `(set-go-to-ligand-n-atoms-limit n-atom-min)`

go to the ligand that has more than n_atom_min atoms

Arguments: n_atom_min (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_go_to_ligand_n_atoms_limit(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-go-to-ligand-n-atoms-limit 1)` | ran (no return value, nothing visible changed) |

### set_recentre_on_read_pdb

Python: `set_recentre_on_read_pdb(int)`  
Scheme: `(set-recentre-on-read-pdb int)`

set the recentre-on-pdb state

Arguments: int (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_recentre_on_read_pdb(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-recentre-on-read-pdb 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: recentre_on_read_pdb was 1, set to 0, read back 0; Scheme: recentre-on-read-pdb was 1, set to 0, read back 0.

### set_reorienting_next_residue_mode

Python: `set_reorienting_next_residue_mode(state)`  
Scheme: `(set-reorienting-next-residue-mode state)`

rotate the view so that the next main-chain atoms are oriented
 in the same direction as the previous - hence side-chain always seems to be
"up" - set this mode to 1 for reorientation-mode - and 0 for off (standard translation)

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_reorienting_next_residue_mode(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-reorienting-next-residue-mode 1)` | ran (no return value, nothing visible changed) |

### set_rotation_centre

Python: `set_rotation_centre(x, y, z)`  
Scheme: `(set-rotation-centre x y z)`

set the rotation centre

Arguments: x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotation_centre(54.5, 9.4, 12.3)` | ran (no return value); changed: rotation centre moved 9.1 A to (54.5, 9.4, 12.3) |
| Scheme | `(set-rotation-centre 54.5 9.4 12.3)` | ran (no return value, nothing visible changed) |

### set_rotation_centre_internal

Python: `set_rotation_centre_internal(x, y, z)`  
Scheme: `(set-rotation-centre-internal x y z)`

The redraw happens somewhere else...

Arguments: x (a number), y (a number), z (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotation_centre_internal(54.5, 9.4, 12.3)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-rotation-centre-internal 54.5 9.4 12.3)` | ran (no return value, nothing visible changed) |

### set_rotation_centre_size

Python: `set_rotation_centre_size(f)`  
Scheme: `(set-rotation-centre-size f)`

set rotoation centre marker size

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotation_centre_size(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-rotation-centre-size 1.0)` | ran (no return value, nothing visible changed) |

### set_rotation_centre_size_from_widget

Python: `set_rotation_centre_size_from_widget(text)`  
Scheme: `(set-rotation-centre-size-from-widget text)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: text (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_rotation_centre_size_from_widget("0.5")` | not run: not callable from scripting: the gchar* argument type is not wrapped in either language (GUI callback) |
| Scheme | `(set-rotation-centre-size-from-widget "0.5")` | not run: not callable from scripting: the gchar* argument type is not wrapped in either language (GUI callback) |

Example written and checked by hand on the test data. Expected: internal callback of the rotation-centre size entry; not usable from scripts (its gchar* argument is not wrapped); use set_rotation_centre_size(0.5) instead.

