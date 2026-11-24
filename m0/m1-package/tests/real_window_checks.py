# real_window_checks.py  (build 28) -- needs a real window (not --no-graphics): run with tests/run-real-window-checks.sh
# 1. keys:
# Sends key events to the graphics window through GTK, so they go through Coot's own C++ key handler (globjects.cc
# key_press_event / key_release_event), then Scheme's graphics-general-key-press-hook, then Python's hook.
# User report 20 Nov: a Python "Control_t" binding did not run on Ctrl-T; recipe 6.3's key "o" is Coot's own (next NCS chain).
# 2. the Help menu (user request 20 Nov) on the real menus: last menu, finds entries, the search window opens.
import ctypes, os, sys
OUT = os.environ.get("KEYTEST_OUT")
res = []
def check(name, ok, info=""):
    res.append((name, ok is True, "" if ok is True else (info or str(ok))))
g = ctypes.PyDLL(None)
P = ctypes.c_void_p
def fn(n, r, a):
    f = getattr(g, n); f.restype = r; f.argtypes = a; return f
list_toplevels = fn("gtk_window_list_toplevels", P, [])
list_len = fn("g_list_length", ctypes.c_uint, [P]); list_nth = fn("g_list_nth_data", P, [P, ctypes.c_uint])
children = fn("gtk_container_get_children", P, [P]); tname = fn("g_type_name_from_instance", ctypes.c_char_p, [P])
title = fn("gtk_window_get_title", ctypes.c_char_p, [P]); is_container = fn("g_type_check_instance_is_a", ctypes.c_int, [P, ctypes.c_size_t])
container_type = fn("gtk_container_get_type", ctypes.c_size_t, [])
widget_window = fn("gtk_widget_get_window", P, [P]); widget_event = fn("gtk_widget_event", ctypes.c_int, [P, P])
event_new = fn("gdk_event_new", P, [ctypes.c_int]); event_free = fn("gdk_event_free", None, [P])
g_object_ref = fn("g_object_ref", P, [P])
class GdkEventKey(ctypes.Structure):
    _fields_ = [("type", ctypes.c_int), ("window", P), ("send_event", ctypes.c_int8), ("time", ctypes.c_uint32),
                ("state", ctypes.c_uint), ("keyval", ctypes.c_uint), ("length", ctypes.c_int), ("string", ctypes.c_char_p),
                ("hardware_keycode", ctypes.c_uint16), ("group", ctypes.c_uint8), ("is_modifier", ctypes.c_uint8)]
def kids(w):
    if not is_container(w, container_type()): return []
    l = children(w)
    return [list_nth(l, i) for i in range(list_len(l))] if l else []
def find(w, typename, acc):
    if tname(w) == typename: acc.append(w)
    for c in kids(w): find(c, typename, acc)
    return acc
def graphics_widgets():
    tl = list_toplevels(); found = []
    for i in range(list_len(tl)):
        w = list_nth(tl, i)
        t = title(w)
        if t and t.startswith(b"Coot"):
            found += find(w, b"GtkDrawingArea", [])
    return found
CTRL = 1 << 2
def send(widget, keyval, press, state=0):
    ev = event_new(8 if press else 9)            # GDK_KEY_PRESS / GDK_KEY_RELEASE
    k = ctypes.cast(ev, ctypes.POINTER(GdkEventKey)).contents
    k.window = g_object_ref(widget_window(widget)); k.send_event = 1; k.state = state; k.keyval = keyval
    k.is_modifier = 1 if keyval in (0xffe3, 0xffe4) else 0
    widget_event(widget, ev); event_free(ev)
def tap(widget, keyval, ctrl=False):
    if ctrl: send(widget, 0xffe3, True)                                   # Control_L down
    send(widget, keyval, True, CTRL if ctrl else 0); send(widget, keyval, False, CTRL if ctrl else 0)
    if ctrl: send(widget, 0xffe3, False, CTRL)                            # Control_L up
fired = []
def run(step=[0]):
    try:
        ws = graphics_widgets()
        if not ws:
            check("the graphics window was found", False, "no GtkDrawingArea in a 'Coot' window"); return finish()
        # the drawing area that has Coot's key handler: the one whose events reach the hook
        before = list(fired)
        add_key_binding("coot0 test v", "v", lambda: fired.append("v"))
        add_key_binding("coot0 test Ctrl-T", "Control_t", lambda: fired.append("ctrl-t"))
        target = None
        for w in ws:
            tap(w, ord("v"))
            if fired and fired[-1] == "v": target = w; break
        check("a plain key bound in Python runs when pressed (v)", target is not None, "no drawing area passed 'v' on: %d tried" % len(ws))
        if target is None: return finish()
        del fired[:]
        tap(target, ord("t"), ctrl=True)
        check("Ctrl-T runs the Python binding made with \"Control_t\"", fired == ["ctrl-t"] or "fired: %r" % fired)
        del fired[:]
        tap(target, ord("t"))
        check("plain t does not run the Ctrl-T binding", fired == [] or "fired: %r" % fired)
        del fired[:]
        add_key_binding("coot0 test o", "o", lambda: fired.append("o"))
        tap(target, ord("o"))
        check("o is Coot's own key (next NCS chain): a binding to it does not run", fired == [] or "fired: %r" % fired)
        # --- Help menu on the real menu bar
        import coot_python
        mb = coot_python.main_menubar()
        names = [coot0_menu_label(i) for i in mb.get_children()]
        check("Help is the last menu", names[-1] == "Help" or "menus: %r" % names)
        ents = coot0_menu_entries()
        check("Help search sees the menu entries (more than 150)", len(ents) > 150 or "%d entries" % len(ents))
        hidden = [p for p, it in ents if not it.get_visible()]
        check("no hidden (removed) entry is offered", not hidden or hidden[:5])
        r = [x[1] for x in coot0_help_search("brighten") if x[0] == "Menu"]
        check("search 'brighten' finds Brighten Maps", any(x.endswith("Brighten Maps") for x in r) or r)
        w = coot0_search_window()
        win, entry, store, view, state = coot0_search_window_widget
        entry.set_text("refine")
        n = len(store)
        while gtk.events_pending(): gtk.main_iteration()
        mapped = fn("gtk_widget_get_mapped", ctypes.c_int, [P])(win._ptr)
        check("the search window opens on screen and lists results for 'refine'", (mapped == 1 and n > 20) or "mapped %r, %d rows" % (mapped, n))
        # (build 29) Enter through GTK, the page served by Coot (main-loop server), fetched while the real main loop runs
        opened = []
        real_open = coot0_open_url
        globals()["coot0_open_url"] = lambda t: opened.append(t) or t
        entry.set_text("sphere refine")
        fn("gtk_widget_activate", ctypes.c_int, [P])(entry._ptr)
        globals()["coot0_open_url"] = real_open
        url = opened[-1] if opened else ""
        got = []
        import threading, urllib.request, time
        def get():
            try: got.append(urllib.request.urlopen(url, timeout=5).read().decode("utf-8"))
            except Exception as e: got.append("ERR %r" % e)
        threading.Thread(target=get).start()
        t0 = time.time()
        while not got and time.time() - t0 < 10:
            while gtk.events_pending(): gtk.main_iteration()
            time.sleep(0.02)
        anchor = url.partition("#")[2]
        check("Enter opens cookbook 4.3, served by Coot with its heading",
              (url.startswith("http://127.0.0.1:") and got and ('id="%s"' % anchor) in got[0]) or "url %r, got %r" % (url, (got or ["nothing"])[0][:80]))
        try: win.destroy()
        except Exception: pass
        sid = fn("g_signal_lookup", ctypes.c_uint, [ctypes.c_char_p, ctypes.c_size_t])(b"activate", fn("gtk_menu_item_get_type", ctypes.c_size_t, [])())
        pending = fn("g_signal_has_handler_pending", ctypes.c_int, [P, ctypes.c_uint, ctypes.c_uint32, ctypes.c_int])
        help_menu = mb.get_children()[-1].get_submenu()
        own = [(coot0_menu_label(i), pending(i._ptr, sid, 0, 1)) for i in help_menu.get_children() if coot0_menu_label(i) in ("Header/Remarks Browser...", "Hints...", "About...")]
        check("Coot's own Help entries (Header/Remarks Browser, Hints, About) keep their handlers", (len(own) == 3 and all(h for n, h in own)) or own)
        kw = coot0_keys_window()
        check("the Keyboard Shortcuts window opens", fn("gtk_widget_get_mapped", ctypes.c_int, [P])(kw._ptr) == 1 or "not mapped")
        kw.destroy()
        label_checks()
    except Exception as e:
        import traceback; check("no exception", False, traceback.format_exc()[-400:])
    finish()
# 3. (build 37) scene text after the 3D view is re-created.  Side-by-side stereo (and going back to mono) makes new 3D views;
# build 36 still used the label pictures (textures) of the old view and drew every label as a filled box.  A text label is
# placed at the centre of an empty scene, the view is saved as an image (screendump_image reads Coot's own GL buffer, not the
# screen), and the lit pixels around the label must look like text (a box fills its whole rectangle).
def pump(n=30):
    import time
    for i in range(n):
        while gtk.events_pending(): gtk.main_iteration()
        time.sleep(0.02)
def lit_fill(ppm):
    data = open(ppm, "rb").read()
    toks, pos = [], 0                           # P6 [# comments] width height maxval, one whitespace byte, then the pixels
    while len(toks) < 4:
        while data[pos:pos + 1].isspace(): pos += 1
        if data[pos:pos + 1] == b"#":
            pos = data.index(b"\n", pos) + 1; continue
        e = pos
        while not data[e:e + 1].isspace(): e += 1
        toks.append(data[pos:e]); pos = e
    w, h = int(toks[1]), int(toks[2]); px = data[pos + 1:]
    lit = [(i % w, i // w) for i in range(w * h) if max(px[3 * i], px[3 * i + 1], px[3 * i + 2]) > 100]
    if not lit: return None, 0
    xs = [x for x, y in lit]; ys = [y for x, y in lit]
    area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
    return len(lit) / float(area), len(lit)
def label_checks():
    import tempfile
    d = tempfile.mkdtemp()
    set_draw_axes(0)
    set_rotation_centre_size(0.0)
    set_rotation_centre(0.0, 0.0, 0.0)
    place_text("MMMWWWMMM", 0.0, 0.0, 0.0, 1)
    results = []
    for mode in ("mono", "side-by-side stereo", "mono again"):
        if mode == "side-by-side stereo": side_by_side_stereo_mode(0)
        if mode == "mono again": mono_mode()
        pump(); graphics_draw(); pump(10)
        f = os.path.join(d, mode.replace(" ", "-") + ".ppm")
        screendump_image(f)
        fill, n = lit_fill(f) if os.path.exists(f) else (None, 0)
        results.append((mode, fill, n))
    ok = all(fill is not None and n > 20 and fill < 0.75 for mode, fill, n in results)
    check("text labels stay text after the 3D view is re-created (mono, side-by-side stereo, mono again)",
          ok or "lit-pixel fill of the label area (a box is ~1.0): %r" % [(m, None if f is None else round(f, 2), n) for m, f, n in results])

def finish():
    lines = [("PASS " if ok else "FAIL ") + n + (("  " + v) if v else "") for n, ok, v in res]
    lines.append("SUMMARY %d / %d" % (sum(1 for r in res if r[1]), len(res)))
    txt = "\n".join(lines) + "\n"
    print(txt)
    if OUT: open(OUT, "w").write(txt)
    coot_real_exit(0)
    return False
import gobject, gtk
gobject.timeout_add(2500, run)
