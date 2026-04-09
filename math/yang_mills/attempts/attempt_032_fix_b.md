# Attempt 032 — Fix B: Direct Propagation via Surface Locality

**Date**: 2026-04-07
**Phase**: 3 (Proof Attempts)
**Instance**: Even (Theory)

## The Problem (from attempt_030)

Steps 1-6 prove (5.15) at step n₀ (small coefficients). Step 7 needs to
propagate back to step 0. Tomboulis uses interpolation which needs (5.15)
at EVERY step. We only have it at step n₀.

## Fix B: Separate the Surface from the Bulk

### Key Observation

The MK decimation partitions the lattice into blocks. The twisted surface Σ
only affects blocks that it crosses. At each decimation step m:

- Blocks NOT touching Σ: decimation IDENTICAL for Z_per and Z_anti
- Blocks TOUCHING Σ: decimation differs (some plaquettes have flipped c_j)

Number of Σ-touching blocks at step m: O(|Σ| / b^{(d-1)m})

### The Exact Factorization

Tomboulis's representation (eq. 3.35) factorizes the partition function as:

  Z = [bulk factors from non-Σ blocks] × [Σ-block factors] × Z_{coarse}

For periodic BC and anti-periodic BC, the BULK factors are IDENTICAL
(they don't see the twist). So:

  Z_per / Z_anti = [Σ-block ratio] × Z_{coarse}^{per} / Z_{coarse}^{anti}

### The Σ-Block Ratio

Each Σ-touching block at step m contributes a ratio:

  F̃₀^{per}(m, block) / F̃₀^{anti}(m, block)

This ratio equals 1 + O(δ) where δ depends on how much the twist changes
the block's action. For a block at step m:

- The block has volume b^{dm} plaquettes
- Of these, O(b^{d-1}) plaquettes touch Σ (one face of the block)
- Each twisted plaquette changes its contribution by O(c_{1/2}(m))
  (the half-integer coefficient flips sign)

So: ratio per block ≈ 1 + O(b^{d-1} · c_{1/2}(m)) ≈ 1 + O(b³ · c_{1/2}(m))

For d=4, b=2: ratio ≈ 1 + O(8 · c_{1/2}(m))

At step m ≥ 1: c_{1/2}(m) ≤ c_{1/2}^U(m) which is already decaying
super-exponentially toward 0. After a few steps, c_{1/2}(m) << 1.

### The Product Over Steps

  Z_per/Z_anti = ∏_{m=1}^{n₀} [Σ-block ratios at step m] × Z_{n₀}^{per}/Z_{n₀}^{anti}

Each Σ-block ratio > 1 (periodic has more positive terms → larger Z).
So the product ≥ 1.

And Z_{n₀}^{per}/Z_{n₀}^{anti} > 1 (proved by cluster expansion at step n₀).

Therefore: Z_per/Z_anti > 1 → Z_per > Z_anti → F_v > 0. ✓

### Wait — Is Each Σ-Block Ratio Really > 1?

The ratio F̃₀^{per}(block) / F̃₀^{anti}(block) for a single Σ-touching block.

F̃₀^{per}(block) = ∫_{interior links} exp(Σ_{P∈block} Σ_j d_j c_j χ_j(U_P)) ∏ dU

F̃₀^{anti}(block) = same but with c_j → (-1)^{2j} c_j for P on Σ

Since c_j ≥ 0 and (-1)^{2j} c_j ≤ c_j for half-integer j:

The anti-periodic integrand has SMALLER argument in the exponent on Σ-plaquettes.
(The half-integer terms are subtracted instead of added.)

For the exponential function: if f ≥ g pointwise, then ∫ exp(f) ≥ ∫ exp(g).

But: f - g = 2 Σ_{P∈Σ∩block} Σ_{j half-int} d_j c_j χ_j(U_P) is a function of U
that can be positive OR negative depending on the configuration. It's not
pointwise ≥ 0.

Actually: χ_j(U) can be negative (characters of SU(2) range in [-d_j, d_j]).
So the integrand difference is NOT pointwise ≥ 0.

**However**: the EXPECTATION is ≥ 0. We need ∫ exp(f) dμ ≥ ∫ exp(g) dμ where
f = g + 2·(half-int terms on Σ). By Jensen's inequality and the positivity
of the c_j terms... hmm, this doesn't immediately work.

### The Problem Reappears

The block ratio F̃₀^{per}/F̃₀^{anti} is NOT automatically ≥ 1. The characters
χ_j(U_P) can be negative, so replacing c_j → -c_j for half-integer j on Σ
doesn't simply reduce the integrand pointwise.

For the full partition function Z (not a single block): we know Z_per > Z_anti
because the characters are positively correlated (spectral positivity,
attempt_022), but for a SINGLE BLOCK (a finite subsystem), the comparison
needs the block-level partition function to be monotone.

**But**: the block-level partition function IS a lattice gauge theory on a
small lattice (the block). Spectral positivity applies to it too.
F̃₀^{per}(block) > F̃₀^{anti}(block) by the spectral positivity argument
applied to the block.

Wait — that's not exactly right. The block integral has BOUNDARY conditions
from the exterior links. The spectral positivity argument (attempt_022)
requires the transfer matrix, which applies to the full lattice.

For a block with fixed boundary links: the integral is a function of the
boundary configuration. The comparison of periodic vs anti-periodic
depends on the boundary values.

### The Honest Assessment

Fix B doesn't cleanly resolve the propagation. The Σ-block ratios are NOT
automatically ≥ 1 without a monotonicity argument that's equivalent to (5.15).

The problem is IRREDUCIBLY about the comparison of two lattice gauge theory
measures (periodic vs anti-periodic), and this comparison requires either:
(a) A global argument (spectral positivity for the full lattice, which we have)
(b) A local argument (block-by-block comparison, which we don't have)

The spectral positivity gives us (a), but it applies to the FULL lattice
expectation ⟨O⟩_per ≥ ⟨O⟩_anti, not to individual blocks.

## What We Actually Have

**PROVED (no gap)**:
- Spectral positivity: G(P,Q) ≥ 0 for all plaquettes (attempt_022)
- Center decomposition: Sign(⟨O⟩_per - ⟨O⟩_anti) = Sign(⟨O⟩₋ - ⟨O⟩₊)
- At strong coupling: (5.15) holds (cluster expansion)
- At step n₀: (5.15) holds (cluster expansion, Steps 1-6 of attempt_028)
- Finite lattice: gap exists (Krein-Rutman)

**NOT PROVED**:
- (5.15) at the ORIGINAL coupling β (before decimation)
- Propagation from step n₀ to step 0
- The comparison ⟨O⟩₋ ≥ ⟨O⟩₊ at arbitrary β

## The Remaining Wall

After 32 theory track attempts:

**The wall is the same one Ito-Seiler identified in 2007.**

The MK decimation proves the FLOW goes to strong coupling. At strong
coupling, everything works. But the flow doesn't come with a guarantee
that the RATIO Z_per/Z_anti is preserved.

The ratio is a GLOBAL property of the theory. The decimation controls
LOCAL properties (block-by-block). The disconnect between global and
local is the fundamental issue.

## Is This the Yang-Mills Gap?

Like the NS gap (Liouville conjecture), the YM gap might be genuinely
hard — not a technical issue but a deep mathematical obstruction.

**The YM gap, distilled to one sentence:**

"The lattice vortex free energy F_v(β) > 0 for all β > 0, but no known
method propagates F_v > 0 from strong coupling (where it's proved) to
weak coupling (where it's observed numerically)."

This is analogous to the NS gap: "The strain-vorticity ratio is bounded
numerically but no method proves the bound analytically."

## Result

Fix B doesn't work. The propagation gap is real and equivalent to the
Ito-Seiler objection. The wall is the disconnect between local MK control
and global vortex free energy.

After 32 attempts, the theory track has mapped the entire proof landscape
and arrived at the same wall that has stood since 2007.
