#!/usr/bin/env python3
"""gen_gtk_consts.py -- extract GTK_*/GDK_*/PANGO_* enum constants and simple #define values (stock ids, key symbols, ...) from the GTK 2 headers.
Enumerator values are evaluated by compiling and running a tiny C program (the AST has no value for enumerators without an initialiser).
usage: gen_gtk_consts.py <env-prefix> <out.json>"""
import sys, os, re, json, subprocess, tempfile
prefix, out = sys.argv[1], sys.argv[2]
env = dict(os.environ, PKG_CONFIG_PATH=f"{prefix}/lib/pkgconfig:{prefix}/share/pkgconfig")
cflags = subprocess.run("pkg-config --cflags gtk+-2.0 gdk-pixbuf-2.0 pango", shell=True, capture_output=True, text=True, env=env).stdout.split()
HEAD = "#include <gtk/gtk.h>\n#include <gdk/gdkkeysyms.h>\n#include <gdk-pixbuf/gdk-pixbuf.h>\n#include <pango/pango.h>\n"
d = tempfile.mkdtemp(); src = os.path.join(d, "all.c"); open(src, "w").write(HEAD)
dec = json.JSONDecoder(); names = set()
for filt in ("GTK_", "GDK_", "PANGO_"):
    txt = subprocess.run(["clang", "-Xclang", "-ast-dump=json", "-Xclang", f"-ast-dump-filter={filt}", "-fsyntax-only", "-x", "c", src] + cflags, capture_output=True, text=True).stdout
    i = 0
    while True:
        j = txt.find("{", i)
        if j < 0: break
        try: o, end = dec.raw_decode(txt, j)
        except json.JSONDecodeError: i = j + 1; continue
        i = end
        if o.get("kind") == "EnumConstantDecl" and re.match(r"^(GTK|GDK|PANGO)_", o.get("name", "")): names.add(o["name"])
prog = HEAD + "#include <stdio.h>\nint main(void){\n" + "".join(f'printf("%s %lld\\n", "{n}", (long long){n});\n' for n in sorted(names)) + "return 0;}\n"
cp = os.path.join(d, "ev.c"); open(cp, "w").write(prog)
r = subprocess.run(["clang", "-w", "-o", os.path.join(d, "ev"), cp] + cflags + ["-Wl,-undefined,dynamic_lookup"], capture_output=True, text=True)
if r.returncode: sys.exit("evaluation program failed to compile: " + r.stderr[:500])
consts = {}
for line in subprocess.run([os.path.join(d, "ev")], capture_output=True, text=True).stdout.splitlines():
    n, v = line.split(); consts[n] = int(v)
# macros: string literals, integer literals, and aliases of those (GDK_Up -> GDK_KEY_Up -> 0xff52)
macros = {}
for line in subprocess.run(["clang", "-E", "-dM", "-x", "c", src] + cflags, capture_output=True, text=True).stdout.splitlines():
    m = re.match(r"#define\s+([A-Za-z_][A-Za-z0-9_]*)\s+(.*)$", line)
    if m and "(" not in m.group(1): macros[m.group(1)] = m.group(2).strip()
def resolve(v, depth=0):
    if depth > 6: return None
    s = re.fullmatch(r'"([^"]*)"', v)
    if s: return s.group(1)
    n = re.fullmatch(r"\(?(0[xX][0-9a-fA-F]+|\d+)[uUlL]*\)?", v)
    if n: return int(n.group(1), 0)
    if v in macros: return resolve(macros[v], depth + 1)
    m = re.fullmatch(r"\((\w+)\)", v)
    if m and m.group(1) in macros: return resolve(macros[m.group(1)], depth + 1)
    return None
for n, v in macros.items():
    if re.match(r"^(GTK|GDK|PANGO)_", n) and n not in consts:
        r_ = resolve(v)
        if r_ is not None: consts[n] = r_
json.dump(dict(sorted(consts.items())), open(out, "w"), separators=(",", ":"))
print(len(names), "enumerators,", len(consts), "constants ->", out, file=sys.stderr)
