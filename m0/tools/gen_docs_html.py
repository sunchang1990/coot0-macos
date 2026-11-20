#!/usr/bin/env python3
"""gen_docs_html.py  (build 28) -- turn the package's Markdown documentation into HTML pages for Help in coot0.

Usage:  python3 m0/tools/gen_docs_html.py [PACKAGE_DIR]      (default: m0/m1-package; the repository README.md is taken too)

Writes PACKAGE_DIR/docs/html/: one page per Markdown file (cookbook, scripting reference, README, CHANGELOG), links between
them rewritten to the .html pages, and search-index.json (every recipe, every function, every section heading) that
Help > Search Menus and Docs uses.  Each page records the sha1 of its Markdown source (<meta name="coot0-source-sha1">)
so the tests can tell when the pages are older than the Markdown.  Only the Markdown the docs use is handled: headings,
paragraphs, lists, tables, fenced code, inline code, bold, italics, links, hidden <!-- comments -->.
"""
import hashlib, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "m1-package"))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DOCS = os.path.join(PKG, "docs")
OUT = os.path.join(DOCS, "html")

# source Markdown (absolute) -> page (relative to OUT)
PAGES = {}
for root, dirs, files in os.walk(DOCS):
    if os.path.abspath(root).startswith(OUT): continue
    for f in sorted(files):
        if f.endswith(".md"):
            src = os.path.join(root, f)
            PAGES[src] = os.path.relpath(src, DOCS)[:-3] + ".html"
for src, page in ((os.path.join(REPO, "README.md"), "coot0-README.html"), (os.path.join(PKG, "CHANGELOG.md"), "CHANGELOG.html")):
    if os.path.exists(src): PAGES[src] = page

def slug(text):
    """GitHub's heading anchors: lower case, drop punctuation except - and _, spaces -> -."""
    t = re.sub(r"<[^>]+>", "", text).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")

def plain(text):
    """Markdown inline text -> plain text (for titles and the search index)."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*`]", "", t).strip()

def inline(text, src):
    """links first (their text may hold code spans), then code spans, then emphasis"""
    out, pos = [], 0
    code = [m.span() for m in re.finditer(r"`[^`]+`", text)]
    for m in re.finditer(r"\[((?:`[^`]*`|[^\]`])+)\]\(([^)\s]+)\)", text):
        if m.start() < pos or any(a <= m.start() < b for a, b in code): continue     # "[C@H](N)" inside a code span is no link
        out.append(inline_code(text[pos:m.start()], src))
        out.append('<a href="%s">%s</a>' % (html.escape(link_target(m.group(2), src)), inline_code(m.group(1), src))); pos = m.end()
    out.append(inline_code(text[pos:], src))
    return "".join(out)

def inline_code(text, src):
    out, pos = [], 0
    for m in re.finditer(r"`([^`]+)`", text):          # code spans first: nothing inside them is Markdown
        out.append(inline_plain(text[pos:m.start()], src)); out.append("<code>%s</code>" % html.escape(m.group(1), quote=False)); pos = m.end()
    out.append(inline_plain(text[pos:], src))
    return "".join(out)

def link_target(url, src):
    if re.match(r"^[a-z]+:", url) or url.startswith("#"): return url
    path, _, frag = url.partition("#")
    target = os.path.normpath(os.path.join(os.path.dirname(src), path))
    if target in PAGES:
        rel = os.path.relpath(os.path.join(OUT, PAGES[target]), os.path.dirname(os.path.join(OUT, PAGES[src])))
        return rel + ("#" + frag if frag else "")
    if src == os.path.join(REPO, "README.md"):           # the repository README: its root files sit at the package root
        if path in ("LICENSE", "LICENSING.md", "CORRESPONDING_SOURCE.md", "THIRD_PARTY_LICENSES.md"):
            return os.path.relpath(os.path.join(OUT, "..", "..", path), os.path.dirname(os.path.join(OUT, PAGES[src])))
        if path == "../../releases": return "https://github.com/sunchang1990/coot0-macos/releases"
    return url

def inline_plain(text, src):
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w/\"])(https?://[^\s<\"]+[^\s<\".,;:)])", r'<a href="\1">\1</a>', t)    # bare URLs
    return t

def table_cells(line):
    s = line.strip()
    if s.startswith("|"): s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"): s = s[:-1]
    cells, cur, code = [], "", False
    for ch in s:
        if ch == "`": code = not code
        if ch == "|" and not code: cells.append(cur.strip()); cur = ""
        else: cur += ch
    cells.append(cur.strip())
    return cells

def convert(src):
    text = open(src, encoding="utf-8").read()
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = text.split("\n")
    body, heads, i, title = [], [], 0, None
    used = {}
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip(); i += 1; code = []
            while i < len(lines) and not lines[i].startswith("```"): code.append(lines[i]); i += 1
            i += 1
            body.append('<pre class="%s"><code>%s</code></pre>' % (lang or "text", html.escape("\n".join(code), quote=False))); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level, t = len(m.group(1)), m.group(2).strip()
            a = slug(t); n = used.get(a, 0); used[a] = n + 1
            if n: a = "%s-%d" % (a, n)
            if title is None: title = plain(t)
            heads.append((level, plain(t), a))
            body.append('<h%d id="%s">%s</h%d>' % (level, html.escape(a), inline(t, src), level)); i += 1; continue
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|?\s*:?-+", lines[i + 1]):
            head = table_cells(line); i += 2; rows = []
            while i < len(lines) and lines[i].startswith("|"): rows.append(table_cells(lines[i])); i += 1
            t = ["<table><thead><tr>" + "".join("<th>%s</th>" % inline(c, src) for c in head) + "</tr></thead><tbody>"]
            for r in rows: t.append("<tr>" + "".join("<td>%s</td>" % inline(c, src) for c in r) + "</tr>")
            body.append("\n".join(t) + "</tbody></table>"); continue
        if re.match(r"^\s*[-*] ", line):
            items = []; depth0 = len(line) - len(line.lstrip())
            while i < len(lines) and (re.match(r"^\s*[-*] ", lines[i]) or (lines[i].startswith("  ") and lines[i].strip() and items)):
                l = lines[i]
                if re.match(r"^\s*[-*] ", l): items.append([len(l) - len(l.lstrip()), re.sub(r"^\s*[-*] ", "", l)])
                else: items[-1][1] += " " + l.strip()
                i += 1
            out, stack = [], []
            for depth, t in items:
                if not stack or depth > stack[-1]: out.append("<ul>"); stack.append(depth)
                while stack and depth < stack[-1]: out.append("</ul>"); stack.pop()
                out.append("<li>%s</li>" % inline(t, src))
            out += ["</ul>"] * len(stack)
            body.append("".join(out)); continue
        if not line.strip(): i += 1; continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|\|)", lines[i]) and not re.match(r"^\s*[-*] ", lines[i]):
            para.append(lines[i]); i += 1
        parts = [inline(p.rstrip(), src) + ("<br>" if p.endswith("  ") else "") for p in para]
        body.append("<p>%s</p>" % "\n".join(parts))
    return title or os.path.basename(src), "\n".join(body), heads

CSS = """
:root { --bg:#fff; --fg:#1d1d1f; --muted:#6e6e73; --line:#d2d2d7; --code:#f5f5f7; --link:#0066cc; }
@media (prefers-color-scheme: dark) { :root { --bg:#1d1d1f; --fg:#f5f5f7; --muted:#a1a1a6; --line:#424245; --code:#2c2c2e; --link:#4da3ff; } }
body { background:var(--bg); color:var(--fg); font:15px/1.5 -apple-system, "Helvetica Neue", sans-serif; max-width:980px; margin:0 auto; padding:16px 24px 64px; }
a { color:var(--link); } h1 { font-size:1.7em; } h2 { margin-top:1.6em; border-bottom:1px solid var(--line); } h3 { margin-top:1.5em; }
code, pre { font:13px/1.45 Menlo, monospace; background:var(--code); border-radius:4px; } code { padding:1px 4px; }
pre { padding:10px 12px; overflow-x:auto; } pre code { padding:0; background:none; }
pre.python { border-left:3px solid #3776ab; } pre.scheme { border-left:3px solid #a14f9b; }
table { border-collapse:collapse; margin:8px 0; display:block; overflow-x:auto; } th, td { border:1px solid var(--line); padding:4px 8px; text-align:left; vertical-align:top; }
.nav { color:var(--muted); font-size:13px; margin-bottom:8px; } :target { background: rgba(255, 214, 10, .25); }
"""

def page(src, title, body):
    rel = os.path.relpath(OUT, os.path.dirname(os.path.join(OUT, PAGES[src])))
    home = os.path.join(rel, "README.html") if rel != "." else "README.html"
    sha = hashlib.sha1(open(src, "rb").read()).hexdigest()
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="coot0-source-sha1" content="%s">\n<title>%s - coot0</title><style>%s</style></head>\n<body>\n'
            '<div class="nav"><a href="%s">coot0 documentation</a></div>\n%s\n</body></html>\n') % (sha, html.escape(title), CSS, home, body)

def main():
    index = []
    os.makedirs(OUT, exist_ok=True)
    for src, rel in sorted(PAGES.items(), key=lambda kv: kv[1]):
        title, body, heads = convert(src)
        dst = os.path.join(OUT, rel); os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, "w", encoding="utf-8").write(page(src, title, body))
        kind = "Cookbook" if rel.startswith("cookbook/") else "Function" if rel.startswith("api/sections/") else "Docs"
        if rel in ("api/A-Z.html",): continue                          # the A-Z table repeats the sections
        for level, t, a in heads:
            if kind == "Function" and level == 3: index.append({"kind": "Function", "title": t, "where": title, "page": rel, "anchor": a})
            elif kind == "Cookbook" and level == 3: index.append({"kind": "Cookbook", "title": t, "where": title, "page": rel, "anchor": a})
            elif level <= 2 and rel != "CHANGELOG.html": index.append({"kind": "Docs", "title": t, "where": title, "page": rel, "anchor": a if level > 1 else ""})
    json.dump(index, open(os.path.join(OUT, "search-index.json"), "w"), indent=0)
    print("gen_docs_html: %d pages, %d search entries -> %s" % (len(PAGES), len(index), OUT))

if __name__ == "__main__":
    main()
