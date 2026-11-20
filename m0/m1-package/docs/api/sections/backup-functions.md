# Backup Functions

[Scripting reference](../README.md) > Backup Functions (16 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### apply_redo

Python: `apply_redo()`  
Scheme: `(apply-redo)`

apply redo - the "Redo" button callback

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_redo()` | ran, returned `0` |
| Scheme | `(apply-redo)` | ran, returned `0` |

Python and Scheme gave the same answer.

### apply_undo

Python: `apply_undo()`  
Scheme: `(apply-undo)`

apply undo - the "Undo" button callback

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `apply_undo()` | ran, returned `0` |
| Scheme | `(apply-undo)` | ran, returned `0` |

Python and Scheme gave the same answer.

### backup_compress_files_state

Python: `backup_compress_files_state()`  
Scheme: `(backup-compress-files-state)`

return the state for compression of backup files

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `backup_compress_files_state()` | ran, returned `1` |
| Scheme | `(backup-compress-files-state)` | ran, returned `1` |

Python and Scheme gave the same answer.

### backup_state

Python: `backup_state(imol)`  
Scheme: `(backup-state imol)`

return the backup state for molecule number imol

 return 0 for backups off, 1 for backups on, -1 for unknown

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `backup_state(0)` | ran, returned `1` |
| Scheme | `(backup-state 0)` | ran, returned `1` |

Python and Scheme gave the same answer.

### decoloned_backup_file_names_state

Python: `decoloned_backup_file_names_state()`  
Scheme: `(decoloned-backup-file-names-state)`

return the state for adding paths to backup file names

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `decoloned_backup_file_names_state()` | ran, returned `0` |
| Scheme | `(decoloned-backup-file-names-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

### have_unsaved_changes_p

Python: `have_unsaved_changes_p(imol)`  
Scheme: `(have-unsaved-changes-p imol)`

does molecule number imol have unsaved changes?
 Returns -1 on bad imol, 0 on no unsaved changes, 1 on has unsaved changes

Arguments: imol (a whole number). Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `have_unsaved_changes_p(0)` | ran, returned `0` |
| Scheme | `(have-unsaved-changes-p 0)` | ran, returned `0` |

Python and Scheme gave the same answer.

### make_backup

Python: `make_backup(imol)`  
Scheme: `(make-backup imol)`

make backup for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `make_backup(0)` | ran (no return value) |
| Scheme | `(make-backup 0)` | ran (no return value) |

### set_backup_compress_files

Python: `set_backup_compress_files(state)`  
Scheme: `(set-backup-compress-files state)`

set if backup files will be compressed or not using gzip

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_backup_compress_files(1)` | ran (no return value) |
| Scheme | `(set-backup-compress-files 1)` | ran (no return value) |

### set_decoloned_backup_file_names

Python: `set_decoloned_backup_file_names(state)`  
Scheme: `(set-decoloned-backup-file-names state)`

set the state for adding paths to backup file names

 by default directories names are added into the filename for backup
 (with / to _ mapping). call this with state=1 to turn off directory
 names

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_decoloned_backup_file_names(1)` | ran (no return value) |
| Scheme | `(set-decoloned-backup-file-names 1)` | ran (no return value) |

### set_have_unsaved_changes

Python: `set_have_unsaved_changes(imol)`  
Scheme: `(set-have-unsaved-changes imol)`

set the molecule number imol to be marked as having unsaved changes

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_have_unsaved_changes(0)` | ran (no return value) |
| Scheme | `(set-have-unsaved-changes 0)` | ran (no return value) |

### set_undo_molecule

Python: `set_undo_molecule(imol)`  
Scheme: `(set-undo-molecule imol)`

set the molecule to which undo operations are done to
 molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_undo_molecule(0)` | ran (no return value) |
| Scheme | `(set-undo-molecule 0)` | ran (no return value) |

### set_unpathed_backup_file_names

Python: `set_unpathed_backup_file_names(state)`  
Scheme: `(set-unpathed-backup-file-names state)`

set the state for adding paths to backup file names

 by default directories names are added into the filename for backup
 (with / to _ mapping). call this with state=1 to turn off directory
 names

Arguments: state (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `set_unpathed_backup_file_names(1)` | ran (no return value) |
| Scheme | `(set-unpathed-backup-file-names 1)` | ran (no return value) |

### show_set_undo_molecule_chooser

Python: `show_set_undo_molecule_chooser()`  
Scheme: `(show-set-undo-molecule-chooser)`

show the Undo Molecule chooser - i.e. choose the molecule
 to which the "Undo" button applies.

Arguments: none. Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `show_set_undo_molecule_chooser()` | stopped Coot when tried without a window (not checked with a window) |
| Scheme | `(show-set-undo-molecule-chooser)` | stopped Coot when tried without a window (not checked with a window) |

### turn_off_backup

Python: `turn_off_backup(imol)`  
Scheme: `(turn-off-backup imol)`

turn off backups for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `turn_off_backup(0)` | ran (no return value) |
| Scheme | `(turn-off-backup 0)` | ran (no return value) |

### turn_on_backup

Python: `turn_on_backup(imol)`  
Scheme: `(turn-on-backup imol)`

turn on backups for molecule number imol

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `turn_on_backup(0)` | ran (no return value) |
| Scheme | `(turn-on-backup 0)` | ran (no return value) |

### unpathed_backup_file_names_state

Python: `unpathed_backup_file_names_state()`  
Scheme: `(unpathed-backup-file-names-state)`

return the state for adding paths to backup file names

Arguments: none. Returns: a whole number.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `unpathed_backup_file_names_state()` | ran, returned `0` |
| Scheme | `(unpathed-backup-file-names-state)` | ran, returned `0` |

Python and Scheme gave the same answer.

