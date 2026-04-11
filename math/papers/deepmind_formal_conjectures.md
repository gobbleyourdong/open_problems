# DeepMind formal-conjectures — github.com/google-deepmind/formal-conjectures

> Lean 4.27.0, Mathlib v4.27.0
> Purpose: benchmark collection of formalized conjecture STATEMENTS (not proofs)

## What they have (merged)
- **P vs NP:** Cook's verifier-based NP, polynomial reductions, NP-completeness, SAT, 3SAT
- **Riemann Hypothesis:** statement via Dirichlet eta
- **Poincaré:** statement (with sorry)

## What they DON'T have (open issues, no PRs merged)
- **Navier-Stokes:** issues #1457, #2293 — stalled, awaiting author
- **Yang-Mills:** issue #2365 — "needs-prerequisites", no PR
- **BSD:** issue #1414 — open, no merged formalization
- **Hodge:** issue #1276 — vague formulation

## Contribution opportunity from our repo

We have ACTUAL PROVED THEOREMS (not just sorry statements):
- `ns_blowup/lean/SingleMode.lean` — strain orthogonality, fully proved
- 8 YM Lean files covering lattice gauge, convexity, MK decimation
- `CertificateEquivalence.lean` — meta-theorem about RH proof structure
- `liouville_conjecture/lean/` — 5 files including small-data decomposition

Their repo is breadth (hundreds of conjectures, all sorry).
Ours is depth (dozens of theorems, many proved).

## How to contribute
- Sign Google CLA
- Downgrade from our Lean 4.29 to their 4.27
- Best targets: NS statement (issue #1457 is stalled), YM definitions
- Link our proof repo externally (they cap proofs at 25-50 lines)
- Our SingleMode.lean is exactly the kind of short result they accept

## Strategic value
Contributing our NS/YM formalizations to DeepMind's repo gives visibility
to our work and connects us to the largest formal math community project.
Their issues are stalled — we can fill the gap.
