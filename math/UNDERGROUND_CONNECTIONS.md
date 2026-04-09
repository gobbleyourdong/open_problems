# Underground Connections — Cross-Problem Transfer Map

> "The mountains connect underground." — systematic approach v2
> Each problem's breakthrough might come from a DIFFERENT problem's tools.

## The Transfer Map

```
    POINCARÉ (solved)
    W-entropy, Ricci flow
         │
         │ monotone functional technique
         │
         ▼
    YANG-MILLS ◄──────────────────────► RIEMANN HYPOTHESIS
    GC > 0, Langevin coupling            Selberg λ₁ ≥ 1/4
    spectral gap of lattice gauge         spectral gap of SL(2,Z)\H
         │                                     │
         │ spectral gap methods                │ L-functions
         │                                     │
         ▼                                     ▼
    NAVIER-STOKES                         BSD
    vorticity bounds                      L-function derivatives
    monotone enstrophy?                   → rational points
         │                                     │
         │ PDE techniques                      │ arithmetic geometry
         │                                     │
         ▼                                     ▼
    HODGE                                 P vs NP
    calibrated submanifolds               meta-complexity
    period integrals                      Kolmogorov complexity
```

## Concrete Transfers

### Transfer 1: YM → RH (spectral gap → spectral gap)

**The connection**: Yang-Mills mass gap is a SPECTRAL GAP of the lattice
transfer matrix. The Selberg eigenvalue conjecture λ₁ ≥ 1/4 is a
SPECTRAL GAP of the Laplacian on SL(2,Z)\H. Same mathematical structure.

**What transfers**:
- The Langevin coupling technique (couple two dynamics, show ordering preserved)
- The gradient correlation GC as a monotone quantity
- The Bakry-Émery criterion (positive curvature → spectral gap)

**Concrete action**: Can the coupled Langevin technique prove λ₁ ≥ 1/4?
The hyperbolic Laplacian on SL(2,Z)\H has a heat kernel. Couple two
heat flows (with and without a "twist"), show the ordering is preserved.
If GC > 0 for the hyperbolic heat kernel: spectral gap follows.

**Risk**: SL(2,Z)\H has NEGATIVE curvature (hyperbolic), while SU(2) has
POSITIVE curvature. The Bakry-Émery argument used positive curvature.
Need a DIFFERENT mechanism for negative curvature.

**But**: the spectral gap for SL(2,Z)\H comes from the ARITHMETIC structure
(the congruence subgroup property), not from curvature. This is a different
mechanism — and might be attackable by a Langevin technique that exploits
arithmetic, not curvature.

### Transfer 2: Poincaré → NS (entropy functional → regularity)

**The connection**: Perelman's W-entropy is monotone under Ricci flow
(∂g/∂t = -2Ric). NS is a flow (∂u/∂t = νΔu - (u·∇)u + ∇p). Both are
nonlinear parabolic PDE systems on manifolds.

**What transfers**:
- The IDEA of finding a monotone entropy for a PDE flow
- The construction: couple curvature (or vorticity) to a test function
  via an exponential weight
- The surgery idea: when the flow blows up, cut and restart

**Concrete action**: Find the "W-entropy for Navier-Stokes":
  W_NS(u, f, τ) = ∫ [τ(|ω|² + |∇f|²) + f - 3] (4πτ)^{-3/2} e^{-f} dx

where ω = curl(u) is vorticity and f solves a conjugate equation.

If W_NS is monotone under NS flow: it controls the enstrophy, prevents
blowup, and gives regularity. This is SPECULATIVE but the Ricci flow
analogy is exact.

### Transfer 3: Hodge → BSD (algebraic cycles → rational points)

**The connection**: Both problems ask "do algebraic objects exist?"
Hodge: do algebraic CYCLES exist? BSD: do rational POINTS exist?

**What transfers**:
- The brute force generator (enumerate, compute, check spanning)
- The MT/Hodge group classification
- The period integral computation

**Concrete action**: For an elliptic curve E of rank 2, view E as a
fiber of a surface S → P¹. The Hodge conjecture for S (proved for
surfaces, Lefschetz 1,1) gives algebraic divisors on S. These divisors
RESTRICT to rational points on the fiber E. The Hodge generator for S
produces the BSD rational points on E.

This is the SHIODA-TATE formula: rank(E/K(t)) = rank(NS(S)) - 2 - Σ(m_v - 1).
The Néron-Severi lattice of S controls the rank of E.

### Transfer 4: P vs NP → RH (meta-complexity → entropy of primes)

**The connection**: Liu-Pass proved OWFs ↔ Kt hardness. The entropy of
primes (RH Mountain 4) is related to Kolmogorov complexity of prime sequences.

**What transfers**:
- The meta-complexity framework (complexity of computing complexity)
- The connection between randomness and structure
- The Cramér model (primes as pseudo-random) ↔ PRGs (crypto as pseudo-random)

**Concrete (speculative) action**: If the prime sequence has high
Kolmogorov complexity (primes are "incompressible"), then ζ(s) has no
unexpected zeros (the zeros are "random" = GUE). RH ⟺ primes have
maximal Kt complexity subject to the prime number theorem constraint.

### Transfer 5: BSD → Hodge (pairs → pairs of cycles)

**The connection**: BSD rank 2 needs PAIRS of points. Hodge for p = 2
needs PAIRS of cycles (or at least, cycles not from divisor products).

**What transfers**:
- The "pair" structure (both problems need TWO independent algebraic objects)
- Descent methods (BSD) ↔ cycle enumeration (Hodge)
- The Selmer group (BSD) ↔ the Chow group (Hodge)

## The "Cheapest Interventions" Across Problems

Applying the T1DM principle: which SINGLE technique, applied across
multiple problems, gives the most leverage?

**Winner: the monotone functional / spectral gap paradigm.**

| Problem | The monotone quantity | Status |
|---------|---------------------|--------|
| Poincaré | W-entropy | FOUND → SOLVED |
| Yang-Mills | GC (gradient correlation) | FOUND → conditional proof |
| NS | ??? (vorticity entropy?) | NOT FOUND → stuck |
| RH | ??? (Selberg spectral gap?) | NOT FOUND → stuck |
| BSD | ??? (regulator monotonicity?) | NOT FOUND → stuck |

**The pattern**: finding the monotone functional = solving the problem.
The systematic approach's next session should SYSTEMATICALLY SEARCH for monotone
functionals on the remaining problems, using the Poincaré/YM templates.

## Session 2 Priority List (Cross-Problem)

1. **NS**: Find the W-entropy analog for Navier-Stokes. Couple |ω|² to a
   test function f via e^{-f}. Compute dW/dt under NS flow. Is it monotone?

2. **RH**: Apply Langevin coupling to the heat kernel on SL(2,Z)\H.
   Does GC > 0 for the hyperbolic Laplacian? If yes: Selberg λ₁ ≥ 1/4 → RH.

3. **BSD**: Use Shioda-Tate to transfer Hodge (surfaces) → BSD (rank of fiber).
   The Hodge generator for the surface S produces the rank-2 points on E.

4. **Hodge**: Implement mirror symmetry computation for specific CY3 families.
   Compute GW invariants = Hodge classes. Verify algebraicity.

5. **P vs NP**: Study Liu-Pass Kt connection. Can Williams' paradigm be
   extended to prove Kt hardness on average?
