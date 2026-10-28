# Brief — AI Governance

What the business requires of its AI licensing and of the AI agents acting for its people. AI
licensing grants employees licenses for AI tools and takes back the ones nobody uses. Agent
governance judges every action an AI agent proposes on a person's behalf, before any tool runs.

## Employees

- The system registers an employee by their employee id.
- A second registration of the same employee is refused.
- Recording training, provisioning a license and recording usage are refused for an employee
  nobody registered.

## Training

- The system records that an employee completed the required training.
- A license is refused to an employee whose training is not recorded, whatever the request says
  about their training.

## The cap

- The system sets the number of licenses the business allows to be assigned. Setting it again
  replaces it.
- A license is refused when as many licenses are assigned as the cap allows, whatever the request
  says about the cap or the count. Before any cap is set, no license can be provisioned.

## Licenses

- An employee is provisioned a license of a tier the request names: standard or enterprise. Any
  other tier is refused. One cap covers both tiers.
- A license's identity is formed by the business from the employee, and carries the prefix `lic`.
  An employee holds at most one active license; a second is refused.
- A refused provisioning is recorded as a denial, with the reason the failed check gives. Nobody
  can record a denial with a reason of their own.

## Usage and reclaim

- The system records each use of a license. The day of use is the day it is recorded, never a day
  the request names.
- A license provisioned and never used counts from the day it was provisioned.
- The system asks to reclaim one license at a time. A license unused for 30 days or more is
  reclaimed: it is released, and its revocation is recorded and announced. A license used more
  recently is left assigned, and the reclaim ends as still active.
- A reclaim whose removal the license registry refuses ends as still active. The license stays
  assigned, and no revocation is announced.
- A reclaimed license no longer counts against the cap.

## Agent actions

An agent proposes an action for a user. The business judges it in this order, and the first
check that fails denies it.

1. The request is well formed.
2. The tool is one the business declares: `READ_RECORD`, `PROVISION_STANDARD_LICENSE` or
   `PROVISION_PREMIUM_LICENSE`. Any other tool is denied as undeclared.
3. The user holds an active license. A user without one is denied as an unauthorized actor.
4. The user's tier allows the tool. A standard license allows reading a record and provisioning a
   standard license. An enterprise license also allows provisioning a premium license. Otherwise
   the action is denied as an unauthorized tool.
5. The parameters satisfy the tool's rules. Otherwise the action is denied as a parameter
   violation.
   - Reading a record: the record type is a license pool or a user profile, and an id is given.
   - Provisioning a standard license: the tier is standard, and the quantity is at most 100.
   - Provisioning a premium license: the tier is premium, and the quantity is at most 50.

- A user's license and tier are the ones AI licensing granted. A reclaimed license no longer
  authorizes anything.
- Every judgment is audited, authorized or denied. An authorized action is also registered, and
  the same action proposed again is registered once.
- An authorized action is announced with its tool, its user, the user's tier and its time. A
  denied one is announced with its tool, its user and the reason.
- A request's identity carries the prefix `AREQ`, and an action's carries `AGOV`.

## Announcements

Employee registered, training completed, license cap set, license provisioned, provision denied,
usage recorded, license revoked, agent action authorized, agent action denied.

## Records

- Every act records what it did on its part's audit trail, with the time it happened.
- A refused act changes no record, except that a refused provisioning is recorded as a denial.
