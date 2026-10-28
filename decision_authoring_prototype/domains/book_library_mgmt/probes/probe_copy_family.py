import sys, tempfile
from pathlib import Path
sys.path.insert(0, "business_domains/book_library_mgmt/testbed/catalog")
import execution_validation as ev
data = Path(tempfile.mkdtemp(prefix="probe_"))
run = ev.Run(Path(sys.argv[1]), data)
r = run("WF_REGISTER_BOOK_V0", ev.book_payload(ev.ODYSSEY, "BC-1")); print("register book", r.status)
key = next(iter(run.store("books.json")))
r = run("WF_REGISTER_PHYSICAL_COPY_V0", ev.auth() | {"identity_key": "no|such|book", "barcode": "BC-X", "copy_fields": {"barcode": "BC-X"}})
print("copy vs unknown book", r.status)
r = run("WF_REGISTER_PHYSICAL_COPY_V0", ev.auth() | {"identity_key": key, "barcode": "BC-X", "copy_fields": {"barcode": "BC-X"}})
print("copy BC-X vs real book", r.status, "| BC-X in copies:", "BC-X" in run.store("physical_copies.json"))
r = run("WF_RETIRE_PHYSICAL_COPY_V0", ev.auth() | {"barcode": "NOPE"}); print("retire unknown copy", r.status)
r = run("WF_RETIRE_PHYSICAL_COPY_V0", ev.auth() | {"barcode": "BC-1"}); r = run("WF_RETIRE_PHYSICAL_COPY_V0", ev.auth() | {"barcode": "BC-1"}); print("retire already-retired copy", r.status)
print("trail ops:", [t.get("operation") or t.get("record",{}).get("operation") for t in run.trail()])
