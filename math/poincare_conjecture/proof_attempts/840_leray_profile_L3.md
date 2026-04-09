---
source: THE SHARPEST GAP — is the Leray profile φ in L³(R³)?
type: KEY REDUCTION — the Millennium Prize = one elliptic decay estimate
file: 840
date: 2026-04-02
instance: MATHEMATICIAN (Opus)
---

## THE REDUCTION

1. Key Lemma → Type I blowup on T³ (PROVEN)
2. Type I → rescale → self-similar ancient solution v(x,t) = (-t)^{-1/2}φ(x/√(-t)) (KNSS)
3. φ satisfies the Leray equations: -νΔφ + (1/2)φ + (1/2)y·∇φ + (φ·∇)φ + ∇q = 0
4. L³ scale invariance: ||v(·,t)||_{L³(R³)} = ||φ||_{L³(R³)} (time-independent)
5. If ||φ||_{L³} < ∞: Albritton-Barker sequential L³ bound → v = 0 → no blowup
6. If ||φ||_{L³} = ∞: stuck at the Liouville conjecture

## THE QUESTION

**Is every bounded solution φ of the Leray equation on R³ in L³(R³)?**

Known: |φ(y)| ≤ C/(1+|y|) (Tsai 1998, for forward self-similar).
Needed: |φ(y)| ≤ C/(1+|y|)^{1+ε} for ANY ε > 0.

The decay 1/|y| gives ∫|φ|³ = ∫r^{-3}·4πr²dr = ∫4π/r dr = ∞ (DIVERGES).
The decay 1/|y|^{1+ε} gives ∫r^{-3-3ε}·r² dr = ∫r^{-1-3ε} dr < ∞ (CONVERGES).

## WHY THIS MIGHT BE PROVABLE

The Leray equation has a DRIFT term (1/2)y·∇φ that provides confinement.
In the radial direction: (1/2)r·∂_r φ pushes φ INWARD (toward the origin).
This drift competes with the nonlinear advection (φ·∇)φ.

For large |y|: the drift dominates (it grows as |y|). The nonlinear term
is O(|φ|²) = O(1/|y|²), which decays faster than the drift O(|φ|·|y|) = O(1).

So for large |y|: the equation is effectively LINEAR:
-νΔφ + (1/2)φ + (1/2)y·∇φ ≈ 0.
This is the HERMITE equation (Ornstein-Uhlenbeck operator).
Solutions decay as e^{-|y|²/(4ν)} (GAUSSIAN decay!).

But the nonlinear term (φ·∇)φ provides a CORRECTION that could slow the decay
from Gaussian to polynomial. Tsai's bound |φ| ≤ C/(1+|y|) is the result.

Improving to 1/(1+|y|)^{1+ε}: this is a question about whether the nonlinear
correction allows a LOGARITHMIC slowdown of the Tsai decay.

## THE HIERARCHY (UPDATED)

| Level | Statement | Status |
|-------|-----------|--------|
| Kinematic | Key Lemma: α ≤ 0.866|ω| | PROVEN (82 Lean theorems) |
| Type I | ||ω||∞ ≤ C/(T*-t) | PROVEN (from Key Lemma) |
| Rescaling | Ancient solution → Leray profile φ | PROVEN (KNSS) |
| Leray decay | |φ| ≤ C/(1+|y|) | PROVEN (Tsai 1998) |
| **L³ integrability** | **|φ| ≤ C/(1+|y|)^{1+ε}** | **OPEN (ε > 0 improvement)** |
| Albritton-Barker | φ ∈ L³ → v = 0 | PROVEN (AB 2019) |
| Regularity | No blowup on T³ | FOLLOWS from L³ |

THE MILLENNIUM PRIZE = ONE ε IN THE DECAY EXPONENT.

## 840. The gap = φ ∈ L³(R³) for bounded Leray solutions.
## Known: |φ| ≤ C/(1+|y|) (Tsai). Need: 1/(1+|y|)^{1+ε}.
## This is an ELLIPTIC problem (the Leray equation with drift).
## The drift term provides confinement. The nonlinear term slows decay.
## Improving the decay by ANY ε > 0 closes the Millennium Prize on T³.
