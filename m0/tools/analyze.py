#!/usr/bin/env python3
"""analyze.py <results.json> [regex]  -- summarise unique error sites (deduplicated by file:line:message).
With a regex, only diagnostics whose message or file matches are listed."""
import json, re, sys, collections
res = json.load(open(sys.argv[1])); rx = re.compile(sys.argv[2]) if len(sys.argv) > 2 else None
sites = {}
for t in res:
    for f, l, k, m in t["diags"]:
        if rx and not (rx.search(m) or rx.search(f)): continue
        sites.setdefault((f.split("coot-src/")[-1], l, m), set()).add(t["dir"] + "/" + t["file"])
ok = sum(1 for t in res if t["rc"] == 0)
print(f"TUs ok {ok}/{len(res)} | matching unique error sites: {len(sites)}")
def key(m):
    q = re.findall(r"'([^']+)'", m); return (re.sub(r"'[^']*'", "'X'", m)[:60] + " :: " + (q[0] if q else ""))
c = collections.Counter(key(m) for (f, l, m) in sites)
for k, v in c.most_common(25): print(f"  {v:5d} {k}")
if rx:
    for (f, l, m), tus in list(sites.items())[:10]: print("  >", f, l, m[:120], "| TUs:", len(tus))
