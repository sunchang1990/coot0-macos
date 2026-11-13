
# Real-space refinement keeps the peptide bonds (regression test for the monomer-library path bug:
# without mon_lib_list.cif Coot made 0 link bond/angle restraints and refined zones tore away from their neighbours).
import os, math, sys
import coot
res = []
def check(name, fn):
    try:
        v = fn(); ok = True if v is None else bool(v); res.append((name, ok, repr(v)[:100]))
    except Exception as e:
        res.append((name, False, "EXC " + repr(e)[:120]))
here = os.environ.get("COOT_PREFIX", ".")
def atoms(fn):
    d = {}
    for l in open(fn):
        if l.startswith(("ATOM", "HETATM")) and l[16] in " A":
            d[(l[21], int(l[22:26]), l[12:16].strip())] = (float(l[30:38]), float(l[38:46]), float(l[46:54]))
    return d
def dist(a, b): return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
imol = coot.read_pdb(os.path.join(here, "test-data", "tutorial-modern.pdb"))
imap = coot.make_and_draw_map(os.path.join(here, "test-data", "rnasa-1.8-all_refmac1.mtz"), "FWT", "PHWT", "", 0, 0)
coot.set_imol_refinement_map(imap)
chain = coot.chain_id_py(imol, 0); r1, r2 = 40, 46
coot.write_pdb_file(imol, "refine_before.pdb")
coot.set_refinement_immediate_replacement(1)
coot.refine_zone(imol, chain, r1, r2, "")
coot.accept_regularizement()
coot.write_pdb_file(imol, "refine_after.pdb")
b, a = atoms("refine_before.pdb"), atoms("refine_after.pdb")
cn = [dist(a[(chain, i, "C")], a[(chain, i + 1, "N")]) for i in range(r1 - 3, r2 + 3) if (chain, i, "C") in a and (chain, i + 1, "N") in a]
check("peptide C-N after refinement all within 1.25-1.42 A (%d bonds, min %.2f max %.2f)" % (len(cn), min(cn), max(cn)), lambda: len(cn) >= 10 and all(1.25 <= d <= 1.42 for d in cn))
flank = [dist(a[k], b[k]) for k in a if k in b and k[0] == chain and k[1] in (r1 - 1, r2 + 1)]
check("flanking (fixed) residues did not move (max %.4f A)" % max(flank), lambda: max(flank) < 0.001)
far = [dist(a[k], b[k]) for k in a if k in b and (k[0] != chain or k[1] < r1 - 1 or k[1] > r2 + 1)]
check("residues outside the zone did not move (max %.4f A)" % max(far), lambda: max(far) < 0.001)
inz = [dist(a[k], b[k]) for k in a if k in b and k[0] == chain and r1 <= k[1] <= r2]
check("zone atoms moved (mean %.3f A)" % (sum(inz) / len(inz)), lambda: sum(inz) / len(inz) > 0.01)

# Stepped Refine on RNA (build 15): Coot's refine_auto_range() needs a CA atom, so nucleotides were never refined and the view centred on "CA".
import __main__
centre = getattr(__main__, "stepped_refine_centre_atom", None)
imol_r = coot.read_pdb(os.path.join(here, "test-data", "1ehz.pdb"))
imap_r = coot.make_and_draw_map(os.path.join(here, "test-data", "1ehz_map.mtz"), "FWT", "PHWT", "", 0, 0)
coot.set_imol_refinement_map(imap_r)
check("Stepped Refine centres a nucleotide on C1' (got %r)" % (centre and centre(imol_r, "A", 22, "")), lambda: centre is not None and centre(imol_r, "A", 22, "") == "C1'")
coot.write_pdb_file(imol_r, "rna_before.pdb")
__main__.refine_auto_range_and_show(imol_r, "A", 22, "", seconds=0)
coot.write_pdb_file(imol_r, "rna_after.pdb")
b, a = atoms("rna_before.pdb"), atoms("rna_after.pdb")
inr = [dist(a[k], b[k]) for k in a if k in b and k[0] == "A" and k[1] == 22]
check("Stepped Refine step refines RNA residue A 22 (mean move %.3f A)" % (sum(inr) / max(1, len(inr))), lambda: len(inr) > 10 and sum(inr) / len(inr) > 0.005)
far = [dist(a[k], b[k]) for k in a if k in b and (k[0] != "A" or k[1] < 20 or k[1] > 24)]
check("RNA residues away from A 21-23 did not move (max %.4f A)" % max(far), lambda: max(far) < 0.001)
w = max(len(r[0]) for r in res)
for n, ok, v in res: print(("PASS " if ok else "FAIL ") + n.ljust(w) + "  " + v)
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
