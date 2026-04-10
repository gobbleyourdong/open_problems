# Backward Decay Test — 2D→3D Dimensional Ladder

**Date:** 2026-04-09
**Script:** `numerics/backward_decay.py`
**Track:** Numerical

## Testing attempt_002's decay claim

Theory track reduced Liouville to: ||w(t)||_∞ → 0 as t → -∞.

## Four-level test

### 1. Heat equation — trivial backward decay
Each Fourier mode grows as e^{|k|²|t|} backward. Bounded ancient ⟹ all
modes zero ⟹ constant. Linear Liouville.

### 2. 2D vorticity — backward decay via maximum principle
No stretching (α=0). Maximum principle gives ||ω(t)||_∞ strictly
decreasing forward. Bounded + monotone → limit L. Strong max principle
forces L=0. **2D Liouville proved.**

### 3. 3D obstruction — stretching breaks max principle
Model: d|ω|²/dt = -2νλ₁|ω|² + 2α|ω|² (diffusion vs stretching).

| νλ₁ | α (stretch) | rate | ω decays? |
|-----|------------|------|-----------|
| 1.0 | 0.5 | +1.0 | YES |
| 1.0 | 1.5 | -1.0 | NO (grows!) |
| 2.0 | 3.0 | -2.0 | NO (grows!) |
| 5.0 | 3.0 | +4.0 | YES |

**When α > νλ₁: vorticity grows.** This is the 2D→3D gap.

### 4. Scale-dependent balance
Diffusion ~ ν/R², stretching ~ C(M). Critical scale R_crit = √(ν/C(M)).

| M | R_crit |
|---|--------|
| 1 | 1.0 |
| 10 | 0.316 |
| 100 | 0.100 |
| 1000 | 0.032 |

- R >> R_crit: diffusion wins → large-scale backward decay (automatic)
- R << R_crit: stretching wins → small-scale persistence (the gap)

## The 2D→3D dimensional ladder

| Dim | Stretching | Max principle | Backward decay | Liouville |
|-----|-----------|---------------|----------------|-----------|
| 2D | α = 0 | YES | YES (proved) | PROVED |
| 3D | α ~ C(M) | NO | OPEN | OPEN |

**The single obstruction: the vortex stretching eigenvalue α.**

## The gap, precisely

Large-scale backward decay is automatic (diffusion always wins at R >> R_crit).
Small-scale backward decay is the open question (stretching can win at R << R_crit).
The bounded ancient condition should constrain the stretching at small scales,
but proving this requires more than the model ODE — it needs the STRUCTURE of
(ω · ∇)u = Sω for bounded divergence-free fields.
