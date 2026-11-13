#!/usr/bin/env python3
"""gen_gtk_protos.py -- extract the C prototypes of the GTK 2 / GDK / GObject / GLib / Pango / gdk-pixbuf functions with clang, as compact type codes.
usage: gen_gtk_protos.py <env-prefix> <out.json>      (needs clang and pkg-config; env-prefix = the conda env / bundle that has include/gtk-2.0)

Type codes: v void, i int32, u uint32, l int64, U uint64, d double, f float, b _Bool, h int16, H uint16, c int8, C uint8,
            p pointer ("p:GtkWidget" keeps the pointee's struct name), s const char* argument, S const char* return (borrowed),
            A char* return (caller must g_free), X by-value struct / unsupported.
Entry: name -> [return code, [argument codes], variadic(0/1), [parameter names]]
"""
import sys, os, re, json, subprocess
prefix, out = sys.argv[1], sys.argv[2]
env = dict(os.environ, PKG_CONFIG_PATH=f"{prefix}/lib/pkgconfig:{prefix}/share/pkgconfig")
cflags = subprocess.run("pkg-config --cflags gtk+-2.0 gdk-pixbuf-2.0 pango", shell=True, capture_output=True, text=True, env=env).stdout.split()
HEAD = "#include <gtk/gtk.h>\n#include <gdk-pixbuf/gdk-pixbuf.h>\n#include <pango/pango.h>\n"
src = "/tmp/_gtkall_protos.c"
open(src, "w").write(HEAD)
PTR_STRUCT = re.compile(r"(?:const\s+|volatile\s+)*(?:struct|union|enum)?\s*_?([A-Za-z0-9_]+)\s*\*")
BASE = {"void": "v", "int": "i", "unsigned int": "u", "long": "l", "unsigned long": "U", "long long": "l", "unsigned long long": "U",
        "double": "d", "float": "f", "_Bool": "b", "short": "h", "unsigned short": "H", "char": "c", "signed char": "c", "unsigned char": "C"}
def code(spelled, desugared, is_ret=False):
    s = re.sub(r"\s+", " ", (desugared or spelled).strip())
    if "*" in s or "[" in s or "(" in s:
        if re.fullmatch(r"const (char|gchar) \*( const)?", s): return "S" if is_ret else "s"
        if re.fullmatch(r"(char|gchar) \*", s): return "A" if is_ret else "p:char"
        m = PTR_STRUCT.search(spelled)
        tn = m.group(1) if m else ""
        return "p:" + tn if tn and tn not in ("void", "const") else "p"
    s = s.replace("const ", "").replace("volatile ", "").strip()
    if s in BASE: return BASE[s]
    if s.startswith("enum "): return "i"
    if re.fullmatch(r"[A-Z][A-Za-z0-9]+", s): return "i"   # typedef'd enum / flags (no by-value structs occur in this API subset; all 264 unknown names are enums)
    return "X"
dec = json.JSONDecoder()
def dump(filt, source):
    r = subprocess.run(["clang", "-Xclang", "-ast-dump=json", "-Xclang", f"-ast-dump-filter={filt}", "-fsyntax-only", "-x", "c", source] + cflags, capture_output=True, text=True)
    txt = r.stdout; i = 0
    while True:
        j = txt.find("{", i)
        if j < 0: return
        try: obj, end = dec.raw_decode(txt, j)
        except json.JSONDecodeError: i = j + 1; continue
        i = end
        if obj.get("kind") == "FunctionDecl" and obj.get("name"): yield obj
raw = {}
for f in ("gtk_", "gdk_", "pango_", "g_"):
    for obj in dump(f, src):
        name = obj["name"]
        if re.match(r"^(gtk|gdk|pango|g)_", name) and name not in raw: raw[name] = obj
# desugar the (non-pointer) return types through probe parameters
spell = sorted({o["type"]["qualType"][:o["type"]["qualType"].index("(")].strip() for o in raw.values() if "(" in o["type"]["qualType"]})
probe = HEAD + "".join(f"void __probe{i}({t} x);\n" for i, t in enumerate(spell) if t != "void")
open("/tmp/_gtkprobe.c", "w").write(probe)
dsug = {}
for obj in dump("__probe", "/tmp/_gtkprobe.c"):
    k = int(obj["name"][len("__probe"):]); p = [q for q in obj.get("inner", []) if q.get("kind") == "ParmVarDecl"]
    if p: dsug[spell[k]] = p[0]["type"].get("desugaredQualType")
protos = {}
for name, obj in raw.items():
    qt = obj["type"]["qualType"]
    variadic = qt.rstrip().endswith("...)")
    rs = qt[:qt.index("(")].strip() if "(" in qt else "int"
    ret = "v" if rs == "void" else code(rs, dsug.get(rs), True)
    parms = [p for p in obj.get("inner", []) if p.get("kind") == "ParmVarDecl"]
    args = [code(p["type"]["qualType"], p["type"].get("desugaredQualType")) for p in parms]
    protos[name] = [ret, args, 1 if variadic else 0, [p.get("name", "") for p in parms]]
json.dump(dict(sorted(protos.items())), open(out, "w"), separators=(",", ":"))
print(len(protos), "prototypes,", len(spell), "return spellings probed ->", out, file=sys.stderr)
