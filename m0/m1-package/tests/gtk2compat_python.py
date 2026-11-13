
# Runs the gtk2compat self-test (PyGTK 2 compatibility layer vs the real GTK 2 libraries, no display) inside Coot's embedded Python.
import os, sys, importlib.util
prefix = os.environ["COOT_PREFIX"]
os.environ["COOT_SELFTEST_NO_MAIN"] = "1"; os.environ["COOT_GTK2COMPAT_HEADLESS"] = "1"
os.environ["COOT_TEST_PIXMAPS"] = os.path.join(prefix, "share/coot/pixmaps")
spec = importlib.util.spec_from_file_location("gtk2compat_selftest", os.path.join(prefix, "tests", "gtk2compat_selftest.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
res = m.run_inprocess()
for n, ok, msg in res: print(("PASS " if ok else "FAIL ") + n + (("\n    " + msg) if not ok else ""))
print("SUMMARY", sum(1 for r in res if r[1]), "/", len(res), flush=True)
import coot; coot.coot_real_exit(0)
