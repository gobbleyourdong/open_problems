# Attempt 002 — Route Survey

**Date**: 2026-04-07
**Phase**: 0 → 1 (Paper Arsenal)
**Track**: theory (Theory)

## The Five Routes

### Route 1: Hilbert-Pólya (Spectral) ★★★★
**Idea**: Find a self-adjoint operator H on a Hilbert space such that
the eigenvalues of 1/2 + iH are the non-trivial zeros of ζ(s).
Self-adjointness → eigenvalues real → zeros on Re(s) = 1/2.

**Status**:
- Berry-Keating (1999): conjectured H = xp + px (quantization of the
  classical Hamiltonian xp). Not self-adjoint on standard L² spaces.
- Connes (1999): trace formula approach via noncommutative geometry.
  Constructed an operator but its spectral properties don't directly give RH.
- Sierra-Townsend (2011): regularized xp model. Reproduces low zeros approximately.
- de Branges: claimed proof via de Branges spaces. Not accepted.
- Bender-Brody-Müller (2017): PT-symmetric quantum mechanics approach.
  Published in PRL but gaps identified by community.

**Gap**: No one has constructed a RIGOROUSLY self-adjoint operator whose
spectrum matches the zeros. The operator is "morally" xp but making it
self-adjoint requires boundary conditions that encode the arithmetic.

**systematic approach fit**: HIGH. The operator, if found, can be studied numerically
(eigenvalue computation). The construction might be formalizable.

### Route 2: Arithmetic Geometry (Weil Analog) ★★★★★
**Idea**: Weil proved RH for curves over F_q using:
1. Intersection theory on the curve × curve
2. Positivity of the intersection form
3. The Castelnuovo-Severi inequality

For ζ(s) over Q: need an "arithmetic surface" and a positivity argument.

**Status**:
- Weil (1948): proved RH for curves over F_q
- Deligne (1974): proved RH for varieties (Weil conjectures)
- Deninger (1990s): proposed a cohomological framework, "arithmetic site"
- Connes-Consani (2010s): "arithmetic site" using tropical geometry and
  the "field with one element" F₁
- No one has completed the program for ζ(s)

**Gap**: The positivity argument. Weil's proof uses the Hodge index theorem
(intersection form is positive definite on a specific subspace). For the
arithmetic case, the analog of the intersection form is the Weil explicit
formula, and positivity is equivalent to RH itself. CIRCULAR.

**systematic approach fit**: HIGH conceptually but the gap IS the problem.

### Route 3: Analytic (Zero-Free Region) ★★
**Idea**: Push the zero-free region closer to Re(s) = 1/2.
Current: 1 - c/(log t)^{2/3}(log log t)^{1/3}.
Need: 1/2 (or just 1/2 + ε for all ε).

**Status**: Stuck since Vinogradov-Korobov (1958). 65+ years with no
improvement to the EXPONENT 2/3. Minor constant improvements only.

**Gap**: The exponential sum methods that give the zero-free region seem
to have a natural barrier at exponent 2/3. New ideas needed.

**systematic approach fit**: LOW. This is a dead end without a new technique.

### Route 4: Criterion-Based (Li, Nyman-Beurling) ★★★
**Idea**: Prove an equivalent criterion.
- Li: λ_n = (1/((n-1)!) (d/ds)^n [s^{n-1} log ξ(s)]|_{s=1} ≥ 0 for all n
- Robin: σ(n) < e^γ n log log n for n > 5040

**Status**:
- Li (1997): proved equivalence. λ_n computed for n up to ~10^4.
- Robin (1984): proved equivalence. Verified for n up to ~10^{10}.
- Nyman-Beurling: Báez-Duarte (2003) sharpened the criterion.
  Burnol (2004-2009): deep work connecting to de Branges spaces.

**Gap**: λ_n grows like (n/2) log n (if RH is true). Proving λ_n ≥ 0
for ALL n requires understanding the arithmetic of ζ, not just estimates.

**systematic approach fit**: MEDIUM. The criteria are computationally testable
(numerical track can compute λ_n). But proving positivity for all n is hard.

### Route 5: Random Matrix Theory ★★
**Idea**: The zeros of ζ(s) behave like eigenvalues of random matrices
from GUE. Use this to constrain zero locations.

**Status**:
- Montgomery (1973): pair correlation matches GUE
- Odlyzko (1987): numerical verification to high precision
- Keating-Snaith (2000): moment conjectures from RMT
- RMT predicts but does not PROVE anything about individual zeros

**Gap**: RMT is a statistical prediction. It says MOST zeros are on
the critical line, but can't rule out individual exceptions.

**systematic approach fit**: LOW for proof, HIGH for understanding structure.

## Assessment

**Primary**: Route 2 (arithmetic geometry) — deepest, most structural,
closest to a complete framework. But the gap IS the problem (positivity).

**Secondary**: Route 1 (Hilbert-Pólya) — if the operator is found, the
proof follows. The operator search is the gap.

**Computational**: Route 4 (Li's criterion) — the numerical track should
compute λ_n to high precision and look for structure.

**Dead**: Route 3 (analytic zero-free) — 65 years stuck at 2/3 exponent.

## Result
Five routes surveyed. Primary = arithmetic geometry. Secondary = Hilbert-Pólya.
Computational = Li's criterion. Two agents running for full literature.
