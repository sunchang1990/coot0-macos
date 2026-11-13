
import sys, os
res = []
def check(name, fn):
    try:
        v = fn(); ok = True if v is None else bool(v); res.append((name, ok, repr(v)[:90]))
    except Exception as e:
        res.append((name, False, "EXC " + repr(e)[:120]))
here = os.environ.get("COOT_PREFIX", ".")
import coot
g = globals()
check("CLIBD_MON points at the monomer library", lambda: os.path.exists(os.path.join(os.environ.get("CLIBD_MON", "/nonexistent"), "list", "mon_lib_list.cif")))
imol = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
check("read tutorial-modern.pdb", lambda: coot.is_valid_model_molecule(imol))
check("monomer restraints for ALA load (dictionary found)", lambda: bool(coot.monomer_restraints_py("ALA")))
check("get_monomer(ATP) loads its dictionary, then restraints exist", lambda: coot.is_valid_model_molecule(coot.get_monomer("ATP")) and bool(coot.monomer_restraints_py("ATP")))
check("get_monomer('GOL') creates a molecule from the dictionary", lambda: coot.is_valid_model_molecule(coot.get_monomer("GOL")))
check("n_chains / n_residues from tutorial model", lambda: coot.n_chains(imol) >= 1 and coot.chain_n_residues(coot.chain_id_py(imol, 0), imol) > 50)
mtz = os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz")
imap = coot.make_and_draw_map(mtz, "FWT", "PHWT", "", 0, 0)
check("make_and_draw_map from the tutorial MTZ (uses syminfo.lib)", lambda: coot.is_valid_map_molecule(imap))
check("map sigma is a positive number", lambda: coot.map_sigma_py(imap) > 0)
check("space group read from the model", lambda: len(str(coot.show_spacegroup(imol))) > 0)
check("symmetry operators of the model (patched PyBool_Check site)", lambda: isinstance(coot.symmetry_operators_py(imol), list) and len(coot.symmetry_operators_py(imol)) > 1)
check("density at an atom position is a number", lambda: isinstance(coot.density_at_point(imap, 0.0, 0.0, 0.0), float))
# Regression for the crash seen with "Calculate > ... Make a Smoother Copy" (smooth_map(imol, 1.25)):
# a non-integer factor made a grid that the space group does not allow (225 x 225 x 400 for
# P 43 21 2); contouring the new map then threw clipper::Message_fatal and aborted Coot.
# The maps are made here with the standard library only (CCP4 map files with symmetry records).
import struct, math, tempfile
def _write_p43212_map(path, n, cell):
    sym_ops = ["X,Y,Z", "-X,-Y,Z+1/2", "-Y+1/2,X+1/2,Z+3/4", "Y+1/2,-X+1/2,Z+1/4",
               "-X+1/2,Y+1/2,-Z+1/4", "X+1/2,-Y+1/2,-Z+3/4", "Y,X,-Z", "-Y,-X,-Z+1/2"]
    sym = b"".join(s.encode().ljust(80) for s in sym_ops)
    nx, ny, nz = n
    hdr = bytearray(1024)
    def pi(i, v): struct.pack_into("<i", hdr, 4*i, v)
    def pf(i, v): struct.pack_into("<f", hdr, 4*i, v)
    pi(0, nx); pi(1, ny); pi(2, nz); pi(3, 2)
    pi(7, nx); pi(8, ny); pi(9, nz)
    for k, v in enumerate(cell): pf(10+k, v)
    pi(16, 1); pi(17, 2); pi(18, 3)
    pf(19, -1.0); pf(20, 1.0); pf(21, 0.0)
    pi(22, 96); pi(23, len(sym))
    hdr[208:212] = b"MAP "; hdr[212:216] = bytes([0x44, 0x44, 0, 0])
    data = bytearray()
    for k in range(nz):
        for j in range(ny):
            for i in range(nx):
                data += struct.pack("<f", math.sin(2*math.pi*i/nx) * math.cos(2*math.pi*j/ny) * math.sin(2*math.pi*k/nz))
    open(path, "wb").write(bytes(hdr) + sym + bytes(data))
_td = tempfile.mkdtemp(prefix="coot-map-test-")
_cell = (13.177, 13.177, 23.837, 90, 90, 90)
_good = os.path.join(_td, "p43212_36x36x64.map"); _write_p43212_map(_good, (36, 36, 64), _cell)
_bad = os.path.join(_td, "p43212_45x45x80.map");  _write_p43212_map(_bad, (45, 45, 80), _cell)
_im = coot.handle_read_ccp4_map(_good, 0)
check("P 43 21 2 test map (36x36x64) reads", lambda: coot.is_valid_map_molecule(_im))
def _smooth_and_recentre(factor):
    ism = coot.smooth_map(_im, factor)
    if not coot.is_valid_map_molecule(ism):
        return False
    coot.set_rotation_centre(3.0*factor, 4.0, 5.0)   # re-contours every map around the new centre
    coot.set_rotation_centre(-2.0, 7.0*factor, 1.0)
    return True
check("smooth_map(1.25) gives a usable map (225-like odd grid used to abort Coot)", lambda: _smooth_and_recentre(1.25))
check("smooth_map(1.1) and smooth_map(2.0) give usable maps", lambda: _smooth_and_recentre(1.1) and _smooth_and_recentre(2.0))
_ib = coot.handle_read_ccp4_map(_bad, 0)
check("a map file whose grid the space group forbids is refused or not drawn, no abort",
      lambda: (not coot.is_valid_map_molecule(_ib)) or (coot.set_rotation_centre(1.0, 2.0, 3.0) is None))
check("Coot is still running and the good map is still usable", lambda: coot.is_valid_map_molecule(_im) and coot.map_sigma_py(_im) > 0)
# ---- data files that `make install` puts into share/coot from other source directories (they were missing from the
# first packages: "Add N-linked glycan" said the link-by-torsion template was not found, Ligand Metric Sliders need the
# ligand database, Fit Loop by database search needs protein.db ...)
def check_strict(name, fn):   # a check passes only when it returns True; anything else is the failure detail
    try:
        v = fn(); res.append((name, v is True, "" if v is True else repr(v)[:120]))
    except Exception as e:
        res.append((name, False, "EXC " + repr(e)[:120]))
import __main__ as _mm
_pkg = os.path.join(here, "share", "coot")
_needed = ["ASN-NAG-via-NAG-ASN.pdb", "pyranose-pyranose-via-BETA1-4.pdb", "link-by-torsion-to-pyranose-core-NAG-ASN.tab",
           "link-by-torsion-to-NAG-core-NAG-SER.tab", "NAG-decorations.tab", "MAN-decorations.tab", "theor-helix-70.pdb",
           "protein_db/protein.db", "cootaneer-llk-2.40.dat", "nautilus_lib.pdb",
           "data/rama/zo-tables/coeffsolution.dat", "data/rama/zo-tables/all-non-pre-pro.tab", "data/ligands-2016.db",
           "data/assign-side-chains/useable-grid-points-nstep=5,box_radius=5.0-charybdis.data",
           "data/cho-models/model-level-1-NAG-NAG-ASN-ASN.tab", "data/cho-acedrg/NAG-acedrg.cif", "data/metal/metal-N-distance.table"]
check_strict("share/coot has the glyco templates, protein database, Cootaneer/Nautilus data, ligand database",
      lambda: True if not [f for f in _needed if not os.path.isfile(os.path.join(_pkg, f))] else [f for f in _needed if not os.path.isfile(os.path.join(_pkg, f))][:5])

# add an N-linked NAG to an ASN of the tutorial model (uses the link template files and NAG-decorations.tab)
def _add_nag_to_asn():
    asn = None
    for ch in _mm.chain_ids(imol):
        for i in range(coot.chain_n_residues(ch, imol)):
            if coot.resname_from_serial_number(imol, ch, i) == "ASN":
                asn = (ch, coot.seqnum_from_serial_number(imol, ch, i)); break
        if asn: break
    if not asn: return "no ASN in the test model"
    n_before = sum(coot.chain_n_residues(c, imol) for c in _mm.chain_ids(imol))
    r = coot.add_linked_residue(imol, asn[0], asn[1], "", "NAG", "NAG-ASN", 1)
    n_after = sum(coot.chain_n_residues(c, imol) for c in _mm.chain_ids(imol))
    # (add_linked_residue's own return value is always 0 in this version of Coot: count the residues instead)
    has_nag = any(coot.resname_from_serial_number(imol, c, i) == "NAG" for c in _mm.chain_ids(imol) for i in range(coot.chain_n_residues(c, imol)))
    return True if (n_after == n_before + 1 and has_nag) else "residues %d -> %d, NAG present: %r" % (n_before, n_after, has_nag)
coot.set_imol_refinement_map(imap)
check_strict("add_linked_residue: NAG-ASN adds a NAG (needs share/coot link templates)", _add_nag_to_asn)

# ---- Calculate > Modules > Carbohydrate (Glyco menu / "N-linked Glycan Addition..." dialog): the Python glue around add_linked_residue
_CHO = ("NAG", "BMA", "MAN", "GAL", "FUC", "SIA", "XYP", "FUL")
for _f in ("cho_restraints_from_models.py", "add_linked_cho.py"):      # (graphics-only modules: not loaded by a headless session)
    if not hasattr(_mm, "multi_add_linked_residue"):
        _fp = os.path.join(_pkg, "python", _f); exec(compile(open(_fp).read(), _fp, "exec"), _mm.__dict__)
def _cho_list():
    return [(c, coot.seqnum_from_serial_number(imol, c, i)) for c in _mm.chain_ids(imol) for i in range(coot.chain_n_residues(c, imol))
            if coot.resname_from_serial_number(imol, c, i) in _CHO]
def _first_asn():
    for ch in _mm.chain_ids(imol):
        for i in range(coot.chain_n_residues(ch, imol)):
            if coot.resname_from_serial_number(imol, ch, i) == "ASN": return ch, coot.seqnum_from_serial_number(imol, ch, i)
def _delete_all_cho():
    for c, n in _cho_list(): coot.delete_residue(imol, c, n, "")
def _glyco_spec_without_fit():
    # the glycan dialog turns "fit and refine for link addition" off; the C++ call then returns False although it added the residue
    _delete_all_cho(); ch, rn = _first_asn()
    coot.set_add_linked_residue_do_fit_and_refine(0)
    try:
        r = _mm.add_linked_residue_and_get_spec(imol, ch, rn, "", "NAG", "NAG-ASN", 2)
    finally:
        coot.set_add_linked_residue_do_fit_and_refine(1)
    ok = isinstance(r, list) and len(r) == 4 and r[0] and len(_cho_list()) == 1 and (r[1], r[2]) == _cho_list()[0]
    return True if ok else "returned %r, residues %r" % (r, _cho_list())
check_strict("glyco dialog: a NAG added with fit-and-refine off still returns its residue spec", _glyco_spec_without_fit)
def _glyco_multi_add():
    _delete_all_cho(); ch, rn = _first_asn()
    coot.set_add_linked_residue_do_fit_and_refine(0)    # state left behind by the dialog: the tree functions must not depend on it
    _mm.multi_add_linked_residue(imol, [ch, rn, ""], [["NAG", "NAG-ASN"], ["NAG", "BETA1-4"], ["BMA", "BETA1-4"]])
    names = sorted(coot.resname_from_serial_number(imol, c, i) for c in _mm.chain_ids(imol) for i in range(coot.chain_n_residues(c, imol))
                   if coot.resname_from_serial_number(imol, c, i) in _CHO)
    return True if names == ["BMA", "NAG", "NAG"] else "carbohydrate residues: %r" % names
check_strict("Glyco > N-link add NAG, NAG, BMA adds all three residues", _glyco_multi_add)
def _glyco_bad_fit_removed():
    # a residue that fits the density badly is deleted again and the old residues restored (this path called delete_residue_by_spec with the wrong arguments)
    _delete_all_cho(); ch, rn = _first_asn()
    coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name(ch, rn, " CA ")
    _mm.add_linked_residue_tree_correlation_cut_off = 2.0     # no residue can reach that
    try:
        r = _mm.add_linked_residue_add_cho_function(imol, [ch, rn, ""], ["NAG-ASN", "NAG"])
    finally:
        _mm.add_linked_residue_tree_correlation_cut_off = 0.5
    return True if (r is False and _cho_list() == []) else "returned %r, carbohydrate residues %r" % (r, _cho_list())
check_strict("glyco tree builder: a badly fitting residue is removed without an error", _glyco_bad_fit_removed)
def _glyco_tree_builds():
    _delete_all_cho(); ch, rn = _first_asn()
    coot.set_go_to_atom_molecule(imol); coot.set_go_to_atom_chain_residue_atom_name(ch, rn, " CA ")
    _mm.add_linked_residue_tree_correlation_cut_off = -2.0    # accept every placement: tests the tree machinery, not the fit
    coot.set_add_linked_residue_do_fit_and_refine(0)           # as left behind by the dialog
    _clash = _mm.clashes_with_symmetry; _mm.clashes_with_symmetry = lambda *a: 0   # (crystal contacts of an arbitrary ASN are not the point here)
    try:
        _mm.add_linked_residue_tree(imol, [ch, rn, ""], [["NAG-ASN", "NAG"], ["BETA1-4", "NAG"], ["BETA1-4", "BMA"]])
    finally:
        _mm.add_linked_residue_tree_correlation_cut_off = 0.5; _mm.clashes_with_symmetry = _clash
    n = len(_cho_list()); _delete_all_cho()
    return True if n == 3 else "%d carbohydrate residues built" % n
check_strict("glyco tree builder: NAG-NAG-BMA tree is built (also after the dialog switched fitting off)", _glyco_tree_builds)

# ---- Calculate > Fit Loop > Fit Loop by Database Search (needs share/coot/protein_db/protein.db: without it no candidates were found)
def _db_loops():
    r = coot.protein_db_loops_py(imol, [["A", 52, ""], ["A", 58, ""]], imap, 10, False)
    n = len(r[1]) if isinstance(r, list) and len(r) > 1 and isinstance(r[1], list) else -1
    return True if n >= 1 else "protein_db_loops returned %r" % (r,)
check_strict("Fit Loop by Database Search finds loop candidates in the protein database", _db_loops)

# ---- Calculate > Other Modelling Tools > Place Helix Here (needs share/coot/theor-helix-70.pdb: -1 without it)
def _place_helix():
    coot.set_rotation_centre(10.0, 10.0, 10.0)
    r = coot.place_helix_here()
    return True if (isinstance(r, int) and r >= 0) else "place_helix_here returned %r" % (r,)
check_strict("Place Helix Here builds a helix (theor-helix-70.pdb is installed)", _place_helix)

# ---- MolProbity helpers: the file of ligand connectivity for reduce/probe (copied a text file into a text file as bytes)
def _reduce_het_dict():
    import tempfile
    g = coot.get_monomer("GOL"); d = tempfile.mkdtemp(prefix="coot-reduce-"); old = os.getcwd(); os.chdir(d)
    try:
        os.makedirs("coot-molprobity"); _mm.write_reduce_het_dict(g, "het-dict.txt")
        ok = os.path.isfile("het-dict.txt") and "GOL" in open("het-dict.txt").read()
    finally:
        os.chdir(old)
    return True if ok else "het-dict.txt missing or without GOL"
check_strict("write_reduce_het_dict writes the ligand connectivity file for reduce and probe", _reduce_het_dict)

# ---- static check of the shipped Python scripts for slips that 2to3 left behind (each one was a real failure of a menu item)
def _py2_leftovers():
    import re
    bad = []
    rules = [(r"getiterator\(", "getiterator() was removed in Python 3.9 (PISA, wiki drug lookup)"),
             (r"\b_thread\.(start|get_url_status)\(", "_thread.start() on a Thread variable (Recent PDBe structures)"),
             (r"[+] *'\\u212B'\.encode|[+] *\"\\u212B\"\.encode", "str + bytes (C-beta deviants labels)"),
             (r"delete_residue_by_spec\(\*", "delete_residue_by_spec takes (imol, spec) (glyco tree builder)"),
             (r"copyfileobj\(open\([^)]*['\"]rb['\"]\)", "binary file copied into a text file (reduce/probe het dict)"),
             (r"stdin\.write\(.*\)\s*$", None)]
    pydir = os.path.join(_pkg, "python")
    for f in sorted(os.listdir(pydir)):
        if not f.endswith(".py"): continue
        for n, line in enumerate(open(os.path.join(pydir, f), errors="replace"), 1):
            if line.lstrip().startswith("#"): continue
            for rx, why in rules:
                if why and re.search(rx, line): bad.append("%s:%d %s" % (f, n, why))
    return True if not bad else bad[:4]
check_strict("shipped Python scripts have none of the known Python 2 leftovers", _py2_leftovers)

# ---- starting programs with piped input (Python 3: pipes are bytes unless text mode is requested)
import tempfile
def _popen_cat():
    d = tempfile.mkdtemp(prefix="coot-popen-test-"); log = os.path.join(d, "cat.log")
    rc = _mm.popen_command("/bin/cat", [], ["alpha", "beta", "END"], log)
    got = open(log).read()
    return True if (rc == 0 and got == "alpha\nbeta\nEND\n") else "rc %r log %r" % (rc, got)
check_strict("popen_command pipes its data lines to the program (refmac, ligand metric sliders)", _popen_cat)
def _popen_cat_screen():
    d = tempfile.mkdtemp(prefix="coot-popen-test-"); log = os.path.join(d, "cat.log")
    rc = _mm.popen_command("/bin/cat", [], ["one", "two"], log, True)
    got = open(log).read()
    return True if (rc == 0 and got == "one\ntwo\n") else "rc %r log %r" % (rc, got)
check_strict("popen_command with output to the terminal as well", _popen_cat_screen)
def _run_concurrently_cat():
    d = tempfile.mkdtemp(prefix="coot-popen-test-"); log = os.path.join(d, "cat.log")
    r = _mm.run_concurrently("cat", [], ["x1", "x2"], log)
    if not r: return "run_concurrently returned %r" % (r,)
    proc, lg = r
    proc.wait(); lg.close()
    got = open(log).read()
    return True if (proc.returncode == 0 and got == "x1\nx2\n") else "rc %r log %r" % (proc.returncode, got)
check_strict("run_concurrently (Run Refmac) sends its data and closes the pipe", _run_concurrently_cat)
def _ccp4_env():
    d = tempfile.mkdtemp(prefix="coot-ccp4-test-")
    for sub in ("bin", "include", "lib/data", "etc"): os.makedirs(os.path.join(d, sub))
    env = _mm.ccp4_child_env({"CCP4": d, "PATH": "/usr/bin", "CINCL": "/already/set"})
    bad = []
    if env.get("CLIBD") != os.path.join(d, "lib", "data"): bad.append("CLIBD " + repr(env.get("CLIBD")))
    if env.get("CINCL") != "/already/set": bad.append("CINCL overwritten: " + repr(env.get("CINCL")))
    if not env.get("CCP4_SCR") or not os.path.isdir(env["CCP4_SCR"]): bad.append("CCP4_SCR " + repr(env.get("CCP4_SCR")))
    if env.get("CCP4") != d or env.get("CBIN") != os.path.join(d, "bin"): bad.append("CCP4/CBIN")
    return True if not bad else bad
check_strict("ccp4_child_env adds CCP4's variables for child programs and keeps those already set", _ccp4_env)

# ---- Calculate > Ca -> Mainchain needs the reference structures (db-main/db-main.cc reads $COOT_REF_STRUCTS/*.pdb); the 0.9.8.96 release
# tarball does not contain them, so every click on a CA atom ended with "COOT_REF_STRUCTS is not defined" (build 11 and earlier)
def _refstructs():
    d = os.environ.get("COOT_REF_STRUCTS", "")
    n = len([f for f in os.listdir(d) if f.endswith(".pdb")]) if os.path.isdir(d) else 0
    return True if n >= 28 else "COOT_REF_STRUCTS=%r, %d pdb files" % (d, n)
check_strict("COOT_REF_STRUCTS points at the 28 reference structures", _refstructs)
def _ca_to_mainchain():
    imol_ca = coot.new_molecule_by_atom_selection(imol, "//A/10-40/CA")
    if not coot.is_valid_model_molecule(imol_ca): return "no CA-only molecule"
    n_ca = coot.n_atoms(imol_ca)
    n0 = coot.graphics_n_molecules()
    coot.db_mainchain(imol_ca, "A", 10, 40, "forwards")
    if coot.graphics_n_molecules() != n0 + 1: return "no new molecule (%d -> %d molecules)" % (n0, coot.graphics_n_molecules())
    imol_mc = n0
    n_mc = coot.n_atoms(imol_mc)
    names = set(a[0][0] for a in (coot.residue_info_py(imol_mc, "A", 20, "") or []))
    return True if (n_mc >= 4 * n_ca and {" N  ", " CA ", " C  ", " O  "} <= names) else "CA-only %d atoms -> %d atoms, residue 20 has %r" % (n_ca, n_mc, sorted(names))
check_strict("db_mainchain builds a main chain (N, CA, C, O) on a CA-only fragment (Ca -> Mainchain)", _ca_to_mainchain)

# File > Fetch PDB & Map using PDB-REDO (build 15), offline: a fake downloader stands in for PDB-REDO.  PDB-REDO answers a missing file with HTTP 404
# and an HTML page; Coot used to save that page as the model (mmCIF-only entries such as 9E5H) and run it as the guided tour.
import __main__, shutil
_redo_dir = tempfile.mkdtemp(prefix="coot-redo-"); _redo_cwd = os.getcwd(); os.chdir(_redo_dir)
_redo_cif = os.path.join(_redo_dir, "src-1ehz.cif")
_imol_src = coot.read_pdb(os.path.join(here, "test-data", "1ehz.pdb")); coot.write_cif_file(_imol_src, _redo_cif); coot.close_molecule(_imol_src)
_redo_urls = []
_redo_json = b'{"error":"Not Found"}'   # what PDB-REDO sends (HTTP 500) for an entry it does not have
_redo_html = b"<html>\n  <body>\n    <h1>Not Found</h1>\n  </body>\n</html>"
def _fake_get_url(url, file_name, have=("pdb", "cif", "mtz", "py")):
    _redo_urls.append(url)
    ext = url.rsplit(".", 1)[-1]
    src = {"pdb": os.path.join(here, "test-data", "1ehz.pdb"), "cif": _redo_cif, "mtz": os.path.join(here, "test-data", "1ehz_map.mtz")}.get(ext)
    with open(file_name, "wb") as f:
        if ext not in have: f.write(_redo_json if "0xyz" in url else _redo_html)
        elif ext == "py": f.write(b"pdb_redo_tour_ran = True\n")
        else: f.write(open(src, "rb").read())
    return 0
_old_get_url = g.get("coot_get_url")
_n0 = coot.graphics_n_molecules()
def _new_mols(): return [i for i in range(_n0, coot.graphics_n_molecules()) if coot.is_valid_model_molecule(i) or coot.is_valid_map_molecule(i)]
try:
    # an mmCIF-only entry: .pdb and .py are 404 pages
    __main__.coot_get_url = lambda u, f: _fake_get_url(u, f, have=("cif", "mtz"))
    g["get_pdb_redo"]("9E5H")
    _m = _new_mols()
    check("PDB-REDO mmCIF-only entry: model read from <id>_final.cif (new molecules %r)" % _m,
          lambda: any(coot.is_valid_model_molecule(i) for i in _m) and any(u.endswith("9e5h_final.cif") for u in _redo_urls))
    check("PDB-REDO mmCIF-only entry: maps made from the MTZ", lambda: sum(1 for i in _m if coot.is_valid_map_molecule(i)) >= 2)
    check("PDB-REDO: the HTML 404 page is not left as 9e5h_final.pdb / 9e5h.py", lambda: not os.path.exists("9e5h_final.pdb") and not os.path.exists("9e5h.py"))
    # nothing there at all (no such entry, or no network): no exception, nothing read, returns False
    __main__.coot_get_url = lambda u, f: _fake_get_url(u, f, have=())
    _n1 = coot.graphics_n_molecules()
    r = g["get_pdb_redo"]("0xyz")
    check("PDB-REDO entry without any files: returns False and reads nothing (got %r)" % (r,), lambda: r is False and coot.graphics_n_molecules() == _n1)
    check("PDB-REDO entry without any files: no JSON/HTML error page left as 0xyz_final.* (left: %r)" % [f for f in os.listdir(".") if f.startswith("0xyz")], lambda: not [f for f in os.listdir(".") if f.startswith("0xyz")])
    # the menu entry calls the Scheme (get-pdb-redo ...): it must reach the checked Python version (and its guided tour)
    __main__.coot_get_url = _fake_get_url
    del _redo_urls[:]; __main__.pdb_redo_tour_ran = False
    coot.run_scheme_command('(get-pdb-redo "1EHZ")')
    check("menu path (Scheme get-pdb-redo) uses the checked downloader (urls %r)" % _redo_urls[:3], lambda: any("pdb-redo.eu/db/1ehz/1ehz_final" in u for u in _redo_urls))
    check("PDB-REDO guided tour (Python) runs when PDB-REDO has it", lambda: getattr(__main__, "pdb_redo_tour_ran", False) is True)
finally:
    if _old_get_url is not None: __main__.coot_get_url = _old_get_url
    os.chdir(_redo_cwd); shutil.rmtree(_redo_dir, ignore_errors=True)

w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
