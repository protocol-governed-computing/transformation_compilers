"""Evaluate a phase document against its rule set: the check kinds, the mechanism half of the
design compiler.

A check kind is a *mechanism*: "is this cell's value in a vocabulary", "is this column absent",
"does this token appear anywhere". It knows how to inspect a phase document and nothing about which
register it is inspecting or why that matters. Those are declared in the register schemas.

This mirrors the platform's own split: a workflow graph declares nodes and bindings and names a
capability by FQDN; the capability implements a mechanism and holds no policy. Adding a governance
rule must not require a new mechanism, and a new mechanism must not carry a rule's intent.

The registry is closed. An unknown check kind is fail-hard, never a skipped rule — a silently
skipped rule is the vacuity failure this codebase has hit repeatedly.

The package holds the document the checks read (`document`), the registry, what every check reads
with (`common`), and the kinds: the keyword subset (`keywords`), the four annotation constructs
(`constructs`), and one module per procedure (`procedures/`). Importing the package registers every
kind.
"""

from transformation.design.evaluate.document import Block, ParsedDocument, Table
from transformation.design.evaluate.registry import CheckFn, Locator, dispatch, kinds
from transformation.design.evaluate.common import place
from transformation.design.evaluate import constructs, keywords, procedures  # noqa: F401

__all__ = ["Block", "CheckFn", "Locator", "ParsedDocument", "Table", "dispatch", "kinds", "place"]
