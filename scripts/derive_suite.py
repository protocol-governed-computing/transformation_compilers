"""Run an execution suite against a derived build, following each declared successor.

A suite dispatches a workflow by the identity it was written against. Where the derived design
replaced that workflow, the suite's name is the predecessor's, and the composition no longer holds
it. This harness dispatches the successor the design declares (`supersedes`), and nothing else:
a name with no declared successor is dispatched as written.

Usage: derive_suite.py <generated.json> <suite.py> <suite arguments>...
"""
import json
import runpy
import sys

from runtime import api

identity = json.load(open(sys.argv[1]))["_identity"]
successor = {**identity["superseded"], **identity["replaced"]}
dispatch = api.run_workflow


def follow(*args, wf_fqdn, **kwargs):
    return dispatch(*args, wf_fqdn=successor.get(wf_fqdn, wf_fqdn), **kwargs)


api.run_workflow = follow
suite = sys.argv[2]
sys.argv = [suite] + sys.argv[3:]
runpy.run_path(suite, run_name="__main__")
