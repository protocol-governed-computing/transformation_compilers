"""Interface structures — what the readers and the evaluator return is what they declare.

`CT_PURE_PARSE_REGISTERS_V0`, `CT_PURE_PARSE_PRIOR_PHASES_V0` and `CT_PURE_EVALUATE_RULES_V0` name, on
each structured field, the STRUCTURE whose `core.json_schema` its value conforms to. This holds the
declaration and the code together:

1. every `STRUCTURE_PHASE_*` schema is a valid JSON Schema;
2. the forms `STRUCTURE_PHASE_PRIORS_V0` writes out equal the structures they restate;
3. every structure a transform's field names is one of these, and every field that names one conforms
   over the corpus: each testbed document parsed, its priors parsed, and the document judged by the
   rule set its phase's workflow seals.

Run:  python scripts/testbed/interface_structures_test.py
Exit: 0 when every check holds, 1 otherwise.
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from transformation.design import emit
from transformation.implementation.capability_transforms.atoms import (
    ct_pure_evaluate_rules_v0 as evaluate,
    ct_pure_parse_prior_phases_v0 as parse_priors,
    ct_pure_parse_registers_v0 as parse,
)

REPO = Path(__file__).resolve().parents[2]
STRUCTURES = REPO / "registry" / "structures"
TRANSFORMS = REPO / "registry" / "design" / "capability_transforms"
CORPUS = REPO / "scripts" / "testbed"
from transformation.machine_block import MACHINE_BLOCK as MACHINE
PARTS = {"header": "STRUCTURE_PHASE_HEADER_V0", "sections": "STRUCTURE_PHASE_SECTIONS_V0",
         "registers": "STRUCTURE_PHASE_REGISTERS_V0"}


def machine(path: Path) -> dict:
    return yaml.safe_load(MACHINE.search(path.read_text(encoding="utf-8")).group(1)) or {}


def schemas() -> dict[str, dict]:
    return {p.stem: machine(p)["core"]["json_schema"] for p in sorted(STRUCTURES.glob("STRUCTURE_PHASE_*.md"))}


def declared_fields() -> dict[str, dict[str, str]]:
    """Transform → field → the structure it names, over the readers and the evaluator."""
    out: dict[str, dict[str, str]] = {}
    for path in sorted(TRANSFORMS.glob("CT_PURE_*_V0.md")):
        core = machine(path)["core"]
        out[path.stem] = {name: spec["structure"].split("::", 1)[1]
                          for side in ("inputs", "outputs") for name, spec in (core.get(side) or {}).items()
                          if isinstance(spec, dict) and spec.get("structure")}
    return out


def sealed_rule_set(phase: str) -> list[dict]:
    code = emit.workflow_fqdn(phase).split("::", 1)[1]
    wf = machine(next(REPO.joinpath("registry").rglob(f"{code}.md")))
    return next(node["inputs"]["rule_set"] for node in wf["core"]["nodes"].values()
                if isinstance(node.get("inputs"), dict) and "rule_set" in node["inputs"])


def corpus() -> list[tuple[Path, str]]:
    docs = []
    for path in sorted(CORPUS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if "## Machine" in text:
            docs.append((path, text))
    return docs


def test_each_structure_is_a_json_schema():
    for code, schema in schemas().items():
        Draft202012Validator.check_schema(schema)
        assert schema.get("$id") == f"transformation::{code}", code


def test_priors_restate_the_structures_they_name():
    s = schemas()
    written = s["STRUCTURE_PHASE_PRIORS_V0"]["additionalProperties"]["properties"]
    for part, code in PARTS.items():
        expected = {k: v for k, v in s[code].items() if k not in ("$schema", "$id")}
        assert written[part] == expected, f"PRIORS restates {part} unlike {code}"


def test_every_named_structure_exists():
    s = schemas()
    for transform, fields in declared_fields().items():
        for field, code in fields.items():
            assert code in s, f"{transform}.{field} names {code}, which is not a phase structure"


def test_outputs_conform_over_the_corpus():
    s = {code: Draft202012Validator(schema) for code, schema in schemas().items()}
    fields = declared_fields()
    reads, judge = fields["CT_PURE_PARSE_REGISTERS_V0"], fields["CT_PURE_EVALUATE_RULES_V0"]
    rule_sets: dict[str, list[dict]] = {}
    docs, judged, failures = corpus(), 0, []

    def check(code: str, value, where: str) -> None:
        errors = list(s[code].iter_errors(value))
        if errors:
            failures.append(f"{where}: {errors[0].message} at {list(errors[0].absolute_path)}")

    for path, text in docs:
        out = parse.execute({"document_text": text})
        for field, code in reads.items():
            check(code, out[field], f"{path.name} {field}")
        phase = str(out["header"].get("phase") or "")
        if phase not in emit_phases():
            continue
        rule_sets.setdefault(phase, sealed_rule_set(phase))
        result = evaluate.execute({**out, "document_text": text, "rule_set": rule_sets[phase],
                                   "observed": {}, "priors": {}})
        check(judge["findings"], result["findings"], f"{path.name} findings")
        judged += 1

    priors = parse_priors.execute({"prior_texts": {f"p{i}": text for i, (_, text) in enumerate(docs[:12])}})
    check(fields["CT_PURE_PARSE_PRIOR_PHASES_V0"]["priors"], priors["priors"], "priors")

    assert not failures, "\n".join(failures[:10])
    assert judged, "no corpus document was judged"
    print(f"        {len(docs)} documents parsed, {judged} judged, every output conforms")


def emit_phases() -> set[str]:
    from transformation.design.catalog import PHASES
    return {spec.id for spec in PHASES}


if __name__ == "__main__":
    tests = [(n, f) for n, f in globals().items() if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
        except Exception as exc:  # report every test, then fail the run
            failed += 1
            print(f"  FAIL  {name}: {exc!r}")
    if failed:
        print(f"\nINTERFACE STRUCTURES FAILED — {failed} of {len(tests)}")
        sys.exit(1)
    print(f"\nINTERFACE STRUCTURES PASSED — {len(tests)} checks, {len(schemas())} structures")
