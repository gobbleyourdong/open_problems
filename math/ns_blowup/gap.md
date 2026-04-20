# Navier-Stokes — Gap Assessment (Updated)

## Phase: 4 (Algebraic Framework Complete)

## The Problem
Prove global regularity for 3D incompressible Navier-Stokes on T³ or R³.

## THREE SUB-GAPS (from even attempt_007 + odd computations)

### Gap 1: Self-Similar Blowup — FORMALLY CLOSED
ODE balance argument (even 005-006) rules out all self-similar profiles.
Exponent α forced to 1, log correction β forced to 0 → φ ∈ L³ → NRS → φ=0.
**Status: CLOSED** (known result, new proof method via W-entropy transfer).

### Gap 2: Type II Blowup — OPEN
No stationary profile → no ODE analysis. Need dynamical methods.
W-entropy might help: does W increase for non-stationary rescaled flows?
**THE NUMBER:** R_II = sup_{Type II} [blowup rate]/[diffusion rate]. Need R_II < 1.
**Status: OPEN** (no computation possible without Type II candidate).

### Gap 3: Log-Enstrophy Growth Rate — OPEN, QUANTIFIED
G(t) = ∫ log(1+|ω|²) dx. If G grows sub-linearly: regularity.
**THE NUMBER:** G_max = sup_t G(t)/t (should be finite for regularity).

Computed (numerical track, gmax_compute.py):
- Taylor-Green (N=32, ν=0.01): G/t decreasing, 2.48 → 0.31. **SUB-LINEAR ✓**
- ABC flow (N=32, ν=0.01): G/t decreasing, 6.34 → 0.62. **SUB-LINEAR ✓**
- Higher Re computation running in background (N=48, ν=0.002).

**Status: CONSISTENT WITH REGULARITY at tested Re.**

### Gap 4 (NEW): Critical Ratio R — THE SHARPEST NUMBER
R = |∫ωSω dx| / ∫|∇ω|² dx (stretching / palinstrophy)
If R < 1 for all time: diffusion dominates → regularity.
At low Re (ν=0.01): R ≈ 0 (trivially regular).
At high Re: R approaches 1? Computing in background.
**THE NUMBER:** sup_t R(t). Need < 1.

### Gap 5 (NEW): Radii Polynomial — IFT Uniqueness
Leray profile in OU-weighted H¹: uniqueness radius r = 1/(2||A⁻¹||C_S).
Computed (odd, leray_radii.py): r = 1.67, profile norm = 2.56.
Need: C_T < r/||profile|| = 0.65. **TIGHT but not ruled out.**
Improving C_S (OU-weighted Sobolev) could widen the margin significantly.

## Proof Architecture

```
                 NS REGULARITY
                      ↑
        ┌─────────────┼─────────────┐
        ↑             ↑             ↑
   Gap 1 (closed) Gap 2 (open)  Gap 3 (open)
   Self-similar   Type II       G_max finite
        ↑             ↑             ↑
   ODE balance    W-entropy     G_max compute
   (even 005)     (even 002)    (odd gmax)
```

### Gap 6 (Session 3): Algebraic Key Lemma — DEFINITIVE TABLE
The vertex property + eigenstructure theorem reduce Key Lemma to pure algebra.

**Definitive c(N) table** (vertex_key_lemma.py, DE + exhaustive signs):
| N | c(N) | Margin from 3/4 | Rigorous cert | Status |
|---|------|-----------------|---------------|--------|
| 2 | 0.2500 = 1/4 | 67% | 0.2500 (exact) | **PROVEN** (KeyLemmaN2.lean) |
| 3 | 0.3333 = 1/3 | 56% | 0.3333 (exact) | **PROVEN** (KeyLemmaN3.lean) |
| 4 | 0.3616 | 52% | **≤ 0.4563** | Cert (grid 41⁴ + Lipschitz) |
| 5 | 0.3553 | 53% | — | DE (100 k-tuples) |
| 6 | **0.3677** | **51%** | **≤ 0.6389** | **PEAK + cert** (grid 15⁶) |
| 7 | 0.3660 | 51% | — | DE (60 k-tuples) |
| 8 | 0.3327 | 56% | — | DE (40 k-tuples) |
| ≥10 | ≤ 0.25 | ≥67% | — | DE (lower effort) |

**CORRECTED**: peak is at **N=6** (not N=4 as previously reported).
The c(N) curve has a PLATEAU at 0.35-0.37 for N=4-7, with N=6 as apex.
Decline resumes at N=8 (c=0.333). Old values (N=5-8 from attempt_845)
were underestimates from insufficient k-tuple sampling.

**Rigorous certificates** (per-sign dominance grid + Lipschitz):
- N=4: ≤ 0.4563 (39% margin), certs/c4_rigorous_cert.md
- N=6: ≤ 0.6389 (15% margin), certs/c6_rigorous_cert.md ← BINDING
See also: certs/cn_vertex_method_correction.md for full correction history.

**Eigenvector mechanism** (attempts/eigenvector_mechanism.md):
- N=2,4: depletion (α≈0, Sê ⊥ ê)
- N=3: compression alignment (α=-1, Sê ∥ ê, degenerate eigenvalues {0.5,0.5,-1})
- N=6: similar to N=4 (distributed depletion)

### Gap 6b: Ashurst Alignment — α/|ω| ≈ 0 at x*
At the vorticity maximum, the stretching rate α = ê·S·ê is approximately
ZERO. Vorticity is orthogonal to its own stretching direction.

**Data** (alignment_anatomy.py, N=3-26, 3310 configs):
- ⟨S²ê/|ω|²⟩ = 0.05, max = 0.25 (threshold 0.75 → 67% margin)
- ⟨α/|ω|⟩ ≈ 0.00 (stretching rate vanishes at vorticity max)
- Adversarial (min a₃²): still S²ê/|ω|² < 0.07

**Algebraic support** (TraceFreeAlignment.lean):
- trace_free_intermediate_eigenvalue_bound: λ₂² ≤ (1/6)||S||²_F **PROVEN**
- key_lemma_via_intermediate_alignment: if ω ∥ e₂, need ||S||²_F/|ω|² < 4.5 **PROVEN**
- Actual max ||S||²_F/|ω|² = 0.66. Margin: >500%.

**THE NUMBER:** max_{x*} α(x*)/|ω(x*)|. Currently ≈ 0.01.
If proven analytically bounded away from √(3/4) ≈ 0.87: Key Lemma follows.

**2026-04-14 REFRAME (attempt_849)**: the binding analytical inequality
is not α/|ω| but the **Frobenius ratio ||S||²_F/|ω|² < 9/8**. The
unconditional operator-norm bound (trace_free_operator_norm_bound,
TraceFreeAlignment.lean) gives S²ê ≤ (2/3)||S||²_F without any alignment
hypothesis. Combined with the diagonal identity Tr(S_j²) = 1/2
(StrainTraceInnerProduct.lean), the remaining open piece is a coherence
bound on the off-diagonal Σ_{j≠k} c_j c_k Tr(S_j S_k). Numerics: max
||S||²_F/|ω|² ≈ 0.66, margin ~1.7× to 9/8. See attempts/attempt_849.

**2026-04-19 CORRECTION (attempts 851, 852, 853 — Tier 2)**: the
Frobenius route must be supplemented by a **non-degeneracy condition**
|ω(x*)|² > 0 that is NOT implied by the first-order vorticity-max
equations Σⱼ sⱼ (ω·vⱼ) kⱼ = 0 alone. Two independent Opus 4.7 sub-instances
(attempts 851, 852) derived N=4 reductions at different mode
configurations and both encountered a degenerate branch where every
a_j = ω·v_j vanishes, making the first-order constraint trivially
satisfied but with ω(x*) = 0. This is a spurious branch — not a vorticity
max. Attempt_850's 2089-sample empirical margin implicitly excluded this
via the numerical guard `best_om2 > 0.01·N`.

**2026-04-19 RETRACTION (attempt 853)**: Lasserre SOS (cvxpy/SCS) at
degrees 4, 6 produced an exact analytic violator of attempt_851's
specific polynomial (R*) at `(c₁,c₂,c₃,c₄) = (−1,−4√2/15,+1,−1)` with
P = 643/360 − 9√2/4. The violator has |ω|² ≈ 0.314 (NOT degenerate) and
Frobenius ratio ≈ 5.57. However the violator relies on attempt_851's
**relaxation of the tight first-order system (E) to loose inequalities**
— it violates (E)-as-equalities. attempt_850's 2089 DNS samples lived on
(E), unaffected by this slack. **The Frobenius route at N=4 is not yet
falsified**; attempt_851's specific reduction is.

**2026-04-19 SECOND SHARPENING (attempt 854)**: Lasserre SOS (cvxpy/SCS)
re-run with (E) as three polynomial **equalities** on the tight 8-var
system (c₁..c₄, s₁..s₄ with sphere constraints). `min P = −1.30956`
across four independent methods (SDP d=2, SDP d=3, SLSQP, projected
sampling, symmetric ansatz — all agree to 8 digits). Tight-system
violator at `(c,s) ≈ (−0.9993, −0.0109, +0.9993, −0.9990,
+0.037, +1.0, −0.037, +0.046)` with |ω|² ≈ 0.172 (not degenerate).
**This is a second structural correction**: the 8-variable set is
strictly larger than the T³ image because the angle-link
`x₄ = (x₁+x₂+x₃)/√3` is not enforced.

**2026-04-19 T³ CONFIRMATION (attempt 855)**: N=128³/256³ grid + 377-seed
BFGS refinement + analytic-Hessian classification on the T³ vorticity
field at attempt_851's configuration. **22 distinct real local maxima
found; worst ratio 0.727 < 9/8 = 1.125, margin ≈ 0.40.** Agent C's SOS
violator is realizable as (c,s) via 2π-shifts n=(20,29,10), signs
(+,+,−) — but at a **saddle point** (Hessian max eig +2.34), NOT a
vorticity max, with |ω|² ≈ 0.17 near a vorticity zero. The "violation"
ratio 8.72 there is driven by a tiny denominator, not a Key Lemma
breach. The T³ angle-link is confirmed load-bearing.

**2026-04-19 SADDLE-VS-MAX (attempt 856)**: Lasserre SOS at attempt_852's
integer-lattice config (k₄=(1,1,0)) with polynomial angle-link enforced
gives min P = −1.164 (tightened from attempt_854's −1.310 but doesn't
flip). T³ exhaustive critical-point scan (2π-periodic field): 60
critical points, **6 true local maxima with max ratio 0.854 < 9/8**
(margin 0.272), 46 saddles. The Lasserre minimum matches a specific T³
saddle (index-2) to 6 digits. **Saddle-vs-max is the binding gap.**

**2026-04-19 ★ CLOSE (attempt 857) ★**: Added Hessian-NSD as Scherer-Hol
matrix-PSD localizer (−H ≽ 0 where H is symbolic sympy-derived
polynomial 3×3 matrix of degree 2 in (c,s)). **Lasserre SOS with
{sphere + polynomial angle-link + first-order + Hessian-NSD + NON-DEG}
gives min P = +1.086 at d=3** (118 s), matching the analytic atom at
x=(0,π,0), c=(1,−1,1,−1), ratio (2+√2)/4 = 0.8536, margin (5−2√2)/8 =
0.272 to 8 digits. **First rigorous algebraic closure of the N=4
Frobenius bound at one configuration with realizable-T³-max semantics.**
Template demonstrated: sphere + angle-link + first-order + Hessian-NSD +
NON-DEG → Lasserre SOS certificate at degree 3.

**Scope:** closes ONE N=4 configuration. Does NOT prove the full N=4 Key
Lemma (needs parameter sweep over attempt_852's orbit + attempt_851's
irrational-angle-link branch). But the method is now demonstrated to be
a rigorous closure technique — not just empirical.

## Multiple Mountains

Mountain 1: W-entropy transfer (Perelman analog for NS)
Mountain 2: ODE balance (Leray profile analysis)
Mountain 3: Log-enstrophy functional (direct energy method)
Mountain 4: Radii polynomial (IFT uniqueness)
Mountain 5: Critical ratio R (stretching vs palinstrophy)
Mountain 6: Ashurst alignment (α ≈ 0 at vorticity max) ★ STRONGEST EVIDENCE

Six mountains surrounding 3 sub-gaps. Gap 1 closed. Gaps 2-3 have
computable numbers (R_II, G_max, R, C_T, α/|ω|). The systematic approach applies.
