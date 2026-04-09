# Attempt 005 — The Exact Obstruction

**Date**: 2026-04-07
**Phase**: 1 (Paper Arsenal — nearing completion)
**Track**: theory (Theory)

## The Obstruction, Precisely

From Balaban's 4D RG (CMP 109, 1987) and the large field papers (CMP 122, 1989):

### Setup
- Lattice at scale k has spacing η = L^{-k}
- Running coupling: g_k² ~ 1/(b₀ k log L) (asymptotic freedom, rigorous)
- Small field: |U(∂p) - 1| < ε₀ η²
- Large field: complement, suppressed by action cost

### The Inequality That Must Hold

At each RG step k, the large-field contribution is bounded by:

  |LF_k| ≤ exp(-c/g_k² + c' · L^{4k} · ε₀⁻² · g_k² + ...)

For the RG to close over infinitely many steps, we need:

  Σ_{k=0}^∞ |LF_k| < ∞

### Plugging in asymptotic freedom: g_k² ~ 1/(b₀ k log L)

  -c/g_k² = -c · b₀ · k · log L  (grows linearly in k)
  c' · L^{4k} · g_k² = c' · L^{4k} / (b₀ k log L)  (grows exponentially in k)

**The exponential term DOMINATES.** For large k:

  exp(-c · b₀ · k · log L + c' · L^{4k} / (b₀ k log L)) → ∞

This is NOT convergent. The large field entropy overwhelms the action suppression.

### Why d=3 Works

In d=3: g_k² = g² (fixed, superrenormalizable). The suppression is:
  exp(-c/g² · L^{2k}) (from η^{2(d-2)} = η² = L^{-2k})

The entropy is L^{3k}. So:
  exp(-c L^{2k}/g² + c' L^{3k})

For large k, L^{2k}/g² grows exponentially but with a SMALLER base than L^{3k}.
Wait — this also diverges?

No. In d=3, the key is that after finitely many RG steps, the coupling flows
to strong coupling and the theory is TRIVIALLY bounded. The sum is FINITE because
the number of steps is finite (K ~ log(1/ε)/log L). The entropy never gets the
chance to dominate.

In d=4, the number of steps is INFINITE (the coupling runs logarithmically,
never reaching strong coupling). So the entropy has infinite time to grow.

## What This Means

The Balaban program fails at the INFINITE COMPOSITION step. Not because any
single step is wrong, but because the bounds don't sum.

### The NS Analogy

In NS: the gap was a single pointwise inequality (C > -|ω|²/4 at max).
All routes converged to this one bound.

In YM: the gap is an INFINITE SERIES of bounds that must compose. No single
bound fails — the failure is collective.

This is structurally harder than NS. It's not one inequality. It's:
"Does the infinite product ∏_k (1 + δ_k) converge?"
where δ_k = |LF_k| and Σ δ_k must converge.

### Possible Resolutions

1. **Better large field bounds**: The naive bound exp(-c/g_k²) may be improvable.
   If the true suppression is exp(-c/g_k⁴) or stronger, the sum converges.
   This requires understanding the GEOMETRY of large field configurations,
   not just the action cost.

2. **Cancellations between steps**: The large field contributions at different
   scales may partially cancel (gauge invariance, Ward identities).
   This is non-perturbative and hard to prove.

3. **Resum the large field contributions**: Instead of bounding each step
   separately and summing, treat ALL large field contributions as a single
   non-perturbative object. This is essentially asking for a new proof technique.

4. **Avoid the RG entirely**: Use a different approach (stochastic quantization,
   operator algebras, probabilistic methods) that doesn't decompose scale-by-scale.

5. **Lattice-direct approach**: Prove the mass gap on the lattice WITHOUT
   taking the continuum limit. Then prove the continuum limit separately.
   The mass gap is a property of the lattice theory at fixed coupling — it
   might be provable by other means (e.g., reflection positivity + cluster
   expansion at FIXED lattice spacing).

## Assessment

Option 5 is the most promising for the systematic approach. The lattice mass gap
(at fixed β) might be provable without the full Balaban machinery. We know:
- Finite lattice: gap exists (Krein-Rutman, attempt_004)
- Strong coupling: gap provable (character expansion, explicit)
- Infinite volume at strong coupling: proven (Osterwalder-Seiler cluster expansion)

The question becomes: **Can we prove the infinite-volume lattice mass gap
at WEAK coupling (large β)?**

If yes, the remaining problem is the continuum limit: does Δ(β) → Δ_phys > 0
as β → ∞? This is a SEPARATE problem from the UV issues.

## The Revised Gap Statement

**OLD**: "Prove exponential clustering for the continuum limit of 4D lattice YM."

**NEW (refined)**: TWO gaps:
1. **Gap A**: Prove the infinite-volume lattice mass gap at ALL couplings β > 0.
2. **Gap B**: Prove the continuum limit β → ∞ preserves the gap.

Gap A might be attackable by lattice methods (cluster expansion, Lee-Yang type
theorems, monotonicity in β). Gap B is the Balaban problem.

## Result
Exact obstruction identified: large field entropy vs action suppression in d=4.
Gap statement refined into two sub-gaps (lattice gap + continuum limit).
The finite-lattice mass gap (attempt_004) is a warm-up for Gap A.
