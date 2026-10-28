"""Probe the catalog's unstated behavior against a snapshot. Usage: probe_catalog.py <snapshot>"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "business_domains/book_library_mgmt/testbed/catalog")
import execution_validation as ev  # noqa: E402

run = ev.Run(Path(sys.argv[1]), Path(tempfile.mkdtemp(prefix="probe_")))
said = lambda label, value: print(f"{label:58} {value}")

run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ODYSSEY, "BC-1"))
key = next(iter(run.store("books.json")))
r = run("WF_RETIRE_BOOK_RECORD_V0", ev.auth() | {"identity_key": key})
r = run("WF_SEARCH_CATALOG_V0", ev.auth() | {"search_criteria": {"title": "The Odyssey"}})
said("search for a retired book, no state given", f"{r.status}, {len((r.surface or {}).get('matching_books') or [])} match(es)")
r = run("WF_SEARCH_CATALOG_V0", ev.auth() | {"search_criteria": {"title": "The Odyssey", "state": "RETIRED"}})
said("search for a retired book, caller asks for RETIRED", f"{r.status}, {len((r.surface or {}).get('matching_books') or [])} match(es)")
r = run("WF_RETIRE_BOOK_RECORD_V0", ev.auth() | {"identity_key": key})
said("retire an already-retired book", r.status)
r = run("WF_SEARCH_CATALOG_V0", ev.auth() | {"search_criteria": {"title": "No Such Book"}})
said("search that matches nothing", r.status)

r = run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ILIAD, "BC-1"))
said("register the Iliad with a barcode already owned", r.status)
r = run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ILIAD, "BC-2"))
said("then register the Iliad with a free barcode", f"{r.status}, held: {any('iliad' in k for k in run.store('books.json'))}")

AENEID = {"title": "The Aeneid", "author": "Virgil", "publication_year": 1697}
p = ev.book_payload(AENEID, "BC-3")
p["book_fields"]["state"] = "RETIRED"
r = run("WF_REGISTER_BOOK_V0", p)
state = next((b.get("state") for k, b in run.store("books.json").items() if "aeneid" in k), None)
said("register a book whose request says state RETIRED", f"{r.status}, recorded {state}")

r = run("WF_REGISTER_PHYSICAL_COPY_V0", ev.auth() | {"identity_key": "no|such|book", "barcode": "BC-X", "copy_fields": {"barcode": "BC-X"}})
r = run("WF_REGISTER_PHYSICAL_COPY_V0", ev.auth() | {"identity_key": key, "barcode": "BC-X", "copy_fields": {"barcode": "BC-X"}})
said("copy barcode reused after a refused registration", r.status)
