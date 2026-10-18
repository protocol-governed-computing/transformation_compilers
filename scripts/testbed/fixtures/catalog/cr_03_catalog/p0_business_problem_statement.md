# Business Problem Statement

**Project Name:** book_library_mgmt

## 1. Context

The catalog holds what the library knows about its books: the works it carries, the editions of
those works, and the physical copies on its shelves. It records each one being registered, its
details being corrected, and its being retired or reinstated.

The business decided at the outset that the catalog announces the moments that matter. Six such
moments are declared: a work registered, a book registered, a physical copy registered,
bibliographic information updated, a book retired, a physical copy retired.

None of them is announced.

---

## 2. Problem Statement

**The catalog says it announces six moments and announces none of them.**

Each of the six is declared. Nothing anywhere refers to any of them, so no announcement can be made
from anywhere. A librarian's system waiting to be told that a copy had been shelved would wait
forever, and nothing would report a fault.

This is not a new requirement. The business already decided these moments are announced, and the
catalog has been silent since it was built. It is a defect, and the same one the identity function
was found to have.

What makes it worth stating plainly is how it stayed hidden. Nothing checks whether a declared moment
is ever announced. The catalog can declare six announcements, make none, and pass every check that
exists.

This change shall:

- make the six declared moments actually announce, at the moments they name;
- check that they do, so that the silence cannot return unnoticed.

### What a caller sees

Nothing. What a caller sends and is told back is unchanged. This is invisible from outside the
system, and it should be.

### What this change does not decide

- **What any listener does with an announcement.** The catalog announces the moment; who attends to
  it is a separate matter and a later one.
- **Whether the six are the right six.** They are the moments the business already declared. Whether
  the catalog should announce more is not this change.
- **Anything about what the catalog holds or how it is searched.** Only the announcing.
- **Anything outside the catalog.** No other subdomain is touched.

### Left for later changes

- **Moments that occurred before this change.** The catalog does not go back and announce them. The
  record is added to and never rewritten.

---

## 3. Clarifications answered by the business author

These questions were put to the business author and answered by them. Where the business had already
settled a convention elsewhere, the answer is that convention. The design process did not assume them.

- **Is each of the six announced at the successful completion of the act it names?** Yes. A moment is
  announced when the act it names has completed and not before.
- **When an act is refused, is anything announced?** No. A refusal is not a moment the catalog
  announces; nothing happened that anyone need be told about.
- **Does a reinstatement announce a moment of its own?** **No. Reinstatement is silent.** The catalog
  performs it and records it, and announces nothing. The six declared moments are the complete set,
  and no seventh is added by this change.
- **What must an announcement carry?** Which thing it concerns and when it occurred. Nothing further.
- **Who is expected to hear these announcements today?** Nobody. The moment exists for the record
  rather than for a listener, and that is a sufficient reason for it to exist.
