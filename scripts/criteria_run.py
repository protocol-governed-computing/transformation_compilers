"""Run a change's acceptance criteria against a composition, whatever version of each act it holds.

A change's criteria are written before its design, so they name acts by the version the change will
deliver, or one a later change delivers. The composition the change is designed against holds an
earlier version, or none. This harness dispatches each workflow the suite names to the version of
its stem the composition holds. A stem the composition does not hold is dispatched as written, and
the act is absent: a criterion that needs it fails.

Usage: criteria_run.py <suite.py> <snapshot> [<domain package root>]
  <domain package root>  a folder holding the domain's package as it was, whose transforms are
                         run in place of the working tree's (criteria_before.sh)
Exit:  the suite's own.
"""
import importlib
import json
import re
import runpy
import sys
from pathlib import Path

from runtime import api

if len(sys.argv) > 3:
    root = Path(sys.argv[3])
    sys.path.insert(0, str(root))
    for package in root.iterdir():
        if (package / "__init__.py").is_file():
            importlib.import_module(package.name)

suite, snapshot = sys.argv[1], Path(sys.argv[2])
held = json.loads((snapshot / "artifact_index" / "index.json").read_text(encoding="utf-8"))["artifacts"]
VERSION = re.compile(r"^(.+)_V(\d+)$")
live: dict[str, str] = {}
for fqdn in held:
    m = VERSION.match(fqdn)
    if m and (m[1] not in live or int(m[2]) > int(VERSION.match(live[m[1]])[2])):
        live[m[1]] = fqdn
dispatch = api.run_workflow


def follow(*args, wf_fqdn, **kwargs):
    m = VERSION.match(wf_fqdn)
    return dispatch(*args, wf_fqdn=live.get(m[1], wf_fqdn) if m else wf_fqdn, **kwargs)


api.run_workflow = follow
sys.argv = [suite, str(snapshot)]
runpy.run_path(suite, run_name="__main__")
