# External Ray-Tracing

[Scripting reference](../README.md) > External Ray-Tracing (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### citation_notice_off

Python: `citation_notice_off()`  
Scheme: `(citation-notice-off)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `citation_notice_off()` | ran (no return value) |
| Scheme | `(citation-notice-off)` | ran (no return value) |

### make_image_povray

Python: `make_image_povray(filename)`  
Scheme: `(make-image-povray filename)`

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_image_povray("tutorial-modern.pdb")` | not run: not run automatically (povray: exits, uses the network, an external program, files or a screen) |
| Scheme | `(make-image-povray "tutorial-modern.pdb")` | not run: not run automatically (povray: exits, uses the network, an external program, files or a screen) |

### make_image_raster3d

Python: `make_image_raster3d(filename)`  
Scheme: `(make-image-raster3d filename)`

a wrapper for the (scheme) function that makes the image, callable
 from callbacks.c

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_image_raster3d("tutorial-modern.pdb")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(make-image-raster3d "tutorial-modern.pdb")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### povray

Python: `povray(filename)`  
Scheme: `(povray filename)`

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `povray("tutorial-modern.pdb")` | not run: not run automatically (povray: exits, uses the network, an external program, files or a screen) |
| Scheme | `(povray "tutorial-modern.pdb")` | not run: not run automatically (povray: exits, uses the network, an external program, files or a screen) |

### raster3d

Python: `raster3d(rd3_filename)`  
Scheme: `(raster3d rd3-filename)`

create a r3d file for the current view

Arguments: rd3_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `raster3d("tutorial-modern.pdb")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(raster3d "tutorial-modern.pdb")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### raster_screen_shot

Python: `raster_screen_shot()`  
Scheme: `(raster-screen-shot)`

script to render and display image

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `raster_screen_shot()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(raster-screen-shot)` | stopped Coot when tried without a window (not checked with a window) |

### renderman

Python: `renderman(rib_filename)`  
Scheme: `(renderman rib-filename)`

Arguments: rib_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `renderman("tutorial-modern.pdb")` | not run: not run automatically (render: exits, uses the network, an external program, files or a screen) |
| Scheme | `(renderman "tutorial-modern.pdb")` | not run: not run automatically (render: exits, uses the network, an external program, files or a screen) |

### set_raster3d_atom_radius

Python: `set_raster3d_atom_radius(f)`  
Scheme: `(set-raster3d-atom-radius f)`

set the atom radius for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_atom_radius(1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-atom-radius 1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_bond_thickness

Python: `set_raster3d_bond_thickness(f)`  
Scheme: `(set-raster3d-bond-thickness f)`

set the bond thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_bond_thickness(1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-bond-thickness 1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_bone_thickness

Python: `set_raster3d_bone_thickness(f)`  
Scheme: `(set-raster3d-bone-thickness f)`

set the bone (skeleton) thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_bone_thickness(1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-bone-thickness 1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_density_thickness

Python: `set_raster3d_density_thickness(f)`  
Scheme: `(set-raster3d-density-thickness f)`

set the density line thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_density_thickness(1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-density-thickness 1.0)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_font_size

Python: `set_raster3d_font_size(size_in)`  
Scheme: `(set-raster3d-font-size size-in)`

set the font size (as a string) for raster3d

Arguments: size_in (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_font_size("hello")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-font-size "hello")` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_shadows_enabled

Python: `set_raster3d_shadows_enabled(state)`  
Scheme: `(set-raster3d-shadows-enabled state)`

turn off shadows for raster3d output - give argument 0 to turn off

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_shadows_enabled(1)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-shadows-enabled 1)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_raster3d_water_sphere

Python: `set_raster3d_water_sphere(istate)`  
Scheme: `(set-raster3d-water-sphere istate)`

set the flag to show waters as spheres for the Raster3D
representation. 1 show as spheres, 0 the usual stars.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_water_sphere(1)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-raster3d-water-sphere 1)` | not run: not run automatically (raster3d: exits, uses the network, an external program, files or a screen) |

### set_renderer_show_atoms

Python: `set_renderer_show_atoms(istate)`  
Scheme: `(set-renderer-show-atoms istate)`

set the flag to show atoms for the Raster3D representation

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_renderer_show_atoms(1)` | not run: not run automatically (render: exits, uses the network, an external program, files or a screen) |
| Scheme | `(set-renderer-show-atoms 1)` | not run: not run automatically (render: exits, uses the network, an external program, files or a screen) |

