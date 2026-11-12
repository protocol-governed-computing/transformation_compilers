# Business Problem Statement

**Project Name:** book_library_mgmt — catalog

## 1. Context

The catalog registers the library's works, their editions and each edition's physical copies. It
retires and reinstates them, corrects their bibliographic information, and answers searches and
enquiries. Every one of those operations is performed by library staff, and each is refused to
anyone the library has not authorized.

The library has said who may perform a catalog operation, what a book's registration must contain,
what a work must name and what a further edition must contain. Those rules are the library's. Today
the catalog does not hold them: they travel with each request, and the catalog applies whatever the
request carries.

---

## 2. Problem Statement

**The catalog applies its rules as the request states them, so a request can change the rules it is
judged by — including the rule that decides who may use the catalog at all.**

Every catalog operation first confirms that the person performing it is authorized staff. It
confirms this against rules the request itself supplies. A request that supplies no rules is
confirmed whoever sends it: someone the library has not authorized registered a book by sending an
empty list of rules, and the catalog holds that book today in the same way as any other.

**A registration that breaks the library's description of a book is registered anyway.** The catalog
checks a book, a work and a further edition against what each must contain, finds what is missing,
and then registers them regardless. The check reports; nothing acts on the report. And what it checks
is a copy the request supplies alongside the book, not the book the catalog then records, so even a
check that refused would be judging something other than what is written.

**The descriptions themselves come from the request.** A request that supplies an empty description
of a book has nothing checked against it.

This change shall:

- hold in the catalog the rules that decide who is authorized to perform a catalog operation, and
  refuse anyone they do not admit, whatever the request says;
- hold in the catalog what a book, a work and a further edition must contain, and refuse a
  registration that does not meet it;
- check the book, work or edition the catalog records, not a copy supplied beside it;
- register a physical copy as registered, whatever state the request gives it;
- leave every correct request from authorized staff admitted, with the same outcome as today.

### What the library already decided about the catalog

These are settled and are not reopened by this change:

- **Only authorized staff perform catalog operations.** The catalog does not decide who is
  authorized; it requires that they are.
- **A book's bibliographic information is its title, author, publication year and subject.** It
  carries at least one subject, and the catalog records a publication year as a number.
- **A work names its title and author.**
- **A further edition is described as a book is.**

### What this change does not decide

- **Who a caller is.** The staff credentials a request presents are the request's own, and whether
  they are genuine is not a question the catalog answers. This change makes the catalog hold the
  rules those credentials are judged by; it does not authenticate the credentials.
- **Which staff are authorized.** That belongs to the staff function, which governs library
  employees.
- **Anything about loans, members or any function other than the catalog.**

### Left for later changes

- **Records already in the catalog.** The library adds to its record and does not rewrite it; a book
  registered under a request's own rules stays as it was made.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. The design process did not
assume them.

- **Should a registration that does not meet the library's description be refused, or registered and
  flagged?** Refused. The library said the parts are required.
- **Should the catalog refuse a request that states rules at all, or ignore the rules it states?**
  Ignore them. The catalog's rules are its own; what a request says about them is not part of the
  request.
- **A physical copy is registered in whatever state the request gives it, and one was registered
  already retired. Does the catalog hold that a copy is registered as registered?** Yes. A copy's
  registration leads to registered, whatever the request carries.
- **Does the catalog hold every rule of its own, including any discovery finds travelling with the
  request?** Yes, all of them.
