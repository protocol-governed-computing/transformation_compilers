# Business Problem Statement

**Project Name:** book_library_mgmt

## 1. Context

This is a new project that does not seem to be part of current software baseline

The proposed name of the project is book_library_mgmt.

The projecy scope includes following functions for managing the library of books

- catalog
- circulation
- patron
- staff
- reservations
- acquisitions
- inventory
- notifications
- policy
- reporting

The scope of this CR-1 is limited to "catalog" function only

## 2. Problem Statement

A community library maintains thousands of books and other published materials. Throughout this
statement, "book" is the general term for anything the library catalogs, including published
materials that are not books.

Library staff currently maintain catalog records manually, leading to inconsistent descriptions,
duplicate entries, and difficulty locating materials.

The library requires a governed catalog management capability that provides a single authoritative
record for each book and each physical copy owned by the library.

Each book in the catalog is described by basic bibliographic information: title, author, publication
year, and subject. Subject says what kind of book it is, and is what staff search on when they are
looking for material rather than for a known title. A book carries at least one subject and may carry
several.

Title, author and publication year together identify a book. Two registrations with the same title,
author and publication year describe the same book, and the catalog holds one record for it.

Title and author are compared without regard to letter case or repeated spacing. "The Odyssey" and
"the odyssey" are the same title. Case and spacing do not change which book is meant, so they must not
produce two records.

The system shall allow authorized staff to:

- register new books
- register physical copies
- update bibliographic information
- retire obsolete records
- search the catalog
- retrieve complete book details

Each physical copy shall belong to exactly one book.

Every business operation shall be traceable and auditable.

The catalog starts empty. The records staff maintain manually today are not imported by this
change.

This release intentionally excludes borrowing, reservations, fines, patron management,
acquisitions, and inventory reconciliation.

The above capabilities are expected to be introduced through future governed change requests rather
than being designed into the initial solution.

## 3. Clarifications answered by the business author

Registering a book requires at least one physical copy. A book is never registered without a copy.

Each physical copy carries a barcode the library assigns, which identifies that copy among all the
copies the library owns.

A physical copy may be retired on its own, when it is lost or damaged.

A physical copy may be registered against a retired book.

A catalog record is never deleted. Retirement is the only way a record leaves use.

Retirement may be reversed: authorized staff may return a retired book record or a retired physical
copy to the registered state.

An update to bibliographic information may change the title, author or publication year. The update
is refused when the changed title, author and publication year would match another registered book,
because that would make one book a duplicate of another.

No retirement follows automatically from another: retiring a book record does not retire its copies,
and retiring the last copy does not retire the book. Staff retire each record explicitly.

A registration whose title, author and publication year match a registered book is refused, because
the book already exists. Staff register a further physical copy against it instead.

A book's subject is free text. The library maintains no list of permitted subjects.

Staff search the catalog by subject or by title. A search returns the bibliographic information of
each matching registered book, and nothing about its physical copies.

A retired book is excluded from search results, and its details remain retrievable.

Retrieving complete book details returns the book's bibliographic information and the physical copies
the library holds of it.

The catalog does not manage which staff are authorized. It requires staff to be authorized; deciding
who is authorized is deferred to the staff function, which governs library employees. Patrons are
library users, not employees, and the patron function does not decide staff authorization.

The nine remaining project functions are adjacent to this change: named and planned, and not
governed by it.
