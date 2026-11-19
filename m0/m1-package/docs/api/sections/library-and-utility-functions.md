# Library and Utility Functions

[Scripting reference](../README.md) > Library and Utility Functions (16 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### coot_checked_exit

Python: `coot_checked_exit(retval)`  
Scheme: `(coot-checked-exit retval)`

Arguments: retval (a whole number). Returns: `gboolean`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_checked_exit(1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-checked-exit 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |

### coot_clear_backup_or_real_exit

Python: `coot_clear_backup_or_real_exit(retval)`  
Scheme: `(coot-clear-backup-or-real-exit retval)`

exit coot doing clear-backup maybe

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_clear_backup_or_real_exit(1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-clear-backup-or-real-exit 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |

### coot_no_state_real_exit

Python: `coot_no_state_real_exit(retval)`  
Scheme: `(coot-no-state-real-exit retval)`

exit without writing a state file

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_no_state_real_exit(1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-no-state-real-exit 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |

### coot_real_exit

Python: `coot_real_exit(retval)`  
Scheme: `(coot-real-exit retval)`

exit from coot, give return value retval back to invoking
 process.

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_real_exit(1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-real-exit 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |

### coot_save_state_and_exit

Python: `coot_save_state_and_exit(retval, save_state_flag)`  
Scheme: `(coot-save-state-and-exit retval save-state-flag)`

exit coot, write a state file

Arguments: retval (a whole number), save_state_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_save_state_and_exit(1, 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |
| Scheme | `(coot-save-state-and-exit 1 1)` | not run: not run automatically (exit: exits, uses the network, an external program, files or a screen) |

### coot_sys_build_type

Python: `coot_sys_build_type()`  
Scheme: `(coot-sys-build-type)`

Arguments: none. Returns: a value (see the result of the example).
Also available in Python as `coot_sys_build_type_py`.
Also available in Scheme as `coot-sys-build-type-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_sys_build_type()` | ran, returned `'Darwin-arm64'` |
| Scheme | `(coot-sys-build-type)` | ran, returned `"Darwin-arm64"` |

### first_coords_imol

Python: `first_coords_imol()`  
Scheme: `(first-coords-imol)`

What is the molecule number of first coordinates molecule?

 return -1 when there is none.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `first_coords_imol()` | ran, returned `0` |
| Scheme | `(first-coords-imol)` | ran, returned `0` |

### first_small_coords_imol

Python: `first_small_coords_imol()`  
Scheme: `(first-small-coords-imol)`

molecule number of first small (<400 atoms) molecule.

return -1 on no such molecule

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `first_small_coords_imol()` | ran, returned `-1` |
| Scheme | `(first-small-coords-imol)` | ran, returned `-1` |

### first_unsaved_coords_imol

Python: `first_unsaved_coords_imol()`  
Scheme: `(first-unsaved-coords-imol)`

What is the molecule number of first unsaved coordinates molecule?

 return -1 when there is none.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `first_unsaved_coords_imol()` | ran, returned `-1` |
| Scheme | `(first-unsaved-coords-imol)` | ran, returned `-1` |

### git_revision_count

Python: `git_revision_count()`  
Scheme: `(git-revision-count)`

return the git revision count for for this build.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `git_revision_count()` | ran, returned `10988` |
| Scheme | `(git-revision-count)` | ran, returned `10988` |

### mmcif_sfs_to_mtz

Python: `mmcif_sfs_to_mtz(cif_file_name, mtz_file_name)`  
Scheme: `(mmcif-sfs-to-mtz cif-file-name mtz-file-name)`

convert the structure factors in cif_file_name to an mtz
 file.

 Return 1 on success. Return 0 on a file without Rfree, return
 -1 on complete failure to write a file.

Arguments: cif_file_name (text), mtz_file_name (text). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `mmcif_sfs_to_mtz("tutorial-modern.pdb", "rnasa-1.8-all_refmac1.mtz")` | not tried |
| Scheme | `(mmcif-sfs-to-mtz "tutorial-modern.pdb" "rnasa-1.8-all_refmac1.mtz")` | not tried |

### molecule_name

Python: `molecule_name(imol)`  
Scheme: `(molecule-name imol)`

return the name of molecule number imol

 Returns 0 if not a valid name ( -> False in scheme)
 e.g. "/a/b/c.pdb" for "d/e/f.mtz FWT PHWT"

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_name(0)` | not tried |
| Scheme | `(molecule-name 0)` | not tried |

### molecule_name_stub

Python: `molecule_name_stub(imol, include_path_flag)`  
Scheme: `(molecule-name-stub imol include-path-flag)`

return the molecule name without file extension

Arguments: imol (a whole number), include_path_flag (a whole number). Returns: a value (see the result of the example).
Also available in Python as `molecule_name_stub_py`.
Also available in Scheme as `molecule-name-stub-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_name_stub(0, 1)` | not tried |
| Scheme | `(molecule-name-stub 0 1)` | not tried |

### run_clear_backups

Python: `run_clear_backups(retval)`  
Scheme: `(run-clear-backups retval)`

run clear-backups

Arguments: retval (a whole number). Returns: nothing.
Also available in Python as `run_clear_backups_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_clear_backups(1)` | not tried |
| Scheme | `(run-clear-backups 1)` | not tried |

### set_molecule_name

Python: `set_molecule_name(imol, new_name)`  
Scheme: `(set-molecule-name imol new-name)`

set the molecule name of the imol-th molecule

Arguments: imol (a whole number), new_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_molecule_name(0, "my-name")` | not tried |
| Scheme | `(set-molecule-name 0 "my-name")` | not tried |

### svn_revision

Python: `svn_revision()`  
Scheme: `(svn-revision)`

an alias to git_revision_count() for backwards compatibility

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `svn_revision()` | not tried |
| Scheme | `(svn-revision)` | not tried |

