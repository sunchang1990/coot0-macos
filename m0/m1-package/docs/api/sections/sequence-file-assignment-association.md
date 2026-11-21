# Sequence File (Assignment/Association)

[Scripting reference](../README.md) > Sequence File (Assignment/Association) (12 functions)

Examples use the test data: molecule 0 = `tutorial-modern.pdb`, molecule 1 = the map made from `rnasa-1.8-all_refmac1.mtz` (FWT/PHWT). See [How to read this reference](../README.md#how-to-read-it).

### alignment_mismatches

Python: `alignment_mismatches(imol)`  
Scheme: `(alignment-mismatches imol)`

do a internal alignment of all the assigned sequences,
 return a list of mismatches that need to be made to model number
 imol to match the input sequence.

Return a list of mutations deletions insetions.
Return False on failure to align (e.g. not assigned sequence)
and the empty list on no alignment mismatches.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `alignment_mismatches_py`.
Also available in Scheme as `alignment-mismatches-scm`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `assign_sequence_to_best_matching_chain("DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")`, then `alignment_mismatches(0)` | ran, returned `[[['VAL', True, 'B', 6, ''], ['VAL', True, 'B', 6, '']], [['Delete', True, 'B', 94, ''], ['Delete', True, 'B', 95, ''],  ...` |
| Scheme | first `(assign-sequence-to-best-matching-chain "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")`, then `(alignment-mismatches 0)` | ran, returned `((("VAL" #t "B" 6 "") ("VAL" #t "B" 6 "") ("VAL" #t "B" 6 "")) (("Delete" #t "B" 94 "") ("Delete" #t "B" 95 "") ("Delete ...` |

Example written and checked by hand on the test data. Expected: a list [mutations, deletions, insertions, alignment text]: chain B has 3 residues (94-96) that the 93-residue sequence lacks; False if no sequence was assigned.

### assign_fasta_sequence

Python: `assign_fasta_sequence(imol, chain_id_in, seq)`  
Scheme: `(assign-fasta-sequence imol chain-id-in seq)`

Assign a FASTA sequence to a given chain in the molecule

Arguments: imol (a whole number), chain_id_in (text), seq (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_fasta_sequence(0, "A", "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |
| Scheme | `(assign-fasta-sequence 0 "A" "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |

### assign_pir_sequence

Python: `assign_pir_sequence(imol, chain_id_in, seq)`  
Scheme: `(assign-pir-sequence imol chain-id-in seq)`

Assign a PIR sequence to a given chain in the molecule. If
 the chain of the molecule already had a chain assigned to it, then
 this will overwrite that old assignment with the new one.

Arguments: imol (a whole number), chain_id_in (text), seq (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_pir_sequence(0, "A", "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |
| Scheme | `(assign-pir-sequence 0 "A" "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |

### assign_sequence

Python: `assign_sequence(imol_model, imol_map, chain_id)`  
Scheme: `(assign-sequence imol-model imol-map chain-id)`

I don't know what this does.

Arguments: imol_model (a whole number), imol_map (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence(0, 1, "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(assign-sequence 0 1 "A")` | ran (no return value, nothing visible changed) |

### assign_sequence_from_file

Python: `assign_sequence_from_file(imol, file)`  
Scheme: `(assign-sequence-from-file imol file)`

Assign a sequence to a given molecule from (whatever) sequence
 file by alignment.

Arguments: imol (a whole number), file (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence_from_file(0, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(assign-sequence-from-file 0 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### assign_sequence_from_string

Python: `assign_sequence_from_string(imol, chain_id_in, seq)`  
Scheme: `(assign-sequence-from-string imol chain-id-in seq)`

Assign a sequence to a given molecule from a simple string

Arguments: imol (a whole number), chain_id_in (text), seq (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `assign_sequence_from_string(0, "A", "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |
| Scheme | `(assign-sequence-from-string 0 "A" "ACDEFGHIKLMNPQRSTVWY")` | ran (no return value, nothing visible changed) |

### associate_sequence_from_file

Python: `associate_sequence_from_file(imol, file_name)`  
Scheme: `(associate-sequence-from-file imol file-name)`

Associate the sequence to the molecule - to be used later for sequence assignment (.c.f assign_pir_sequence)

Arguments: imol (a whole number), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `associate_sequence_from_file(0, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(associate-sequence-from-file 0 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### delete_all_sequences_from_molecule

Python: `delete_all_sequences_from_molecule(imol)`  
Scheme: `(delete-all-sequences-from-molecule imol)`

Delete all the sequences from a given molecule

Arguments: imol (a whole number). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_all_sequences_from_molecule(0)` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-all-sequences-from-molecule 0)` | ran (no return value, nothing visible changed) |

### delete_sequence_by_chain_id

Python: `delete_sequence_by_chain_id(imol, chain_id_in)`  
Scheme: `(delete-sequence-by-chain-id imol chain-id-in)`

Delete the sequence for a given chain_id from a given molecule

Arguments: imol (a whole number), chain_id_in (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `delete_sequence_by_chain_id(0, "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(delete-sequence-by-chain-id 0 "A")` | ran (no return value, nothing visible changed) |

### print_sequence_chain

Python: `print_sequence_chain(imol, chain_id)`  
Scheme: `(print-sequence-chain imol chain-id)`

Print the sequence to the console of the given molecule

Arguments: imol (a whole number), chain_id (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_sequence_chain(0, "A")` | ran (no return value, nothing visible changed) |
| Scheme | `(print-sequence-chain 0 "A")` | ran (no return value, nothing visible changed) |

### print_sequence_chain_general

Python: `print_sequence_chain_general(imol, chain_id, pir_format, file_output, file_name)`  
Scheme: `(print-sequence-chain-general imol chain-id pir-format file-output file-name)`

optionally write the sequence to the file for the given molecule,
 optionally in PIR format

Arguments: imol (a whole number), chain_id (text), pir_format (a whole number), file_output (a whole number), file_name (text). Returns: nothing.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | `print_sequence_chain_general(0, "A", 1, 1, "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |
| Scheme | `(print-sequence-chain-general 0 "A" 1 1 "tutorial-modern.pdb")` | ran (no return value, nothing visible changed) |

### sequence_info

Python: `sequence_info(imol)`  
Scheme: `(sequence-info imol)`

return the sequence info that has been assigned to molecule
 number imol. return as a list of dotted pairs [[chain-id, seq]]. To
 be used in constructing the cootaneer gui. Return False when no
 sequence has been assigned.

Arguments: imol (a whole number). Returns: a value (see the result of the example).
Also available in Python as `sequence_info_py`.

| | Example | When tried (test data, no window) |
|---|---|---|
| Python | first `assign_sequence_to_best_matching_chain("DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")`, then `sequence_info(0)` | ran, returned `[['A', 'DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID'], ['B', 'DVSGTVCL ...` |
| Scheme | first `(assign-sequence-to-best-matching-chain "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID")`, then `(sequence-info 0)` | ran, returned `(("A" . "DVSGTVCLSALPPEATDTLNLIASDGPFPYSQDGVVFQNRESVLPTQSYGYYHEYTVITPGARTRGTRRIICGEATQEDYYTGDHYATFSLID") ("B" . "DVSGTVC ...` |

Example written and checked by hand on the test data. Expected: the assigned sequences as [chain-id, sequence] pairs (Scheme: dotted pairs); False when no sequence has been assigned.

Python and Scheme gave different answers (see the table: often only because the example changed the data, or a list is ordered differently).

