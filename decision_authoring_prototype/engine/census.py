"""Step 1 census: classify every P7 register leaf as decision / case / mechanical / unaccounted."""
import json, re, sys
from collections import Counter, defaultdict
import yaml

path = sys.argv[1]
text = open(path).read()
reg = yaml.safe_load(re.findall(r"```yaml\n(.*?)```", text, re.S)[0])["registers"]

def leaves(x):
    if isinstance(x, dict):
        return sum(leaves(v) for v in x.values())
    if isinstance(x, list):
        return sum(leaves(v) for v in x)
    return 1

DOMAIN_FIELDS = {"title", "author", "publication_year", "subject", "barcode",
                 "book_fields", "copy_fields", "search_criteria", "updated_fields"}
ACTOR_FIELDS = {"staff_id", "staff_credentials"}
# Literals that state a rule, a schema or a state value: content only a human can decide.
RULE_STEPS = {"confirm_authorization", "refuse_incomplete_record", "require_submission_complete",
              "require_identity_unchanged", "refuse_incomplete_correction",
              "validate_book_fields", "validate_work_fields", "validate_edition_fields",
              "check_corrected_record"}
KEY_CTS = ("CT_PURE_FORM_BOOK_IDENTITY_KEY", "CT_PURE_FORM_WORK_IDENTITY_KEY")

count = Counter()
by_reg = defaultdict(Counter)
unaccounted = []

def add(r, cls, n, note=None):
    count[cls] += n
    by_reg[r][cls] += n
    if cls == "unaccounted":
        unaccounted.append((r, note))

for r, rows in reg.items():
    if not rows or not isinstance(rows, list):
        continue
    for row in rows:
        n = leaves(row)
        if r == "new_artifacts":
            fam = row["family"]
            if fam in ("WF", "AC", "EV"):
                add(r, "decision", 2)          # code + summary name an operation, actor or event
                add(r, "mechanical", n - 2)
            else:
                add(r, "mechanical", n)
        elif r == "interface_fields":
            name = row["artifact"]
            if row["field"] in DOMAIN_FIELDS and "::IN_" in name:
                add(r, "decision", n)          # what a request must carry
            elif "::AC_" in name:
                add(r, "decision", n)          # who the actor is and what authorizes them
            elif "::EV_" in name and row["field"] not in {"timestamp"} | ACTOR_FIELDS:
                add(r, "decision", n)          # what an event records
            else:
                add(r, "mechanical", n)
        elif r == "step_bindings":
            b = row["bound_to"]
            if isinstance(b, dict) and row["step"] in RULE_STEPS and row["field"] in ("rules", "schema"):
                add(r, "decision", n)
            elif isinstance(b, dict) and isinstance(b.get("literal"), dict) and b["literal"].get("state") in ("REGISTERED", "RETIRED"):
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
