"""Probe corrections that change a book's identity (cr_01 P0 §3). Usage: probe_update.py <snapshot>"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "business_domains/book_library_mgmt/testbed/catalog")
import execution_validation as ev  # noqa: E402

run = ev.Run(Path(sys.argv[1]), Path(tempfile.mkdtemp(prefix="probe_")))
said = lambda label, value: print(f"{label:62} {value}")
books, copies, works = (lambda: run.store("books.json")), (lambda: run.store("physical_copies.json")), (lambda: run.store("works.json"))
fix = lambda key, fields: run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", ev.auth() | {
    "identity_key": key, "updated_fields": {**fields, "subject": ["epic"]}})

run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ODYSSEY, "BC-1"))
run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ILIAD, "BC-2"))
odyssey = next(k for k in books() if "odyssey" in k)
iliad = next(k for k in books() if "iliad" in k)

r = fix(odyssey, ev.ODYSSEY)
said("correct the subject only", f"{r.status}, subject {books()[odyssey].get('subject')}")

r = fix(odyssey, {**ev.ILIAD})
said("correct the Odyssey into the Iliad (a duplicate)", f"{r.status}, Odyssey still held: {odyssey in books()}")

fixed_year = {**ev.ODYSSEY, "publication_year": 1615}
r = fix(odyssey, fixed_year)
new = next((k for k in books() if "odyssey" in k), None)
said("correct the Odyssey's year (identity changes)", f"{r.status}, key {odyssey} -> {new}")
said("  its copy follows", f"BC-1 names {copies().get('BC-1', {}).get('identity_key')}")
r = run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ODYSSEY, "BC-3"))
said("  the old identity is free: register the 1614 Odyssey again", r.status)

retitled = {**ev.ILIAD, "title": "The Iliad of Homer"}
r = fix(iliad, retitled)
moved = next((b for k, b in books().items() if "iliad of homer" in k), {})
said("retitle the Iliad (its work changes)", f"{r.status}, work {moved.get('work_key')}, held: {moved.get('work_key') in works()}")
