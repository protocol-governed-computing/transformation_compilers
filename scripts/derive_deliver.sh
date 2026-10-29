#!/usr/bin/env bash
# Deliver one change request that the derive route designed: from the change's ledger to the
# domain's artifacts, its design of record, the working snapshot and the retirement ledger.
# derive_build.sh rehearses the same steps in scratch; this one writes the real ones.
#
# Usage: derive_deliver.sh <domain> <cr dir>
#   <domain>  a folder under business_domains/
#   <cr dir>  business_domains/<domain>/cr_dossiers/cr_NN_<subject>/, holding the change's
#             ledger.yaml. The dossier is written beside it: baseline.json, P0 to P8.
#
# The ledger is the decision; everything else here is derived from it and the composition it is
# designed against. Nothing is committed. Run the domain's suites and the regression afterwards.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
W="$(cd "$REPO/.." && pwd)"
NAME="${1:?usage: derive_deliver.sh <domain> <cr dir>}"
CR="$(cd "${2:?usage: derive_deliver.sh <domain> <cr dir>}" && pwd)"
CR_NAME="$(basename "$CR")"
DOMAIN="$W/business_domains/$NAME"
BASELINE="$(ls "$DOMAIN"/design/p7_*.md)"
LEDGER="$CR/ledger.yaml"
S="$(mktemp -d)"
trap 'rm -rf "$S"' EXIT
cd "$W"
[[ -f "$LEDGER" ]] || { echo "no ledger at $LEDGER"; exit 1; }

# The change is designed against the composition as it stands, which holds the domain as its
# design of record describes it (rulings: a change request pins the composition without its own
# output).
echo "== pin"
tc baseline show --snapshot snapshot > "$CR/baseline.json"

echo "== derive"
tc phase derive design "$LEDGER" "$BASELINE" --out "$S/generated.json"
tc phase derive splice "$DOMAIN/design" "$S/generated.json" "$S/identity" >/dev/null
tc phase derive identities "$S/identity" "$S/generated.json" --snapshot snapshot --root "$DOMAIN" \
  --release pgc_release/snapshot --retired .github/process/retired_identities.yaml
tc phase derive splice "$DOMAIN/design" "$S/generated.json" "$S/dossier" >/dev/null
for f in "$S"/dossier/p[78]_*.md; do
  b="$(basename "$f")"; cp "$f" "$CR/${b/_baseline.md/_$CR_NAME.md}"
done

echo "== phase documents"
tc phase derive project "$LEDGER" "$BASELINE" --design "$S/generated.json" --snapshot snapshot \
  --cr "$CR_NAME" --out "$CR" >/dev/null
doc() { ls "$CR"/"$1"_*.md; }
admitted=0
for spec in "p0" "p1 --prior p0=$(doc p0)" "p2 --prior p1=$(doc p1)" "p3 --prior p2=$(doc p2)" \
            "p4 --prior p3=$(doc p3)" "p5 --prior p0=$(doc p0)" "p6 --prior p5=$(doc p5) --prior p0=$(doc p0)"; do
  set -- $spec; phase=$1; shift
  if tc phase check "$(doc "$phase")" --phase "$phase" --snapshot snapshot "$@" >"$S/$phase.verdict"; then
    admitted=$((admitted + 1))
  else
    sed -n '1,6p' "$S/$phase.verdict"
  fi
done
echo "  phase documents: $admitted/7 admissible (p0 to p6)"
[[ $admitted == 7 ]] || { echo "  not delivered: a phase document is inadmissible"; exit 1; }

echo "== construction check"
tc construction check "$CR" --snapshot snapshot | grep -E "Completeness|REFUSED|refused" | grep -v '^  OK'

echo "== emit"
# Artifacts the derived design no longer names. A replaced one stays until emit marks it superseded.
python - "$S/generated.json" "$DOMAIN/registry" <<'PY'
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
tc construction emit "$CR" --root "$DOMAIN" --snapshot snapshot --force \
  | grep -E "REFUSED|refused|changes meaning|still names|marked|emitted" | grep -v "^    " || true

# Delivery deletes what the design superseded, replaced or retired, and records each deletion in
# the retirement ledger. Callers in the domain's testbed and client are repointed to successors.
python - "$S/generated.json" "$DOMAIN" "$W/.github/process/retired_identities.yaml" "$CR_NAME" <<'PY'
import json, re, sys
from pathlib import Path
import yaml
g = json.load(open(sys.argv[1]))["_identity"]
domain, ledger_path, cr = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
short = lambda c: c.split("::")[-1]
gone = {c: (n, f"superseded by {short(n)}: the change's ledger derives it with a changed meaning")
        for c, n in g["superseded"].items()}
gone.update({c: (n, f"replaced by {short(n)}: the change's ledger says it takes its place")
             for c, n in g["replaced"].items()})
gone.update({c: (None, "the change's ledger no longer derives it") for c in g["retired"]})
for p in (domain / "registry").rglob("*_V[0-9]*.md"):
    if any(p.stem == short(c) for c in gone):
        p.unlink()
ledger = yaml.safe_load(ledger_path.read_text(encoding="utf-8")) or {}
entries = ledger.get("retired") or []
for c, (successor, why) in sorted(gone.items()):
    entry = {"identity": c, "decided_by": "the domain owner, through the change's ledger",
             "determination": why + "; no retention condition is declared",
             "change": f"{domain.name}/cr_dossiers/{cr}"}
    if successor:
        entry["superseded_by"] = successor
    entries.append(entry)
text = ledger_path.read_text(encoding="utf-8")
head = text[:text.index("retired:")]
ledger_path.write_text(head + yaml.safe_dump({"retired": entries}, sort_keys=False, allow_unicode=True, width=100),
                       encoding="utf-8")
moved = {short(c): short(n) for c, (n, _) in gone.items() if n}
touched = set()
for root in ("testbed", "client"):
    for p in (domain / root).rglob("*"):
        if p.is_file() and p.suffix in (".py", ".json", ".html", ".js", ".yaml", ".md"):
            text = p.read_text(encoding="utf-8")
            new = re.sub(r"\b(" + "|".join(map(re.escape, moved)) + r")\b", lambda m: moved[m.group(1)], text) \
                if moved else text
            if new != text:
                p.write_text(new, encoding="utf-8")
                touched.add(str(p.relative_to(domain)))
named = sorted({str(p.relative_to(domain)) for root in ("testbed", "client") for p in (domain / root).rglob("*")
                if p.is_file() and p.suffix in (".py", ".json", ".html", ".js")
                and any(re.search(r"\b" + short(c) + r"\b", p.read_text(encoding="utf-8"))
                        for c in g["retired"])})
print(f"  retired by record: {len(g['superseded'])} superseded, {len(g['replaced'])} replaced, "
      f"{len(g['retired'])} no longer derived")
print(f"  callers repointed to successors: {len(touched)} file(s)")
for p in named:
    print(f"  STILL NAMES A RETIRED IDENTITY: {p}")
PY

echo "== compile, assemble, design of record"
rm -rf "$DOMAIN/snapshot/compiled"   # what the domain compiled before, including what it no longer has
protocol_compiler/compile_domain.sh "$DOMAIN" | grep -E 'Build Summary|conformance\]'
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 ./snapshot_assembler/assemble.sh | grep -E 'round-trip|composition'
(cd "$REPO" && python scripts/write_baseline_designs.py >/dev/null && python scripts/write_baseline_designs.py --check)

echo "== execution validation"
for t in "$DOMAIN"/testbed/*/execution_validation*.py; do
  echo "  ${t#$DOMAIN/testbed/}"
  python "$t" 2>&1 | grep -E 'FAIL|criteria hold|Error' | sed 's/^/  /' || true
done
