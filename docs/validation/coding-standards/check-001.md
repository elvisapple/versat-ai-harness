# CHECK-001 — Resolved coding policy and PR review

Outcome: pass. The existing exact-provider verifier accepted the canonical
index and lock entries in four synthetic consumer contexts: software without a
technology, software with Python, hybrid with Python, and library with Python.
All resolved the core coding Standard. Only the Python contexts resolved the
Python Standard.

Reviewed the policy and PR checklist with these cases:

- A function writes a payment record and decides whether the payment qualifies
  for a discount. The responsibilities change for separate reasons. The
  reviewer asks to isolate the policy from persistence and keep the dependency
  on a narrow storage contract so the policy can be exercised without I/O.
- A replacement storage implementation returns a missing-value sentinel while
  the existing contract promises a domain error. The reviewer rejects the
  substitution unless the implementation preserves that guarantee or the
  caller-facing change is reviewed. The interface review checks that clients
  depend on the operations they need, and that known variants can extend the
  boundary without edits to unrelated policy.

The Standard also gives naming and control-flow criteria. The PR template
directs reviewers to the Standard, whose verification boundary explicitly
reserves semantic design and changelog accuracy for people. The technology
Standard identifies the mechanical lint and formatter rules.
