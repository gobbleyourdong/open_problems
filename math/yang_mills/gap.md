# Yang-Mills Mass Gap — Current Gap Assessment

## Phase: 1 (Paper Arsenal — nearly complete)

## The Problem (Jaffe-Witten formulation)

For any compact simple gauge group G (e.g., SU(2), SU(3)):

1. **Existence**: Construct a quantum Yang-Mills theory on R⁴ satisfying the
   Wightman axioms (or equivalently, the Osterwalder-Schrader axioms in Euclidean signature).

2. **Mass Gap**: The theory has a mass gap Δ > 0, meaning the spectrum of the
   Hamiltonian H satisfies: spec(H) ⊂ {0} ∪ [Δ, ∞) with Δ > 0.

## THE GAP (refined, 2026-04-07)

The problem decomposes into **two sub-gaps**, both open:

### Gap A: Infinite-Volume Lattice Mass Gap

**Statement**: For SU(2) lattice gauge theory with Wilson action at coupling β > 0
on the infinite lattice Z⁴, prove the transfer matrix has a spectral gap Δ(β) > 0.

**What's known**:
- β → 0 (strong coupling): PROVEN. Osterwalder-Seiler cluster expansion gives
  exponential decay of correlations. Mass gap Δ ~ -ln(β/4).
- Finite lattice, any β: PROVEN (Krein-Rutman, attempt_004). The transfer matrix
  has a strictly positive kernel → simple leading eigenvalue.
- Infinite volume, weak coupling: OPEN. Cluster expansion fails at weak coupling.
  No rigorous infinite-volume construction at large β.

**The difficulty**: At weak coupling (large β), the lattice theory is "almost continuous"
and the nonperturbative dynamics that generate the mass gap are subtle.

### Gap B: Continuum Limit Preserves the Gap

**Statement**: As β → ∞ with physical scale fixed (asymptotic freedom scaling),
prove lim Δ(β)/Λ_QCD(β) = m > 0 where m is the physical glueball mass.

**What's known**:
- Balaban proved: UV stability (small field) at each finite RG step, with coupling
  running per asymptotic freedom (rigorous bounds, CMP 109 Theorem 2).
- **THE OBSTRUCTION**: Large field entropy exp(c'L^{4k}) vs action suppression
  exp(-c·b₀·k·log L). The entropy grows exponentially in k, the suppression only
  linearly. The infinite RG composition FAILS with current bounds.
- In d=3: no obstruction (superrenormalizable, finite RG steps).
- Numerical evidence: overwhelming (lattice Monte Carlo, all studied β).

**The difficulty**: This is the Balaban completion problem. Either:
(a) Find better large-field bounds (geometric structure, not just action cost), or
(b) Find a proof method that avoids scale-by-scale decomposition entirely.

## Structural Comparison with NS

| Aspect | NS | YM |
|--------|----|----|
| Gap type | Single pointwise inequality | Infinite series of bounds |
| Gap statement | C > -\|ω\|²/4 at max | Σ_k LF_k < ∞ |
| Known side | Most routes killed algebraically | Balaban small field complete |
| Unknown side | Liouville conjecture | Large field composition |
| Certificates | 1.33M SOS, 0 failures | Finite lattice gap (Krein-Rutman) |
| Numerics | Adversarial search, margin 51% | MC, all β show gap |

**YM is structurally harder**: not one inequality but a convergence problem.

## Anti-Problem (refined)

"What would a 4D YM theory WITHOUT a mass gap look like?"

On the lattice: there would exist a β* where Δ(β*) = 0. This means:
- The transfer matrix has a degenerate leading eigenvalue at β*
- Or: correlations decay as power law (not exponential) at β*
- This implies a PHASE TRANSITION (deconfinement) at β*

For pure SU(N) in d=4: no phase transition is observed numerically for any
N ≥ 2. The theory is confining at ALL couplings. (Contrast: finite-T phase
transition at the deconfinement temperature IS observed, but that's a different
direction — β_t, not β.)

If we could prove "no phase transition in β for SU(2) lattice YM in d=4",
that would imply Gap A: the mass gap, provably nonzero at strong coupling,
cannot vanish at any finite β.

## Proof Routes (ranked by promise, REVISED 2026-04-07)

### DEAD routes:
- ❌ **Lee-Yang / Fisher zeros** — No gauge theory analog exists (50 years, no progress)
- ❌ **Spin foam positivity** — 6j-symbols have mixed signs, no structure to exploit
- ❌ **Direct Balaban completion** — Large field entropy obstruction (exp vs linear)
- ❌ **FKG inequality for SU(2)** — SU(2)^|E| not a distributive lattice. No FKG. (attempt_020)

### ALIVE routes:

1. **Fix Tomboulis (2007) via plaquette positive correlation** ★★★★★
   - Tomboulis gap (5.15) reduces to: Cov(O, Q) ≥ 0 for positive plaquette
     observables O, Q (attempt_016 → attempt_018 → attempt_020)
   - This is PLAQUETTE POSITIVE CORRELATION — weaker than FKG
   - PROVED at strong coupling (cluster expansion) and weak coupling (perturbation)
   - OPEN at intermediate coupling — THE REFINED GAP
   - Numerically appears to hold everywhere
   - THE PRIMARY ROUTE.

2. **Extend SZZ/Nissim strong-coupling methods** ★★★
   - Closest existing attempt at "confinement for all couplings"
   - RG decimation gives upper+lower bounds on Z
   - Ito-Seiler found gaps → identify exact failure, attempt repair
   - arXiv:0707.2179 + arXiv:0711.4930

3. **Strong-weak interpolation via convexity** ★★★
   - Pressure p(β) is convex (proven). Analytic at strong coupling (OS) and
     plausibly at weak coupling (Balaban). If analyticity regions overlap → done.
   - Need to push both radii of convergence.

4. **Tomboulis-Yaffe BC insensitivity** ★★★
   - Proved: BC insensitivity ⟹ mass gap
   - Extended to SU(N) (Ito 2008)
   - Need to prove BC insensitivity at all β

## Status
- [x] Paper arsenal built (30+ papers, MANIFEST.md)
- [x] Manifest populated (equations, Mathlib gaps)
- [x] Key equations extracted (core_definitions.md)
- [x] Approach routes identified (5 routes, ranked)
- [x] Lean definitions started (4 files, 3 proofs)
- [x] Balaban obstruction precisely identified (attempt_005)
- [x] Finite lattice mass gap theorem stated (FiniteLatticeGap.lean)
- [x] Character expansion implemented + tested (su2_character_expansion.py)
- [x] numerical track numerical campaign started (Session 3, Cycle 6)
  - 4⁴ SU(2) lattice, β=1.0-4.0, 150 configs
  - ⟨P⟩ matches theory (β=1: 0.243 vs 0.25 prediction)
  - **Correlator decay**: C(r) drops 50-200x from r=0→1 at ALL β=1.5-4.0
  - **Mass gap**: Δ ≈ 4-6 in lattice units, no sign of closing at any β
  - Lattice too coarse for precision — need L≥8 at weak coupling
  - Qualitative: confinement at all tested couplings ✓
- [ ] 3D transfer matrix constructed
- [x] No-phase-transition literature surveyed (attempt_009)
- [x] Tomboulis gap identified: inequality (5.15) (attempt_011)
- [x] SZZ/Nissim correction: strong coupling only (attempt_012)
- [x] (5.15) reduced to FKG in character basis (attempt_018)
- [ ] Lean proofs of gauge invariance
- [ ] numerical track MK decimation test (Request 1)
- [ ] FKG for lattice gauge theory — literature check
