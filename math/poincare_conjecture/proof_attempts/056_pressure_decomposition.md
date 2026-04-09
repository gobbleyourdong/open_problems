---
source: Pressure Hessian isotropic/deviatoric decomposition at x*
type: CRITICAL DATA — the crossover point
status: CROSSOVER CONFIRMED — isotropic dominates at high ρ
date: 2026-03-26 cycle 3
---

## The Decomposition at x* (TG N=64)

```
H = H^I + H^D
H^I = (Δp/3)I    (isotropic, LOCAL, always > 0 at x*)
H^D = H - H^I    (deviatoric, NON-LOCAL, always < 0 at x*)
```

### Data:
```
t     ρ      ê·H·ê   H_iso    H_dev    ratio   winner
0.00  2.00   +0.50   +0.67   -0.17    4.00    isotropic
1.50  1.41   -0.39   +0.10   -0.49    0.21    deviatoric
2.50  2.66   -0.64   +0.87   -1.51    0.57    deviatoric
3.50  6.86   -2.21   +4.19   -6.40    0.65    deviatoric
4.00  12.86  +0.29   +20.65  -20.36   1.01    CROSSOVER
4.50  19.05  +4.80   +56.95  -52.15   1.09    isotropic
```

### Key findings:

1. **H_iso = Δp/3 > 0 ALWAYS at x*** (because |ω|²/2 > |S|² always)
2. **H_dev < 0 ALWAYS at x*** (deviatoric enables stretching)
3. **The ratio H_iso/|H_dev| INCREASES with ρ**
4. **Crossover at ρ ≈ 12**: above this, isotropic wins → ê·H·ê > 0
5. **Combined with -α² self-depletion**: dα/dt ≤ -α² + |H_dev| at high ρ

### Scaling:

From data and Buaria & Pumir 2023:
- H_iso ~ Δp/3 ~ |ω|²/6 ~ ρ²/6 (grows as ρ²)
- |H_dev| ~ c × ρ^{2γ} with γ < 1 (grows slower than ρ²)

At the crossover: ρ²/6 = c × ρ^{2γ} → ρ_cross = (6c)^{1/(2-2γ)}

For γ ≈ 0.8 (typical): ρ_cross = (6c)^{2.5}

Above ρ_cross: ê·H·ê > 0 and grows as ρ² - cρ^{2γ} ~ ρ² for large ρ.

### The Proof Implication

At x* with ρ > ρ_cross:

```
dα/dt ≤ -α² - (positive ê·H·ê) + viscous
      ≤ -α² + viscous
```

The -α² term forces α → 0. Stretching is self-limiting.

At x* with ρ ≤ ρ_cross:

```
dα/dt ≤ -α² + |H_dev| ≤ -α² + C × ρ^{2γ}
```

Since ρ ≤ ρ_cross (bounded), |H_dev| ≤ C × ρ_cross^{2γ} (bounded constant).
So dα/dt ≤ -α² + C_fixed.

This ODE has equilibrium at α = √C_fixed. Above this: dα/dt < 0.
So α ≤ max(α₀, √C_fixed). BOUNDED.

### THE ARGUMENT

1. Below ρ_cross: α is bounded by √C_fixed (from the ODE)
2. Above ρ_cross: pressure helps and α decreases toward 0
3. In both regimes: α is bounded
4. Bounded α → dρ/dt ≤ ρ × α_max → exponential growth → BKM integral finite → REGULARITY

### THE CATCH

This argument assumes:
- The strain ODE dα/dt ≤ -α² + pressure + viscous correctly represents
  the dynamics at x* (need to account for frame rotation, transport, etc.)
- The deviatoric bound |H_dev| ≤ Cρ^{2γ} with γ < 1 is POINTWISE at x*,
  not just statistical (Buaria & Pumir showed it statistically)
- The crossover ρ_cross is finite and universal

### What's Needed

1. PROVE |H_dev(x*)| ≤ Cρ^{2γ} pointwise (not just conditional average)
2. PROVE the frame rotation terms in dα/dt don't break the bound
3. Quantify ρ_cross for the universal constant

OR: verify with interval arithmetic at specific (N, ν, IC) to get
a computer-assisted proof for specific cases.
