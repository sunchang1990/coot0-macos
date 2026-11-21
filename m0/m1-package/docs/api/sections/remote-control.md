# Remote Control

[Scripting reference](../README.md) > Remote Control (7 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### get_remote_control_port_number

Python: `get_remote_control_port_number()`  
Scheme: `(get-remote-control-port-number)`

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `get_remote_control_port_number()` | ran, returned `0` |
| Scheme | `(get-remote-control-port-number)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the port Coot listens on for remote control; 0 when not set.

Python and Scheme gave the same answer.

### make_socket_listener_maybe

Python: `make_socket_listener_maybe()`  
Scheme: `(make-socket-listener-maybe)`

try to make socket listener

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_socket_listener_maybe()` | ran (no return value, nothing visible changed) |
| Scheme | `(make-socket-listener-maybe)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: opens the remote-control socket listener if a port was set (needs the network otherwise).

Note: only run without a port (no-op); with set_remote_control_port it would listen on a network port

### set_coot_listener_socket_state_internal

Python: `set_coot_listener_socket_state_internal(sock_state)`  
Scheme: `(set-coot-listener-socket-state-internal sock-state)`

Arguments: sock_state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_coot_listener_socket_state_internal(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-coot-listener-socket-state-internal 0)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: internal: records whether the listener socket is open (no getter, nothing visible).

### set_remote_control_port

Python: `set_remote_control_port(port_number)`  
Scheme: `(set-remote-control-port port-number)`

Arguments: port_number (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_remote_control_port(5001)` | ran (no return value); changed: get_remote_control_port_number(): 0 -> 5001 |
| Scheme | `(set-remote-control-port 5001)` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: sets the remote-control port number (does not open a socket by itself).

### set_socket_python_string_waiting

Python: `set_socket_python_string_waiting(s)`  
Scheme: `(set-socket-python-string-waiting s)`

feed the main thread a python script to evaluate

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_socket_python_string_waiting("set_rotation_centre(4, 5, 6)")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-socket-python-string-waiting "set_rotation_centre(4, 5, 6)")` | ran (no return value, nothing visible changed) |

Example written and checked by hand on the test data. Expected: internal (remote control): queues a Python command for the main loop to run.

### set_socket_string_waiting

Python: `set_socket_string_waiting(s)`  
Scheme: `(set-socket-string-waiting s)`

feed the main thread a scheme script to evaluate

Arguments: s (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_socket_string_waiting("(set-rotation-centre 1 2 3)")` | ran (no return value, nothing visible changed) |
| Scheme | `(set-socket-string-waiting "(set-rotation-centre 1 2 3)")` | not run: waits for Coot's socket listener (no answer without one) |

Example written and checked by hand on the test data. Expected: internal (remote control): queues a Scheme command for the main loop to run.

Note: the queued command did not run during the headless try (the main-loop handler belongs to the socket listener)

### set_tip_of_the_day_flag

Python: `set_tip_of_the_day_flag(state)`  
Scheme: `(set-tip-of-the-day-flag state)`

tooltip

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_tip_of_the_day_flag(1)` | ran (no return value, nothing visible changed) |
| Scheme | `(set-tip-of-the-day-flag 1)` | ran (no return value, nothing visible changed) |

