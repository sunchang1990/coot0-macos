# Smooth Scrolling

[Scripting reference](../README.md) > Smooth Scrolling (8 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_smooth_scroll

Python: `get_smooth_scroll()`  
Scheme: `(get-smooth-scroll)`

return the smooth scrolling state

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_smooth_scroll()` | ran, returned `1` |
| Scheme | `(get-smooth-scroll)` | ran, returned `1` |

Python and Scheme gave the same answer.

### get_text_for_smooth_scroll_limit

Python: `get_text_for_smooth_scroll_limit()`  
Scheme: `(get-text-for-smooth-scroll-limit)`

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_smooth_scroll_limit()` | ran, returned `'10.0 '` |
| Scheme | `(get-text-for-smooth-scroll-limit)` | ran, returned `"10.0 "` |

Python and Scheme gave the same answer.

### get_text_for_smooth_scroll_steps

Python: `get_text_for_smooth_scroll_steps()`  
Scheme: `(get-text-for-smooth-scroll-steps)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: none. Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_text_for_smooth_scroll_steps()` | ran, returned `'40   '` |
| Scheme | `(get-text-for-smooth-scroll-steps)` | ran, returned `"40   "` |

Python and Scheme gave the same answer.

### set_smooth_scroll_flag

Python: `set_smooth_scroll_flag(v)`  
Scheme: `(set-smooth-scroll-flag v)`

set smooth scrolling

 @param v use v=1 to turn on smooth scrolling, v=0 for off (default on).

Arguments: v (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-smooth-scroll-flag 1)` | ran (no return value, nothing visible changed) |

### set_smooth_scroll_limit

Python: `set_smooth_scroll_limit(lim)`  
Scheme: `(set-smooth-scroll-limit lim)`

do not scroll for distances greater this limit

Arguments: lim (a number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_limit(1.0)` | ran (no return value); changed: get_text_for_smooth_scroll_limit(): '10.0 ' -> '1.0  ' |
| Scheme | `(set-smooth-scroll-limit 1.0)` | ran (no return value, nothing visible changed) |

### set_smooth_scroll_limit_str

Python: `set_smooth_scroll_limit_str(t)`  
Scheme: `(set-smooth-scroll-limit-str t)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_limit_str("hello")` | ran (no return value); changed: get_text_for_smooth_scroll_limit(): '1.0  ' -> '10.0 ' |
| Scheme | `(set-smooth-scroll-limit-str "hello")` | ran (no return value, nothing visible changed) |

### set_smooth_scroll_steps

Python: `set_smooth_scroll_steps(i)`  
Scheme: `(set-smooth-scroll-steps i)`

set the number of steps in the smooth scroll

 Set more steps (e.g. 50) for more smoothness (default 10).

Arguments: i (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_steps(1)` | ran (no return value); changed: get_text_for_smooth_scroll_steps(): '40   ' -> '1    ' |
| Scheme | `(set-smooth-scroll-steps 1)` | ran (no return value, nothing visible changed) |

### set_smooth_scroll_steps_str

Python: `set_smooth_scroll_steps_str(t)`  
Scheme: `(set-smooth-scroll-steps-str t)`

MOVE-ME to c-interface-gtk-widgets.h

Arguments: t (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_smooth_scroll_steps_str("hello")` | ran (no return value); changed: get_text_for_smooth_scroll_steps(): '1    ' -> '10   ' |
| Scheme | `(set-smooth-scroll-steps-str "hello")` | ran (no return value, nothing visible changed) |

