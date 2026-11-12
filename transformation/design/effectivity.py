"""Rule effectivity: which rule set judged a document, and whether a change to it was declared.

A rule set is named by its register schema's `$id`. Under one `$id` the rules may change only by a
recorded revision, and a revision never alters a prior document's admissibility. A change that can
takes a new `$id`. So:

- a **digest** names a rule set's exact content, read from the rules themselves;
- a **revision** records a change and the digest it produced (`x-revisions` in the schema), and a
  rule set whose digest no revision records changed without declaring its effectivity;
- **`judged_by`** names the rule set a verdict was rendered against: the `$id` the rules carry in
  their identities, the digest, and the revision that digest is recorded under;
- an **approval** is given under one `$id`, and stands unconfirmed under any other;
- the **difference** between two rule sets is named rule by rule, by identity.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any

from transformation.design.rules import Rule
from transformation.design.schema import PhaseShape


def _canonical(rule: Rule) -> dict[str, Any]:
    """What a rule is, as a digest reads it. The section title is a reading aid the sealed form
    fills from the register, so it is not part of what the rule is."""
    return {"id": rule.id, "identity": rule.identity, "check": rule.check, "register": rule.register,
            "params": rule.params, "intent": rule.intent}


def digest(rules: list[Rule]) -> str:
    """The digest of a rule set, in order: a sealed rule set is a list."""
    text = json.dumps([_canonical(r) for r in rules], sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False)
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def schema_of(rules: list[Rule]) -> str | None:
    """The `$id` a rule set belongs to, read from its rules' identities, or None for one sealed
    before rules carried an identity. Fail-hard on a mixture."""
    ids = {r.identity.split("#", 1)[0] for r in rules}
    if ids == {""}:
        return None
    if len(ids) != 1:
        raise ValueError(f"a rule set belongs to one schema; these rules name {sorted(ids)}")
    return ids.pop()


def unrecorded(shape: PhaseShape, rules: list[Rule]) -> str | None:
    """Why the schema's rules are not its last recorded revision, or None when they are."""
    if not shape.revisions:
        return f"{shape.schema_id} records no revision"
    last = shape.revisions[-1]
    actual = digest(rules)
    if last["digest"] != actual:
        return (f"{shape.schema_id} expands into {actual}, but its last revision ({last['revision']}) "
                f"records {last['digest']} — a change to the rules records its effectivity "
                f"(`tc phase revise`)")
    return None


def judged_by(rules: list[Rule], shape: PhaseShape | None) -> dict[str, Any]:
    """The rule set a verdict was rendered against. `shape` is the working tree's schema for the
    phase; a revision is named when that schema records the digest, and is `None` otherwise."""
    schema, actual = schema_of(rules), digest(rules)
    revision = None
    if shape is not None and shape.schema_id == schema:
        revision = next((r["revision"] for r in shape.revisions if r["digest"] == actual), None)
    return {"schema": schema, "revision": revision, "digest": actual}


def approval_standing(header: dict[str, Any], current: str) -> dict[str, Any] | None:
    """Where a document's approval stands under the current rule set, or None when it has none.

    An approval is a fact about the rule set it was given under. Under that `$id` it stands
    confirmed; under any other it stands unconfirmed until a person re-confirms it.
    """
    approval = header.get("approval")
    if not isinstance(approval, dict):
        return None
    confirmed = approval.get("rule_set") == current
    return {"gate": approval.get("gate"), "state": approval.get("state"),
            "given_under": approval.get("rule_set"), "current": current,
            "standing": "confirmed" if confirmed else "unconfirmed"}


def difference(before: list[Rule], after: list[Rule]) -> dict[str, list[str]]:
    """Two rule sets, compared rule by rule by identity."""
    a = {r.identity: _canonical(r) for r in before}
    b = {r.identity: _canonical(r) for r in after}
    return {"added": sorted(set(b) - set(a)), "removed": sorted(set(a) - set(b)),
            "changed": sorted(i for i in set(a) & set(b) if a[i] != b[i])}
