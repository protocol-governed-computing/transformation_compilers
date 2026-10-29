#!/usr/bin/env bash
# Run a domain's acceptance criteria against the domain as it was before a change: the domain at a
# git revision, compiled and assembled with the rest of the working composition, in scratch. Nothing
# in the workspace is touched.
#
# Usage: criteria_before.sh <domain> <git revision of business_domains> <suite>...
#   <suite>  a path under the domain, as the working tree holds it now
#
# A change's criteria are worth what they tell apart. Run against the composition before the change,
# a criterion the change delivers fails; run after, it holds. derive_deliver.sh does both for every
# change it delivers. This script does the first half for a change delivered before it did.
set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
W="$(cd "$REPO/.." && pwd)"
NAME="${1:?usage: criteria_before.sh <domain> <revision> <suite>...}"
REV="${2:?usage: criteria_before.sh <domain> <revision> <suite>...}"
shift 2
S="$(mktemp -d)"
trap 'rm -rf "$S"' EXIT
cd "$W"

echo "== $NAME at $REV"
mkdir -p "$S/domain"
git -C business_domains archive "$REV" "$NAME" | tar -x -C "$S/domain"
rm -rf "$S/domain/$NAME/snapshot/compiled"
# The domain's transforms as they were: its package from the revision, ahead of the working tree's.
export PGC_IMPL_ROOTS="$S/domain:$W/software_governance:$W/conformance_workloads:$W/business_domains"
protocol_compiler/compile_domain.sh "$S/domain/$NAME" | grep -E 'Build Summary|conformance\]'
roots=""
for r in "$W"/business_domains/*/snapshot/compiled "$W"/conformance_workloads/workloads/*/snapshot/compiled \
         "$W"/snapshot_inspector/snapshot/compiled "$W"/software_governance/snapshot/compiled \
         "$W"/transformation_compilers/snapshot/compiled; do
  [[ "$r" == "$W/business_domains/$NAME/snapshot/compiled" ]] || roots="$roots$r:"
done
PGC_SNAPSHOT_PROFILE=GOVERNANCE_SURFACE_PROFILE_V0 PGC_SOURCE_ROOTS="$roots$S/domain/$NAME/snapshot/compiled" \
  PGC_SNAPSHOT_OUT="$S/snapshot" ./snapshot_assembler/assemble.sh | grep -E 'round-trip'

echo "== criteria, before the change"
for suite in "$@"; do
  echo "  $suite"
  python "$REPO/scripts/criteria_run.py" "$W/business_domains/$NAME/$suite" "$S/snapshot" "$S/domain" 2>&1 \
    | grep -E '^\s*(OK|FAIL)\s|criteria hold' | sed 's/^/  /' || true
done
