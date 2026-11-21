# Screen Translation

[Scripting reference](../README.md) > Screen Translation (3 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### translate_scene_x

Python: `translate_scene_x(nsteps)`  
Scheme: `(translate-scene-x nsteps)`

translate rotation centre relative to screen axes for nsteps

Arguments: nsteps (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `translate_scene_x(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(translate-scene-x 1)` | ran (no return value, nothing visible changed) |

### translate_scene_y

Python: `translate_scene_y(nsteps)`  
Scheme: `(translate-scene-y nsteps)`

translate rotation centre relative to screen axes for nsteps

Arguments: nsteps (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `translate_scene_y(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(translate-scene-y 1)` | ran (no return value, nothing visible changed) |

### translate_scene_z

Python: `translate_scene_z(nsteps)`  
Scheme: `(translate-scene-z nsteps)`

translate rotation centre relative to screen axes for nsteps

Arguments: nsteps (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `translate_scene_z(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(translate-scene-z 1)` | ran (no return value, nothing visible changed) |

