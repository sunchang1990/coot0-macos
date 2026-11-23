#!/usr/bin/env python3
# check_history_names.py COOT_SRC API_INDEX_JSON  (build 35)
# Every command name that Coot's C++ writes into its command log (terminal echo, 0-coot-history.py/.scm) must be a real
# scripting function in at least one language (coot0 adds the _py / -scm ending itself), or be listed below with the reason
# it cannot be one; and text arguments must be recorded in quotes.  Coot 0.9.8.96: 18 wrong names, 26 unquoted arguments.
# Prints PASS / FAIL lines and SUMMARY n / m; exit status 1 on a failure.
import re, glob, json, os, sys
src, index = sys.argv[1], sys.argv[2]
NOT_SCRIPTABLE = {   # name as logged -> why no scripting function has it (these become comments in the history files)
    "move-molecule-here": "logged by a dialog button (move_molecule_here_by_widget); no scripting function",
    "set-density-size-em": "set_density_size_em is not in Coot's scripting interface",
    "toggle-display-map": "junk.cc, not compiled",
    "toggle-display-mol": "junk.cc, not compiled",
}
E = json.load(open(index))
py = {e.get("py") for e in E if e.get("py")}; scm = {e.get("scm") for e in E if e.get("scm")}
def base(n):
    n = n.replace("-", "_")
    for suf in ("_scm", "_py"):
        if n.endswith(suf): return n[: -len(suf)]
    return n
def known(n):
    b = base(n); own = n.replace("-", "_")
    return (own in py or b in py or b + "_py" in py or
            own.replace("_", "-") in scm or b.replace("_", "-") in scm or b.replace("_", "-") + "-scm" in scm)
names = {}; unquoted = []
for f in sorted(glob.glob(os.path.join(src, "src", "*.cc"))):
    if "coot_wrap" in f: continue
    s = open(f, encoding="latin-1").read()
    s = re.sub(r'(?m)^\s*//.*$', '', s)          # whole-line comments (an old name kept in a comment is not logged)
    for pat in (r'add_to_history_typed\(\s*"([A-Za-z0-9_-]+)"', r'std::string\s+cmd\s*=\s*"([A-Za-z0-9_-]+)"',
                r'command_strings\.push_back\("([A-Za-z0-9_-]+)"\);'):
        for m in re.finditer(pat, s): names.setdefault(m.group(1), os.path.basename(f))
    for m in re.finditer(r'\n[A-Za-z][\w:\s\*&<>]*?\b(\w+)\s*\(([^)]*)\)\s*\{', s):
        fn, params = m.groups()
        if fn in ("add_to_history_typed", "add_to_history_simple"): continue
        end = s.find("\n}\n", m.end()); body = s[m.end(): end if end > 0 else m.end() + 3000]
        if "add_to_history" not in body: continue
        for p in params.split(","):
            p = p.strip()
            if re.search(r'(char\s*\*|std::string|string\s*&|String)', p):
                v = re.split(r'[\s\*&]+', p)[-1]
                if re.search(r'(args|commands|command_strings)\.push_back\(\s*(clipper::String\(\s*)?%s\s*\)?\s*\)' % re.escape(v), body):
                    unquoted.append("%s %s(%s)" % (os.path.basename(f), fn, v))
bad = sorted(n for n in names if not known(n) and n not in NOT_SCRIPTABLE)
res = [("%d logged names are real scripting functions or listed as not scriptable" % len(names), not bad, bad[:20]),
       ("text arguments are logged in quotes", not unquoted, unquoted[:20]),
       ("the not-scriptable list is still needed (each name is still logged)", all(n in names for n in NOT_SCRIPTABLE),
        [n for n in NOT_SCRIPTABLE if n not in names])]
for name, ok, detail in res: print(("PASS " if ok else "FAIL ") + name + ("" if ok else "  %r" % (detail,)))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res))
sys.exit(0 if all(r[1] for r in res) else 1)
