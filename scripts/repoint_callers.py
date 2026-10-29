"""Callers outside a delivered domain: find each that names what the change supersedes, replaces or
retires, and repoint the ones that can be.

A domain's artifacts are named outside it: platform tests use them as fixtures, test corpora cite
them, regression steps dispatch them. A delivery that repoints only the domain's own testbed leaves
those naming identities that no longer exist, and the next run finds out.

- **A superseded or replaced artifact has a successor.** Every caller is repointed to it, in place.
- **A retired artifact has none.** No text substitution keeps a caller meaning what it did, so the
  delivery is refused before anything is written, naming each caller.
- **Another domain's declaration that names a changed artifact** is that domain's own change, so it
  refuses the delivery too.

A caller is a source file in a repository of the workspace: code, scripts, payloads, and fixtures
under a `testbed/`, and the workspace process (the runbook's commands). History is not a caller and
is never rewritten: documents, dossiers, designs of record, snapshots and the retirement ledger. A full name (`<domain>::<CODE>`) is matched
anywhere. A short name is matched only in a file that also names the domain, because short names are
unique only within a domain.

Usage: repoint_callers.py check <workspace> <domain> <generated.json>
       repoint_callers.py apply <workspace> <domain> <generated.json>
Exit:  0, or 1 when `check` finds a caller the delivery cannot repoint.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

CODE = (".py", ".json", ".sh", ".yaml", ".yml", ".html", ".js")
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", "snapshot", "compiled", "traces", "dist",
             "cr_dossiers", "dossiers", "doc"}
HISTORY = {"retired_identities.yaml", "route_seals.yaml"}
RECORD = re.compile(r"^p[78]_.*_baseline\.md$")   # a design of record, regenerated from its registry


def short(code: str) -> str:
    return code.split("::")[-1]


def gone(generated: dict) -> tuple[dict[str, str], list[str]]:
    """{predecessor: successor} for what the change supersedes or replaces, and what it retires."""
    i = generated["_identity"]
    return {**i["superseded"], **i["replaced"]}, list(i["retired"])


def callers(workspace: Path, domain: str):
    """Every caller file outside the domain, with whether it is another domain's declaration."""
    for repo in sorted(p for p in workspace.iterdir() if (p / ".git").exists() and p.name != "pgc_release"):
        for path in repo.rglob("*"):
            rel = path.relative_to(workspace)
            parts = set(rel.parts[:-1])
            if (not path.is_file() or parts & SKIP_DIRS or path.name in HISTORY or RECORD.match(path.name)
                    or rel.parts[1] == "build"):
                continue
            if rel.parts[:2] == ("business_domains", domain):
                continue
            declaration = "registry" in parts and path.suffix == ".md"
            if path.suffix in CODE or declaration or (path.suffix == ".md" and parts & {"testbed", "process"}):
                yield path, declaration


def pattern(names: list[str], text: str, domain: str) -> re.Pattern | None:
    """Full names always; short names only where the file names the domain."""
    alternatives = [re.escape(f"{domain}::{short(n)}") for n in names]
    if domain in text:
        alternatives += [re.escape(short(n)) for n in names]
    return re.compile(r"(?<![A-Za-z0-9_])(" + "|".join(alternatives) + r")(?![A-Za-z0-9_])") if names else None


def check(workspace: Path, domain: str, generated: dict) -> list[str]:
    moved, retired = gone(generated)
    problems = []
    for path, declaration in callers(workspace, domain):
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(workspace)
        if retired and (p := pattern(retired, text, domain)) and (m := p.search(text)):
            problems.append(f"{rel} names {m.group(1)}, which this change retires with no successor")
        if declaration and moved and (p := pattern(list(moved), text, domain)) and (m := p.search(text)):
            problems.append(f"{rel} declares a reference to {m.group(1)}: repointing another domain's "
                            "declaration is that domain's own change")
    return problems


def apply(workspace: Path, domain: str, generated: dict) -> list[str]:
    moved, _ = gone(generated)
    to = {**{short(o): short(n) for o, n in moved.items()},
          **{f"{domain}::{short(o)}": f"{domain}::{short(n)}" for o, n in moved.items()}}
    touched = []
    for path, declaration in callers(workspace, domain):
        if declaration:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        p = pattern(list(moved), text, domain)
        if p is None:
            continue
        new = p.sub(lambda m: to[m.group(1)], text)
        if new != text:
            path.write_text(new, encoding="utf-8")
            touched.append(str(path.relative_to(workspace)))
    return touched


def main() -> int:
    mode, workspace, domain, generated = sys.argv[1], Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
    g = json.loads(generated.read_text(encoding="utf-8"))
    if mode == "check":
        problems = check(workspace, domain, g)
        for line in problems:
            print(f"  CALLER OUTSIDE THE DOMAIN: {line}")
        return 1 if problems else 0
    touched = apply(workspace, domain, g)
    print(f"  callers outside the domain repointed to successors: {len(touched)} file(s)")
    for rel in touched:
        print(f"    {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
