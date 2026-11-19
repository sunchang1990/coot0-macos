# Coot scripting cookbook (coot0)

Short recipes for everyday tasks, each in **Python** and in **Scheme**. Every recipe is run by the test suite of
the package (`tests/cookbook_run.py`, part of `tests/run-headless-tests.sh`) on the test data, in both
languages, so what you read here works in this version of coot0. Two recipes need the graphics window and are
marked so (6.4 and 7.6); they are not run by the test.

## How to use a recipe

- **Type it in**: Calculate > Scripting > Python... (or Scheme...) and paste the lines; or
- **Save it in a file** (`my-recipe.py` / `my-recipe.scm`) and open it with Calculate > Run Script...; or
- **Run it without a window**: `coot0 --no-graphics --script my-recipe.py` (recipe 7.1).

The recipes read the test files `tutorial-modern.pdb` and `rnasa-1.8-all_refmac1.mtz` from the folder Coot works
in; recipe 1.1 copies them there. Replace them with your own files (full paths work everywhere). Molecule numbers
are kept in variables (`imol`, `imol_map`): Coot gives every new molecule the next free number.

Each function used here is described, with an example, in the [scripting reference](../api/README.md).

## [1. Files and maps](01-files-and-maps.md)

- [1.1 Copy the test files into the folder Coot works in](01-files-and-maps.md#11-copy-the-test-files-into-the-folder-coot-works-in)
- [1.2 Read a model and keep its molecule number](01-files-and-maps.md#12-read-a-model-and-keep-its-molecule-number)
- [1.3 Make the 2Fo-Fc and the difference map from an MTZ file](01-files-and-maps.md#13-make-the-2fo-fc-and-the-difference-map-from-an-mtz-file)
- [1.4 Read all maps of an MTZ file at once](01-files-and-maps.md#14-read-all-maps-of-an-mtz-file-at-once)
- [1.5 Choose the map that refinement uses](01-files-and-maps.md#15-choose-the-map-that-refinement-uses)
- [1.6 Contour level and map radius](01-files-and-maps.md#16-contour-level-and-map-radius)
- [1.7 Save a model (PDB or mmCIF) and part of it](01-files-and-maps.md#17-save-a-model-pdb-or-mmcif-and-part-of-it)
- [1.8 Save a map to a file and read it back](01-files-and-maps.md#18-save-a-map-to-a-file-and-read-it-back)
- [1.9 List what is loaded](01-files-and-maps.md#19-list-what-is-loaded)
- [1.10 Cell, space group and close a molecule](01-files-and-maps.md#110-cell-space-group-and-close-a-molecule)

## [2. The view](02-view.md)

- [2.1 Go to a residue](02-view.md#21-go-to-a-residue)
- [2.2 Go to a point (x, y, z in Å)](02-view.md#22-go-to-a-point-x-y-z-in-å)
- [2.3 Zoom](02-view.md#23-zoom)
- [2.4 Save views and go back to them](02-view.md#24-save-views-and-go-back-to-them)
- [2.5 Show or hide a molecule or a map](02-view.md#25-show-or-hide-a-molecule-or-a-map)
- [2.6 Symmetry copies](02-view.md#26-symmetry-copies)
- [2.7 CA trace instead of all bonds, and back](02-view.md#27-ca-trace-instead-of-all-bonds-and-back)
- [2.8 Label atoms](02-view.md#28-label-atoms)
- [2.9 Background colour](02-view.md#29-background-colour)

## [3. Selections and information](03-selections.md)

- [3.1 Chains, residues and the sequence](03-selections.md#31-chains-residues-and-the-sequence)
- [3.2 Name and atoms of one residue](03-selections.md#32-name-and-atoms-of-one-residue)
- [3.3 Find all residues of one type](03-selections.md#33-find-all-residues-of-one-type)
- [3.4 Residues near a residue](03-selections.md#34-residues-near-a-residue)
- [3.5 Distance between two atoms](03-selections.md#35-distance-between-two-atoms)
- [3.6 Make a new molecule from a selection](03-selections.md#36-make-a-new-molecule-from-a-selection)
- [3.7 Residues with alternative conformations or missing atoms](03-selections.md#37-residues-with-alternative-conformations-or-missing-atoms)
- [3.8 Average and median B-factor](03-selections.md#38-average-and-median-b-factor)

## [4. Refinement](04-refinement.md)

- [4.1 Refine a range of residues against the map](04-refinement.md#41-refine-a-range-of-residues-against-the-map)
- [4.2 Refine a list of residues (they need not be next to each other)](04-refinement.md#42-refine-a-list-of-residues-they-need-not-be-next-to-each-other)
- [4.3 Sphere refine: a residue and everything around it](04-refinement.md#43-sphere-refine-a-residue-and-everything-around-it)
- [4.4 Geometry only (regularize, no map)](04-refinement.md#44-geometry-only-regularize-no-map)
- [4.5 Map weight and restraints](04-refinement.md#45-map-weight-and-restraints)
- [4.6 Rigid-body fit of a range](04-refinement.md#46-rigid-body-fit-of-a-range)
- [4.7 Best rotamer for a side chain](04-refinement.md#47-best-rotamer-for-a-side-chain)
- [4.8 Flip a peptide](04-refinement.md#48-flip-a-peptide)
- [4.9 Refine every chain in pieces (a whole model)](04-refinement.md#49-refine-every-chain-in-pieces-a-whole-model)

## [5. Editing a model](05-editing.md)

- [5.1 Copy a molecule](05-editing.md#51-copy-a-molecule)
- [5.2 Copy one chain or a piece into a new molecule](05-editing.md#52-copy-one-chain-or-a-piece-into-a-new-molecule)
- [5.3 Delete a residue, a range, a side chain, an atom](05-editing.md#53-delete-a-residue-a-range-a-side-chain-an-atom)
- [5.4 Delete all hydrogens or all waters](05-editing.md#54-delete-all-hydrogens-or-all-waters)
- [5.5 Renumber residues](05-editing.md#55-renumber-residues)
- [5.6 Change a chain ID](05-editing.md#56-change-a-chain-id)
- [5.7 Merge molecules](05-editing.md#57-merge-molecules)
- [5.8 Mutate a residue](05-editing.md#58-mutate-a-residue)
- [5.9 Mutate a range to a new sequence](05-editing.md#59-mutate-a-range-to-a-new-sequence)
- [5.10 Add a residue at the end of a chain](05-editing.md#510-add-a-residue-at-the-end-of-a-chain)
- [5.11 Set B-factors and occupancies](05-editing.md#511-set-b-factors-and-occupancies)
- [5.12 Undo](05-editing.md#512-undo)
- [5.13 Move a molecule](05-editing.md#513-move-a-molecule)
- [5.14 Rename a residue (no new atoms)](05-editing.md#514-rename-a-residue-no-new-atoms)

## [6. Customize Coot: toolbar, menus, keys, colours, preferences](06-customize.md)

- [6.1 A toolbar button that runs your code](06-customize.md#61-a-toolbar-button-that-runs-your-code)
- [6.2 A menu of your own](06-customize.md#62-a-menu-of-your-own)
- [6.3 A key that runs your code](06-customize.md#63-a-key-that-runs-your-code)
- [6.4 Colours: map, background, symmetry](06-customize.md#64-colours-map-background-symmetry)
- [6.5 Thicker bonds, bigger labels, colour by chain](06-customize.md#65-thicker-bonds-bigger-labels-colour-by-chain)
- [6.6 Messages for the user](06-customize.md#66-messages-for-the-user)
- [6.7 Preferences you can set from a script](06-customize.md#67-preferences-you-can-set-from-a-script)
- [6.8 Run your settings every time Coot starts](06-customize.md#68-run-your-settings-every-time-coot-starts)

## [7. Automatic workflows: scripts, loops, hooks](07-automation.md)

- [7.1 Run a script without the window (batch)](07-automation.md#71-run-a-script-without-the-window-batch)
- [7.2 Loop over every residue: a table of B-factors](07-automation.md#72-loop-over-every-residue-a-table-of-b-factors)
- [7.3 Write a report file: fit to the map of every residue](07-automation.md#73-write-a-report-file-fit-to-the-map-of-every-residue)
- [7.4 Do the same to many files](07-automation.md#74-do-the-same-to-many-files)
- [7.5 A hook: run your code after every change of a model](07-automation.md#75-a-hook-run-your-code-after-every-change-of-a-model)
- [7.6 Repeat something while Coot runs (every 10 seconds)](07-automation.md#76-repeat-something-while-coot-runs-every-10-seconds)
- [7.7 Python from Scheme and Scheme from Python](07-automation.md#77-python-from-scheme-and-scheme-from-python)

## [8. Validation](08-validation.md)

- [8.1 Ramachandran: residues outside the allowed regions](08-validation.md#81-ramachandran-residues-outside-the-allowed-regions)
- [8.2 Fit to the map: the worst residues](08-validation.md#82-fit-to-the-map-the-worst-residues)
- [8.3 Rotamers](08-validation.md#83-rotamers)
- [8.4 Geometry: the worst restraints of a residue](08-validation.md#84-geometry-the-worst-restraints-of-a-residue)
- [8.5 Cis peptides and wrong chiral centres](08-validation.md#85-cis-peptides-and-wrong-chiral-centres)
- [8.6 Atoms that overlap (clashes)](08-validation.md#86-atoms-that-overlap-clashes)
- [8.7 Peaks in the difference map](08-validation.md#87-peaks-in-the-difference-map)
- [8.8 Density not explained by the model (unmodelled blobs)](08-validation.md#88-density-not-explained-by-the-model-unmodelled-blobs)

## [9. NCS (non-crystallographic symmetry)](09-ncs.md)

- [9.1 Which chains are NCS copies](09-ncs.md#91-which-chains-are-ncs-copies)
- [9.2 How different are the copies (per residue)](09-ncs.md#92-how-different-are-the-copies-per-residue)
- [9.3 Show the NCS copies as ghosts](09-ncs.md#93-show-the-ncs-copies-as-ghosts)
- [9.4 Copy the master chain onto the other copies](09-ncs.md#94-copy-the-master-chain-onto-the-other-copies)
- [9.5 Superpose one chain onto another](09-ncs.md#95-superpose-one-chain-onto-another)
- [9.6 Least-squares fit on chosen residues](09-ncs.md#96-least-squares-fit-on-chosen-residues)

## [10. Ligands](10-ligands.md)

- [10.1 Make a ligand from the dictionary](10-ligands.md#101-make-a-ligand-from-the-dictionary)
- [10.2 Read your own dictionary (from acedrg, grade, eLBOW...)](10-ligands.md#102-read-your-own-dictionary-from-acedrg-grade-elbow)
- [10.3 Put a ligand at a place and add it to the protein](10-ligands.md#103-put-a-ligand-at-a-place-and-add-it-to-the-protein)
- [10.4 Residues around a ligand](10-ligands.md#104-residues-around-a-ligand)
- [10.5 Fit a ligand into the density (Find Ligands from a script)](10-ligands.md#105-fit-a-ligand-into-the-density-find-ligands-from-a-script)
- [10.6 Geometry of a ligand](10-ligands.md#106-geometry-of-a-ligand)
