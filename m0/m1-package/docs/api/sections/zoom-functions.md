# Zoom Functions

[Scripting reference](../README.md) > Zoom Functions (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### scale_zoom

Python: `scale_zoom(f)`  
Scheme: `(scale-zoom f)`

scale the view by f

 external (scripting) interface (with redraw)
 @param f the smaller f, the bigger the zoom, typical value 1.3.
 Values outside the range 0.5 to 1.8 are filtered out

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scale_zoom(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(scale-zoom 1.0)` | ran (no return value, nothing visible changed) |

### scale_zoom_internal

Python: `scale_zoom_internal(f)`  
Scheme: `(scale-zoom-internal f)`

internal interface

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `scale_zoom_internal(1.0)` | ran (no return value, nothing visible changed) |
| Scheme | `(scale-zoom-internal 1.0)` | ran (no return value, nothing visible changed) |

### set_smooth_scroll_do_zoom

Python: `set_smooth_scroll_do_zoom(i)`  
Scheme: `(set-smooth-scroll-do-zoom i)`

set smooth scroll with zoom
 @param i 0 means no, 1 means yes: (default 0)

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_do_zoom(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-smooth-scroll-do-zoom 1)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: smooth_scroll_do_zoom was 0, set to 1, read back 1; Scheme: smooth-scroll-do-zoom was 0, set to 1, read back 1.

### set_smooth_scroll_zoom_limit

Python: `set_smooth_scroll_zoom_limit(f)`  
Scheme: `(set-smooth-scroll-zoom-limit f)`

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_zoom_limit(1.0)` | ran (no return value); changed: smooth_scroll_zoom_limit(): 30 -> 1 |
| Scheme | `(set-smooth-scroll-zoom-limit 1.0)` | ran (no return value, nothing visible changed) |

Setting checked (set to another value and read back, then put back): Python: smooth_scroll_zoom_limit was 30.0, set to 45.5, read back 45.5; Scheme: smooth-scroll-zoom-limit was 30.0, set to 45.5, read back 45.5.

### set_zoom

Python: `set_zoom(f)`  
Scheme: `(set-zoom f)`

set the zoom factor (absolute value) - maybe should be called set_zoom_factor()

Arguments: f (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_zoom(1.0)` | ran (no return value); changed: zoom: 100.0 -> 1.0 |
| Scheme | `(set-zoom 1.0)` | ran (no return value, nothing visible changed) |

### smooth_scroll_do_zoom

Python: `smooth_scroll_do_zoom()`  
Scheme: `(smooth-scroll-do-zoom)`

return the state of the above system

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `smooth_scroll_do_zoom()` | ran, returned `0` |
| Scheme | `(smooth-scroll-do-zoom)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: 0: the smooth-scroll zoom setting is off by default (state query).

Python and Scheme gave the same answer.

### smooth_scroll_zoom_limit

Python: `smooth_scroll_zoom_limit()`  
Scheme: `(smooth-scroll-zoom-limit)`

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `smooth_scroll_zoom_limit()` | ran, returned `30.0` |
| Scheme | `(smooth-scroll-zoom-limit)` | ran, returned `30.0` |

Python and Scheme gave the same answer.

### zoom_factor

Python: `zoom_factor()`  
Scheme: `(zoom-factor)`

return the current zoom factor i.e. get_zoom_factor()

Arguments: none. Returns: a number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `zoom_factor()` | ran, returned `100.0` |
| Scheme | `(zoom-factor)` | ran, returned `100.0` |

Python and Scheme gave the same answer.

