# Pattern 023: Cluster Expansion Verification — Step 5 Confirmed

**Date**: 2026-04-07
**Instance**: Odd
**Responding to**: attempt_028 (Even instance)

## What I Tested

Step 5 of the even instance's proof: "Cluster expansion converges for BOTH
Z and Z⁻ when |c_j| < ε₀, and (5.15) holds within the convergence regime."

## Results

### 1. Absolute Convergence: CONFIRMED ✓

Z_anti = Σ_j (-1)^{2j} c_j^F satisfies |Z_anti| ≤ Σ_j |c_j|^F = Z_per.
The anti-periodic series is absolutely convergent whenever the periodic
series converges. The cluster expansion criterion |c_j| < ε₀ controls
BOTH measures.

### 2. Z_per ≥ Z_anti: CONFIRMED ✓

For 2D torus (exact computation):
- Even L: Z_per = Z_anti (Z₂ symmetry from attempt_019)
- Odd L: Z_per > Z_anti (half-integer terms don't cancel)
- All L, all β: Z_per ≥ Z_anti ✓

For 1D chain: Z_per = Z_anti for even L (symmetry).

### 3. Margin Scaling

In 2D, the margin Z_per - Z_anti scales as c_{1/2}^{F} where F = L².
This goes to 0 exponentially as L → ∞ (consistent with σ = 0 in 2D YM).

In 4D, the margin should scale as exp(-σ · Area(Σ)) where σ > 0
(the physical string tension). This is the content of confinement.

### 4. For Even Instance

**Step 5 is solid.** The absolute convergence argument is elementary:
|c_j^{eff}| = |(-1)^{2j} c_j| = |c_j| for all j. The cluster expansion
criterion involves |c_j|, so it controls both periodic and anti-periodic.

**The remaining question is Step 7**: propagation from the decimated
theory back to the original. This is the core of the Ito-Seiler dispute.
The numerical data can't resolve this — it's a purely analytical question
about the uniformity of the interpolation in |Λ|.

## Key Observation for the Proof

The 2D case shows Z_per = Z_anti for even L (Z₂ symmetry). In 4D,
the symmetry still gives Z_per(even L) = Z_anti(even L) because the
center twist squares to the identity.

**Wait — this would mean Tomboulis (5.15) is an EQUALITY for even L in 4D too!**

If ⟨O⟩_per = ⟨O⟩_anti for even L, then (5.15) is trivially satisfied (≥ holds).
And for odd L, the proof would follow from the small asymmetry.

But I need to verify: does the Z₂ symmetry extend to 4D with the full
link-coupling structure? In 2D, plaquettes are independent (after gauge fixing),
so the symmetry is manifest. In 4D, shared links couple plaquettes, and the
symmetry might break.

**This is the CRITICAL question for the next attempt.**
