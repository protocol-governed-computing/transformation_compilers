"""Read a phase's rule set out of the composition, rather than out of the working tree.

A rule set exists in two places by design: declared in Python, and sealed inside the workflow the
compiler built from that declaration. `design/emit.py` keeps them in step, and the generator is
authoritative when they differ.

They are not interchangeable, and which one judges a document is a governance question rather than a
convenience. A dossier pins the composition it is validated against, and that composition carries the
rules in force when it was pinned — so **the pin already names the rule set**. Judging by the working
tree instead judges a document by rules written after it was approved, which is how a single added
column turned every dossier ever written red while none of them had changed.

So this is the read that makes a pin mean what it says.
"""

from __future__ import annotations

from inspector import api


def _find_rule_set(obj):
    """The `rule_set` a compiled workflow carries, wherever the node structure puts it.

    Searched rather than addressed by path: the rule set is node input, and which node holds it is
    the workflow's business. A path would couple this read to a topology that is free to change.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "rule_set":
                return value
            found = _find_rule_set(value)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = _find_rule_set(value)
            if found is not None:
                return found
    return None


def sealed_rule_set(wf: str, snapshot_root: str) -> list[dict]:
    """The rule set as it exists in the composition — no Python declaration consulted.

    Fail-hard on both failures it can have. A workflow that will not read, and a workflow that reads
    and carries no rules, are different faults with one consequence: a document judged by nothing and
    told it is admissible.
    """
    status, artifact = api.query("si.artifact.show", {"artifact": wf}, snapshot_root)
    if status != "SUCCESS":
        raise RuntimeError(f"{wf} not readable from {snapshot_root}: {status}")
    rules = _find_rule_set(artifact)
    if rules is None:
        raise RuntimeError(f"{wf} carries no rule_set — the governance did not survive compilation")
    return rules
