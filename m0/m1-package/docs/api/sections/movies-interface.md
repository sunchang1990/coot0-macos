# Movies Interface

[Scripting reference](../README.md) > Movies Interface (5 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### movie_file_name_prefix

Python: `movie_file_name_prefix()`  
Scheme: `(movie-file-name-prefix)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `movie_file_name_prefix_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `movie_file_name_prefix()` | not tried |
| Scheme | `(movie-file-name-prefix)` | not tried |

### movie_frame_number

Python: `movie_frame_number()`  
Scheme: `(movie-frame-number)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `movie_frame_number()` | not tried |
| Scheme | `(movie-frame-number)` | not tried |

### set_make_movie_mode

Python: `set_make_movie_mode(make_movies_flag)`  
Scheme: `(set-make-movie-mode make-movies-flag)`

Arguments: make_movies_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_make_movie_mode(1)` | not tried |
| Scheme | `(set-make-movie-mode 1)` | not tried |

### set_movie_file_name_prefix

Python: `set_movie_file_name_prefix(file_name)`  
Scheme: `(set-movie-file-name-prefix file-name)`

Arguments: file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_movie_file_name_prefix("tutorial-modern.pdb")` | not tried |
| Scheme | `(set-movie-file-name-prefix "tutorial-modern.pdb")` | not tried |

### set_movie_frame_number

Python: `set_movie_frame_number(frame_number)`  
Scheme: `(set-movie-frame-number frame-number)`

Arguments: frame_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_movie_frame_number(1)` | not tried |
| Scheme | `(set-movie-frame-number 1)` | not tried |

