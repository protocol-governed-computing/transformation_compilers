"""Invoke the phase-workflow generator from a terminal.

The generator itself is `transformation.design.emit` — inside the package, because construction has
to be able to import and invoke it. This is the other caller: a person who has just edited a rule
module or a template and wants the workflows brought back into agreement.

Run:  python scripts/emit_rule_sets.py --snapshot <assembled snapshot> [--check]
Exit: 0 if every workflow already matched (or was rewritten), 1 under --check if any differed.
"""

from __future__ import annotations

import sys

from transformation.design.emit import emit


def main() -> int:
    # The default action writes, so an argument this script does not understand must stop it rather
    # than fall through to the default. Falling through, `--help` would re-emit every workflow and
    # report it as work done, the wrong way round for a flag whose whole meaning is "do nothing yet".
    args = sys.argv[1:]
    snapshot = None
    if "--snapshot" in args:
        at = args.index("--snapshot")
        snapshot = args[at + 1] if at + 1 < len(args) else None
        args = args[:at] + args[at + 2:]
    unknown = [a for a in args if a != "--check"]
    if unknown or snapshot is None:
        print(__doc__.strip())
        if unknown:
            print(f"\nunrecognised argument(s): {' '.join(unknown)}")
        else:
            print("\n--snapshot is required: the observing steps answer what its capability declares")
        return 2

    check_only = "--check" in args
    results = emit(snapshot, check_only=check_only)

    for e in results:
        state = "OK      " if not e.drifted else ("DRIFTED " if check_only else "WROTE   ")
        if e.unrecorded:
            state = "REFUSED "
        print(f"  {state} {e.phase}  {e.rules:>3} rules  {e.filename}")
        if e.unrecorded:
            print(f"           {e.unrecorded}")

    refused = [e for e in results if e.unrecorded]
    if refused:
        print(f"\n{len(refused)} rule set(s) changed without a recorded revision (REVISION_UNRECORDED).")
        return 1
    drifted = [e for e in results if e.drifted]
    if check_only and drifted:
        print(f"\n{len(drifted)} workflow(s) do not agree with the generator that produces them.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
