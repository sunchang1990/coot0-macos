# Python-3 leftovers in Coot's GUI scripts (found with the scripts loaded on the PyGTK layer)

Method: `pyflakes python/*.py` -> 1005 unique names used but not defined in their own file (most are Coot API / GTK names that exist at run time because the scripts share one namespace).
Each name was then looked up in the real namespace after `coot_load_modules.py` had run (tests/gui_harness.py): 33 were not defined anywhere (listing below, taken BEFORE patch 0025).
A regex scan for Python-2 idioms (types.*Type, apply(), file(), has_key, string.*, xrange, ...) found the remaining sites; everything except the groups below had been fixed by the earlier automatic port (patch 0008).

## Names not defined at run time (first location)

- `CG_spin_research` (2 uses), e.g. find_baddies.py:41
- `CG_spin_search` (2 uses), e.g. find_baddies.py:158
- `ListType` (10 uses), e.g. coot_utils.py:740
- `StringType` (8 uses), e.g. coot_toolbuttons.py:569
- `apply` (3 uses), e.g. coot_toolbuttons.py:87
- `backup_mode` (1 use), e.g. coot_utils.py:72
- `c_beta_deviations` (4 uses), e.g. dynamic_atom_overlaps_and_other_outliers.py:24
- `chain_n_iresidues` (1 use), e.g. mutate.py:25
- `cif_cod_str` (1 use), e.g. local_code.py:5
- `coot_tmp_dir` (1 use), e.g. get_ebi.py:127
- `coot_tooltips` (9 uses), e.g. clear_backup.py:132
- `cs_mol_ur` (1 use), e.g. coot_utils.py:3747
- `dots_file_name` (1 use), e.g. enhanced_ligand.py:246
- `extra_restraints2refmac_restraints_file` (1 use), e.g. gui_prosmart.py:270
- `file` (6 uses), e.g. 3d_generator_import.py:386
- `handle_chelx_fcf_file` (1 use), e.g. shelx.py:643
- `imol` (2 uses), e.g. enhanced_ligand.py:239
- `imol_coords` (1 use), e.g. refmac.py:615
- `imol_copy` (3 uses), e.g. gap.py:158
- `imol_diff_map` (1 use), e.g. coot_gui.py:6130
- `imol_map` (3 uses), e.g. gui_ligand_sliders.py:15
- `isNumbertype` (1 use), e.g. coot_utils.py:2042
- `mol_no_ls` (1 use), e.g. coot_gui.py:954
- `residue_name_by_spec` (1 use), e.g. gui_add_linked_cho.py:515
- `residue_spec` (1 use), e.g. coot_gui.py:1776
- `save_dialog_positions_to_preferences_file` (1 use), e.g. extensions.py:1844
- `scored_residues` (1 use), e.g. find_baddies.py:44
- `sequence_list` (1 use), e.g. mutate.py:34
- `setup_wii` (1 use), e.g. coot_gui.py:5850
- `stop_wii` (1 use), e.g. coot_gui.py:5858
- `tip_list` (4 uses), e.g. tips_gui.py:21

Most of the short lowercase ones (imol, imol_map, imol_copy, ...) are local variables or names defined under `try/except NameError` guards (not bugs).
Real bugs among them: ListType/StringType/apply/file/isNumbertype (py2 idioms), coot_tooltips (only reached for PyGTK < 2.12: dead code), chain_n_iresidues, residue_name_by_spec,
handle_chelx_fcf_file, save_dialog_positions_to_preferences_file, mol_no_ls (typos), molecule_atom_overlaps_gui and pepflips_by_difference_map_gui (Python versions never written; ported from Scheme).

## Python-2 idiom sites before the fix (count by category)

- file(: 7 line(s) in 4 file(s)
- types-names: 62 line(s) in 11 file(s)
- apply(: 3 line(s) in 3 file(s)
- int-division-index: 13 line(s) in 6 file(s)
- os.popen23: 2 line(s) in 2 file(s)
- backtick: 1 line(s) in 1 file(s)

After patch 0025: `tests/gui_python_dialogs.py` check 'no Python-2-only names in the shipped scripts' walks the AST of every shipped script (incl. rcrane) and passes.
