#!/usr/bin/env bash
# Derive a business domain from its ledger and run it through the unchanged pipeline, in a scratch
# directory. Nothing in the domain repository or the working snapshot is touched.
#
# Usage: derive_build.sh <domain> <scratch dir>
#   <domain>  a folder under testbed/ledgers holding ledger.yaml, named as in business_domains/;
#             DECISION_LEDGERS names another folder of such folders
# The derived rows are written to <scratch dir>/generated.json.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
W="$(cd "$REPO/.." && pwd)"
NAME="${1:?usage: derive_build.sh <domain> <scratch dir>}"
S="${2:?usage: derive_build.sh <domain> <scratch dir>}"
HERE="${DECISION_LEDGERS:-$REPO/testbed/ledgers}/$NAME"
DOMAIN="$W/business_domains/$NAME"
BASELINE="$(ls "$DOMAIN"/design/p7_*.md)"
cd "$W"

echo "== derive"
rm -rf "$S/dossier" "$S/identity" "$S/domain" "$S/snapshot" && mkdir -p "$S"
tc phase derive design "$HERE/ledger.yaml" "$BASELINE" --out "$S/generated.json" \
  --retired .github/process/retired_identities.yaml

# Each artifact's identity is decided by meaning, against the composition the design is pinned to:
# the working snapshot, which holds the domain as its design of record describes it.
echo "== identities"
tc phase derive splice "$DOMAIN/design" "$S/generated.json" "$S/identity" >/dev/null
tc phase derive identities "$S/identity" "$S/generated.json" --snapshot snapshot --root "$DOMAIN" \
  --release pgc_release/snapshot --retired .github/process/retired_identities.yaml
tc phase derive splice "$DOMAIN/design" "$S/generated.json" "$S/dossier"

# The phase documents between the ledger and the design, each judged by the rule set that governs
# an authored one, against the documents it cites. P2 to P4 restate what the derivation observed,
# so they are projected once identities are decided.
echo "== phase documents"
rm -rf "$S/phases"
tc phase derive project "$HERE/ledger.yaml" "$BASELINE" --design "$S/generated.json" --snapshot snapshot \
  --out "$S/phases" >/dev/null
doc() { ls "$S"/phases/"$1"_*.md; }
admitted=0
for spec in "p0" "p1 --prior p0=$(doc p0)" "p2 --prior p1=$(doc p1)" "p3 --prior p2=$(doc p2)" \
            "p4 --prior p3=$(doc p3)" "p5 --prior p0=$(doc p0)" "p6 --prior p5=$(doc p5) --prior p0=$(doc p0)"; do
  set -- $spec; phase=$1; shift
  if tc phase check "$(doc "$phase")" --phase "$phase" --snapshot snapshot "$@" >"$S/phases/$phase.verdict"; then
    admitted=$((admitted + 1))
  else
    sed -n '1,6p' "$S/phases/$phase.verdict"
  fi
done
echo "  phase documents: $admitted/7 admissible (p0 to p6)"

echo "== construction check"
tc construction check "$S/dossier" --snapshot snapshot --root "$DOMAIN" | grep -v '^  OK'

echo "== emit, compile"
mkdir -p "$S/domain" && cp -R "$DOMAIN" "$S/domain/"
rm -rf "$S/domain/$NAME/snapshot/compiled"
# Artifacts the derived design no longer names. A replaced one stays until emit marks it superseded.
python - "$S/generated.json" "$S/domain/$NAME/registry" <<'PY'
import json, sys
from pathlib import Path
g = json.load(open(sys.argv[1]))
short = lambda c: c.split("::")[-1]
live = {short(r["code"]) for r in g["new_artifacts"]} | {short(c) for c in g["_identity"]["kept"]}
replaced = {short(c) for c in list(g["_identity"]["superseded"]) + list(g["_identity"]["replaced"])}
for p in Path(sys.argv[2]).rglob("*_V[0-9]*.md"):
    kept = p.stem.startswith("STRUCTURE_BUILD") or (p.stem.startswith("TEST_DATA_") and p.stem[10:] in live)
    if p.parent.name not in ("structures",) and p.stem not in live | replaced and not kept:
        p.unlink()
PY
tc construction emit "$S/dossier" --root "$S/domain/$NAME" --snapshot snapshot --force | grep -E "REFUSED|refused|changes meaning|still names|marked|emitted" | grep -v "^    "
# Delivery deletes what the design replaced or retired, and records each deletion as the retirement
# ledger takes it. In scratch, the record is written beside the build.
python - "$S/generated.json" "$S/domain/$NAME/registry" "$S/retirements.yaml" <<'PY'
import json, sys, yaml
from pathlib import Path
g = json.load(open(sys.argv[1]))["_identity"]
gone = {c: f"superseded by {n}: the ledger derives it with a changed meaning" for c, n in g["superseded"].items()}
gone.update({c: f"replaced by {n}: the ledger says it takes its place" for c, n in g["replaced"].items()})
gone.update({c: "the ledger no longer derives it" for c in g["retired"]})
for p in Path(sys.argv[2]).rglob("*_V[0-9]*.md"):
    if any(p.stem == c.split("::")[-1] for c in gone):
        p.unlink()
yaml.safe_dump({"retired": [{"identity": c, "decided_by": "the domain's ledger, as its owner answered it",
                             "determination": why, "change": "tc phase derive identities"}
                            for c, why in sorted(gone.items())]}, open(sys.argv[3], "w"), sort_keys=False)
print(f"  retired by record: {len(g['superseded'])} superseded, {len(g['replaced'])} replaced, "
      f"{len(g['retired'])} no longer derived")
PY
protocol_compiler/compile_domain.sh "$S/domain/$NAME" | grep -E 'Build Summary|conformance\]'

echo "== assemble"
roots=""
for r in "$W"/business_domains/*/snapshot/compiled "$W"/conformance_workloads/workloads/*/snapshot/compiled \
         "$W"/snapshot_inspector/snapshot/compiled "$W"/software_governance/snapshot/compiled \
         "$W"/transformation_compilers/snapshot/compiled; do
  [[ "$r" == "$DOMAIN/snapshot/compiled" ]] || roots="$roots$r:"
done
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 PGC_SOURCE_ROOTS="$roots$S/domain/$NAME/snapshot/compiled" \
  PGC_SNAPSHOT_OUT="$S/snapshot" ./snapshot_assembler/assemble.sh | grep -E 'round-trip|composition'

echo "== execution validation"
for t in "$DOMAIN"/testbed/*/execution_validation*.py; do
  echo "  ${t#$DOMAIN/testbed/}"
  python "$REPO/scripts/derive_suite.py" "$S/generated.json" "$t" "$S/snapshot" 2>&1 \
    | grep -E 'FAIL|criteria hold|Error' | sed 's/^/  /' || true
done
# Criteria the owner's answers added, which the domain's own suites do not hold yet.
for t in "$HERE"/checks/execution_validation*.py; do
  [[ -f "$t" ]] || continue
  echo "  owner answers: ${t#$HERE/}"
  python "$REPO/scripts/derive_suite.py" "$S/generated.json" "$t" "$S/snapshot" 2>&1 \
    | grep -E 'FAIL|criteria hold|Error' | sed 's/^/  /' || true
done
