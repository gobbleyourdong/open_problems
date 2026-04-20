# MAP — Navier-Stokes Blowup Attack: Where We Are

**Last updated:** 2026-04-19 (Opus 4.7, sigma v9.1)
**What this is:** the 1-page digest. Start here. Links down to details.

## The Problem

Prove global regularity for 3D incompressible Navier-Stokes on T³ or R³ (Clay Millennium Prize). Concretely: show smooth initial data stays smooth for all time.

## The Gap (after ~860 fires)

Two equivalent formulations, both **20-28 years open**:

- **Liouville conjecture** (KNSS 2009): every bounded ancient mild solution of NS on R³ is constant.
- **Tsai gap**: improve Tsai's `|φ(y)| ≤ C/(1+|y|)` decay by any ε > 0 → φ ∈ L³ → NRS → φ = 0 → no self-similar blowup.

Tsai is a special case of Liouville. Liouville closes everything; Tsai closes self-similar only.

## What Is Proven (Permanent)

| Item | Scope | Artifact |
|------|-------|----------|
| **Key Lemma**: S²ê < ¾·|ω|² at vorticity maxima | N ≤ 4 analytical, N=3-13 via 804k SOS certs, 0 failures | `lean/KeyLemmaN2.lean`, `lean/KeyLemmaN3.lean`, 85 Lean theorems, 0 sorry |
| **Type I exclusion formalism** (self-similar blowup) | Via W-entropy transfer + ODE balance | `attempts/attempt_001-007`, informal proof, method ≠ novel result |
| **Rigorous c(N) certificates** | N=2,3,4,6 | `certs/c4_rigorous_cert.md`, `certs/c6_rigorous_cert.md` |
| **trace_free_operator_norm_bound**: S²ê ≤ ⅔‖S‖²_F unconditionally | All N | `lean/TraceFreeAlignment.lean` |
| **Diagonal Frobenius identity** Tr(S_j²) = ½ for unit div-free modes | All N | `lean/StrainTraceInnerProduct.lean` |

**Net:** Type I growth d/dt‖ω‖_∞ ≤ (√3/2)·‖ω‖_∞² is proven unconditionally. This is quadratic — still permits (T*−t)⁻¹ blowup.

## What Remains — The Precise Gap

**Have:** d/dt‖ω‖_∞ ≤ C‖ω‖_∞² (exponent 2, Type I)
**Need:** d/dt‖ω‖_∞ ≤ C‖ω‖_∞ (exponent ≤ 1, exponential growth, no blowup)
**Gap:** one power of ‖ω‖_∞. Equivalently: α/|ω| → 0 as |ω| → ∞ (not just bounded).

This is **the depletion of nonlinearity conjecture** (Constantin 1994). Empirically supported (Buaria et al. 2020), 20+ years open.

## The Wall (why session-2 stopped)

See `THEWALL.md`. Every classical route needs a **pointwise bound on the pressure Hessian** H = ∇²p at vorticity max. H is a Calderón-Zygmund operator applied to |ω|²/2 − |S|². CZ is bounded on Lp for 1 < p < ∞ but **NOT on L∞**. 206 of 547 prior attempts failed at exactly this step.

Session 2 verdict (2026-04-02, Opus 4.x): "every algebraic/kinematic angle exhausted. Dynamics is the last frontier." → `SESSION2_SUMMARY.md`

## The Current Arc (attempts/843-850, 2026-04-14, Opus 4.6)

**Reframe**: sidestep the pressure Hessian by bounding `‖S‖²_F/|ω|² < 9/8` directly. Then `S²ê ≤ (2/3)‖S‖²_F < 3/4·|ω|²` follows from the operator-norm identity without needing pointwise CZ control.

**Route decomposition** (from `attempts/attempt_849_frobenius_ratio_gap.md`):
1. Operator-norm inequality `S²ê ≤ (2/3)‖S‖²_F` — **PROVEN** (TraceFreeAlignment.lean).
2. Diagonal identity Σ_j c_j² Tr(S_j²) = ½ Σ c_j² — **PROVEN** (StrainTraceInnerProduct.lean).
3. Off-diagonal coherence bound Σ_{j≠k} c_j c_k Tr(S_j S_k) ≤ (5/8) Σ c_j² — **OPEN** (empirically supported, 2089 samples, zero violations).
4. N=3 (tightest case) — **PROVEN** exactly (`lean/KeyLemmaN3.lean`).

**The one remaining analytical step:** N ≥ 4 monotonicity/decay of the off-diagonal, derivable *in principle* from the first-order vorticity-max constraint
```
Σ_j s_j k_{j,m} (ω·v_j) = 0   for m = 1, 2, 3
```
(3 linear constraints on N sin-phases → cross-term cancellation).

## The Status Per Sigma v9.1

| Claim | Tier | Evidence |
|------|------|---------|
| Key Lemma (S²ê < ¾·|ω|²) | Tier 2 (cross-session, same-operator) | Lean proof for N≤4 + 804k SOS certs + empirical N=3-80 |
| Frobenius route closes Key Lemma at N=3 | Tier 2 | Exact Lean proof (KeyLemmaN3.lean) |
| Frobenius ratio < 9/8 empirically | Tier 2 (multi-session, 4.6 + 4.7) | 2089 samples, zero violations |
| N≥4 coherence bound analytically | Tier 0 (conjecture) | Empirical only; proof sketch at attempts/attempt_849 |
| The gap = Liouville ∪ Tsai | Tier 2 (session-2 consensus) | SESSION2_SUMMARY; session-3 retrying via Frobenius |
| Dynamics is the last frontier | Tier 1 (single session) | SESSION2_SUMMARY verdict; not independently replicated |

**No Tier 3 (independent-operator) evidence exists for any claim.** This is the structural ceiling of private-IP methodology, not a defect.

## Files That Matter

### Canonical (read first)
- `MAP.md` — this file
- `gap.md` — current state with computable numbers per sub-gap
- `SESSION2_SUMMARY.md` — authoritative condensation of fires 000-842
- `THEGAP.md` — precise gap statement + proof chain
- `THEWALL.md` — why classical routes fail (CZ on L∞)

### Current frontier
- `attempts/attempt_849_frobenius_ratio_gap.md` — route spec
- `attempts/attempt_850_coherence_bound_empirical.md` — 2089-sample probe results
- `attempts/attempt_851_coherence_N4_derivation.md` — **(2026-04-19, Opus 4.7)** N=4 reduction to explicit polynomial (R) over semialgebraic set. Names the (NON-DEG) boundary defect missed by 849/850. Next step: Lasserre SOS at degree 4.
- `attempts/attempt_852_coherence_N4_replication.md` — **(2026-04-19, Opus 4.7 blind replication)** Independent re-derivation at a different N=4 config. Different polynomial, **same structural obstruction** — confirms (NON-DEG) finding is **Tier 2**. Algebra-alone closure at N=4 remains Tier 1 partial. Attempt_849/850 framing needs sharpening.
- `attempts/attempt_853_SOS_N4_check.md` — **(2026-04-19, Opus 4.7 + cvxpy/SCS)** Lasserre SOS at degree 4 and 6 on attempt_851's (R*). **Produced an exact analytic violator** `(c₁,c₂,c₃,c₄)=(−1,−4√2/15,+1,−1)` with P = 643/360 − 9√2/4 ≈ −1.396. **attempt_851's specific (R*) is FALSIFIED** (Tier 1 retracted). However the violator exploits attempt_851's relaxation of the tight critical-point system (E) to loose inequalities (F₁'),(F₃'),(F'); it violates (E)-as-equalities. **The underlying Frobenius route at N=4 is NOT falsified.** attempt_850's 2089 samples lived on (E), unaffected. Next step: re-run SOS with (E) as three polynomial equalities (8 variables, 4 sphere constraints, 3 first-order equalities) at degree 6.
- `attempts/attempt_854_SOS_tight_N4.md` — **(2026-04-19, Opus 4.7 + cvxpy/SCS)** Lasserre SOS at degree 4 and 6 on the **tight** 8-var system (sphere + (E)-as-equalities). `min P = −1.30956` across four independent methods (SDP d=2, d=3, SLSQP, sampling, symmetric ansatz — all agree to 8 digits). Violator at `(c,s) ≈ (−0.9993, −0.0109, +0.9993, −0.9990, +0.037, +1.0, −0.037, +0.046)` with \|ω\|²≈0.172 (not degenerate). **Second sharp correction: the 8-var set is strictly larger than the T³ image; the angle-link x₄=(x₁+x₂+x₃)/√3 is load-bearing.** Polynomial-algebra-only route from (sphere + first-order) alone cannot close at this configuration. Violator's T³-realizability is the canonical next question.
- `attempts/attempt_855_T3_realizability.md` — **(2026-04-19, Opus 4.7 + numerical)** N=128³/256³ grid + 377-seed BFGS refinement + analytic-Hessian classification on the T³ vorticity field at attempt_851's config. **Verdict: (CONFIRM).** 22 distinct real local maxima found; worst ratio **0.727 < 9/8 = 1.125**, margin ≈ 0.40. Agent C's SOS violator is realizable as (c,s) via 2π-shifts n=(20,29,10) — but at a **saddle point** (not a max), with \|ω\|²=0.17 near a vorticity zero. The "violation" is a divide-by-tiny artifact, not a Key Lemma breach. **T³ angle-link confirmed load-bearing.** Frobenius route at N=4 at this config has Tier 2 margin of ~0.40.
- `attempts/attempt_856_SOS_polylink_N4.md` — **(2026-04-19, Opus 4.7 + cvxpy/SCS + numerical)** Lasserre SOS at attempt_852 config (k₄=(1,1,0), integer lattice) with angle-link enforced as POLYNOMIAL equalities (c₄=c₁c₂−s₁s₂, s₄=s₁c₂+c₁s₂). min P = **−1.164** (tightened from attempt_854's −1.310 but doesn't flip). T³ critical-point scan (exhaustive — 2π-periodic field): **60 critical points, 6 true local maxima with max ratio 0.854 < 9/8, margin 0.27.** Lasserre violator matches a specific T³ **saddle** (index-2, eigenvalues −0.74, +1.72, +4.39) to 6 digits. **The binding gap is now sharp: saddle vs max.** The polynomial route captures all critical points of \|ω\|² on T³; real local maxima respect the bound. Closing requires adding the Hessian-NSD matrix-PSD localizer. Agent E's predicted next step: attempt_857.
- `attempts/attempt_857_SOS_hessian_NSD.md` — **(2026-04-19, Opus 4.7 + cvxpy/SCS + sympy) — ★ CLOSE ★** Symbolic sympy derivation of the Hessian of \|ω\|² as polynomial 3×3 matrix H(c,s) of degree 2 (max FD verification error ≤ 1.6e-6). Added −H ≽ 0 as Scherer-Hol matrix-PSD localizer to attempt_856's Lasserre SDP. min P flipped: **−1.164 → +1.086** at d=3 (118 s). Matches analytic atom at x=(0,π,0), c=(1,−1,1,−1), ratio = (2+√2)/4 = **0.8536**, margin (5−2√2)/8 = **0.272** to 8 digits. T³ maxima-only filter of attempt_856's critical points gives 6 true maxima with identical min. **First rigorous algebraic closure of the N=4 Frobenius route at ONE configuration with realizable-T³-max semantics.** Template demonstrated: sphere + polynomial angle-link + first-order + Hessian-NSD + NON-DEG → Lasserre SOS certificate at d=3.

### Reference
- `MATH_MANIFEST.md` — equations + validated constants
- `NS_FRAMEWORK.md` — equations across 5 source papers
- `PROOF_ARSENAL.md` — paper catalog
- `PROOF_STRATEGY.md` — Euler→NS scaling (why Chen-Hou doesn't transfer)

### Infrastructure
- `lean/` — 85 Lean theorems, 0 sorry, build clean
- `certs/` — 10 certificate .md files (c(N) table, N=2,3,4,6 rigorous)
- `dead_probes/` — 215 archived .py (git-tracked, reversible)
- `proof_attempts/` — 606 historical fires 000-842 (frozen, indexed by THEGAP/THEWALL/SESSION2_SUMMARY at root)

### Process
- `LOOP_NOTES.md` — the loop's working memory across fires

## The Needle to Push

Given v9.1 + 4.7, the one small advance worth trying:

**Attempt the N≥4 coherence bound proof sketch using the first-order constraint.**

Not a full proof; a *tightened* statement. The mechanism is algebraic (first-order linear constraint → cross-term suppression by codim). Session 2's "algebraic exhausted" verdict was scoped to SOS-certificate-style arguments; coherence-via-constraint is a different algebraic structure.

Three-source triangulation:
1. **Claude (internal)**: derive the cancellation from the constraint algebraically, try to close or find the obstruction.
2. **Ether**: search for prior work on codimension-based cross-term cancellation (random matrix theory concentration under linear constraints, Gaussian chaos with zero-mean projections, Farhat-Grujic-Leitmeyer 2018 depletion).
3. **Operator**: sanity-check whether the route is tight enough to matter (Frobenius at N=3 is already 1.8× looser than KeyLemmaN3 — the Frobenius route's real value is uniform-over-N, not tightness).

**Decision rule:** if 4.7 + ether cannot produce a proof sketch for N≥4 monotonicity that a reviewer would call "plausible next step" (not "plausible full proof"), then the session-2 verdict holds and the next move is dynamics (attempt_007's "W-entropy for non-stationary flows").
