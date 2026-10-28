"""Cut the rows of a P7 design intent that belong to a set of artifacts.

A row belongs to an artifact when its owning column names it. The slice is what the front end
must reproduce for that family; `compare.py` diffs two slices.
"""
import json
import re
import sys

import yaml

# The column that names a row's owning artifact, per register.
OWNER = {
    "new_artifacts": "code",
    "rb_declarations": "binds_wf",
    "execution_topology": "workflow",
    "cc_composition": "cc_code",
    "step_bindings": "owner",
    "interface_fields": "artifact",
    "implementation_bindings": "ct_code",
    "runtime_policies": "rb_code",
    "artifact_properties": "artifact",
    "structure_stores": "store_name",
    "test_cases": "ct_code",
    "test_case_values": "ct_code",
}


def short(code):
    return str(code).split("::")[-1]


def load(path):
    text = open(path).read()
    block = re.findall(r"```yaml\n(.*?)```", text, re.S)
    return yaml.safe_load(block[0] if block else text)["registers"]


def cut(registers, members):
    out = {}
    for name, column in OWNER.items():
        rows = [row for row in registers.get(name) or [] if short(row.get(column)) in members]
        if rows:
            out[name] = rows
    return out


if __name__ == "__main__":
    registers = load(sys.argv[1])
    members = set(sys.argv[2].split(","))
    json.dump(cut(registers, members), sys.stdout, indent=1, default=str)
