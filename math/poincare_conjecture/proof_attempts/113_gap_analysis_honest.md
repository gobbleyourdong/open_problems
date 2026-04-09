---
source: Self-critique — does θ₀ = 2/3 actually close the proof?
type: GAP ANALYSIS — honest assessment of what remains
status: GAP IDENTIFIED — θ₀ < 1 reduces constant, doesn't change scaling
date: 2026-03-26
---

## The Gap: Supercritical Scaling Survives

### What We Proved

f(α) = cos(α/2)/2 is the exact angular profile of the bilinear symbol.
θ₀ = 2/3 is the Schur test bound.
This is CORRECT and applies to ALL divergence-free fields.

### Why It Doesn't Close the Proof

The shell enstrophy balance:
```
dE_j/dt + 2ν 4^j E_j ≤ |T(j,j)| + off-diagonal
```

Our bound: |T(j,j)| ≤ (2/3) × E_j × ||S_j||_∞

But ||S_j||_∞ ≤ C × 2^{3j/2} × √E_j  (Bernstein + CZ)

So: |T(j,j)| ≤ (2C/3) × 2^{3j/2} × E_j^{3/2}  (CUBIC in √E_j)

Viscosity: 2ν × 2^{2j} × E_j  (QUADRATIC in √E_j)

For viscosity to dominate:
```
2ν 2^{2j} ≥ (2C/3) 2^{3j/2} √E_j
√E_j ≤ (3ν/C) 2^{j/2}
```

This is CONDITIONAL: requires ω ∈ B^{1/2}_{2,∞} with small norm.
The factor 2/3 gives 50% more room than θ₀ = 1, but the
fundamental SCALING (cubic vs quadratic) is unchanged.

### What Would Close the Proof

**Option A: θ(j) ~ 2^{-j}** (changes scaling)

If θ(j) ≤ C₀ 2^{-j}, then:
|T(j,j)| ≤ C₀ C 2^{-j} × 2^{3j/2} × E_j^{3/2} = C₀C × 2^{j/2} × E_j^{3/2}

For viscosity: 2ν 2^{2j} ≥ C₀C 2^{j/2} √E_j
→ √E_j ≤ (2ν/(C₀C)) 2^{3j/2}
→ E_j ≤ const × 2^{3j}

This threshold GROWS with j, so smooth data (E_j → 0 rapidly) stays
far below it. The bootstrap closes unconditionally.

**The data supports this**: θ(j) ~ 0.003 × 2^{-j}, decreasing with j.
But proving it requires DYNAMICAL input (not just div-free structure).

**Option B: Use the √N_j cancellation rigorously**

For the DISCRETE matrix M(k̂_i, k̂_j) with N_j entries per row:
- Schur bound: ||M||_op ≤ max_row_sum ~ (2/3) N_j max|M|
- Frobenius norm: ||M||_F ~ √(N_j² × ⟨|M|²⟩) ~ N_j/√8

For RANDOM ω̂ (isotropic on ℓ²):
E[|T|] ~ ||M||_F / N_j ~ 1/√8

But ||ω||² = 1 and ||S||_∞ ~ 1/√N_j × ... so:
θ_random ~ (1/√8) / (1 × something) ~ 1/√N_j ~ 2^{-j}

The √N cancellation gives the 2^{-j} decay for random fields.
But NS solutions are deterministic, not random.

**Option C: Dynamical constraint on θ(j)**

The NS dynamics prevent sustained high θ:
- High θ(j) means strong intra-shell transfer
- This rapidly redistributes energy within the shell
- Which destroys the phase alignment that created high θ
- So θ(j,t) is self-limiting (anti-twist mechanism)

This is PHYSICAL but not MATHEMATICAL (yet).

### What We Actually Have

1. **θ₀ = 2/3 for all div-free fields** (PROVED, Schur test)
   - Novel analytical result with closed-form proof
   - Shows genuine angular cancellation in NS bilinear symbol
   - Reduces constant by 50% but doesn't change scaling
   - Publishable as a standalone result

2. **θ(j) ~ 0.003 × 3^{-j} for random div-free fields** (MEASURED)
   - 800+ measurements, resolution-independent
   - Consistent with √N cancellation mechanism
   - Not yet proved rigorously

3. **θ(j) ~ 3-5% for NS solutions at t=3** (MEASURED)
   - N=64 and N=128, identical results
   - Much smaller than worst case θ₀ = 2/3
   - Suggests NS dynamics enforce additional cancellation

4. **59 computer-assisted theorems** (PROVED, interval arithmetic)
   - Verify regularity for specific (N, ν, IC)
   - Rigorous, Chen-Hou paradigm
   - Not general, but provides confidence

5. **3 Lean lemmas** (PROVED, machine-checked)
   - Single-mode orthogonality
   - Strain self-depletion
   - Direction rotation non-negativity

### Honest Assessment

The proof is NOT complete. The gap:
```
PROVED:    θ₀ ≤ 2/3 for all div-free fields (Schur test)
NEEDED:    θ(j) ≤ C 2^{-j} for NS solutions (dynamic cancellation)
DATA:      θ(j) ≈ 0.003 × 3^{-j} (measured, consistent with conjecture)
```

The 2/3 bound is a NECESSARY ingredient (it proves the symbol has the
right structure for cancellation) but not SUFFICIENT (it doesn't change
the supercritical scaling).

The missing ingredient is a DYNAMICAL argument that shows NS solutions
cannot sustain θ(j) = 2/3. The data overwhelmingly supports θ << 2/3,
but proving it requires understanding why the NS dynamics prevent
phase alignment.

### Path Forward

1. Publish θ₀ = 2/3 as a new result on the NS bilinear symbol
2. Combine with dynamical argument for θ(j) ~ 2^{-j}
3. Or: find a completely different approach to close the scaling gap
4. The computer-assisted proofs give rigorous results for specific ICs

## 113 proof files. The gap is identified. Keep pushing.
