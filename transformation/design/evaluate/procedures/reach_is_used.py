"""The `REACH_IS_USED` procedure (DESIGN_LANGUAGE §6)."""

from __future__ import annotations

from transformation.design.evaluate.common import (
    _act_stores,
    _at,
    _binding_stores,
    _declared_reach,
    _store_keys,
    _where,
)
from transformation.design.evaluate.document import ParsedDocument
from transformation.design.evaluate.registry import Locator, check


@check("REACH_IS_USED")
def _reach_is_used(doc: ParsedDocument, rule) -> list[tuple[Locator, str]]:
    """A declared reach must be read by something the act does.

    Half of one statement, and the half that alone permits a reserve: an act may declare a reach to
    records it never touches, and nothing would say so. The other half — refusing an undeclared read
    — permits the opposite, a read nobody declared. Together the declared set and the used set are
    the same set, which is the whole of what the business asked for.

    A binding the composition does not publish is not judged here. The reach that matters consults
    another subdomain's existing binding, which is always published; one this design authors has no
    stores in the composition yet, and refusing it would refuse the design for being new.
    """
    observed = doc.observed.get(rule.params["observation"]) or []
    if not observed:
        return [(_at(_where(rule)),
                 "no store surface was observed — whether a declared reach is read cannot be "
                 "checked against stores nobody published")]

    covers = _binding_stores(observed)
    reads = _act_stores(doc, rule, _store_keys(observed))

    out = []
    for act, bindings in sorted(_declared_reach(doc, rule).items()):
        for binding in sorted(bindings):
            stores = covers.get(binding)
            if stores is None:
                continue
            if stores & reads.get(act, set()):
                continue
            out.append((
                _at(_where(rule), act),
                rule.params["detail"].format(
                    binding=binding,
                    stores=", ".join(sorted(s.split("::")[-1] for s in stores)) or "no records",
                ),
            ))
    return out
