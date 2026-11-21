# Library and Utility Functions

[Scripting reference](../README.md) > Library and Utility Functions (16 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### coot_checked_exit

Python: `coot_checked_exit(retval)`  
Scheme: `(coot-checked-exit retval)`

Arguments: retval (a whole number). Returns: `gboolean`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_checked_exit(0)` | not run: exits Coot |
| Scheme | `(coot-checked-exit 0)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: exits Coot, first asking about unsaved molecules (in the GUI).

### coot_clear_backup_or_real_exit

Python: `coot_clear_backup_or_real_exit(retval)`  
Scheme: `(coot-clear-backup-or-real-exit retval)`

exit coot doing clear-backup maybe

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_clear_backup_or_real_exit(0)` | not run: exits Coot |
| Scheme | `(coot-clear-backup-or-real-exit 0)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: exits Coot, offering to clear old backups first.

### coot_no_state_real_exit

Python: `coot_no_state_real_exit(retval)`  
Scheme: `(coot-no-state-real-exit retval)`

exit without writing a state file

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_no_state_real_exit(0)` | not run: exits Coot |
| Scheme | `(coot-no-state-real-exit 0)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: exits Coot with return value 0 without writing a state file.

### coot_real_exit

Python: `coot_real_exit(retval)`  
Scheme: `(coot-real-exit retval)`

exit from coot, give return value retval back to invoking
 process.

Arguments: retval (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_real_exit(0)` | not run: exits Coot |
| Scheme | `(coot-real-exit 0)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: exits Coot with the given return value.

### coot_save_state_and_exit

Python: `coot_save_state_and_exit(retval, save_state_flag)`  
Scheme: `(coot-save-state-and-exit retval save-state-flag)`

exit coot, write a state file

Arguments: retval (a whole number), save_state_flag (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `coot_save_state_and_exit(0, 1)` | not run: exits Coot |
| Scheme | `(coot-save-state-and-exit 0 1)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: writes the state file (flag 1) and exits Coot.

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

Python and Scheme gave the same answer.

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

Example written and checked by hand on the test data. Expected: the first model molecule (0); -1 if none.

Python and Scheme gave the same answer.

### first_small_coords_imol

Python: `first_small_coords_imol()`  
Scheme: `(first-small-coords-imol)`

molecule number of first small (<400 atoms) molecule.

return -1 on no such molecule

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `read_pdb("nag_only.pdb")`, then `first_small_coords_imol()` | ran, returned `3` |
| Scheme | first `(read-pdb "nag_only.pdb")`, then `(first-small-coords-imol)` | ran, returned `3` |

Example written and checked by hand on the test data. Expected: returns the first model molecule with fewer than 400 atoms, -1 if none.

Python and Scheme gave the same answer.

### first_unsaved_coords_imol

Python: `first_unsaved_coords_imol()`  
Scheme: `(first-unsaved-coords-imol)`

What is the molecule number of first unsaved coordinates molecule?

 return -1 when there is none.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `delete_residue(0, "A", 41, "")`, then `first_unsaved_coords_imol()` | ran, returned `0` |
| Scheme | first `(delete-residue 0 "A" 41 "")`, then `(first-unsaved-coords-imol)` | ran, returned `0` |

Example written and checked by hand on the test data. Expected: returns the first model molecule with unsaved changes; -1 when nothing has changed.

Python and Scheme gave the same answer.

### git_revision_count

Python: `git_revision_count()`  
Scheme: `(git-revision-count)`

return the git revision count for for this build.

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `git_revision_count()` | ran, returned `10988` |
| Scheme | `(git-revision-count)` | ran, returned `10988` |

Python and Scheme gave the same answer.

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
| Python | first `open("sf.cif", "w").write("data_r1xyzsf\n_cell.length_a 64.897\n_cell.length_b 78.323\n_cell.length_c 38.792\n_cell.angle_alpha 90.0\n_cell.angle_beta 90.0\n_ce ...`, then `mmcif_sfs_to_mtz("sf.cif", "sf.mtz")` | ran, returned `0` |
| Scheme | `(mmcif-sfs-to-mtz "tutorial-modern.pdb" "rnasa-1.8-all_refmac1.mtz")` | ran, returned `-1` |

Example written and checked by hand on the test data. Expected: converts an mmCIF structure-factor file to MTZ: 1 = written with R-free flags, 0 = written without free flags (or failed), -1 = could not read.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

### molecule_name

Python: `molecule_name(imol)`  
Scheme: `(molecule-name imol)`

return the name of molecule number imol

 Returns 0 if not a valid name ( -> False in scheme)
 e.g. "/a/b/c.pdb" for "d/e/f.mtz FWT PHWT"

Arguments: imol (a whole number). Returns: text.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_name(0)` | ran, returned `'tutorial-modern.pdb'` |
| Scheme | `(molecule-name 0)` | ran, returned `"tutorial-modern.pdb"` |

Python and Scheme gave the same answer.

### molecule_name_stub

Python: `molecule_name_stub(imol, include_path_flag)`  
Scheme: `(molecule-name-stub imol include-path-flag)`

return the molecule name without file extension

Arguments: imol (a whole number), include_path_flag (a whole number). Returns: a value (see the result of the example).
Also available in Python as `molecule_name_stub_py`.
Also available in Scheme as `molecule-name-stub-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `molecule_name_stub(0, 1)` | ran, returned `'tutorial-modern'` |
| Scheme | `(molecule-name-stub 0 1)` | ran, returned `"tutorial-modern"` |

Python and Scheme gave the same answer.

### run_clear_backups

Python: `run_clear_backups(retval)`  
Scheme: `(run-clear-backups retval)`

run clear-backups

Arguments: retval (a whole number). Returns: nothing.
Also available in Python as `run_clear_backups_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `run_clear_backups(0)` | not run: exits Coot |
| Scheme | `(run-clear-backups 0)` | not run: exits Coot |

Example written and checked by hand on the test data. Expected: runs clear_backups_maybe() and then exits; without guile-gtk (this build) the Scheme version exits at once.

### set_molecule_name

Python: `set_molecule_name(imol, new_name)`  
Scheme: `(set-molecule-name imol new-name)`

set the molecule name of the imol-th molecule

Arguments: imol (a whole number), new_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_molecule_name(0, "my-name")` | ran (no return value); changed: molecule 0 renamed to my-name; molecule_name(0): 'tutorial-modern.pdb' -> 'my-name' |
| Scheme | `(set-molecule-name 0 "my-name")` | ran (no return value, nothing visible changed) |

### svn_revision

Python: `svn_revision()`  
Scheme: `(svn-revision)`

an alias to git_revision_count() for backwards compatibility

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `svn_revision()` | ran, returned `10988` |
| Scheme | `(svn-revision)` | ran, returned `10988` |

Python and Scheme gave the same answer.

