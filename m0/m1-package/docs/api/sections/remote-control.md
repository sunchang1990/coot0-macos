# Remote Control

[Scripting reference](../README.md) > Remote Control (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_remote_control_port_number

Python: `get_remote_control_port_number()`  
Scheme: `(get-remote-control-port-number)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_remote_control_port_number()` | not run: not run automatically (remote: exits, uses the network, an external program, files or a screen) |
| Scheme | `(get-remote-control-port-number)` | not run: not run automatically (remote: exits, uses the network, an external program, files or a screen) |

### make_socket_listener_maybe

Python: `make_socket_listener_maybe()`  
Scheme: `(make-socket-listener-maybe)`

try to make socket listener

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_socket_listener_maybe()` | not tried |
| Scheme | `(make-socket-listener-maybe)` | not tried |

### set_coot_listener_socket_state_internal

Python: `set_coot_listener_socket_state_internal(sock_state)`  
Scheme: `(set-coot-listener-socket-state-internal sock-state)`

Arguments: sock_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_coot_listener_socket_state_internal(1)` | not tried |
| Scheme | `(set-coot-listener-socket-state-internal 1)` | not tried |

### set_remote_control_port

Python: `set_remote_control_port(port_number)`  
Scheme: `(set-remote-control-port port-number)`

Arguments: port_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_remote_control_port(1)` | not tried |
| Scheme | `(set-remote-control-port 1)` | not tried |

### set_socket_python_string_waiting

Python: `set_socket_python_string_waiting(s)`  
Scheme: `(set-socket-python-string-waiting s)`

feed the main thread a python script to evaluate

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_socket_python_string_waiting("hello")` | not tried |
| Scheme | `(set-socket-python-string-waiting "hello")` | not tried |

### set_socket_string_waiting

Python: `set_socket_string_waiting(s)`  
Scheme: `(set-socket-string-waiting s)`

feed the main thread a scheme script to evaluate

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_socket_string_waiting("hello")` | not tried |
| Scheme | `(set-socket-string-waiting "hello")` | not tried |

### set_tip_of_the_day_flag

Python: `set_tip_of_the_day_flag(state)`  
Scheme: `(set-tip-of-the-day-flag state)`

tooltip

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_tip_of_the_day_flag(1)` | not tried |
| Scheme | `(set-tip-of-the-day-flag 1)` | not tried |

