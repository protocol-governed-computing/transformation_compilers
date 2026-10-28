"""Diff generated P7 rows against the baseline slice for the same family.

Rows are matched on their key columns. Prose (`summary`) is not compared: it is description, not
behavior. A store's `used_by` is compared only over the family's own components.
"""
import json
import sys
from collections import Counter

sys.path.insert(0, __import__("os").path.dirname(__file__))
from p7_slice import cut, load, short  # noqa: E402

KEYS = {
    "new_artifacts": ("code",),
    "rb_declarations": ("binds_wf",),
    "execution_topology": ("workflow", "node"),
    "cc_composition": ("cc_code", "step_name"),
    "step_bindings": ("owner", "step", "direction", "field"),
    "interface_fields": ("artifact", "direction", "field"),
    "artifact_properties": ("artifact", "property"),
    "structure_stores": ("store_name",),
}
PROSE = {"summary"}


def norm(row, family):
    out = {k: v for k, v in row.items() if not k.startswith("_") and k not in PROSE}
    if "used_by" in out:
        out["used_by"] = sorted(c.strip() for c in out["used_by"].split(",") if short(c.strip()) in family)
    return out


def main(baseline_path, generated_path, extra_members=""):
    generated = json.load(open(generated_path))
    generated = {k: v for k, v in generated.items() if k in KEYS}
    members = {short(r[c]) for reg, rows in generated.items() for r in rows
               for c in KEYS[reg][:1]} | set(filter(None, extra_members.split(",")))
    baseline = cut(load(baseline_path), members)
    family = members
    totals = Counter()
    for reg, keys in KEYS.items():
        b = {tuple(r[k] for k in keys): norm(r, family) for r in baseline.get(reg, [])}
        g = {tuple(r[k] for k in keys): norm(r, family) for r in generated.get(reg, [])}
        same = [k for k in b if k in g and b[k] == g[k]]
        changed = [k for k in b if k in g and b[k] != g[k]]
        only_b = [k for k in b if k not in g]
        only_g = [k for k in g if k not in b]
        totals.update(same=len(same), changed=len(changed), only_baseline=len(only_b), only_generated=len(only_g))
        print(f"\n== {reg}: same {len(same)}, changed {len(changed)}, "
              f"baseline-only {len(only_b)}, generated-only {len(only_g)}")
        for k in changed:
            diff = {c: (b[k].get(c), g[k].get(c)) for c in set(b[k]) | set(g[k]) if b[k].get(c) != g[k].get(c)}
            print("  ~", "/".join(map(short, k)), json.dumps(diff, default=str))
        for k in only_b:
            print("  - baseline only:", "/".join(map(short, k)))
        for k in only_g:
            print("  + generated only:", "/".join(map(short, k)))
    print("\nTOTAL", dict(totals))
    src = Counter(r["_from"].split(":")[0] for rows in generated.values() for r in rows)
    print("generated rows by source:", dict(src),
          "untraced:", sum(1 for rows in generated.values() for r in rows if not r.get("_from")))


if __name__ == "__main__":
    main(*sys.argv[1:])
