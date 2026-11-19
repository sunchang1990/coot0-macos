# 7. Automatic workflows: scripts, loops, hooks

### 7.1 Run a script without the window (batch)

Write the commands into a file and give it to coot0 with `--script`. `--no-graphics` runs without a window;
end the script with `coot_real_exit(0)` (Scheme: `(coot-real-exit 0)`) so that Coot quits when it is done.
In a Terminal:

```
coot0 --no-graphics --script my-job.py
coot0 --no-graphics --script my-job.scm
```

A small job, `my-job.py` / `my-job.scm`: refine A40-A45 and save the result.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
set_imol_refinement_map(imol_map)
set_refinement_immediate_replacement(1)
refine_zone(imol, "A", 40, 45, "")
accept_regularizement()
write_pdb_file(imol, "refined.pdb")
# coot_real_exit(0)        <- at the end of a batch script
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(set-imol-refinement-map imol-map)
(set-refinement-immediate-replacement 1)
(refine-zone imol "A" 40 45 "")
(accept-regularizement)
(write-pdb-file imol "refined.pdb")
; (coot-real-exit 0)       <- at the end of a batch script
```
<!-- check-py: os.path.getsize("refined.pdb") > 100000 -->
<!-- check-scm: (file-exists? "refined.pdb") -->

With a window, open the script with Calculate > Run Script..., or start `coot0 --script my-job.py`.

### 7.2 Loop over every residue: a table of B-factors

```python
imol = read_pdb("tutorial-modern.pdb")
for r in all_residues(imol)[:10]:                 # remove [:10] for all residues
    ch, resno, ins = r[1], r[2], r[3]
    atoms = residue_info(imol, ch, resno, ins)
    mean_b = sum(a[1][1] for a in atoms) / len(atoms)
    print("%s %4d %s  mean B %5.1f" % (ch, resno, residue_name(imol, ch, resno, ins), mean_b))
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(for-each
  (lambda (r)
    (let* ((ch (list-ref r 1)) (resno (list-ref r 2)) (ins (list-ref r 3))
           (atoms (residue-info imol ch resno ins))
           (mean-b (/ (apply + (map (lambda (a) (cadr (cadr a))) atoms)) (length atoms))))
      (format #t "~a ~a ~a  mean B ~,1f~%" ch resno (residue-name imol ch resno ins) mean-b)))
  (list-head (all-residues imol) 10))
```

### 7.3 Write a report file: fit to the map of every residue

A tab-separated file you can open in Excel or Numbers.

```python
imol = read_pdb("tutorial-modern.pdb")
imol_map = make_and_draw_map("rnasa-1.8-all_refmac1.mtz", "FWT", "PHWT", "", 0, 0)
with open("density-fit.tsv", "w") as f:
    f.write("chain\tresidue\tname\tdensity\n")
    for r in all_residues(imol):
        spec = [r[1], r[2], r[3]]
        f.write("%s\t%d\t%s\t%.3f\n" % (r[1], r[2], residue_name(imol, *spec), density_score_residue(imol, spec, imol_map)))
print("written density-fit.tsv")
```

```scheme
(define imol (read-pdb "tutorial-modern.pdb"))
(define imol-map (make-and-draw-map "rnasa-1.8-all_refmac1.mtz" "FWT" "PHWT" "" 0 0))
(call-with-output-file "density-fit.tsv"
  (lambda (port)
    (display "chain\tresidue\tname\tdensity\n" port)
    (for-each
      (lambda (r)
        (let ((spec (list-tail r 1)))
          (format port "~a\t~a\t~a\t~,3f~%" (list-ref r 1) (list-ref r 2)
                  (apply residue-name imol spec) (density-score-residue imol spec imol-map))))
      (all-residues imol))))
```
<!-- check-py: len(open("density-fit.tsv").readlines()) == 190 -->
<!-- check-scm: (file-exists? "density-fit.tsv") -->

### 7.4 Do the same to many files

All `.pdb` files of a folder: report the number of residues per chain.

```python
import glob
for fn in sorted(glob.glob("*.pdb")):
    imol = read_pdb(fn)
    print(fn, [(ch, chain_n_residues(ch, imol)) for ch in chain_ids(imol)])
    close_molecule(imol)
```

```scheme
(use-modules (ice-9 ftw))
(for-each
  (lambda (fn)
    (let ((imol (read-pdb fn)))
      (format #t "~a ~a~%" fn (map (lambda (ch) (list ch (chain-n-residues ch imol))) (chain-ids imol)))
      (close-molecule imol)))
  (scandir "." (lambda (f) (string-suffix? ".pdb" f))))
```

### 7.5 A hook: run your code after every change of a model

Coot calls `post_manipulation_script` (Python) or `post-manipulation-hook` (Scheme) after every refinement,
deletion or mutation, with the molecule number and what happened.

```python
def post_manipulation_script(imol, mode):
    print("molecule", imol, "was changed, mode", mode)   # DELETED, MUTATED or MOVINGATOMS
    return 1

imol = read_pdb("tutorial-modern.pdb")
delete_residue(imol, "A", 93, "")          # -> prints the message
```

```scheme
(set! post-manipulation-hook
  (lambda (imol mode)
    (format #t "molecule ~a was changed, mode ~a~%" imol mode)))
(define imol (read-pdb "tutorial-modern.pdb"))
(delete-residue imol "A" 93 "")
```
<!-- check-py: callable(post_manipulation_script) -->

To switch it off: `post_manipulation_script = False` / `(set! post-manipulation-hook #f)`.

### 7.6 Repeat something while Coot runs (every 10 seconds)

Saves a copy of molecule 0 every 10 seconds while the window is open (return `False` to stop).

```python
import gobject
def autosave():
    if is_valid_model_molecule(0):
        write_pdb_file(0, "autosave.pdb")
    return True                             # True = keep going

gobject.timeout_add(10000, autosave)
```

```scheme
(call-with-output-file "autosave.py"
  (lambda (port) (display "
import gobject
def autosave():
    if is_valid_model_molecule(0):
        write_pdb_file(0, 'autosave.pdb')
    return True
gobject.timeout_add(10000, autosave)
" port)))
(run-python-script "autosave.py")
```
<!-- not-run: the timer runs only while Coot shows its window -->

### 7.7 Python from Scheme and Scheme from Python

```python
imol = read_pdb("tutorial-modern.pdb")
print(run_scheme_command('(residue-name %d "A" 41 "")' % imol))     # GLU
```

```scheme
(display (run-python-command "2 ** 10")) (newline)
```
