# External Ray-Tracing

[Scripting reference](../README.md) > External Ray-Tracing (15 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### citation_notice_off

Python: `citation_notice_off()`  
Scheme: `(citation-notice-off)`

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `citation_notice_off()` | ran (no return value, nothing visible changed) |
| Scheme | `(citation-notice-off)` | ran (no return value, nothing visible changed) |

### make_image_povray

Python: `make_image_povray(filename)`  
Scheme: `(make-image-povray filename)`

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_image_povray("image.pov")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |
| Scheme | `(make-image-povray "image.pov")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |

Example written and checked by hand on the test data. Expected: renders the view with POV-Ray to an image.

### make_image_raster3d

Python: `make_image_raster3d(filename)`  
Scheme: `(make-image-raster3d filename)`

a wrapper for the (scheme) function that makes the image, callable
 from callbacks.c

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_image_raster3d("image.r3d")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |
| Scheme | `(make-image-raster3d "image.r3d")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |

Example written and checked by hand on the test data. Expected: renders the view with Raster3D to an image.

### povray

Python: `povray(filename)`  
Scheme: `(povray filename)`

Arguments: filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `povray("image.pov")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |
| Scheme | `(povray "image.pov")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |

Example written and checked by hand on the test data. Expected: writes a POV-Ray scene file of the view.

### raster3d

Python: `raster3d(rd3_filename)`  
Scheme: `(raster3d rd3-filename)`

create a r3d file for the current view

Arguments: rd3_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `raster3d("image.r3d")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |
| Scheme | `(raster3d "image.r3d")` | not run: uses the graphics window and an external renderer (raster3d/povray); renderman() stopped Coot without a screen in the sa ... |

Example written and checked by hand on the test data. Expected: writes a Raster3D scene file of the view.

### raster_screen_shot

Python: `raster_screen_shot()`  
Scheme: `(raster-screen-shot)`

script to render and display image

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `raster_screen_shot()` | not run: needs the graphics window (stops Coot without a screen) and Raster3D |
| Scheme | `(raster-screen-shot)` | not run: needs the graphics window (stops Coot without a screen) and Raster3D |

Example written and checked by hand on the test data. Expected: renders the current view with Raster3D and shows the image.

### renderman

Python: `renderman(rib_filename)`  
Scheme: `(renderman rib-filename)`

Arguments: rib_filename (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `renderman("scene.rib")` | not run: needs the graphics window (stops Coot without a screen) |
| Scheme | `(renderman "scene.rib")` | not run: needs the graphics window (stops Coot without a screen) |

Example written and checked by hand on the test data. Expected: writes a RenderMan .rib scene of the view.

### set_raster3d_atom_radius

Python: `set_raster3d_atom_radius(f)`  
Scheme: `(set-raster3d-atom-radius f)`

set the atom radius for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_atom_radius(0.4)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-atom-radius 0.35)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the atom sphere radius in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_raster3d_bond_thickness

Python: `set_raster3d_bond_thickness(f)`  
Scheme: `(set-raster3d-bond-thickness f)`

set the bond thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_bond_thickness(0.3)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-bond-thickness 0.25)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the bond thickness in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_raster3d_bone_thickness

Python: `set_raster3d_bone_thickness(f)`  
Scheme: `(set-raster3d-bone-thickness f)`

set the bone (skeleton) thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_bone_thickness(0.1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-bone-thickness 0.12)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the skeleton (bone) thickness in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_raster3d_density_thickness

Python: `set_raster3d_density_thickness(f)`  
Scheme: `(set-raster3d-density-thickness f)`

set the density line thickness for the Raster3D representation

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_density_thickness(0.05)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-density-thickness 0.04)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the density-line thickness in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_raster3d_font_size

Python: `set_raster3d_font_size(size_in)`  
Scheme: `(set-raster3d-font-size size-in)`

set the font size (as a string) for raster3d

Arguments: size_in (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_font_size("12")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-font-size "14")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the label font size (a string) in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_raster3d_shadows_enabled

Python: `set_raster3d_shadows_enabled(state)`  
Scheme: `(set-raster3d-shadows-enabled state)`

turn off shadows for raster3d output - give argument 0 to turn off

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_shadows_enabled(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-shadows-enabled 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the shadows on/off in Raster3D images (default on); takes effect in the next raster3d()/povray() image.

### set_raster3d_water_sphere

Python: `set_raster3d_water_sphere(istate)`  
Scheme: `(set-raster3d-water-sphere istate)`

set the flag to show waters as spheres for the Raster3D
representation. 1 show as spheres, 0 the usual stars.

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_raster3d_water_sphere(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-raster3d-water-sphere 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the waters drawn as spheres in Raster3D images; takes effect in the next raster3d()/povray() image.

### set_renderer_show_atoms

Python: `set_renderer_show_atoms(istate)`  
Scheme: `(set-renderer-show-atoms istate)`

set the flag to show atoms for the Raster3D representation

Arguments: istate (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_renderer_show_atoms(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-renderer-show-atoms 1)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the atoms drawn as spheres in Raster3D/POV-Ray images; takes effect in the next raster3d()/povray() image.

