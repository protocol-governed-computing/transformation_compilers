"""Run an execution suite against a derived build, following each declared successor.

A suite dispatches a workflow by the identity it was written against. Where the derived design
replaced that workflow, or a delivered change did before it, the suite's name is a predecessor's,
and the composition no longer holds it. This harness dispatches the successor the design declares:
this derivation's identities, the lineage (`supersedes`) the design carries, and the successors
the retirement ledger records, followed to the last version. A name with no declared successor is dispatched as written.

Usage: derive_suite.py <generated.json> <suite.py> <suite arguments>...
"""
import json
import runpy
import sys
from pathlib import Path

import yaml

from runtime import api

RETIRED = Path(__file__).resolve().parents[2] / ".github" / "process" / "retired_identities.yaml"

design = json.load(open(sys.argv[1]))
identity = design["_identity"]
ledger = yaml.safe_load(RETIRED.read_text(encoding="utf-8")) if RETIRED.is_file() else None
recorded = (ledger or {}).get("retired") or []
successor = {e["identity"]: e["superseded_by"] for e in recorded if e.get("superseded_by")}
successor |= {old: r["artifact"] for r in design.get("artifact_properties") or []
             if r.get("property") == "supersedes"
             for old in (r["value"] if isinstance(r["value"], list) else [r["value"]])}
successor.update({**identity["superseded"], **identity["replaced"]})
dispatch = api.run_workflow


def last(wf_fqdn):
    seen = {wf_fqdn}
    while wf_fqdn in successor and successor[wf_fqdn] not in seen:
        wf_fqdn = successor[wf_fqdn]
        seen.add(wf_fqdn)
    return wf_fqdn


def follow(*args, wf_fqdn, **kwargs):
    return dispatch(*args, wf_fqdn=last(wf_fqdn), **kwargs)


api.run_workflow = follow
suite = sys.argv[2]
sys.argv = [suite] + sys.argv[3:]
runpy.run_path(suite, run_name="__main__")
