
import os, sys
sys.path.insert(0, os.path.join(os.environ["COOT_PREFIX"], "tests"))
import gui_harness as H
g, errs, log = H.load()
os.environ["COOT_AUDIT_DIR"] = "/tmp/coot-audit-selftest"
os.environ.setdefault("COOT_AUDIT_ONLY", os.environ.get("AUDIT_ST_ONLY", ""))
exec(compile(open(os.path.join(os.environ["COOT_PREFIX"], "tests", "gui_audit.py")).read(), "gui_audit.py", "exec"), {"__name__": "gui_audit"})
