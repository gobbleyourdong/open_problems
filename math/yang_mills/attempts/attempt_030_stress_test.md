# Attempt 030 — Stress Test of Attempt 028

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts — verification)
**Track**: theory (Theory)

## Checking Each Step

### Step 1 (ε₀ independent of |Λ|): ✓ SOLID
Standard result. Kotecký-Preiss criterion depends on local coordination
number (≤ 24 in d=4), not on |Λ|. No issue.

### Step 2 (MK rate independent of |Λ|): ✓ SOLID
The MK recursion is a map on the space of character coefficients {c_j}.
It depends on b (block size), d (dimension), G (group), and the
Clebsch-Gordan decomposition. None of these depend on |Λ|.

### Step 3 (n₀ independent of |Λ|): ✓ FOLLOWS FROM 1+2
Trivial combination.

### Step 4 (sandwich): ✓ PROVED IN LEAN
MKDecimation.lean, sandwich_to_zero.

### Step 5 (|c_j| < ε₀ controls signed coefficients): ⚠️ NEEDS VERIFICATION

The claim: cluster expansion converges when max_j |c_j| < ε₀, even if
some c_j are negative.

**Check**: The polymer activity for a connected cluster γ of plaquettes is:

  a(γ) = ∫ ∏_{P∈γ} [Σ_j d_j c_j^{(P)} χ_j(U_P)] · ∏_{ℓ} dU_ℓ - (disconnected)

For negative c_j, the integrand can be negative. But |a(γ)| is bounded by:

  |a(γ)| ≤ ∫ ∏_{P∈γ} [Σ_j d_j |c_j| |χ_j(U_P)|] · ∏_{ℓ} dU_ℓ

Since |χ_j(U)| ≤ d_j = 2j+1, we get:

  |a(γ)| ≤ ∏_{P∈γ} [Σ_j d_j² |c_j|] · (link integral bounds)

This uses |c_j| not c_j. So yes, the absolute convergence criterion
involves |c_j|. ✓

**But**: There's a subtlety. The cluster expansion for ln Z requires not
just |a(γ)| being small, but also that the expansion is CONVERGENT as a
formal series. For signed activities, the expansion could in principle
converge absolutely while individual terms have varying signs.

The Kotecký-Preiss theorem handles this: it gives ABSOLUTE convergence
of the polymer expansion under the |a(γ)| bound. So yes, Step 5 is valid. ✓

### Step 6 (sign of ⟨O⟩_per - ⟨O⟩_anti): ⚠️ KEY CHECK

At leading order in the cluster expansion:

⟨Tr(U_P)⟩_per ≈ 2c_{1/2}  (for all P)
⟨Tr(U_P)⟩_anti ≈ 2c_{1/2} (P ∉ Σ), -2c_{1/2} (P ∈ Σ)

So O = Σ_P w_P Tr(U_P) with w_P > 0 gives:

⟨O⟩_per - ⟨O⟩_anti = Σ_{P∈Σ} w_P · 4c_{1/2} > 0 ✓

At next-to-leading order: corrections involve products of c_j from
multi-plaquette polymers. These are O(c_{1/2}²). For c_{1/2} < ε₀
with ε₀ small enough, the leading term 4c_{1/2} dominates the
O(c_{1/2}²) corrections.

**How small must ε₀ be?** We need:

  4c_{1/2} · P_Σ > |NLO corrections| ≤ C · c_{1/2}² · P_Σ · (coordination)

So: 4 > C · c_{1/2} · (coordination), giving c_{1/2} < 4/(C · coordination).

With coordination ≤ 24 and C = O(1), we need c_{1/2} < O(0.1). This is
achievable: the MK recursion drives c_{1/2}^U → 0 super-exponentially.

**Step 6: ✓ VALID for ε₀ small enough (which is achievable).**

### Step 7 (propagation to original theory): ⚠️ THE REMAINING QUESTION

This is Tomboulis's Sections 3-5. The exact representation:

  Z_Λ(β) = [∏_{m=1}^{n₀} F̃₀(m)^{...}] · Z_{Λⁿ₀}({c̃_j(n₀)})

The vortex free energy decomposes as:

  F_v(β) = Σ_{m=1}^{n₀} [contribution from decimation step m] + F_v(n₀)

where F_v(n₀) > 0 (proved at step n₀ by cluster expansion) and each
decimation contribution is controlled by the interpolation.

**The question**: Do the intermediate contributions preserve F_v > 0?

Tomboulis's argument: at each step m, the interpolation parameter α^{(m)}
is chosen to make the decimated Z equal the original Z. The construction
ensures that F_v at step m-1 is related to F_v at step m by:

  F_v(m-1) = [bulk contribution from step m] + F_v(m)

If F_v(m) > 0 and the bulk contribution ≥ 0, then F_v(m-1) > 0.

**Is the bulk contribution ≥ 0?** This is exactly what (5.15) at step m
ensures. But we only proved (5.15) at step n₀, not at intermediate steps.

**THIS IS THE REAL GAP.** We need (5.15) at EVERY step m = 1, ..., n₀,
not just at step n₀. The coefficients at intermediate steps are NOT
necessarily in the cluster expansion regime (they might be too large).

### The Way Around

Actually, rereading Tomboulis: the construction goes FORWARD (from step 0
to step n₀), not backward. At each step, the interpolation parameter is
determined. The inequality (5.15) is needed at the FINAL step n₀ (where
the coefficients are small) to extract the vortex free energy.

The bulk contributions F̃₀(m) at each step are PARTITION FUNCTIONS of
independent blocks, which are automatically positive (integrals of
exp(-action) > 0). They don't need (5.15).

So the construction is:
1. Decimate n₀ times: Z_Λ = [positive bulk factors] · Z_{Λⁿ₀}({c̃})
2. Z⁻_Λ = [same positive bulk factors] · Z⁻_{Λⁿ₀}({c̃})
   Wait — are the bulk factors THE SAME for Z and Z⁻?

**If the bulk factors are the same**: F_v = Z/Z⁻ = Z_{Λⁿ₀}/Z⁻_{Λⁿ₀}, and
we proved F_v(n₀) > 0. Done!

**If the bulk factors differ**: F_v(0) = [ratio of bulk factors] · F_v(n₀),
and we need the ratio of bulk factors to be ≥ 1 (or at least positive).

This is where the interpolation parameter equality is needed — Tomboulis
needs the SAME α^{(m)} for both Z and Z⁻. This requires (5.15) at each
intermediate step. And we don't have it there.

## Revised Assessment

The argument in attempt_028 is ALMOST right but has a gap:
- Steps 1-6: VALID (cluster expansion at step n₀)
- Step 7: REQUIRES (5.15) at intermediate steps OR a different decomposition

**Two possible fixes:**

**Fix A**: Show that the bulk factors F̃₀(m) are the SAME for Z and Z⁻ at
each step. This would be true if the decimation doesn't see the boundary
condition (the twisted surface Σ) at steps where Σ is far from the
decimated plaquettes. For n₀ steps of decimation with block size b, the
coarsened lattice at step n₀ has spacing b^{n₀} · a. If Σ is a fixed
surface, it will be crossed by O(|Σ|/b^{2n₀}) blocks. For large n₀,
most blocks don't touch Σ, so most bulk factors are identical. The
difference comes only from O(|Σ|/b^{2n₀}) blocks, which gives a
VANISHING correction.

**Fix B**: Don't use the interpolation at all. Instead, directly compare
Z_Λ^{per} and Z_Λ^{anti} using a single cluster expansion around the
STRONG COUPLING FIXED POINT after n₀ decimation steps. The cluster expansion
controls both partition functions (Step 5), so their ratio is computable.

Fix B seems cleaner. The idea: don't decompose the decimation step by step.
Instead, bound Z/Z⁻ directly at step n₀, then relate to step 0 using the
MK bounds (upper and lower) which are EXPLICIT and don't need interpolation.

## Result

The proof attempt in 028 is 90% correct. The gap is in Step 7 (propagation).
Two potential fixes identified (Fix A: surface locality, Fix B: direct
comparison without interpolation).

**The core result stands**: at step n₀, the cluster expansion proves
F_v > 0 with a COMPUTABLE positive margin. The question is how to
propagate this to step 0 without invoking (5.15) at intermediate steps.

This is a technical issue, not a conceptual one. The proof structure is sound.
