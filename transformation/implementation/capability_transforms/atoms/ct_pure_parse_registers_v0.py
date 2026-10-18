"""
CT_PURE_PARSE_REGISTERS_V0

Pure Capability Transform (Atom)

Purpose:
    Parse a phase document into structured registers — the header fields and registers its
    Machine block carries, and the numbered sections of its prose.

Implementation:
    - Reads supplied text only; never touches the filesystem
    - Reports what the document contains and judges nothing: an absent section is simply
      absent, and the rule set decides what that means
    - No side effects, no external state

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError

from transformation.design.read import parse_text


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_PARSE_REGISTERS_V0.

    Inputs:
        document_text (str): full text of the phase document

    Outputs:
        header (dict): header field name → declared value
        sections (list): ordered prose sections with number, title and text
        registers (list): registers by id, each with columns and rows, or text
    """
    if "document_text" not in inputs:
        raise CTExecutionError(
            "CT_PURE_PARSE_REGISTERS_V0: missing required input 'document_text'"
        )

    document_text = inputs["document_text"]

    if not isinstance(document_text, str):
        raise CTExecutionError(
            "CT_PURE_PARSE_REGISTERS_V0: 'document_text' must be a string, "
            f"got {type(document_text).__name__}"
        )

    header, sections, registers = parse_text(document_text)

    return {"header": header, "sections": sections, "registers": registers}
