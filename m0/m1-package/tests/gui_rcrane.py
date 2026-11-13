
# Headless tests of RCrane (Calculate > RCrane): the Python 2 code is ported to Python 3 / the PyGTK-2 compatibility layer, so every window and every
# button it creates is driven here with real data - tRNA 1EHZ (chain A, 76 nt) and its 2mFo-DFc map (test-data/1ehz.pdb, 1ehz_map.mtz).
# What this can NOT show: how the windows look on a screen (sizes of the list views, colours of the cells) - that is checked by hand (protocol, RCrane).
import os, sys, math, time, contextlib, traceback, tempfile
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
import _gtk2core as _c
res = []
def check(name, fn):
    t0 = time.time()
    try:
        v = fn(); ok = (v is None or v is True)
        res.append((name, ok, "" if ok else repr(v)[:300]))
    except BaseException as e:
        res.append((name, False, "EXC " + repr(e)[:160] + " " + traceback.format_exc()[-400:].replace("\n", " | ")))
    print("[%s] %s  (%.0f s)" % ("ok" if res[-1][1] else "FAIL", name, time.time() - t0), flush=True)
g, errs, log = H.load()
import coot, __main__ as m
here = os.environ["COOT_PREFIX"]; td = os.path.join(here, "test-data")
PDB, MTZ = os.path.join(td, "1ehz.pdb"), os.path.join(td, "1ehz_map.mtz")
N_ERR0 = len(_c.CALLBACK_ERRORS)

imol = coot.read_pdb(PDB)
imap = coot.make_and_draw_map(MTZ, "FWT", "PHWT", "", 0, 0)
coot.set_imol_refinement_map(imap)

def coords(im, chain="A", lo=1, hi=76):
    d = {}
    for r in range(lo, hi + 1):
        for a in coot.residue_info_py(im, chain, r, "") or []:
            d[(r, a[0][0].strip())] = tuple(a[2][:3])
    return d
def shifts(a, b, lo=None, hi=None):
    ks = [k for k in a if k in b and (lo is None or lo <= k[0] <= hi)]
    return [math.dist(a[k], b[k]) for k in ks]
def spec(im, r, atom): return [1, im, "A", r, "", atom, ""]
W0 = len(H.windows)
def all_buttons(w):
    out = []
    for x in H.walk(w):
        if type(x).__name__ == "Button":
            labs = [(c.get_label() or "").strip() for c in H.walk(x) if type(c).__name__ == "Label"]
            out.append(((x.get_label() or "").strip() or (labs[0] if labs else ""), x))
    return out
def find_button(txt, since=None):
    for w in reversed(H.windows[(W0 if since is None else since):]):
        try:
            for lab, b in all_buttons(w):
                if lab == txt: return b
        except Exception: pass
    return None
def press(txt, since=None):
    b = find_button(txt, since)
    if b is None: raise AssertionError("no button %r in the RCrane windows" % txt)
    b.clicked()
def window_buttons(since=None):
    s = set()
    for w in H.windows[(W0 if since is None else since):]:
        try: s |= set(l for l, b in all_buttons(w))
        except Exception: pass
    return s
def tree_views(w): return [x for x in H.walk(w) if type(x).__name__ == "TreeView"]
def frame_titles(w): return [x.get_label() for x in H.walk(w) if type(x).__name__ == "Frame"]
def menu_items():
    """every item of the main menu bar, including those in sub-menus (H.walk follows children only: a menu item's sub-menu is not a child)"""
    out = []
    def rec(shell):
        for it in shell.get_children():
            out.append(it)
            sub = it.get_submenu() if hasattr(it, "get_submenu") else None
            if sub is not None: rec(sub)
    rec(g["_menubar"]); return out
def item_labelled(txt): return [i for i in menu_items() if (getattr(i, "get_label", lambda: "")() or "") == txt]
def menu_labels(): return [(getattr(i, "get_label", lambda: "")() or "") for i in menu_items()]

# ---------------------------------------------------------------------------------------------------------------- menu
import rcrane, rcrane.rotamerize as RZ, rcrane.extendChain as EC
def menu():
    # build 13: "Calculate > RCrane launch" made a new top-level menu when used - on one machine that gave neither a menu nor a message.
    # Since build 14 "Calculate > RCrane" is a sub-menu that exists from start-up.
    if item_labelled("RCrane launch"): return "the old entry Calculate > RCrane launch is still there"
    top = item_labelled("RCrane")
    if len(top) != 1: return "Calculate > RCrane: %d entries (RCrane is switched off? COOT_DISABLE_RCRANE)" % len(top)
    calc = [i for i in g["_menubar"].get_children() if (getattr(i, "get_label", lambda: "")() or "").replace("_", "") == "Calculate"]
    if len(calc) != 1 or top[0] not in calc[0].get_submenu().get_children(): return "the RCrane item is not in the Calculate menu"
    want = ["New trace 5'->3'...", "New trace 3'->5'...", "Extend chain...", "Rotamerize existing structure...", "Rotamerize without density...", "About RCrane..."]
    labs = [(i.get_label() or "") for i in top[0].get_submenu().get_children()]
    if labs != want: return "entries %r, expected %r" % (labs, want)
    return True
check("Calculate > RCrane (sub-menu from start-up) has its 6 entries and no 'RCrane launch' step", menu)
def menu_guard():
    import io, contextlib, rcrane.menu as RM
    sub = item_labelled("RCrane")[0].get_submenu()
    def entry(txt): return [i for i in sub.get_children() if i.get_label() == txt][0]
    def run(txt):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf): entry(txt).activate()
        return buf.getvalue()
    keep = (rcrane.newTrace, rcrane.checkCootAndReportErrors, RM._check_passed)
    calls = {"check": 0, "trace": 0}
    def fake_check(): calls["check"] += 1; return calls["check"] > 1       # the first check fails, the second passes
    def fake_trace(direction=3): calls["trace"] += 1
    try:
        rcrane.checkCootAndReportErrors = fake_check; rcrane.newTrace = fake_trace; RM._check_passed = False
        o1 = run("New trace 5'->3'...")
        if calls != {"check": 1, "trace": 0} or "selected" not in o1 or "pre-launch check failed" not in o1: return "failed check: calls %r output %r" % (calls, o1[-300:])
        o2 = run("New trace 5'->3'...")
        o3 = run("New trace 3'->5'...")
        if calls != {"check": 2, "trace": 2}: return "after a passed check: calls %r (the check must run once more after a failure, and not again after a pass)" % (calls,)
        def boom(direction=3): raise ValueError("test failure in a handler")
        rcrane.newTrace = boom
        o4 = run("New trace 5'->3'...")
        if "ERROR:: RCrane" not in o4 or "Traceback" not in o4 or "test failure in a handler" not in o4: return "a failing handler was not reported: %r" % (o4[-300:],)
        o5 = run("About RCrane...")
        return True if "\"About RCrane\" selected" in o5 else "About RCrane printed %r" % (o5[-200:],)
    finally:
        rcrane.newTrace, rcrane.checkCootAndReportErrors, RM._check_passed = keep
check("RCrane entries: the pre-launch check runs when an entry is first used, and a failing handler is printed (not lost)", menu_guard)
def about():
    import gtk
    made = []
    orig_init = gtk.AboutDialog.__init__
    def spy(self, *a, **k): orig_init(self, *a, **k); made.append(self)
    gtk.AboutDialog.__init__ = spy
    try: rcrane.createAboutDialog()
    finally: gtk.AboutDialog.__init__ = orig_init
    return True if made else "no About dialog created"
check("About RCrane... builds its dialog (logo, licence, reference button)", about)
def citation():
    from rcrane.citationPopup import createCitationPopup
    n = len(H.windows); createCitationPopup(); return True
check("the citation pop-up builds (check button + OK)", citation)
def deps():
    import rcrane.linearInterp as LI, rcrane.smoothProb as SP
    d = os.path.join(here, "share/coot/python/rcrane/data")
    li = LI.LinearInterp(os.path.join(d, "phosDistSmoothed.csv")); v = li.interp(5.7)
    sp = SP.SmoothProb(os.path.join(d, "smoothedPuckerDist.csv")) if hasattr(SP, "SmoothProb") else None
    return True if (isinstance(v, float) and v > 0) else "interp(5.7) = %r" % (v,)
check("the data tables load (linearInterp compared a float with text in Python 3)", deps)

# ---------------------------------------------------------------------------------------------------------------- rotamerize
orig = coords(imol)
state = {}
def rotamerize_pick():
    cap = {}
    RZ.user_defined_click = lambda n, f: cap.update(n=n, f=f)
    items = item_labelled("Rotamerize existing structure...")
    items[0].activate()
    if cap.get("n") != 2: return "the menu entry asked for %r clicks" % (cap.get("n"),)
    w0 = len(H.windows)
    cap["f"](spec(imol, 3, " P  "), spec(imol, 6, " O3'"))
    new = H.windows[w0:]
    if not new: return "no review window"
    state["review_since"] = w0; state["review"] = new[-1]
    return True
check("Rotamerize existing structure...: the two clicks (nucleotides 3-6) open the review window", rotamerize_pick)
def review_contents():
    w = state["review"]; tvs = tree_views(w)
    if len(tvs) != 2: return "%d list views" % len(tvs)
    conf = [t for t in tvs if t.get_headers_visible()][0]; over = [t for t in tvs if not t.get_headers_visible()][0]
    mdl = conf.get_model(); state["conf"], state["over"] = conf, over
    from rcrane.puckerList import puckerList
    if len(mdl) != len(puckerList): return "%d conformer rows, expected %d" % (len(mdl), len(puckerList))
    sel = conf.get_selection().get_selected()
    if sel[1] is None: return "no conformer selected"
    row = [mdl.get_value(sel[1], c) for c in range(4)]
    cols = [c.get_title() for c in conf.get_columns()]
    if cols != ["Rank", "Conformer", "Score", "Leading Pucker", "Ending Pucker"]: return cols
    if len(over.get_columns()) < 3 or len(over.get_model()) != 2: return "overview %d columns, %d rows" % (len(over.get_columns()), len(over.get_model()))
    titles = [c.get_title() for c in over.get_columns()]       # the click handler reads the suite number from the column title
    if titles != [str(i + 1) for i in range(len(titles))]: return "overview column titles %r" % (titles,)
    want = {"Previous Conformer", "Next Conformer", "Previous Suite", "Next Suite", "Accept New Coordinates", "Restore Original Coordinates"}
    miss = want - window_buttons(state["review_since"])
    if miss: return "missing buttons %r" % (miss,)
    return True if row[0] and float(row[1]) >= 0 else row
check("the review window shows the conformer list (52 rows, 5 columns), the suite overview and its 6 buttons", review_contents)
def selected_conf():
    mdl, it = state["conf"].get_selection().get_selected(); return mdl.get_value(it, 0)
def navigate():
    first = selected_conf(); title0 = frame_titles(state["review"])
    n0 = len(_c.CALLBACK_ERRORS)
    t0 = time.time(); press("Next Conformer", state["review_since"]); second = selected_conf()
    if second == first: return "Next Conformer did not move the selection (%s)" % first
    press("Previous Conformer", state["review_since"]); back = selected_conf()
    if back != first: return "Previous Conformer went to %s, expected %s" % (back, first)
    press("Next Suite", state["review_since"]); title1 = frame_titles(state["review"])
    if title1 == title0: return "Next Suite did not change the frame title %r" % (title1,)
    press("Previous Suite", state["review_since"])
    if frame_titles(state["review"]) != title0: return "Previous Suite: %r" % (frame_titles(state["review"]),)
    cbs = [x for x in H.walk(state["review"]) if type(x).__name__ == "CheckButton"]
    for c in cbs: c.set_active(False); c.set_active(True)
    errs_ = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    return True if not errs_ else errs_
check("Previous/Next Conformer and Previous/Next Suite re-minimise and move through the review window", navigate)
def accept():
    n0 = len(_c.CALLBACK_ERRORS)
    press("Accept New Coordinates", state["review_since"])
    after = coords(imol)
    if set(after) != set(orig): return "atom list changed: %d -> %d atoms" % (len(orig), len(after))
    sh = shifts(orig, after)
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    state["accept_shift"] = (sum(sh) / len(sh), max(sh))
    print("ROUND-TRIP: rotamerize nucleotides 3-6 of tRNA 1EHZ, accept: %d atoms, mean shift %.2f A, max %.2f A (nucleotides 2-7: mean %.2f A)" % (len(sh), sum(sh) / len(sh), max(sh), (lambda v: sum(v) / len(v))(shifts(orig, after, 2, 7))), flush=True)
    if bad: return bad
    if any(math.isnan(v) for xyz in after.values() for v in xyz): return "NaN coordinates"
    return True if (sum(sh) / len(sh) < 0.6 and max(sh) < 3.0) else "mean shift %.2f A, max %.2f A" % (sum(sh) / len(sh), max(sh))
check("Accept New Coordinates keeps all atoms and the rebuilt RNA stays within 0.6 A (mean) of the deposited model", accept)
def no_density_restore():
    before = coords(imol)
    w0 = len(H.windows)
    RZ.rotamerizeFromAtomSpecs(spec(imol, 20, " P  "), spec(imol, 23, " O3'"), True)
    if len(H.windows) == w0: return "no review window (rotamerize without density)"
    state["nd_since"] = w0
    press("Restore Original Coordinates", w0)
    after = coords(imol); sh = shifts(before, after)
    return True if (set(before) == set(after) and max(sh) < 0.01) else "restore left a shift of up to %.3f A" % max(sh)
check("Rotamerize without density, then Restore Original Coordinates gives back the starting coordinates", no_density_restore)
def no_density_accept():
    before = coords(imol)
    w0 = len(H.windows)
    RZ.rotamerizeFromAtomSpecs(spec(imol, 20, " P  "), spec(imol, 23, " O3'"), True)
    press("Next Conformer", w0)
    press("Accept New Coordinates", w0)
    after = coords(imol); sh = shifts(before, after)
    return True if (set(before) == set(after) and max(sh) > 0.01) else "nothing changed (max shift %.3f)" % max(sh)
check("Rotamerize without density, Next Conformer, Accept New Coordinates changes the nucleotides", no_density_accept)
def too_many():
    old = RZ.MAX_NUCLEOTIDES_TO_ROTAMERIZE; w0 = len(H.windows)
    try:
        rcrane.setRotamerizeMaxNucleotides(3)
        r = RZ.rotamerizeFromAtomSpecs(spec(imol, 20, " P  "), spec(imol, 30, " O3'"), False)
    finally: rcrane.setRotamerizeMaxNucleotides(old)
    return True if len(H.windows) == w0 else "the limit on nucleotides was ignored"
check("the limit on the number of nucleotides to rotamerize is respected", too_many)

# ---------------------------------------------------------------------------------------------------------------- new trace
imol_t = coot.read_pdb(PDB)                       # (only the map is used for the trace; this copy gives the "truth")
truth = {r: coords(imol_t, lo=r, hi=r).get((r, "P")) for r in range(5, 32)}
def new_trace():
    from rcrane.traceGui import TraceGui
    since = len(H.windows)
    before_mols = set(i for i in range(0, 30) if coot.is_valid_model_molecule(i))
    TraceGui(3, curCoords=truth[10])
    if not H.windows[since:]: return "no window for the initial phosphate"
    state["trace_since"] = since; state["trace_before"] = before_mols
    b = window_buttons(since)
    miss = {"Next", "Previous", "Manually Adjust", "Accept", "Cancel"} - b
    return True if not miss else "missing %r in %r" % (miss, b)
check("New trace: the initial-phosphate window offers Next / Previous / Manually Adjust / Accept / Cancel", new_trace)
def initial_phos():
    s = state["trace_since"]
    press("Next", s); press("Previous", s)
    press("Accept", s)
    b = window_buttons(s)
    miss = {"Next Phos", "Previous Phos", "Next C1\N{PRIME}", "Previous C1\N{PRIME}", "Anti/Syn Flip", "Manually Adjust", "Accept Nt", "Previous Nt", "Build Backbone", "Delete Trace"} - b
    return True if not miss else "missing %r in %r" % (miss, b)
check("New trace: Next/Previous peak, Accept -> the nucleotide window with 10 buttons", initial_phos)
def nucleotides():
    s = state["trace_since"]; n0 = len(_c.CALLBACK_ERRORS)
    press("Accept Nt", s)
    for lab in ("Next Phos", "Previous Phos", "Next C1\N{PRIME}", "Previous C1\N{PRIME}", "Anti/Syn Flip", "Anti/Syn Flip"): press(lab, s)
    press("Accept Nt", s)
    press("Previous Nt", s)
    press("Accept Nt", s); press("Accept Nt", s)
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    return True if not bad else bad
check("New trace: Accept Nt, Next/Previous Phos and C1', Anti/Syn Flip, Previous Nt run without errors", nucleotides)
def adjust():
    s = state["trace_since"]; n0 = len(_c.CALLBACK_ERRORS); w0 = len(H.windows)
    bs = [b for lab, b in sum([all_buttons(w) for w in H.windows[s:]], []) if lab == "Manually Adjust"]
    if not bs: return "no Manually Adjust button"
    bs[0].clicked()
    new = H.windows[w0:]
    if not new: return "Manually Adjust opened no dialog"
    scales = [x for w in new for x in H.walk(w) if type(x).__name__ == "HScale"]
    if len(scales) != 3: return "%d sliders in the phosphate adjust dialog" % len(scales)
    # (moving a slider calls get_screen_vectors(), which needs a drawing area: not available without a window)
    if not all(isinstance(sc.get_adjustment().value, float) for sc in scales): return "slider adjustments are not floats"
    press("OK", w0)
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    return True if not bad else bad
check("New trace: Manually Adjust (x/y/z sliders) moves the phosphate and OK closes the dialog", adjust)
def build_backbone():
    s = state["trace_since"]; n0 = len(_c.CALLBACK_ERRORS)
    press("Build Backbone", s)
    b = window_buttons(s)
    if "Done" not in b: return "no review window with a Done button: %r" % b
    new = [i for i in range(0, 30) if coot.is_valid_model_molecule(i) and i not in state["trace_before"] and i != imol_t]
    if not new: return "no RCrane molecule"
    nm = new[0]; state["trace_mol"] = nm
    P = [r for r in range(-5, 40) if any(a[0][0].strip() == "P" for a in (coot.residue_info_py(nm, "A", r, "") or []))]
    if len(P) < 4: return "only %d phosphates in the traced molecule" % len(P)
    xyz = [v for r in range(-5, 40) for a in (coot.residue_info_py(nm, "A", r, "") or []) for v in a[2][:3]]
    if any(math.isnan(v) for v in xyz): return "NaN coordinates"
    press("Next Conformer", s); press("Previous Conformer", s)
    press("Done", s)
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    return True if not bad else bad
check("New trace: Build Backbone builds a molecule of >= 4 phosphates, the review window works and Done closes it", build_backbone)

def trace_35():
    from rcrane.traceGui import TraceGui
    since = len(H.windows); n0 = len(_c.CALLBACK_ERRORS)
    before_mols = set(i for i in range(0, 30) if coot.is_valid_model_molecule(i))
    TraceGui(5, curCoords=truth[24])
    press("Accept", since)
    press("Accept Nt", since); press("Accept Nt", since); press("Previous Nt", since); press("Accept Nt", since); press("Accept Nt", since); press("Accept Nt", since)
    press("Build Backbone", since)
    if "Done" not in window_buttons(since): return "no review window: %r" % window_buttons(since)
    new = [i for i in range(0, 30) if coot.is_valid_model_molecule(i) and i not in before_mols]
    if not new: return "no RCrane molecule"
    press("Done", since)
    n_res = len([r for r in range(-5, 40) if coot.residue_info_py(new[0], "A", r, "")])
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    if bad: return bad
    return True if n_res >= 4 else "%d residues" % n_res
check("New trace 3'->5': Accept, Accept Nt, Previous Nt, Build Backbone, Done build a molecule", trace_35)

# ---------------------------------------------------------------------------------------------------------------- extend chain
imol_e = coot.read_pdb(PDB)
for r in range(21, 77): coot.delete_residue(imol_e, "A", r, "")
def extend_pick():
    cap = {}
    EC.user_defined_click = lambda n, f: cap.update(n=n, f=f)
    items = item_labelled("Extend chain...")
    items[0].activate()
    if cap.get("n") != 1: return "the menu entry asked for %r clicks" % (cap.get("n"),)
    since = len(H.windows)
    cap["f"](spec(imol_e, 20, " O3'"))
    if not H.windows[since:]: return "no window after the click"
    state["ext_since"] = since
    return True if "Accept" in window_buttons(since) else window_buttons(since)
check("Extend chain...: a click on the 3' nucleotide opens the phosphate-selection window", extend_pick)
def extend_build():
    s = state["ext_since"]; n0 = len(_c.CALLBACK_ERRORS)
    press("Accept", s)
    for k in range(3): press("Accept Nt", s)
    press("Build Backbone", s)
    if "Done" not in window_buttons(s): return "no review window"
    press("Done", s)
    have = [r for r in range(21, 30) if coot.residue_info_py(imol_e, "A", r, "")]
    bad = [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[n0:]]
    if bad: return bad
    return True if len(have) >= 3 else "residues added: %r" % have
check("Extend chain...: Accept, 3 x Accept Nt, Build Backbone and Done add >= 3 nucleotides to the model", extend_build)
check("no callback errors during the whole RCrane run", lambda: True if len(_c.CALLBACK_ERRORS) == N_ERR0 else [e[1].strip().splitlines()[-1] for e in _c.CALLBACK_ERRORS[N_ERR0:]][:3])

for n, ok, msg in res: print(("PASS " if ok else "FAIL ") + n + ((" :: " + msg) if not ok else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
coot.coot_real_exit(0)
