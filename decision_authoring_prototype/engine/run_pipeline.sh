#!/usr/bin/env bash
# Derive a business domain from its ledger and run it through the unchanged pipeline, in a scratch
# directory. Nothing in the domain repository or the working snapshot is touched.
#
# Usage: run_pipeline.sh <domain> <scratch dir>
#   <domain>  a folder under ../domains holding ledger.yaml, named as in business_domains/
set -euo pipefail
ENGINE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROTO="$(cd "$ENGINE/.." && pwd)"
W="$(cd "$PROTO/../.." && pwd)"
NAME="${1:?usage: run_pipeline.sh <domain> <scratch dir>}"
S="${2:?usage: run_pipeline.sh <domain> <scratch dir>}"
HERE="$PROTO/domains/$NAME"
DOMAIN="$W/business_domains/$NAME"
BASELINE="$(ls "$DOMAIN"/design/p7_*.md)"
cd "$W"

(cd "$ENGINE" && python compose.py "$HERE/ledger.yaml" "$BASELINE") > "$HERE/generated.json"
rm -rf "$S/dossier" "$S/domain" "$S/snapshot"
python "$ENGINE/splice.py" "$DOMAIN/design" "$HERE/generated.json" "$S/dossier" whole

echo "== construction check"
tc construction check "$S/dossier" --snapshot snapshot --root "$DOMAIN" | grep -v '^  OK'

echo "== emit, compile"
mkdir -p "$S/domain" && cp -R "$DOMAIN" "$S/domain/"
rm -rf "$S/domain/$NAME/snapshot/compiled"
# Artifacts the derived design no longer names.
python - "$HERE/generated.json" "$S/domain/$NAME/registry" <<'PY'
import json, sys
from pathlib import Path
live = {r["code"].split("::")[-1] for r in json.load(open(sys.argv[1]))["new_artifacts"]}
for p in Path(sys.argv[2]).rglob("*_V[0-9]*.md"):
    kept = p.stem.startswith("STRUCTURE_BUILD") or (p.stem.startswith("TEST_DATA_") and p.stem[10:] in live)
    if p.parent.name not in ("structures",) and p.stem not in live and not kept:
        print("  removed", p.stem); p.unlink()
PY
tc construction emit "$S/dossier" --root "$S/domain/$NAME" --force | tail -1
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
  python "$t" "$S/snapshot" | grep -E 'FAIL|criteria hold' | sed 's/^/  /'
done
# Criteria the owner's answers added, which the domain's own suites do not hold yet.
for t in "$HERE"/checks/execution_validation*.py; do
  [[ -f "$t" ]] || continue
  echo "  prototype: ${t#$HERE/}"
  python "$t" "$S/snapshot" | grep -E 'FAIL|criteria hold' | sed 's/^/  /'
done
