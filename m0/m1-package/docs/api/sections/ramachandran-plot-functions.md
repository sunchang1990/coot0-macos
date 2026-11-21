# Ramachandran Plot Functions

[Scripting reference](../README.md) > Ramachandran Plot Functions (14 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### accept_phi_psi_moving_atoms

Python: `accept_phi_psi_moving_atoms()`  
Scheme: `(accept-phi-psi-moving-atoms)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `accept_phi_psi_moving_atoms()` | ran (no return value, nothing visible changed) |
| Scheme | `(accept-phi-psi-moving-atoms)` | ran (no return value, nothing visible changed) |

### add_on_rama_choices

Python: `add_on_rama_choices()`  
Scheme: `(add-on-rama-choices)`

the the menu

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `add_on_rama_choices()` | ran (no return value, nothing visible changed) |
| Scheme | `(add-on-rama-choices)` | ran (no return value, nothing visible changed) |

### destroy_edit_backbone_rama_plot

Python: `destroy_edit_backbone_rama_plot()`  
Scheme: `(destroy-edit-backbone-rama-plot)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `destroy_edit_backbone_rama_plot()` | ran (no return value, nothing visible changed) |
| Scheme | `(destroy-edit-backbone-rama-plot)` | ran (no return value, nothing visible changed) |

### do_ramachandran_plot

Python: `do_ramachandran_plot(imol)`  
Scheme: `(do-ramachandran-plot imol)`

Ramachandran plot for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `do_ramachandran_plot(0)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(do-ramachandran-plot 0)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens the Ramachandran plot window for molecule 0.

### ramachandran_plot_differences

Python: `ramachandran_plot_differences(imol1, imol2)`  
Scheme: `(ramachandran-plot-differences imol1 imol2)`

2 molecule ramachandran plot (NCS differences) a.k.a. A Kleywegt Plot.

Arguments: imol1 (a whole number), imol2 (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ramachandran_plot_differences(0, 0)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(ramachandran-plot-differences 0 0)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens a Kleywegt plot window (phi/psi differences between two molecules).

### ramachandran_plot_differences_by_chain

Python: `ramachandran_plot_differences_by_chain(imol1, imol2, a_chain, b_chain)`  
Scheme: `(ramachandran-plot-differences-by-chain imol1 imol2 a-chain b-chain)`

A chain-specific Kleywegt Plot.

Arguments: imol1 (a whole number), imol2 (a whole number), a_chain (text), b_chain (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ramachandran_plot_differences_by_chain(0, 0, "A", "B")` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(ramachandran-plot-differences-by-chain 0 0 "A" "B")` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: opens a Kleywegt plot window comparing chain A with its NCS copy chain B.

### ramachandran_psi_axis_mode

Python: `ramachandran_psi_axis_mode()`  
Scheme: `(ramachandran-psi-axis-mode)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `ramachandran_psi_axis_mode()` | ran, returned `0` |
| Scheme | `(ramachandran-psi-axis-mode)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the psi axis mode of the Ramachandran plot (0 = standard -180..180).

Python and Scheme gave the same answer.

### set_kleywegt_plot_n_diffs

Python: `set_kleywegt_plot_n_diffs(n_diffs)`  
Scheme: `(set-kleywegt-plot-n-diffs n-diffs)`

set the number of biggest difference arrows on the Kleywegt
 plot.

Arguments: n_diffs (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_kleywegt_plot_n_diffs(10)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-kleywegt-plot-n-diffs 10)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets how many biggest-difference arrows the Kleywegt plot draws.

### set_moving_atoms

Python: `set_moving_atoms(phi, psi)`  
Scheme: `(set-moving-atoms phi psi)`

Arguments: phi (a number), psi (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_moving_atoms(-60.0, -45.0)` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(set-moving-atoms -60.0 -45.0)` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: internal (Ramachandran plot editing): sets phi/psi of the residue being edited in the plot.

### set_ramachandran_plot_background_block_size

Python: `set_ramachandran_plot_background_block_size(blocksize)`  
Scheme: `(set-ramachandran-plot-background-block-size blocksize)`

set the ramachandran plot background block size.

 Smaller is smoother but slower. Should be divisible exactly into
 360. Default value is 10.

Arguments: blocksize (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ramachandran_plot_background_block_size(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ramachandran-plot-background-block-size 1.0)` | ran (no return value, nothing visible changed) |

### set_ramachandran_plot_contour_levels

Python: `set_ramachandran_plot_contour_levels(level_prefered, level_allowed)`  
Scheme: `(set-ramachandran-plot-contour-levels level-prefered level-allowed)`

set the contour levels for the ramachandran plot, default
 values are 0.02 (prefered) 0.002 (allowed)

Arguments: level_prefered (a number), level_allowed (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ramachandran_plot_contour_levels(1.5, 1.5)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-ramachandran-plot-contour-levels 1.5 1.5)` | ran (no return value, nothing visible changed) |

### set_ramachandran_psi_axis_mode

Python: `set_ramachandran_psi_axis_mode(mode)`  
Scheme: `(set-ramachandran-psi-axis-mode mode)`

set the psi axis for the ramachandran plot. Default (0) from -180
 to 180. Alternative (1) from -120 to 240.

Arguments: mode (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_ramachandran_psi_axis_mode(1)` | ran (no return value); changed: ramachandran_psi_axis_mode(): 0 -> 1 |
| Scheme | `(set-ramachandran-psi-axis-mode 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: ramachandran_psi_axis_mode was 0, set to 1, read back 1; Scheme: ramachandran-psi-axis-mode was 0, set to 1, read back 1.

### setup_dynamic_distances

Python: `setup_dynamic_distances(state)`  
Scheme: `(setup-dynamic-distances state)`

no need to export this to scripting interface

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_dynamic_distances(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-dynamic-distances 1)` | ran (no return value, nothing visible changed) |

### setup_edit_phi_psi

Python: `setup_edit_phi_psi(state)`  
Scheme: `(setup-edit-phi-psi state)`

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `setup_edit_phi_psi(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(setup-edit-phi-psi 1)` | ran (no return value, nothing visible changed) |

