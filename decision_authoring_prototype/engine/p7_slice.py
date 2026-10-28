"""Cut the rows of a P7 design intent that belong to a set of artifacts.

A row belongs to an artifact when its owning column names it. The slice is what the front end
must reproduce for that family; `compare.py` diffs two slices.
"""
import json
import sys

import yaml

from transformation.decision.splice import OWNER, short
from transformation.machine_block import machine_yaml


def load(path):
    text = open(path).read()
    return yaml.safe_load(machine_yaml(text) or text)["registers"]


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
