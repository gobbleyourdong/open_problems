# Kontorovich Lean-RH — github.com/AlexKontorovich/Lean-RH

> Author: Alex Kontorovich
> Last commit: October 14, 2020 (dormant 5.5 years)
> Lean version: Lean 3 (community edition 3.18.4)

## What it has
- RH statement via Dirichlet eta: if 0 < Re(s) < 1 and η(s) = 0, then Re(s) = 1/2
- Convergence proof for eta series (Cauchy criterion)
- Custom abstract algebra typeclasses (not Mathlib)

## What it doesn't have
- No Li criterion, no Robin inequality, no de Bruijn-Newman
- No structural analysis of certificates
- No meta-theorems about proof strategy
- No partial results

## Compatibility with our work
NONE. Lean 3 vs our Lean 4. Custom types vs our axiom-level approach.
Cannot import or contribute without a full Lean 3→4 port.

## Our CertificateEquivalence.lean is strictly more useful
We prove: all known RH certificates are EQUIVALENT to RH (not weaker),
therefore certificate accumulation can't advance the proof. Kontorovich
only states RH; we prove something ABOUT RH's proof structure.
