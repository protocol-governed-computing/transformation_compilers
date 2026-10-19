"""
CT_PURE_RENDER_ARTIFACTS_V0

Pure Capability Transform (Atom)

Purpose:
    Render every protocol artifact a mandate schedules, from the design that determines it.

Implementation:
    - Renders the whole mandate in one call: a capability contract is a fixed pipeline with no
      iteration, so a step that rendered one artifact could never render twenty-five
    - Emits the Machine block, which is what the compiler reads, the snapshot seals and the runtime
      executes; an artifact's prose is human narrative no register determines
    - Invents nothing. Every value comes from a register or a constitution-fixed default, and the
      completeness gate ahead of this step is what guarantees there is nothing left to invent
    - No side effects, no external state

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError

from transformation.build.render import render_all, render_document


def _registers(parsed: list) -> Dict[str, list]:
    return {entry["id"]: entry["value"] if isinstance(entry.get("value"), list) else []
            for entry in parsed or []}


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_RENDER_ARTIFACTS_V0.

    Inputs:
        design_registers (list): parsed P7 registers
        mandate_registers (list): parsed P8 registers

    Outputs:
        artifacts (list): one entry per artifact, each {path, domain, machine}
        documents (list): the same artifacts as {path, text} — what persistence is handed
        artifact_count (int): how many were rendered
        sources (dict): per artifact code, where each value the renderer did not read from a
            register came from — path → [origin, governing artifact]
    """
    for required in ("design_registers", "mandate_registers"):
        if required not in inputs:
            raise CTExecutionError(
                f"CT_PURE_RENDER_ARTIFACTS_V0: missing required input {required!r}"
            )

    artifacts = render_all(_registers(inputs["design_registers"]),
                           _registers(inputs["mandate_registers"]))
    if not artifacts:
        raise CTExecutionError(
            "CT_PURE_RENDER_ARTIFACTS_V0: the mandate schedules no artifact this design declares — "
            "a construction that emits nothing is a reconciliation failure, not an empty build"
        )

    return {
        "artifacts": [{"path": a["path"], "domain": a["domain"], "machine": a["machine"]}
                      for a in artifacts],
        # Rendering the document here rather than in a second transform keeps one derivation: the
        # machine block and the document that carries it cannot disagree if one produced both.
        "documents": [{"path": a["path"], "text": render_document(a)} for a in artifacts],
        "artifact_count": len(artifacts),
        # Only the renderer knows where a value came from, because it put it there. Without this
        # the provenance step read every leaf as stated by the design, and the completeness gate
        # could not refuse a value the renderer supplied.
        "sources": {str(a["machine"].get("fqdn", "")).split("::")[-1]:
                    {path: list(record) for path, record in (a.get("supplied") or {}).items()}
                    for a in artifacts},
    }
