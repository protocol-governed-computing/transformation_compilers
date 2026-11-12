"""Construction Completeness — the Construction lifecycle's admission gate.

A phase document is admitted by `tc phase check` against a declared rule set. A *design* is admitted
to construction by this: does it uniquely determine the artifacts it specifies? `UNIQUELY_DETERMINED_
OR_STOP` is the rule, and a percentage below the threshold is a refusal, not a report.

    CR-1 as first authored     54.8%
    construction requirement   100%, or the generator is inventing design

**The requirement list is derived, never declared.** It is the shape `render_all` emits, walked leaf
by leaf, so it cannot drift from construction — it *is* construction. An earlier version kept a
hand-written list and read 100% while the generator could reproduce one artifact in twenty-five: it
asked whether a contract declared a pipeline and never whether each step declared its store. A
hand-maintained list of what construction needs is a second opinion about construction, and the
weaker one. The declared list held 170 facts; the derived one holds 710.

**This needs nothing to have been built.** That is what separates it from the acceptance harness,
which compares a render against artifacts that already exist and can therefore only ever judge CR-1.
This judges a design on its own, which is what every CR after the first needs before a line of it is
authored.
"""

from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

from transformation.build.render import requirements


@dataclass
class Completeness:
    """What a design determines, and what it leaves to the generator to invent."""

    facts: list[tuple[str, str, bool]] = field(default_factory=list)

    @property
    def determined(self) -> int:
        return sum(1 for _, _, ok in self.facts if ok)

    @property
    def total(self) -> int:
        return len(self.facts)

    @property
    def percentage(self) -> float:
        return 100.0 * self.determined / self.total if self.total else 0.0

    @property
    def by_artifact(self) -> dict[str, list[tuple[str, bool]]]:
        out: dict[str, list[tuple[str, bool]]] = {}
        for code, path, ok in self.facts:
            out.setdefault(code, []).append((path, ok))
        return out

    @property
    def undetermined(self) -> Counter:
        """Undetermined facts by field, with list indices collapsed."""
        counts: Counter = Counter()
        for _, path, ok in self.facts:
            if not ok:
                counts[re.sub(r"\[\d+\]", "[]", path)] += 1
        return counts

    def meets(self, threshold: float) -> bool:
        return self.percentage + 1e-9 >= threshold


def measure(p7: dict, p8: dict, provenance: dict) -> Completeness:
    """Measure a design against what construction requires of it.

    `provenance` is where each rendered value came from, as attribution reports it
    (`transformation.build.provenance`). The measure reads it and derives no origin of its own.
    """
    return Completeness(facts=requirements(p7, p8, provenance))


# Amendments — what completeness cannot see -----------------------------------------------------
#
# Completeness asks whether every fact the design must state is stated. It cannot ask whether an
# amendment keeps the artifact it amends, because it has no view of what exists. That comparison is
# `sameness`, run by construction against the composition. What remains here is carrying forward the
# explanation no register can state, so an amendment written whole does not lose it.

def _leaves(value, path=""):
    """Every fact an artifact states, addressed by where it sits.

    A list is walked by index rather than reduced to its length: a capability contract's pipeline is
    a list, and comparing lengths says three steps became three steps while every field inside them
    disappeared. That is exactly what slipped past — the compiler caught it afterwards, on a schema
    requirement, which is later than the design could have been fixed.
    """
    if isinstance(value, dict):
        for key, item in value.items():
            yield from _leaves(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            # Keyed by identity where the items carry one, by position where they do not. A design
            # that inserts a pipeline step shifts every step after it, and a positional comparison
            # reads the whole tail as deleted — which is the opposite of what an amendment usually
            # does. `step` names a contract's steps; `code` and `name` cover the rest.
            key = next((item[k] for k in ("step", "code", "name")
                        if isinstance(item, dict) and item.get(k)), index)
            yield from _leaves(item, f"{path}[{key}]")
    else:
        yield path, value


def carry_forward(rendered: list[dict], existing: dict[str, dict]) -> None:
    """Preserve, in each amended artifact, the leaves no register of the design can express.

    Mutates the rendered machine blocks in place and records the origin of each preserved leaf, so
    the measure counts it as accounted for rather than as a fact somebody stated.

    Confined to descriptions deliberately. Every other leaf the design omits is a leaf it could have
    stated, and preserving those would let an amendment inherit anything its predecessor happened to
    carry — which is the drift this whole change is about, moving one level down.
    """
    from transformation.build.render import _carried

    for artifact in rendered:
        code = artifact["path"].rsplit("/", 1)[-1].removesuffix(".md")
        prior = existing.get(code)
        if not prior:
            continue
        now = dict(_leaves(artifact["machine"]))
        supplied = artifact.setdefault("supplied", {})
        for path, value in _leaves(prior):
            if path in now or not path.endswith("description"):
                continue
            # `_leaves` emits a leading separator, so the first segment is empty.
            target, *rest = path.lstrip(".").split(".")
            cursor = artifact["machine"]
            ok = True
            for depth, key in enumerate([target] + rest[:-1]):
                # A description may sit under a block the design renders nothing else into, as a
                # contract's `extensions` does; that block is made to hold it, at the top level only.
                if depth == 0 and len(rest) == 1 and isinstance(cursor, dict) and key not in cursor:
                    cursor[key] = {}
                if not isinstance(cursor, dict) or key not in cursor:
                    ok = False
                    break
                cursor = cursor[key]
            if ok and isinstance(cursor, dict):
                cursor[rest[-1] if rest else target] = value
                # Recorded as provenance addresses a leaf: no leading separator. Recorded with one,
                # the record matched no leaf, and a carried value read as stated by the design.
                _carried(supplied, path.lstrip("."))
