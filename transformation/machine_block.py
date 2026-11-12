"""
The machine block of a document: the YAML under its `## Machine` heading.

A declaration's prose may carry YAML of its own, as an example or as a picture of what a rule
realizes, and a machine block may carry backticks inside a value. A reader that takes the first
fenced block, or stops at the first fence, reads the wrong YAML for such a document. Every reader
here takes the block this one rule finds.

It is the compiler's rule (`compiler.atoms.machine_block`), stated again because this package may
not import the compiler; `.github/process/frontmatter_fidelity.py` checks the two agree.
"""

import re

MACHINE_BLOCK = re.compile(r"^## Machine\s*\n+```yaml\s*\n(?P<machine_yaml>.*?)\n```", re.MULTILINE | re.DOTALL)


def machine_yaml(text: str) -> str | None:
    """The YAML source of a document's machine block, or None where it has none."""
    found = MACHINE_BLOCK.search(text)
    return found.group("machine_yaml") if found else None
