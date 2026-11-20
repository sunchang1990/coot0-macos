# Sequence View Interface

[Scripting reference](../README.md) > Sequence View Interface (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### add_on_sequence_view_choices

Python: `add_on_sequence_view_choices()`  
Scheme: `(add-on-sequence-view-choices)`

this is a widget function, it shouldn't be here

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_on_sequence_view_choices()` | ran (no return value) |
| Scheme | `(add-on-sequence-view-choices)` | ran (no return value) |

### change_peptide_carbonyl_by

Python: `change_peptide_carbonyl_by(angle)`  
Scheme: `(change-peptide-carbonyl-by angle)`

Arguments: angle (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_peptide_carbonyl_by(10.0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(change-peptide-carbonyl-by 10.0)` | stopped Coot when tried without a window (not checked with a window) |

### change_peptide_carbonyl_by_current_button_pos

Python: `change_peptide_carbonyl_by_current_button_pos(ix, iy)`  
Scheme: `(change-peptide-carbonyl-by-current-button-pos ix iy)`

Arguments: ix (a whole number), iy (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_peptide_carbonyl_by_current_button_pos(1, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(change-peptide-carbonyl-by-current-button-pos 1 1)` | stopped Coot when tried without a window (not checked with a window) |

### change_peptide_peptide_by

Python: `change_peptide_peptide_by(angle)`  
Scheme: `(change-peptide-peptide-by angle)`

in degrees.

Arguments: angle (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_peptide_peptide_by(10.0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(change-peptide-peptide-by 10.0)` | stopped Coot when tried without a window (not checked with a window) |

### change_peptide_peptide_by_current_button_pos

Python: `change_peptide_peptide_by_current_button_pos(ix, iy)`  
Scheme: `(change-peptide-peptide-by-current-button-pos ix iy)`

Arguments: ix (a whole number), iy (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `change_peptide_peptide_by_current_button_pos(1, 1)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(change-peptide-peptide-by-current-button-pos 1 1)` | stopped Coot when tried without a window (not checked with a window) |

### do_sequence_view

Python: `do_sequence_view(imol)`  
Scheme: `(do-sequence-view imol)`

display the sequence view dialog for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_sequence_view(0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(do-sequence-view 0)` | stopped Coot when tried without a window (not checked with a window) |

### execute_setup_backbone_torsion_edit

Python: `execute_setup_backbone_torsion_edit(imol, atom_index)`  
Scheme: `(execute-setup-backbone-torsion-edit imol atom-index)`

in degress

Arguments: imol (a whole number), atom_index (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `execute_setup_backbone_torsion_edit(0, 0)` | ran (no return value) |
| Scheme | `(execute-setup-backbone-torsion-edit 0 0)` | ran (no return value) |

### nsv

Python: `nsv(imol)`  
Scheme: `(nsv imol)`

display the sequence view for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `nsv(0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(nsv 0)` | stopped Coot when tried without a window (not checked with a window) |

### sequence_view_old_style

Python: `sequence_view_old_style(imol)`  
Scheme: `(sequence-view-old-style imol)`

show old style sequence view

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `sequence_view_old_style(0)` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(sequence-view-old-style 0)` | stopped Coot when tried without a window (not checked with a window) |

### set_backbone_torsion_carbonyl_button_start_pos

Python: `set_backbone_torsion_carbonyl_button_start_pos(ix, iy)`  
Scheme: `(set-backbone-torsion-carbonyl-button-start-pos ix iy)`

Arguments: ix (a whole number), iy (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_backbone_torsion_carbonyl_button_start_pos(1, 1)` | ran (no return value) |
| Scheme | `(set-backbone-torsion-carbonyl-button-start-pos 1 1)` | ran (no return value) |

### set_backbone_torsion_peptide_button_start_pos

Python: `set_backbone_torsion_peptide_button_start_pos(ix, iy)`  
Scheme: `(set-backbone-torsion-peptide-button-start-pos ix iy)`

Arguments: ix (a whole number), iy (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_backbone_torsion_peptide_button_start_pos(1, 1)` | ran (no return value) |
| Scheme | `(set-backbone-torsion-peptide-button-start-pos 1 1)` | ran (no return value) |

### set_nsv_canvas_pixel_limit

Python: `set_nsv_canvas_pixel_limit(cpl)`  
Scheme: `(set-nsv-canvas-pixel-limit cpl)`

set the pixel limit for sequence view windows

Arguments: cpl (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_nsv_canvas_pixel_limit(1)` | ran (no return value) |
| Scheme | `(set-nsv-canvas-pixel-limit 1)` | ran (no return value) |

### set_sequence_view_is_docked

Python: `set_sequence_view_is_docked(state)`  
Scheme: `(set-sequence-view-is-docked state)`

control where the sequence view is displayed

in the main application or a new dialog

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_sequence_view_is_docked(1)` | ran (no return value) |
| Scheme | `(set-sequence-view-is-docked 1)` | ran (no return value) |

### setup_backbone_torsion_edit

Python: `setup_backbone_torsion_edit(state)`  
Scheme: `(setup-backbone-torsion-edit state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_backbone_torsion_edit(1)` | ran (no return value) |
| Scheme | `(setup-backbone-torsion-edit 1)` | ran (no return value) |

### update_sequence_view_current_position_highlight_from_active_atom

Python: `update_sequence_view_current_position_highlight_from_active_atom()`  
Scheme: `(update-sequence-view-current-position-highlight-from-active-atom)`

update the sequnce view current position highlight based on active atom

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `update_sequence_view_current_position_highlight_from_active_atom()` | ran (no return value) |
| Scheme | `(update-sequence-view-current-position-highlight-from-active-atom)` | ran (no return value) |

