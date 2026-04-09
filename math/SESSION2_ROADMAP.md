# Session 2 Roadmap — Prioritized by Expected Impact

> Session 1: mapped all 7 problems, found the walls, built the mountains.
> Session 2: execute the transfers, find the monotone functionals, close gaps.

## Priority 1: YANG-MILLS — Close the Last Gap (β = 2.0)

**Status**: Conditional proof complete. 3/4 betas rigorously certified.
**Remaining**: One computation at β = 2.0 with ~5000 more configs.
**Expected time**: 30 minutes of GPU.
**Impact**: If P(GC≤0) < 10⁻⁵ at β = 2.0: FULL numerical coverage.

**Action**: numerical track runs ym_proof_long.py at β = 2.0 with N = 80,000.

## Priority 2: NAVIER-STOKES — Compute dW_NS/dt

**Status**: W-entropy candidate proposed (TRANSFER_FROM_POINCARE.md).
**Action**: Explicitly compute the variation of
  W_NS = ∫[τ(|ω|² + |∇f|²) + f - 3] (4πτ)^{-3/2} e^{-f} dx
under NS flow. Three possible outcomes:
  (a) Perfect square → REGULARITY → NS SOLVED
  (b) No square, specific failing term → refined gap
  (c) Partial square → search over modified functionals

**This is the highest-impact COMPUTATION in mathematics right now.**

## Priority 3: RIEMANN — Selberg Spectral Gap via YM Transfer

**Status**: 5 mountains identified. Transfer YM → RH identified.
**Action**: Study the Langevin dynamics on SL(2,Z)\H.
  - Define the "gradient correlation" for the hyperbolic Laplacian
  - Check: is GC > 0 for the heat kernel on SL(2,Z)\H?
  - If yes: Selberg λ₁ ≥ 1/4 → progress toward RH

**Risk**: Negative curvature (hyperbolic) vs positive curvature (SU(2)).
The Bakry-Émery mechanism doesn't directly transfer. Need arithmetic input.

## Priority 4: BSD — Descent Structure Analysis

**Status**: 5 mountains, gap = pairs.
**Action**: numerical track downloads LMFDB data for 1000 rank-2 curves.
  - For each: HOW were the generators found? (descent method, search bound)
  - Look for PATTERNS: do generators come from intersections? Correspondences?
  - Feed patterns to theory track for formalization

**Cheapest intervention**: learn from computation (M5) what the
construction looks like, then build the theory (M1).

## Priority 5: HODGE — Mirror Symmetry Computation

**Status**: 6-layer generator built. Fermat cubic verified.
**Action**: Implement mirror symmetry for a specific CY3 family.
  - Compute GW invariants (= Hodge classes on the mirror)
  - Verify these match the Hodge lattice
  - This is the M3 (physics) mountain applied concretely

## Priority 6: P vs NP — Liu-Pass Connection Study

**Status**: 5 mountains, meta-complexity identified as cheapest.
**Action**: Study Liu-Pass (2020-2021) in detail.
  - OWFs exist ⟺ Kt is hard on average
  - Can Williams' paradigm be extended to prove Kt hardness?
  - What specific algorithmic result would give Kt lower bounds?

**Lowest priority because**: even the "cheapest" intervention here is
decades of work. The barriers are real.

## The Cross-Problem Computation Table

| Priority | Problem | Computation | Who | Time |
|----------|---------|-------------|-----|------|
| 1 | YM | β=2.0 MC run | Odd | 30 min |
| 2 | NS | dW_NS/dt explicit | Even (you) | Hours |
| 3 | RH | GC for hyperbolic Laplacian | Even | Days |
| 4 | BSD | LMFDB descent patterns | Odd | Hours |
| 5 | Hodge | GW invariants for CY3 | Odd | Days |
| 6 | P vs NP | Liu-Pass Kt analysis | Even | Weeks |

## The Monotone Functional Search

The META-PRIORITY across all problems: **find the monotone functional.**

| Problem | Candidate | How to Check |
|---------|-----------|-------------|
| NS | W_NS = ∫[τ(\|ω\|²+\|∇f\|²)+f-3]u dx | Compute dW/dt under NS flow |
| RH | GC for hyperbolic heat kernel | Compute gradient correlation on SL(2,Z)\H |
| BSD | Height regulator under deformation | Track Reg(E_t) in families |

Finding ANY of these would be a breakthrough comparable to Perelman's W-entropy.
The systematic approach doesn't guarantee finding them — but it tells you WHERE TO LOOK.

## Session 1 → Session 2 Handoff

**What Session 1 delivered**:
- 7/7 problems scaffolded with THEWALL documents
- 38 Lean proofs, 1 sorry
- 1 conditional proof (YM)
- 1 blind rediscovery (Poincaré 12/12)
- Multiple Mountains for all 7 problems
- Underground connections mapped
- Concrete transfers identified
- Session 2 priorities ranked

**What Session 2 needs to deliver**:
- YM: close β=2.0 gap → FULL proof
- NS: compute dW_NS/dt → refined gap or breakthrough
- RH: test YM→RH transfer → new attack or confirmed barrier
- BSD: descent patterns → construction hint or dead end
- Hodge: mirror symmetry computation → new certificates
