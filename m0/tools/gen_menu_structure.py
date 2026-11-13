#!/usr/bin/env python3
"""gen_menu_structure.py -- the main window's menubar (labels, nesting, item kinds) as JSON, extracted from src/gtk2-interface.c.
usage: gen_menu_structure.py <gtk2-interface.c> <out.json>"""
import re, sys, json
src, out = sys.argv[1], sys.argv[2]
nodes, children, submenu = {}, {}, {}
txt = open(src, errors="replace").read()
for line in txt.splitlines():
    s = line.strip()
    m = re.match(r'(\w+) = gtk_menu_bar_new \(\);', s)
    if m: nodes[m.group(1)] = {"kind": "menubar"}; continue
    m = re.match(r'(\w+) = gtk_menu_new \(\);', s)
    if m: nodes[m.group(1)] = {"kind": "menu"}; continue
    m = re.match(r'(\w+) = gtk_(image_|check_|radio_)?menu_item_new_with_mnemonic \((?:\w+, )?"((?:[^"\\]|\\.)*)"\);', s)
    if m: nodes[m.group(1)] = {"kind": (m.group(2) or "").strip("_") + "item" if m.group(2) else "item", "label": m.group(3).replace('\\"', '"')}; continue
    m = re.match(r'(\w+) = gtk_separator_menu_item_new \(\);', s)
    if m: nodes[m.group(1)] = {"kind": "separator"}; continue
    m = re.match(r'gtk_container_add \(GTK_CONTAINER \((\w+)\), (\w+)\);', s)
    if m and m.group(1) in nodes and m.group(2) in nodes and nodes[m.group(1)]["kind"] in ("menu", "menubar"):
        children.setdefault(m.group(1), []).append(m.group(2)); continue
    m = re.match(r'gtk_menu_item_set_submenu \(GTK_MENU_ITEM \((\w+)\), (\w+)\);', s)
    if m: submenu[m.group(1)] = m.group(2)
bar = next(k for k, v in nodes.items() if v["kind"] == "menubar")
def build(var):
    n = dict(nodes[var]); n["var"] = var
    if var in children: n["children"] = [build(c) for c in children[var]]
    if var in submenu: n["submenu"] = build(submenu[var])
    return n
tree = build(bar)
def count(n): return 1 + sum(count(c) for c in n.get("children", [])) + (count(n["submenu"]) if "submenu" in n else 0)
json.dump(tree, open(out, "w"), indent=1)
print("menubar", bar, "-", count(tree), "nodes ->", out, file=sys.stderr)
