#!/usr/bin/env python3
"""selftest.py -- tests of the PyGTK 2 compatibility layer against the real GTK 2 libraries, without a display.
Each case runs in its own subprocess (a crash is reported as a failure of that case only).

  COOT_GTK2_LIBDIR=<dir with libgtk-quartz-2.0.0.dylib ...>  python selftest.py [case ...]
(inside a Coot bundle COOT_PREFIX is used instead.)  COOT_GTK2COMPAT_HEADLESS=1 is set so that nothing is shown (there is no window server).
"""
import os, sys, subprocess, traceback, glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
CASES = {}
def case(f): CASES[f.__name__] = f; return f
def eq(a, b, what=""):
    assert a == b, "%s: %r != %r" % (what, a, b)

@case
def imports_and_constants():
    import pygtk; pygtk.require("2.0")
    import gtk, gobject, pango
    import gtk.gdk, gtk.keysyms
    eq(gtk.WINDOW_TOPLEVEL, 0); eq(gtk.POLICY_AUTOMATIC, 1); eq(gtk.POLICY_ALWAYS, 0); eq(gtk.STOCK_YES, "gtk-yes")
    eq(gtk.gdk.CONTROL_MASK, 4); eq(gtk.keysyms.Up, 65362); eq(pango.WEIGHT_BOLD, 700); eq(gobject.TYPE_STRING, 64)
    assert gtk.pygtk_version >= (2, 12); eq(gtk.RESPONSE_ACCEPT, -3); eq(gtk.ASSISTANT_PAGE_CONFIRM, 2)

@case
def boxes_buttons_labels_entries():
    import gtk
    w = gtk.Window(gtk.WINDOW_TOPLEVEL); w.set_title("t"); eq(w.get_title(), "t")
    w2 = gtk.Window(); w2.set_default_size(100, 50)
    vb = gtk.VBox(False, 3); hb = gtk.HBox(False, 0)
    b1 = gtk.Button("_One"); b2 = gtk.Button("Two"); lab = gtk.Label("lbl"); en = gtk.Entry(); sep = gtk.HSeparator()
    hb.pack_start(b1, False, False, 2); hb.pack_start(b2); hb.pack_end(lab, True, True, 0)
    vb.pack_start(hb, False, False, 5); vb.pack_start(en, True, True, 0); vb.pack_start(sep, False, False, 2)
    w.add(vb); w.set_border_width(4)
    ch = hb.get_children(); eq(len(ch), 3); eq([type(c).__name__ for c in ch], ["Button", "Button", "Label"])
    assert ch[0] is b1, "same Python wrapper expected for the same widget"
    eq(b1.get_label(), "_One"); b2.set_label("Zwei"); eq(b2.get_label(), "Zwei")
    eq(lab.get_text(), "lbl"); lab.set_text("neu"); eq(lab.get_text(), "neu"); lab.set_line_wrap(True); lab.set_alignment(0.0, 0.5)
    en.set_text("hello"); eq(en.get_text(), "hello"); en.set_editable(False); en2 = gtk.Entry(max=5); eq(en2.get_max_length(), 5)
    eq(w.get_children()[0], vb); eq(vb.get_parent(), w)
    b1.set_sensitive(False); eq(b1.get_sensitive(), False); b1.set_size_request(40, 20)
    sb = gtk.Button(stock=gtk.STOCK_OK); assert sb.get_label() == "gtk-ok"
    fr = gtk.Frame("f"); eq(fr.get_label(), "f"); fr2 = gtk.Frame(label="g"); eq(fr2.get_label(), "g"); fr.add(gtk.Label("in"))
    sw = gtk.ScrolledWindow(); sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS); sw.add_with_viewport(gtk.VBox())
    eq(sw.get_policy(), (1, 0))
    t = gtk.Table(2, 3, False); t.attach(gtk.Label("a"), 0, 1, 0, 1); t.attach(gtk.Label("b"), 1, 2, 0, 1, gtk.EXPAND, gtk.FILL, 2, 2)
    eq(len(t.get_children()), 2)
    eq([type(c).__name__ for c in t], ["Label", "Label"]); eq(len(list(hb)), 3)   # PyGTK 2 Container iteration (glyco dialog: "for c in table")
    vb.destroy()

@case
def toggles_and_radios():
    import gtk
    cb = gtk.CheckButton("chk"); eq(cb.get_active(), False); cb.set_active(True); eq(cb.get_active(), True); eq(cb.get_label(), "chk")
    r1 = gtk.RadioButton(None, "a"); r2 = gtk.RadioButton(r1, "b"); r1.set_active(True)
    eq(r1.get_active(), True); eq(r2.get_active(), False); r2.set_active(True); eq(r1.get_active(), False)
    eq(len(r1.get_group()), 2)
    tb = gtk.ToggleButton("t"); tb.set_active(True); eq(tb.get_active(), True)

@case
def signals():
    import gtk
    b = gtk.Button("x"); calls = []
    hid = b.connect("clicked", lambda w, *a: calls.append((w, a)), "u1", 2)
    b.emit("clicked"); eq(len(calls), 1); assert calls[0][0] is b; eq(calls[0][1], ("u1", 2))
    b.handler_block(hid); b.emit("clicked"); eq(len(calls), 1); b.handler_unblock(hid); b.emit("clicked"); eq(len(calls), 2)
    b.disconnect(hid); b.emit("clicked"); eq(len(calls), 2)
    cb = gtk.CheckButton("c"); st = []
    cb.connect("toggled", lambda w: st.append(w.get_active())); cb.set_active(True); cb.set_active(False); eq(st, [True, False])
    w = gtk.Window(); seen = []
    w.connect("delete_event", lambda win, ev: seen.append(("del", ev is not None)) or True)
    r = w.emit("delete-event", None) if False else None
    adj = gtk.Adjustment(1.0, 0.0, 10.0, 1.0, 2.0, 0.0); vals = []
    adj.connect("value_changed", lambda a: vals.append(a.get_value())); adj.set_value(4.5); eq(vals, [4.5])
    e = gtk.Entry(); ch = []; e.connect("changed", lambda w: ch.append(w.get_text())); e.set_text("ab"); eq(ch[-1], "ab")
    mi = gtk.MenuItem("m"); act = []; mi.connect("activate", lambda w: act.append(1)); mi.activate(); eq(act, [1])
    # an exception in a callback is printed, not propagated
    b2 = gtk.Button("y"); b2.connect("clicked", lambda w: 1 / 0); b2.emit("clicked")
    # connect_object passes the object last
    got = []; b3 = gtk.Button("z"); o = gtk.Label("obj"); b3.connect_object("clicked", lambda *a: got.append(a), o); b3.emit("clicked")
    eq(len(got[0]), 2); eq(got[0][0], o); eq(got[0][1], b3)
    try: b.connect("no_such_signal", lambda w: None); raise AssertionError("expected TypeError")
    except TypeError: pass

@case
def text_buffers():
    import gtk, pango
    tv = gtk.TextView(); buf = tv.get_buffer(); eq(type(buf).__name__, "TextBuffer")
    tv.set_editable(False); tv.set_wrap_mode(gtk.WRAP_WORD_CHAR); tv.set_cursor_visible(False)
    buf.set_text("hello world"); start, end = buf.get_bounds(); eq(buf.get_text(start, end), "hello world")
    end = buf.get_end_iter(); eq(end.get_offset(), 11)
    tag = buf.create_tag(foreground="red", weight=pango.WEIGHT_BOLD); assert tag is not None
    buf.insert_with_tags(end, " bold", tag); eq(buf.get_text(*buf.get_bounds()), "hello world bold")
    buf.create_tag("blue", foreground="blue"); e2 = buf.get_end_iter(); buf.insert_with_tags_by_name(e2, " BLUE", "blue")
    eq(buf.get_text(buf.get_start_iter(), buf.get_end_iter()), "hello world bold BLUE")
    it = buf.get_iter_at_offset(6); eq(it.get_offset(), 6); eq(it.get_char(), "w")
    buf.apply_tag(tag, buf.get_iter_at_offset(0), it)
    buf.place_cursor(buf.get_end_iter()); mark = buf.get_insert(); assert mark is not None
    tv.scroll_mark_onscreen(mark)
    tv2 = gtk.TextView(); tv2.set_size_request(100, 50)

@case
def list_stores_and_combos():
    import gtk, gobject
    ls = gtk.ListStore(gobject.TYPE_STRING); eq(len(ls), 0)
    for s in ("b", "a", "c"): ls.append([s])
    eq(len(ls), 3); eq(ls[1][0], "a"); eq([r[0] for r in ls], ["b", "a", "c"])
    ls.set_sort_column_id(0, gtk.SORT_ASCENDING); eq([r[0] for r in ls], ["a", "b", "c"])
    it = ls.get_iter(2); eq(ls.get_value(it, 0), "c"); eq(ls.get(it, 0), ("c",))
    ls3 = gtk.ListStore(gtk.gdk.Pixbuf, str, str)
    ls3.append([None, "icon.svg", "/x/icon.svg"]); ls3.append([None, "stock", None])
    eq(len(ls3), 2); eq(ls3.get(ls3.get_iter(0), 0, 1, 2), (None, "icon.svg", "/x/icon.svg")); eq(ls3.get(ls3.get_iter(1), 1, 2), ("stock", None))
    li = gtk.ListStore(int, float, bool); li.append([3, 2.5, True]); eq(li.get(li.get_iter(0), 0, 1, 2), (3, 2.5, True))
    cb = gtk.combo_box_new_text()
    for t in ("one", "two", "three"): cb.append_text(t)
    eq(cb.get_active(), -1); cb.set_active(1); eq(cb.get_active(), 1); eq(cb.get_active_text(), "two")
    m = cb.get_model(); eq(len(m), 3); eq(m[2][0], "three")
    it = cb.get_active_iter(); eq(m.get_value(it, 0), "two")
    cb.set_active_iter(m.get_iter(2)); eq(cb.get_active_text(), "three")
    cb2 = gtk.ComboBox(); cb2.set_wrap_width(10); cb2.set_model(ls3); crpx = gtk.CellRendererPixbuf(); cb2.pack_start(crpx, False); cb2.add_attribute(crpx, "pixbuf", 0)
    eq(cb2.get_active_iter(), None)
    comp = gtk.EntryCompletion(); comp.set_model(ls); comp.set_text_column(0); e = gtk.Entry(); e.set_completion(comp)

@case
def tree_views():
    """TreeView / TreeViewColumn / TreeSelection / CellRendererText properties / ListStore GType names (RCrane's review window needs all of them)."""
    import gtk, pango, _gtk2core as _c
    n_errors = len(_c.CALLBACK_ERRORS)
    ls = gtk.ListStore(str, str, 'gboolean', int)                       # GType names are accepted as in PyGTK
    for row in (["a", "1.00", True, 5], ["b", "2.00", False, 6], ["c", "3.00", False, 7]): ls.append(row)
    eq(len(ls), 3); eq(ls[0][2], True); eq(ls[1][3], 6); eq(ls.get_path(ls.get_iter(2)), (2,)); eq(ls.get_path(ls.get_iter((1,))), (1,))
    win = gtk.Window()
    bg = win.get_style().bg[gtk.STATE_NORMAL]
    assert isinstance(bg, gtk.gdk.Color) and (bg.red or bg.green or bg.blue), bg           # a real colour out of the GtkStyle struct
    tv = gtk.TreeView(ls); tv.set_enable_search(False); tv.set_headers_visible(True); tv.set_grid_lines(gtk.TREE_VIEW_GRID_LINES_VERTICAL)
    r1 = gtk.CellRendererText(); r1.set_property("xalign", 0.5); r1.set_property("cell-background-gdk", bg); r1.set_property("cell-background", "red")
    r1.set_property("weight", pango.WEIGHT_HEAVY); r1.set_property("width-chars", 8); r1.set_property("height", 20); r1.set_property("cell-background", None)
    col1 = gtk.TreeViewColumn("Name", r1, text=0, cell_background_set=2); col1.set_expand(True)
    eq(tv.append_column(col1), 1); eq(col1.get_title(), "Name"); assert tv.get_column(0) is col1 and tv.get_columns() == [col1]
    eq(col1.get_cell_renderers(), [r1])
    r2 = gtk.CellRendererText(); col2 = gtk.TreeViewColumn("Score", r2, markup=1)
    seen = []
    def cdf(column, cell, model, it, data):
        seen.append((column is col2, cell is r2, model is ls, model.get_value(it, 0), data))
        cell.set_property("cell-background", "red" if model.get_value(it, 2) else None)
    col2.set_cell_data_func(r2, cdf, (2, 3)); tv.append_column(col2)
    _c.call("gtk_tree_view_column_cell_set_cell_data", col2, ls, ls.get_iter(0), False, False)        # what GTK does for every row it draws
    eq(seen, [(True, True, True, "a", (2, 3))]); eq(r2.get_property("cell-background-set"), True)
    _c.call("gtk_tree_view_column_cell_set_cell_data", col2, ls, ls.get_iter(1), False, False); eq(r2.get_property("cell-background-set"), False)
    eq(_c.CALLBACK_ERRORS[n_errors:], [])
    col2.set_cell_data_func(r2, None)
    sel = tv.get_selection(); assert isinstance(sel, gtk.TreeSelection)
    eq(sel.get_selected()[1], None)
    sel.select_iter(ls.get_iter(1)); model, it = sel.get_selected()
    assert model is ls and model.get_path(it) == (1,) and model.get_value(it, 0) == "b"
    eq(sel.get_selected_rows()[1], [(1,)]); assert sel.get_tree_view() is tv
    ch = []; hid = sel.connect("changed", lambda s: ch.append(s.get_selected()[1] is not None))
    sel.select_iter(ls.get_iter(2)); eq(ch, [True]); sel.disconnect(hid); sel.select_iter(ls.get_iter(0)); eq(ch, [True])
    sel.set_mode(gtk.SELECTION_NONE); eq(sel.get_mode(), gtk.SELECTION_NONE)
    assert tv.get_model() is ls; tv.set_model(None); eq(tv.get_model(), None); tv.set_model(ls)
    tv.scroll_to_cell((1,), None, True, 0.5, 0.0); tv.set_cursor((2,)); eq(tv.get_cursor()[0], (2,)); eq(tv.get_path_at_pos(5, 5), None)      # not realised: nothing under the pointer
    cs = col1.cell_get_size(); eq(len(cs), 5); assert all(isinstance(v, int) for v in cs[1:]) and cs[4] >= 0, cs
    w, h = tv.size_request(); assert w >= 0 and h >= 0
    eq(tv.style_get_property("vertical-separator"), 2)
    sw = gtk.ScrolledWindow(); sw.add(tv); sw.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
    eq(sw.style_get_property("scrollbar-spacing"), 3); assert sw.get_vscrollbar().size_request()[0] > 0 and gtk.VScrollbar().size_request()[0] > 0
    assert gtk.HScrollbar().size_request()[1] > 0 and sw.get_hscrollbar() is not None
    try: tv.style_get_property("no-such-style-property"); raise AssertionError("no TypeError")
    except TypeError: pass
    hb = gtk.HBox(False, 0); b = gtk.Button("x"); hb.pack_start(b, True, False, 7)
    eq(hb.query_child_packing(b)[:3], (True, False, 7))
    overview = gtk.ListStore(*([str] * 4)); overview.append(["1", "2", "3", "4"]); eq(len(overview[0]), 4)
    changed = []; hid2 = ls.connect("row-changed", lambda m, path, it: changed.append(path))
    ls.row_changed((1,), ls.get_iter((1,))); eq(len(changed), 1); ls.row_changed(0, ls.get_iter(0)); eq(len(changed), 2); ls.disconnect(hid2)

@case
def menus_toolbars():
    import gtk
    menu = gtk.Menu(); mb = gtk.MenuBar(); top = gtk.MenuItem("File")
    for l in ("A", "B", "C"): menu.append(gtk.MenuItem(l))
    menu.append(gtk.SeparatorMenuItem()); top.set_submenu(menu); mb.append(top)
    eq(len(menu.get_children()), 4); eq(len(mb.get_children()), 1); eq(top.get_submenu(), menu)
    eq(mb.get_children()[0].get_label(), "File")
    tb = gtk.Toolbar(); eq(len(tb.get_children()), 0)
    b1 = gtk.ToolButton(icon_widget=gtk.image_new_from_stock(gtk.STOCK_OPEN, gtk.ICON_SIZE_SMALL_TOOLBAR), label="Open")
    b2 = gtk.ToggleToolButton(); b2.set_label("tog"); sep = gtk.SeparatorToolItem(); ti = gtk.ToolItem()
    for it in (b1, b2, sep, ti): tb.insert(it, -1)
    ch = tb.get_children(); eq(len(ch), 4); assert ch[0] is b1
    b2.set_active(True); eq(b2.get_active(), True)
    tb.set_style(gtk.TOOLBAR_ICONS); tb.set_style(gtk.TOOLBAR_BOTH_HORIZ)
    b1.set_tooltip_text("tip"); b1.set_is_important(True)
    img = gtk.image_new_from_stock("gtk-ok", gtk.ICON_SIZE_MENU); eq(type(img).__name__, "Image")
    tips = gtk.Tooltips(); tips.set_tip(b1, "a tip", None)

@case
def sliders_progress_notebook_assistant():
    import gtk
    pb = gtk.ProgressBar(); pb.set_fraction(0.25); eq(round(pb.get_fraction(), 3), 0.25); pb.set_text("x"); pb.pulse()
    adj = gtk.Adjustment(5.0, 0.0, 10.0, 1.0, 2.0, 0.0); sc = gtk.HScale(adj); sc.set_digits(1); eq(sc.get_value(), 5.0); sc.set_value(7.0); eq(adj.get_value(), 7.0)
    sp = gtk.SpinButton(gtk.Adjustment(1, 0, 100, 1, 10, 0), 1.0, 0); eq(sp.get_value(), 1.0); sp.set_value(3); eq(sp.get_value_as_int(), 3)
    nb = gtk.Notebook(); nb.append_page(gtk.Label("page"), gtk.Label("tab")); eq(nb.get_n_pages(), 1)
    asst = gtk.Assistant(); pg = gtk.VBox(); asst.append_page(pg); asst.set_page_type(pg, gtk.ASSISTANT_PAGE_CONTENT); asst.set_page_title(pg, "T")
    asst.set_page_complete(pg, True); eq(asst.get_page_complete(pg), True); eq(asst.get_n_pages(), 1)
    for s in ("close", "cancel", "apply"): asst.connect(s, lambda *a: None)
    da = gtk.DrawingArea(); da.set_size_request(10, 10); da.connect("expose-event", lambda w, e: True)

@case
def dialogs():
    import gtk
    w = gtk.Window()
    d = gtk.Dialog("Title", w, gtk.DIALOG_MODAL | gtk.DIALOG_NO_SEPARATOR, (gtk.STOCK_YES, gtk.RESPONSE_ACCEPT, gtk.STOCK_NO, gtk.RESPONSE_REJECT))
    eq(d.get_title(), "Title"); assert d.vbox is not None; eq(len(d.action_area.get_children()), 2); d.vbox.pack_end(gtk.Label("q"), True, True, 0)
    md = gtk.MessageDialog(type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK); md.set_markup("<b>hi</b>")
    md2 = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, "plain 100% & <text>")
    fc = gtk.FileChooserDialog("Open", None, gtk.FILE_CHOOSER_ACTION_OPEN, (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    fc.set_default_response(gtk.RESPONSE_OK)
    fs = gtk.FileSelection("file selection"); fs.ok_button.connect("clicked", lambda *a: None); fs.cancel_button.connect("clicked", lambda w: None)
    res = []; d.connect("response", lambda dlg, rid: res.append(rid)); d.response(gtk.RESPONSE_ACCEPT); eq(res, [gtk.RESPONSE_ACCEPT])

@case
def gdk_and_pango():
    import gtk, pango
    c = gtk.gdk.color_parse("#ff8000"); eq((c.red, c.green, c.blue), (65535, 32896, 0)); c2 = gtk.gdk.Color(red=1, green=2, blue=3); eq((c2.red, c2.green, c2.blue), (1, 2, 3))
    try: gtk.gdk.color_parse("not-a-colour"); raise AssertionError("expected ValueError")
    except ValueError: pass
    eq(gtk.gdk.keyval_from_name("Up"), gtk.keysyms.Up); eq(gtk.gdk.unicode_to_keyval("a"), 97)
    fd = pango.FontDescription("Sans Bold 10"); eq(fd.get_size() // pango.SCALE, 10); eq(fd.get_weight(), pango.WEIGHT_BOLD); assert "Bold" in str(fd)
    lab = gtk.Label("x"); lab.modify_font(fd)
    e = gtk.Entry(); e.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse("#bfe6bf"))
    gtk.gdk.Font("fixed")          # created and ignored by Coot's scripts; must not raise on GDK-Quartz
    # pixbufs
    pngs = glob.glob(os.path.join(os.environ.get("COOT_TEST_PIXMAPS", ""), "*.png")) if os.environ.get("COOT_TEST_PIXMAPS") else []
    if pngs:
        pb = gtk.gdk.pixbuf_new_from_file(pngs[0]); assert pb.get_width() > 0
        small = gtk.gdk.pixbuf_new_from_file_at_size(pngs[0], 16, 16); assert small.get_width() <= 16
    try: gtk.gdk.pixbuf_new_from_file("/no/such/file.png"); raise AssertionError("expected GError")
    except gtk.GError: pass
    th = gtk.icon_theme_get_default()     # None without a screen (headless); checked in the real GUI by gui_python_smoke.py
    ids = gtk.stock_list_ids(); assert len(ids) > 50 and all(isinstance(i, str) for i in ids) and "gtk-ok" in ids
    f = gtk.IconFactory(); f.add_default()

@case
def gobject_sources_and_errors():
    import gtk, gobject, ctypes
    import _gtk2core as c
    hits = []; idles = []
    def tick(*a): hits.append(a); return len(hits) < 3
    sid = gobject.timeout_add(1, tick, "x", 1)
    iid = gobject.idle_add(lambda *a: idles.append(a) and False, "i")
    import time
    for _ in range(3000):
        c.call("g_main_context_iteration", None, False)
        if len(hits) >= 3 and idles: break
        time.sleep(0.001)
    eq(hits, [("x", 1)] * 3)            # the timeout fired three times and removed itself when the callback returned False
    eq(idles, [("i",)])
    sid2 = gobject.timeout_add(100000, lambda: True); assert gobject.source_remove(sid2)
    try: c.call("gtk_list_store_new", 1, 64, 64); raise AssertionError("variadic call with extra arguments must be refused")
    except TypeError: pass
    b = gtk.Button("p"); b.set_property("label", "via property"); eq(b.get_property("label"), "via property")
    b.set_name("nm"); eq(b.get_name(), "nm")
    try: b.no_such_method(); raise AssertionError("expected AttributeError")
    except AttributeError: pass

def run_case(name):
    env = dict(os.environ, COOT_GTK2COMPAT_HEADLESS="1", PYTHONPATH=os.path.dirname(HERE) + os.pathsep + os.environ.get("PYTHONPATH", ""))
    r = subprocess.run([sys.executable, os.path.abspath(__file__), "--case", name], capture_output=True, text=True, env=env, timeout=120)
    ok = r.returncode == 0 and "CASE-OK" in r.stdout
    return ok, (r.stdout + r.stderr).strip()

def run_inprocess(names=None):
    """For use inside Coot's embedded Python (tests/gtk2compat_python.py): no subprocess isolation."""
    os.environ["COOT_GTK2COMPAT_HEADLESS"] = "1"
    results = []
    for n in names or list(CASES):
        try: CASES[n](); results.append((n, True, ""))
        except BaseException: results.append((n, False, traceback.format_exc()[-600:]))
    return results

if __name__ == "__main__" and not os.environ.get("COOT_SELFTEST_NO_MAIN"):
    if len(sys.argv) > 2 and sys.argv[1] == "--case":
        try:
            CASES[sys.argv[2]](); print("CASE-OK")
        except BaseException:
            traceback.print_exc(); sys.exit(1)
        sys.exit(0)
    names = sys.argv[1:] or list(CASES)
    npass = 0
    for n in names:
        ok, out = run_case(n)
        print(("PASS " if ok else "FAIL ") + n)
        if not ok: print("    " + out.replace("\n", "\n    ")[-1500:])
        npass += ok
    print("SUMMARY", npass, "/", len(names), flush=True)
    sys.exit(0 if npass == len(names) else 1)
