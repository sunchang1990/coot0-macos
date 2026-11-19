# Screen Rotation

[Scripting reference](../README.md) > Screen Rotation (4 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### rotate_x_scene

Python: `rotate_x_scene(nsteps, stepsize)`  
Scheme: `(rotate-x-scene nsteps stepsize)`

rotate view round x axis stepsize degrees for nstep such steps

Arguments: nsteps (a whole number), stepsize (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotate_x_scene(1, 1.0)` | not tried |
| Scheme | `(rotate-x-scene 1 1.0)` | not tried |

### rotate_y_scene

Python: `rotate_y_scene(nsteps, stepsize)`  
Scheme: `(rotate-y-scene nsteps stepsize)`

rotate view round y axis stepsize degrees for nstep such steps

Arguments: nsteps (a whole number), stepsize (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotate_y_scene(1, 1.0)` | not tried |
| Scheme | `(rotate-y-scene 1 1.0)` | not tried |

### rotate_z_scene

Python: `rotate_z_scene(nsteps, stepsize)`  
Scheme: `(rotate-z-scene nsteps stepsize)`

rotate view round z axis stepsize degrees for nstep such steps

Arguments: nsteps (a whole number), stepsize (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `rotate_z_scene(1, 1.0)` | not tried |
| Scheme | `(rotate-z-scene 1 1.0)` | not tried |

### spin_zoom_trans

Python: `spin_zoom_trans(axis, nstep, stepsize, zoom_by, x_rel, y_rel, z_rel)`  
Scheme: `(spin-zoom-trans axis nstep stepsize zoom-by x-rel y-rel z-rel)`

Bells and whistles rotation

 spin, zoom and translate.

 where axis is either x,y or z,
 stepsize is in degrees,
 zoom_by and x_rel etc are how much zoom, x,y,z should
 have changed by after nstep steps.

Arguments: axis (a whole number), nstep (a whole number), stepsize (a number), zoom_by (a number), x_rel (a number), y_rel (a number), z_rel (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `spin_zoom_trans(1, 1, 1.0, 100.0, 1.0, 1.0, 1.0)` | not tried |
| Scheme | `(spin-zoom-trans 1 1 1.0 100.0 1.0 1.0 1.0)` | not tried |

