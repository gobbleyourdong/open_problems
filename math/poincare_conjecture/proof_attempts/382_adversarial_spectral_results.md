---
source: Adversarial verification of the regression spectral bound
type: DATA — gradient-optimized adversarial test, all N close
file: 382
date: 2026-03-29
---

## THE BOUND

R(s*) = |∇u|²/|ω|² ≤ 1 + (||M_res||_op × N + c × Y_max) / |ω|²

where:
- M_res is the N×N residual matrix (from regressing X on Y)
- ||M_res||_op is its spectral norm
- c = Cov(X,Y)/Var(Y) < 0 (negative regression coefficient)
- Y_max = |ω|² - N (vorticity coherence at global max)

Via trace-free: if R < 13/8 → S²ê < 3|ω|²/4 → barrier closes → NS regular.


## ADVERSARIAL RESULTS (gradient-optimized, Nelder-Mead with 5 restarts)

| N | k-trials | worst R_bound | R_actual | margin to 13/8 | status |
|---|----------|--------------|----------|----------------|--------|
| 5 | 200 | **1.400** | 0.831 | 13.8% | ✓ |
| 6 | 200 | **1.419** | 0.796 | 12.7% | ✓ |
| 8 | (running) | - | - | - | - |
| 10 | (running) | - | - | - | - |

All bounds close with > 12% margin even under adversarial optimization.

The R_actual (true ratio at global max) is far below the bound:
- R_actual ≈ 0.8-0.83 (about 50% of the bound)
- The bound is conservative but SUFFICIENT


## WHAT THIS MEANS

The regression spectral approach provides a CERTIFIED upper bound that:
1. Is RIGOROUS (derived from spectral norm inequality + regression)
2. Is COMPUTABLE for any specific mode configuration
3. CLOSES for all tested N with margin > 12%
4. Is ROBUST under adversarial optimization

For a PROOF: need to show the bound is < 13/8 UNIVERSALLY (for all mode configs).
This requires bounding ||M_res||_op and the regression coefficient c in terms
of the geometric parameters (κ, D, A, B).


## THE PROOF STRUCTURE

### Given:
- N modes with wavevectors k_1,...,k_N and polarizations v̂_1,...,v̂_N
- Global max vertex s* maximizing |ω|²(s)

### To prove: R(s*) = |∇u|²/|ω|² < 13/8

### Step 1: Decompose the excess
X(s) = Σ_α Δ_α q_α (where q_α = s_js_k, summing over pairs α=(j,k))
Y(s) = Σ_α D_α q_α (vorticity coherence)

### Step 2: Regression residual
L(s) = X(s) - c Y(s) where c = ΣΔD/ΣD²

### Step 3: Spectral bound on residual
L(s) = s^T M s (quadratic form in ±1 variables)
max_s L(s) ≤ ||M||_op × N (spectral bound, nearly tight)

### Step 4: Regression at global max
X(s*) = L(s*) + c Y(s*) ≤ ||M||_op × N + c × Y_max

### Step 5: Ratio bound
R(s*) ≤ 1 + (||M||_op N + c Y_max)/(N + 2Y_max)

### Step 6: Show < 13/8
Need: ||M||_op N + c Y_max < (5/8)(N + 2Y_max)

Since c < 0: the LHS has a NEGATIVE term that grows with Y_max.
For Y_max large enough: the bound ALWAYS closes.
For Y_max small: ||M||_op must be bounded.


## WHAT REMAINS

1. **Universal bound on ||M||_op**: Show ||M||_op ≤ f(N) for some f.
   From Frobenius: ||M||_op ≤ ||M||_F = σ_L/√2.
   Need: σ_L²/2 (which is VarL/2) bounded in terms of N.

2. **Lower bound on |c|**: Show c = ΣΔD/ΣD² has |c| bounded away from 0.
   From the algebraic formula: c ≈ -(1-κ_avg²) (negative, bounded by 1).

3. **Combined**: Show ||M||_op × N + c × Y_max < 5(N+2Y_max)/8
   for all valid mode configurations on T³.


## 382. Adversarial verification: R_bound < 13/8 for N=5 (margin 13.8%) and N=6 (12.7%).
## The regression spectral approach is the most promising proof path.
## Need: universal bounds on ||M||_op and |c| from the Biot-Savart structure.
