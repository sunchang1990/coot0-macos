# api_state.py  (build 31) -- a snapshot of what a scripting call can change, for the example runs of docs/api.
# Used inside Coot (Python):  snap = Snapshot(globals(), index_entries); a = snap.take(); ...call...; b = snap.take();
# snap.diff(a, b) -> a list of short, readable changes, e.g.
#   "molecule 0: A41 coordinates", "new molecule 2 (map)", "draw_hydrogens_state(0): 1 -> 0", "rotation centre moved 3.2 A".
# What is watched:
#   - every model molecule: its atoms (written to a PDB file and compared residue by residue: added, deleted, renamed,
#     coordinates, B-factors, occupancies, alt confs), its name and whether it is displayed;
#   - every map: sigma, mean, contour level, displayed, colour;
#   - the molecule list (new or closed molecules), the rotation centre, the zoom;
#   - the read-only getters of the API that take no argument or one molecule number (about 100 settings), called before
#     and after.  Getters whose answer changes by itself (counters, time) are dropped at the start.
import os, re, io, json, contextlib, tempfile, math

GETTER = re.compile(r"^(get_|is_|n_|has_|show_|.*_state$|.*_p$|.*_flag$|.*_mode$|.*_level$|.*_colour$|.*_width$|.*_size$|.*_cut_off$|.*_limit$|.*_radius$|"
                    r"graphics_n|.*_n_.*|first_|.*_sigma$|.*_mean$|.*_name$|.*_imol$|.*_molecule_number$|imol_refinement_map$|refinement_.*)")
BAD = ("set_", "add_", "delete", "remove", "clear", "make_", "read_", "write_", "save", "export", "import", "run_", "toggle", "refine",
       "fit", "mutate", "move", "apply", "fetch", "exit", "quit", "new_", "copy", "merge", "close", "undo", "redo", "accept", "reset",
       "do_", "go_to", "probe", "reduce", "refmac", "screendump", "handle_", "pointer", "_py_", "widget", "dialog", "window", "file",
       "show_", "display_", "unsaved", "backup", "time", "random", "history", "news", "ccp4i", "sleep", "fps", "rock",
       "bonds_representation", "radii", "intermediate_atoms", "_py$")

def _q(fn, *a):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return fn(*a)

def _fmt(v):
    if isinstance(v, float): return ("%.4g" % v)
    if isinstance(v, (list, tuple)): return "[" + ", ".join(_fmt(x) for x in v) + "]"
    return repr(v)

class Snapshot:
    def __init__(self, g, entries=None):
        self.g = g
        self.tmp = tempfile.mkdtemp(prefix="coot0-snap-")
        self.getters0, self.getters1 = [], []
        keys = set(e["key"] for e in entries or [])
        partners = set()                                   # the getter of every set_X: X, get_X, X_state, ...
        for k in keys:
            if k.startswith("set_"):
                b = k[4:]
                partners.update(c for c in (b, "get_" + b, b + "_state", "get_" + b + "_state", b + "_p", b.replace("_state", ""),
                                            "get_" + b.replace("_state", "")) if c in keys)
        for e in entries or []:
            py = e.get("py")
            if not py or py not in g or not callable(g.get(py)): continue
            k = e["key"].lower()
            if not (GETTER.match(k) or e["key"] in partners) or any(re.search(b, k) for b in BAD if b != "show_"): continue
            if (e.get("py_ret") or e.get("ret") or "void").strip() == "void": continue
            args = e.get("py_args") or []
            if not args: self.getters0.append(py)
            elif len(args) == 1 and args[0][0].strip() == "int" and ("imol" in args[0][1] or "mol" in args[0][1]): self.getters1.append(py)
        self.stable()

    def stable(self):
        """drop getters that fail, take long, or change between two calls with nothing done in between"""
        import time
        keep0, keep1, first, self.side_effects = [], [], {}, []
        nmol = lambda: _q(self.g["graphics_n_molecules"])
        def tidy(n0, name):                                # a "getter" that made a molecule is no getter
            if nmol() != n0:
                self.side_effects.append(name)
                for i in range(n0, nmol()): _q(self.g["close_molecule"], i)
                return True
            return False
        for name in self.getters0:
            try:
                n0 = nmol(); t = time.time(); first[name] = _q(self.g[name])
                if tidy(n0, name): continue
                if time.time() - t < 0.05 and len(repr(first[name])) < 3000: keep0.append(name)
            except Exception: pass
        for name in self.getters1:
            try:
                n0 = nmol(); t = time.time(); first[name] = [_q(self.g[name], i) for i in (0, 1)]
                if tidy(n0, name): continue
                if time.time() - t < 0.1 and len(repr(first[name])) < 3000: keep1.append(name)
            except Exception: pass
        time.sleep(0.5)                                  # a value that moves by itself (idle functions, clocks) is no use
        keep0 = [n for n in keep0 if _q(self.g[n]) == first[n]]
        keep1 = [n for n in keep1 if [_q(self.g[n], i) for i in (0, 1)] == first[n]]
        self.getters0, self.getters1 = keep0, keep1

    def _molecules(self):
        g = self.g; out = {}
        n = _q(g["graphics_n_molecules"])
        for i in range(n):
            if _q(g["is_valid_model_molecule"], i):
                p = os.path.join(self.tmp, "m%d.pdb" % i)
                try: os.remove(p)
                except OSError: pass
                _q(g["write_pdb_file"], i, p)
                res = {}
                try:
                    for l in open(p, errors="replace"):
                        if l.startswith(("ATOM", "HETATM")):
                            rid = "%s%s%s" % (l[21].strip() or "_", l[22:26].strip(), l[26].strip())
                            res.setdefault(rid, []).append(l[12:27] + "|" + l[30:66] + "|" + l[0:6].strip())
                except OSError: pass
                out[i] = ("model", _q(g["molecule_name"], i), _q(g["mol_is_displayed"], i) if "mol_is_displayed" in g else None, res)
            elif _q(g["is_valid_map_molecule"], i):
                vals = []
                for fn in ("map_sigma_py", "map_mean_py", "get_contour_level_absolute", "map_is_displayed", "map_colour_components_py"):
                    try: vals.append(_q(g[fn], i) if fn in g else None)
                    except Exception: vals.append(None)
                out[i] = ("map", _q(g["molecule_name"], i), vals)
        return out

    def take(self):
        g = self.g; s = {}
        try: s["molecules"] = self._molecules()
        except Exception as x: s["molecules"] = {"error": str(x)}
        try: s["centre"] = tuple(round(v, 2) for v in _q(g["rotation_centre"]))
        except Exception: s["centre"] = None
        try: s["zoom"] = round(_q(g["zoom_factor"]), 2) if "zoom_factor" in g else None
        except Exception: s["zoom"] = None
        gv = {}
        for name in self.getters0:
            try: gv[name + "()"] = _q(g[name])
            except Exception as x: gv[name + "()"] = "error"
        for name in self.getters1:
            for i in (0, 1):
                try: gv["%s(%d)" % (name, i)] = _q(g[name], i)
                except Exception: gv["%s(%d)" % (name, i)] = "error"
        s["getters"] = gv
        return s

    @staticmethod
    def _res_diff(a, b):
        """residue dict -> list of 'A41 coordinates' etc."""
        out = []
        added = [r for r in b if r not in a]; gone = [r for r in a if r not in b]
        if added: out.append("added %d residue(s) (%s)" % (len(added), ", ".join(added[:4]) + (" ..." if len(added) > 4 else "")))
        if gone: out.append("deleted %d residue(s) (%s)" % (len(gone), ", ".join(gone[:4]) + (" ..." if len(gone) > 4 else "")))
        kinds = {}
        for r in a:
            if r not in b or a[r] == b[r]: continue
            la, lb = a[r], b[r]
            what = set()
            if len(la) != len(lb) or [x[:15] for x in la] != [x[:15] for x in lb]: what.add("atoms")
            else:
                for x, y in zip(la, lb):
                    xs, ys = x.split("|"), y.split("|")
                    if xs[1][:24] != ys[1][:24]: what.add("coordinates")
                    if xs[1][24:30] != ys[1][24:30]: what.add("occupancies")
                    if xs[1][30:] != ys[1][30:]: what.add("B-factors")
                    if xs[2] != ys[2]: what.add("ATOM/HETATM")
            for w in what: kinds.setdefault(w, []).append(r)
        for w, rs in sorted(kinds.items()):
            out.append("%s of %d residue(s) (%s)" % (w, len(rs), ", ".join(rs[:4]) + (" ..." if len(rs) > 4 else "")))
        return out

    def diff(self, a, b):
        out = []
        ma, mb = a.get("molecules", {}), b.get("molecules", {})
        for i in sorted(set(ma) | set(mb), key=str):
            if i not in ma: out.append("new molecule %s (%s, %s)" % (i, mb[i][0], os.path.basename(str(mb[i][1])))); continue
            if i not in mb: out.append("molecule %s closed" % i); continue
            x, y = ma[i], mb[i]
            if x[0] != y[0]: out.append("molecule %s is now a %s" % (i, y[0])); continue
            if x[1] != y[1]: out.append("molecule %s renamed to %s" % (i, os.path.basename(str(y[1]))))
            if x[0] == "model":
                if x[2] != y[2]: out.append("molecule %s displayed: %s -> %s" % (i, x[2], y[2]))
                out += ["molecule %s: %s" % (i, t) for t in self._res_diff(x[3], y[3])]
            else:
                names = ("sigma", "mean", "contour level", "displayed", "colour")
                for n, p, q in zip(names, x[2], y[2]):
                    if p != q and not (isinstance(p, float) and isinstance(q, float) and abs(p - q) < 1e-4 * max(1, abs(p))):
                        out.append("map %s %s: %s -> %s" % (i, n, _fmt(p), _fmt(q)))
        if a.get("centre") and b.get("centre") and a["centre"] != b["centre"]:
            out.append("rotation centre moved %.1f A to (%s)" % (math.dist(a["centre"], b["centre"]), ", ".join("%.1f" % v for v in b["centre"])))
        if a.get("zoom") != b.get("zoom"): out.append("zoom: %s -> %s" % (a.get("zoom"), b.get("zoom")))
        ga, gb = a.get("getters", {}), b.get("getters", {})
        for k in ga:
            if k in gb and ga[k] != gb[k]:
                out.append("%s: %s -> %s" % (k, _fmt(ga[k])[:60], _fmt(gb[k])[:60]))
        return out
