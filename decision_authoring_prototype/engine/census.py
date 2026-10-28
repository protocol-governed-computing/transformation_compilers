"""Step 1 census: classify every P7 register leaf as decision / case / mechanical / unaccounted.

Usage: census.py <p7 document> <census_profile.yaml>
The profile names what in one domain's P7 states a human decision.
"""
import re, sys
from collections import Counter, defaultdict
import yaml

from transformation.machine_block import machine_yaml

path, profile_path = sys.argv[1], sys.argv[2]
text = open(path).read()
reg = yaml.safe_load(machine_yaml(text))["registers"]
prof = yaml.safe_load(open(profile_path))

def leaves(x):
    if isinstance(x, dict):
        return sum(leaves(v) for v in x.values())
    if isinstance(x, list):
        return sum(leaves(v) for v in x)
    return 1

DOMAIN_FIELDS = set(prof["domain_fields"])
ACTOR_FIELDS = set(prof["actor_fields"])
# Literals that state a rule, a schema or a state value: content only a human can decide.
RULE_STEPS = set(prof.get("rule_steps", []))
RULE_FIELDS = set(prof.get("rule_fields", []))
# Fields whose literal states a decision wherever they are bound.
DECISION_FIELDS = set(prof.get("decision_fields", []))
KEY_CTS = tuple(prof.get("key_cts", []))
STATES = set(prof["states"])
# Event fields the trail supplies rather than the business.
EVENT_MECHANICAL = {"timestamp"} | set(prof.get("event_mechanical_fields", [])) | ACTOR_FIELDS

count = Counter()
by_reg = defaultdict(Counter)

def add(r, cls, n):
    count[cls] += n
    by_reg[r][cls] += n

def states_a_state(lit):
    if isinstance(lit, dict):
        return lit.get("state") in STATES
    if isinstance(lit, list):
        return bool(lit) and all(v in STATES for v in lit)
    return lit in STATES

for r, rows in reg.items():
    if not rows or not isinstance(rows, list):
        continue
    for row in rows:
        n = leaves(row)
        if r == "new_artifacts":
            fam = row["family"]
            if fam in ("WF", "AC", "EV", "TI"):
                add(r, "decision", 2)          # code + summary name an operation, actor, event or offered act
                add(r, "mechanical", n - 2)
            else:
                add(r, "mechanical", n)
        elif r == "interface_fields":
            name = row["artifact"]
            if row["field"] in DOMAIN_FIELDS and "::IN_" in name:
                add(r, "decision", n)          # what a request must carry
            elif "::AC_" in name:
                add(r, "decision", n)          # who the actor is and what authorizes them
            elif "::EV_" in name and row["field"] not in EVENT_MECHANICAL:
                add(r, "decision", n)          # what an event records
            else:
                add(r, "mechanical", n)
        elif r == "step_bindings":
            b = row["bound_to"]
            lit = b.get("literal") if isinstance(b, dict) else None
            if isinstance(b, dict) and row["step"] in RULE_STEPS and row["field"] in RULE_FIELDS:
                add(r, "decision", n)
            elif lit is not None and row["field"] in DECISION_FIELDS:
                add(r, "decision", n)
            elif lit is not None and states_a_state(lit):
                add(r, "decision", n)          # lifecycle state
            else:
                add(r, "mechanical", n)
        elif r == "cc_composition":
            if row["kind"] == "CT" and any(k in row["capability"] for k in KEY_CTS):
                add(r, "decision", 1)          # consumes: which attributes form an identity
                add(r, "mechanical", n - 1)
            else:
                add(r, "mechanical", n)
        elif r == "artifact_properties":
            if row["property"].startswith("emit."):
                add(r, "decision", 1)          # which operations publish which events
                add(r, "mechanical", n - 1)
            else:
                add(r, "mechanical", n)
        elif r == "transport_bindings":
            add(r, "decision", 1)              # operation: the public name of an offered act
            add(r, "mechanical", n - 1)
        elif r == "vocabulary_extensions":
            add(r, "decision", 1)              # value: a name the business chose
            add(r, "mechanical", n - 1)
        elif r in ("test_cases", "test_case_values"):
            add(r, "case", n)
        else:
            add(r, "mechanical", n)

total = sum(count.values())
print(f"total leaves: {total}")
for k in ("decision", "case", "mechanical", "unaccounted"):
    print(f"  {k:12} {count[k]:5}  {100*count[k]/total:5.1f}%")
print()
for r, c in by_reg.items():
    print(f"  {r:26} " + "  ".join(f"{k}={c[k]}" for k in ("decision", "case", "mechanical") if c[k]))
