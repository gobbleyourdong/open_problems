---
source: T³ LIOUVILLE THEOREM — ancient solutions with Type I decay are trivial
type: THEOREM + PROOF — proven on T³, gap is the rescaling T³→R³
file: 806
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THEOREM

Let v be a smooth bounded ancient solution of the incompressible Navier-Stokes
equations on T³ × (-∞, 0] with viscosity ν > 0 and Type I decay:
    ||v(·,t)||_{L∞(T³)} ≤ C/√(-t) for all t < 0.
Then v ≡ 0.

## PROOF

Step 1: L² vanishing.
Since T³ is compact with |T³| = (2π)³:
    ||v(·,t)||²_{L²(T³)} ≤ ||v(·,t)||²_∞ · |T³| ≤ C²(2π)³/(-t) → 0 as t → -∞.

Step 2: Energy equality.
For smooth solutions on T³ (periodic BC → no boundary terms):
    ||v(t₂)||²_{L²} + 2ν ∫_{t₁}^{t₂} ||∇v(τ)||²_{L²} dτ = ||v(t₁)||²_{L²}
for all t₁ < t₂ ≤ 0.

Step 3: Limit.
Set t₂ = 0, t₁ = s, and send s → -∞:
    ||v(0)||²_{L²} + 2ν ∫_{-∞}^{0} ||∇v(τ)||²_{L²} dτ = lim_{s→-∞} ||v(s)||²_{L²} = 0.

Step 4: Conclusion.
Both terms on the LHS are non-negative. Their sum is 0.
Therefore ||v(0)||²_{L²} = 0, i.e., v(·,0) = 0 in L²(T³).
By forward uniqueness of mild solutions: v ≡ 0 for all t ≥ 0.
By backward uniqueness (ESS, or smoothness + uniqueness of ancient solutions):
v ≡ 0 for all t < 0. ∎

## WHY THIS WORKS ON T³ BUT NOT R³

| Feature | T³ | R³ |
|---------|----|----|
| Bounded → L² | ✓ (compact) | ✗ (infinite measure) |
| Energy equality exact | ✓ (no boundary) | ✗ (flux through ∂B_R) |
| L² → 0 from Type I | ✓ (step 1) | ✗ (||v||_{L²(R³)} may be ∞) |

On R³: ||v||∞ ≤ C/√(-t) does NOT give ||v||_{L²(R³)} → 0 because:
- R³ has infinite volume
- The integral ∫_{R³} |v|² could be ∞ even for bounded v
- The local energy inequality has boundary flux terms on B_R

## THE REMAINING GAP

The standard blowup argument (KNSS):
1. Type I blowup on T³ at (x₀, T*)
2. Rescale: u_λ(x,t) = λu(x₀+λx, T*+λ²t) on T³/λ
3. λ → 0: u_λ → v, ancient solution on R³
4. Need: v ≡ 0 (Liouville conjecture on R³, OPEN)

Our T³ Liouville theorem proves v ≡ 0 if v lived on T³.
But the rescaling changes the domain from T³ to R³.
The ancient solution lives on R³, where our theorem doesn't apply.

## KEY QUESTION

Can we avoid the spatial rescaling? I.e., can we derive a contradiction
from Type I blowup on T³ WITHOUT constructing an ancient solution on R³?

If yes: the T³ Liouville theorem + the Key Lemma (Type I growth) would
give NS regularity on T³.

## APPROACHES TO AVOID RESCALING

### A. Direct energy argument on T³
Use the energy equality for the ORIGINAL solution u on T³:
||u(t₂)||² + 2ν∫||∇u||² = ||u(t₁)||²

This goes FORWARD in time. At t₂ = T* (blowup): ||u||_{L²} stays bounded
(energy decreases). No contradiction — the L² norm is controlled.

### B. Enstrophy argument on T³
d/dt ||ω||² = 2∫ω·Sω - 2ν||∇ω||²
The stretching integral ∫ω·Sω involves the CZ operator → L∞ barrier (THEWALL).
The Key Lemma bounds α at the max but not the integral. See file 803.

### C. Backward uniqueness on T³
If we could show v(·, T*) = 0 (the solution vanishes at blowup time):
backward uniqueness would give v ≡ 0. But v(·, T*) is where the blowup
occurs — it's NOT zero (the vorticity diverges).

### D. Time-reversed argument
Consider w(x,t) = u(x, T*-t) (time reversal). This satisfies:
∂_t w + (w·∇)w = -∇p - νΔw (anti-diffusion!)
This is ILL-POSED. Not useful.

### E. Frequency-localized argument
On T³: Fourier modes are discrete. Near blowup, energy cascades to high
modes. Can the Key Lemma + viscous damping + discrete spectrum prevent
the cascade from completing?
STATUS: UNEXPLORED. This is the most promising direction.

## 806. T³ Liouville: bounded ancient solutions with Type I decay are trivial.
## Proof: energy equality + compact domain → L² → 0 → v ≡ 0. Simple.
## Gap: ancient solution from blowup rescaling lives on R³, not T³.
## Key question: can we avoid the rescaling and stay on T³?
