#!/usr/bin/env python3
"""Mechanical Python 2 -> 3 port of Coot 0.9.8.96's shipped scripts (python/*.py).  Run with Python 3.11 (lib2to3).
Usage: port_python_scripts.py <dir>     (rewrites *.py in place, except coot.py which is SWIG output)
Steps: 1) lib2to3 (print, has_key, execfile, raw_input, dict views, tuple-parameter lambdas ... but NOT the 'import' fixer,
          because the scripts are imported as top-level modules, not as a package)
       2) leading tabs -> spaces using Python 2's tab stop of 8 (Python 3 rejects the mixed tab/space indentation Python 2 accepted)
       3) string-module functions removed in Python 3 (string.join/split/lower/...) -> str methods, by balanced-parenthesis rewrite"""
import os, re, sys, glob, subprocess

d = sys.argv[1]
import shutil
files = sorted(f for f in glob.glob(os.path.join(d, "*.py")) if os.path.basename(f) != "coot.py")
# *.py.in configure templates (e.g. coot_load_modules.py.in) are Python 2 source too: port them via a temporary .py name
ins = sorted(glob.glob(os.path.join(d, "*.py.in")))
tmp_of = {}
for f in ins:
    t = f + ".tmp.py"; shutil.copy(f, t); tmp_of[t] = f; files.append(t)

# 1) lib2to3
subprocess.run([sys.executable, "-W", "ignore", "-m", "lib2to3", "-w", "-n", "-x", "import", "-x", "future"] + files,
               capture_output=True, text=True, check=True)

# 2) tabs
def expand_leading(path):
    lines = open(path, errors="surrogateescape").read().split("\n"); n = 0
    for i, l in enumerate(lines):
        m = re.match(r"^[ \t]+", l)
        if m and "\t" in m.group(0):
            lines[i] = m.group(0).expandtabs(8) + l[m.end():]; n += 1
    open(path, "w", errors="surrogateescape").write("\n".join(lines)); return n

# 3) string module
METHODS = {"capitalize", "expandtabs", "find", "rfind", "index", "rindex", "lower", "upper", "lstrip", "rstrip", "strip", "replace",
           "swapcase", "translate", "zfill", "ljust", "rjust", "center", "count", "split", "rsplit"}
ATTRS = {"uppercase": "ascii_uppercase", "lowercase": "ascii_lowercase", "letters": "ascii_letters"}
CALL = re.compile(r"\bstring\.(atoi|atof|atol|join|joinfields|splitfields|" + "|".join(sorted(METHODS)) + r")\(")

def split_args(s):
    args, depth, cur, q = [], 0, "", None
    i = 0
    while i < len(s):
        c = s[i]
        if q:
            cur += c
            if c == "\\": cur += s[i + 1]; i += 1
            elif c == q: q = None
        elif c in "'\"": q = c; cur += c
        elif c in "([{": depth += 1; cur += c
        elif c in ")]}": depth -= 1; cur += c
        elif c == "," and depth == 0: args.append(cur.strip()); cur = ""
        else: cur += c
        i += 1
    if cur.strip(): args.append(cur.strip())
    return args

def find_close(s, start):  # s[start] is just after '('
    depth, q, i = 1, None, start
    while i < len(s):
        c = s[i]
        if q:
            if c == "\\": i += 1
            elif c == q: q = None
        elif c in "'\"": q = c
        elif c == "(": depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0: return i
        i += 1
    raise ValueError("unbalanced")

def rewrite_string_calls(text):
    n = 0
    while True:
        ms = list(CALL.finditer(text))
        if not ms: break
        m = ms[-1]                                  # innermost-last first
        end = find_close(text, m.end()); args = split_args(text[m.end():end]); name = m.group(1)
        recv = "(" + args[0] + ")" if args else ""
        if name in ("atoi", "atol"): new = "int(" + ", ".join(args) + ")"
        elif name == "atof": new = "float(" + args[0] + ")"
        elif name in ("join", "joinfields"):
            sep = args[1] if len(args) > 1 else '" "'
            new = "(" + sep + ").join(" + args[0] + ")"
        elif name == "splitfields": new = recv + ".split(" + ", ".join(args[1:]) + ")"
        else: new = recv + "." + name + "(" + ", ".join(args[1:]) + ")"
        text = text[:m.start()] + new + text[end + 1:]; n += 1
    for a, b in ATTRS.items():
        text, k = re.subn(r"\bstring\." + a + r"\b", "string." + b, text); n += k
    return text, n

tot_tabs = tot_str = 0
for f in files:
    tot_tabs += expand_leading(f)
    t = open(f, errors="surrogateescape").read(); t2, n = rewrite_string_calls(t)
    if n: open(f, "w", errors="surrogateescape").write(t2); tot_str += n
for t, f in tmp_of.items(): os.replace(t, f)
print(f"ported {len(files)} files: {tot_tabs} tab-indented lines normalised, {tot_str} string-module uses rewritten")
