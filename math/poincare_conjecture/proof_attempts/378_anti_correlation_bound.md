---
source: Amplitude-direction anti-correlation — the missing ingredient
type: PROOF APPROACH — quantifying why S²ê ≪ λ_max × diagonal
file: 378
date: 2026-03-29
---

## THE ANTI-CORRELATION MECHANISM

From file 377: for N=5 at the Lagrange optimal config:
- λ_max(direction Gram) = 4 (directions maximize alignment along ê)
- diagonal = |ω|²/5 (amplitudes maximize at γ*=arccos(1/√5))
- Product bound: S²ê ≤ 4|ω|²/5 = 0.8|ω|² (EXCEEDS 3/4)
- Actual: S²ê ≈ 0.28|ω|² (3× better than bound)

WHY? Because the configurations that maximize λ_max require specific
polarization choices that REDUCE the amplitudes, and vice versa.


## FORMAL STATEMENT

S²ê = |Σ r_k d̂_k|² = Σ_i (Σ_k r_k d̂_k·e_i)²  (for any ON basis {e_i})

where r_k = |ŝ_k| = (a_k sinγ_k)/2 and d̂_k = ŝ_k/|ŝ_k| (unit direction).

The key: r_k and d̂_k are NOT independent. For fixed k-vector and ê:
- r_k = (a_k/2)sinγ_k where a_k ≤ |ω|cosγ_k (sign-flip constraint)
- d̂_k is determined by v̂_k = (cosγ_k)ê + (sinγ_k)n̂_k (mode polarization)

The polarization angle γ_k controls BOTH:
- The amplitude: r_k ≤ (|ω|/4)sin(2γ_k), maximized at γ_k = π/4
- The direction: d̂_k depends on the projection of the mode's 2D plane onto R³

For γ_k → 0 (aligned with ê): r_k → 0 but d̂_k is free.
For γ_k → π/4: r_k is maximized but d̂_k is constrained (more of v̂_k is in ê-direction).
For γ_k → π/2: r_k → 0 (sign-flip constraint a_k → 0).


## THE COSINE-SINE TRADEOFF

For the ê-component of d̂_k:

d̂_k · ê = α̂_k/|ŝ_k| = (ê·k̂)(ê·ŵ) / √((ê·k̂)² + (ê·ŵ)²)
         = cosθ × sinθ cosψ / √(cos²θ + sin²θ cos²ψ)
         ≤ 1/2  (AM-GM on sinθcosθ)

So: the ê-component of d̂_k ≤ 1/2 (regardless of mode geometry).

This means: even if all d̂_k align along ê, the projection is ≤ 1/2.

The ê-ê contribution to S²ê: (Σ r_k × d̂_k·ê)² ≤ (Σ r_k/2)² = (Σ|ŝ_k|/2)².

From the per-mode bound: Σ|ŝ_k| ≤ |ω|√(N-1)/2. So:
ê-ê contribution ≤ (N-1)|ω|²/16.

For N=5: ≤ |ω|²/4. And the ⊥ contributions add more, so this doesn't close.


## BETTER: WEIGHTED FRAME BOUND

Instead of S²ê ≤ λ_max × Σr_k², use the WEIGHTED version:

S²ê = |Σ r_k d̂_k|² ≤ (max_k r_k) × (Σ r_k) (since all terms same sign... NO,
this isn't right — d̂_k has different directions.)

Better: S²ê = Σ_{j,k} r_j r_k (d̂_j · d̂_k).

Define G_{jk} = d̂_j · d̂_k (the direction Gram matrix). Then:

S²ê = r^T G r where r = (r_1,...,r_N).

S²ê ≤ ||G|| × ||r||² where ||G|| is the operator norm (= λ_max).

But this is the frame bound that already fails.

Alternative: S²ê = r^T G r ≤ trace(G × diag(r²))  ... no, that gives Σr_k² (since G_kk=1).

Let me try Schur complement: S²ê = r^T G r. If G has spectral decomposition
G = Σ λ_i u_i u_i^T, then S²ê = Σ λ_i (r·u_i)².

Since |r·u_i| ≤ ||r|| = √(Σr_k²): S²ê ≤ λ_max × Σr_k².

This is the same frame bound. Can't improve without structural constraint.


## THE STRUCTURAL CONSTRAINT: r AND d̂ ARE CO-DETERMINED

For each mode k: both r_k and d̂_k depend on the SAME polarization v̂_k.

Specifically: v̂_k = (cosγ_k)ê + (sinγ_k)n̂_k determines:
- r_k = a_k sinγ_k/2 ≤ |ω|cosγ_k sinγ_k/2 = (|ω|/4)sin(2γ_k)
- d̂_k = specific function of v̂_k, k̂_k (lies in the Biot-Savart 2D plane ⊥ v̂_k)

For the amplitude to be large (sin(2γ_k) near 1): γ_k ≈ π/4.
At γ_k = π/4: v̂_k = (1/√2)ê + (1/√2)n̂_k. The 2D plane ⊥ v̂_k
passes closer to ê than for γ_k near 0 or π/2.

The d̂_k at γ=π/4 has ê-component: d̂_k·ê ≤ some function(γ,k-geometry).

For the SPECIFIC bound needed:

S²ê = Σr_jr_k(d̂_j·d̂_k) ≤ (Σr_k)² × max(d̂_j·d̂_k over weighted pairs)

Hmm, this requires bounding the average direction correlation weighted by amplitudes.


## A POTENTIAL ROUTE: THE CAUCHY-SCHWARZ TRICK

S²ê = |Σ r_k d̂_k|² = |Σ r_k d̂_k|²

By Cauchy-Schwarz with weights w_k > 0:
= |Σ (w_k^{1/2} d̂_k) × (r_k/w_k^{1/2})|²
≤ (Σ w_k |d̂_k|²) × (Σ r_k²/w_k)  (C-S)
= (Σ w_k) × (Σ r_k²/w_k)

Choose w_k = r_k: gives (Σ r_k) × (Σ r_k) = (Σ r_k)². Same as triangle.

Choose w_k = r_k^α for some α: gives (Σ r_k^α)(Σ r_k^{2-α}).

For α=2: (Σ r_k²)(Σ 1) = N × Σr_k². Frame bound.
For α=1: triangle inequality.

Need a SMARTER choice of w_k that exploits the structure.

What if w_k = cos²γ_k (the "efficiency" of each mode)?

(Σ cos²γ_k)(Σ r_k²/cos²γ_k) = (Σ cos²γ_k)(Σ a_k²sin²γ_k/(4cos²γ_k))

The first factor: Σcos²γ_k ≥ 1 (from the constraint Σa_kcos²γ_k/|ω| = ... hmm, depends on the config).

This is getting too abstract. Let me try something computational.


## NUMERICAL: WHAT IS THE ACTUAL ANTI-CORRELATION?

Define the "effective frame constant" C_eff = S²ê / Σr_k² for each config.

If C_eff < 3 for all configs: then S²ê ≤ 3 × |ω|²/4 = 3|ω|²/4 (using diagonal ≤ |ω|²/4).

From file 377: for N=5 Lagrange, C_eff = 0.8|ω|² / (|ω|²/5) = 4. Exceeds 3.

But: the N=5 Lagrange is NOT achievable (numerically the worst is 0.28, not 0.8).
The ACTUAL C_eff = 0.28|ω|² / (actual diagonal).

Need to measure C_eff across adversarial configs. If C_eff < 3 always: done.


## 378. The anti-correlation between amplitudes and directions is the key mechanism.
## Formalizing it requires a joint bound on S²ê = r^T G r.
## The Cauchy-Schwarz trick with structured weights might work.
## Need: C_eff = S²ê/Σr_k² < 3 at all tested configs.
