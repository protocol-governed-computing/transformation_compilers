# Business Problem Statement

**Project Name:** book_library_mgmt — catalog

> **This dossier is at P0 and its phase run has not begun.** It records a confirmed business
> requirement and the execution path a change would take. It is not a design.

## 1. Context

Every catalog operation is admitted at a boundary before anything happens. The boundary states what a
requester must supply for that operation, and turns away a request that does not supply it. That
statement is the library's account of what each operation needs from the person performing it.

## 2. Problem Statement

**Two catalog operations turn away correct requests, because the boundary asks for things the
operation does not need.**

**Registering a further edition of a work the library already holds.** The boundary asks for the
publication year as text. The catalog records publication years as numbers, everywhere else it names
them — including at the boundary of the neighbouring operation that registers a work for the first
time. A librarian supplying the year the way the catalog holds it is turned away.

**Correcting the bibliographic information of a record.** The boundary asks for the title, the author
and the publication year of the record being corrected. A correction names the record it corrects and
supplies the fields it changes; it does not restate the fields it leaves alone. A librarian correcting
the subject headings of a record is turned away for not resupplying its title.

**Neither operation uses what it asks for.** The steps that carry out the correction read the record
named and the changed fields; they never read the title, author or year supplied alongside. The
boundary is asking for three things and discarding them, and refusing the request when they are
absent.

## 3. Why This Surfaced Now

**The boundary was not turning anyone away.** It admitted every request regardless of what was
supplied, so a statement of what an operation needs was never compared against anything and could
drift from the operation freely. The platform has since made the boundary determine admission from
what it declares, and these two statements turned out not to describe their operations.

**The requirement is confirmed rather than anticipated.** The library's own end-to-end exercise of the
catalog — registering a work, adding two further editions, correcting a legacy record — now fails at
the second edition and again at the correction. Both failures are correct behaviour by a boundary
enforcing a wrong statement.

## 4. What This Is Not

**It is not a relaxation.** Nothing about who may perform a catalog operation, or what they must be
authorised to do, changes. The boundary keeps every requirement that describes its operation and
loses the ones that do not.

**It is not a correction to the platform.** The boundary now does what it always declared it did. What
is wrong is what these two operations declared they need.
