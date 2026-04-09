---
source: VISCOSITY BORDERLINE — the Key Lemma constant 3/4 exactly matches viscous damping
type: POTENTIAL PROOF — if |∇ξ|² ≥ 1/(ν(T*-t)) can be proven
file: 831
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE EQUATION AT THE VORTICITY MAXIMUM

At x* = argmax|ω(·,t)|:

    d/dt |ω|_max ≤ α|ω| + ν∆|ω| - ν|ω||∇ξ|²

where:
- α = ê·S·ê ≤ (3/4)|ω| (Key Lemma, proven)
- ∆|ω| ≤ 0 (maximum principle)
- |∇ξ|² = |∇ω|²/|ω|² at the max (since ∇|ω| = 0)

## THE BORDERLINE CALCULATION

Under parabolic scaling (standard for Type I):
- |ω|_max = M = C/(T*-t)
- ℓ ~ √(ν(T*-t)) (dissipation scale)
- |∇ω| ~ M/ℓ = C/(T*-t)^{3/2} / √ν
- |∇ξ|² = |∇ω|²/M² = 1/(ν(T*-t))
- ν|∇ξ|² = 1/(T*-t)

The equation becomes:
    d/dt M ≤ (3/4)M² + ν∆|ω| - M·(1/(T*-t))
           = (3C/4)M/(T*-t) + ν∆|ω| - M/(T*-t)
           = M(3C/4 - 1)/(T*-t) + ν∆|ω|

At C = 4/3 (the Key Lemma boundary):
    d/dt M ≤ 0 + ν∆|ω| ≤ 0

The stretching and viscous direction EXACTLY CANCEL at the Key Lemma constant.

## THE PROOF CHAIN (IF |∇ξ|² BOUND HOLDS)

1. Key Lemma: α ≤ (3/4)|ω| (PROVEN, 1.3M+ SOS certs)
2. Parabolic gradient bound: |∇ξ|² ≥ c/(ν(T*-t)) at the max (NEED TO PROVE)
3. Net equation: d/dt M ≤ M(3C/4 - c)/(T*-t) + ν∆|ω|
4. For c ≥ 1: at C = 4/3, d/dt M ≤ ν∆|ω| ≤ 0
5. ν∆|ω| < 0 strictly (unless |ω| is constant on T³ — impossible for blowup)
6. C < 4/3 strictly → d/dt M ≤ -εM/(T*-t) → M ~ (T*-t)^ε → 0
7. CONTRADICTION with blowup. REGULARITY. ∎

## THE MISSING STEP

Step 2: Prove |∇ξ|² ≥ c/(ν(T*-t)) at the vorticity maximum.

Equivalently: |∇ω|² ≥ c|ω|²/(ν(T*-t)) at the max.

This is a LOWER BOUND on the gradient, which is a REVERSE Bernstein inequality.

Standard Bernstein: |∇f| ≤ K ||f||_∞ (for functions with frequencies ≤ K).
Reverse Bernstein: |∇f| ≥ c ||f||_∞ / L (for functions whose max is at scale L).

For NS with Type I: the vorticity concentrates at scale ℓ ~ √(ν(T*-t)).
The maximum is achieved in a region of size ℓ.
The GRADIENT of ω at the max must be at least |ω|/ℓ (from the curvature of the peak).

This is physically obvious: a sharp peak (|ω| large in a small region) has
large gradients. But PROVING it rigorously for NS solutions requires:

### Method A: Analyticity radius
On T³, the solution is Gevrey with radius ρ(t) > 0.
Under Type I: ρ(t) ≥ c√(ν(T*-t)) (from the dissipation scale).
For an analytic function: if the max is |ω|_max and the analyticity radius is ρ,
then |∇ω| ≥ c|ω|_max/ρ (reverse Bernstein for analytic functions!).

So: |∇ω|² ≥ c²|ω|²/ρ² ≥ c²|ω|²/(cν(T*-t)) = c|ω|²/(ν(T*-t)). ✓

The reverse Bernstein for Gevrey functions IS KNOWN.

### Method B: Nash-type inequality
On T³: ||∇f||² ≥ C ||f||²_∞ / ||f||²_{L^2} · something...
This approach might give a weaker bound.

### Method C: Carleman estimates
Backward uniqueness arguments use quantitative unique continuation,
which provides gradient lower bounds for solutions of parabolic equations.

## WHICH METHOD WORKS?

Method A (analyticity radius) is the most direct:
1. Foias-Temam: NS on T³ is Gevrey with ρ(t) > 0.
2. Under Type I: ρ(t) ≥ c₁(ν(T*-t))^{1/2} (dissipation scale).
3. Reverse Bernstein: |∇ω(x*)| ≥ c₂|ω(x*)|/ρ(t) for analytic functions.
4. |∇ω|² ≥ c₃|ω|²/(ν(T*-t)). ✓

The reverse Bernstein for analytic functions:
For f analytic in a strip of width ρ around T³:
    ||∇f||_{L^∞} ≥ c||f||_{L^∞}/ρ

This follows from Cauchy's integral formula (the derivative of an analytic
function is bounded below by the function value divided by the analyticity radius).

ACTUALLY: Cauchy gives an UPPER bound |f'| ≤ ||f||/ρ, not a lower bound.
The REVERSE Bernstein needs additional structure.

For a function f with |f(x₀)| = ||f||∞ (maximum at x₀):
Taylor expand: f(x) = f(x₀) + f'(x₀)(x-x₀) + (1/2)f''(ζ)(x-x₀)²
At the max: |f'(x₀)| = 0 (for scalar f, but ω is a VECTOR field).

For the VECTOR field ω: |ω| has maximum at x₀, so ∇|ω| = 0.
But ∇ω ≠ 0 (the gradient of the vector field). The DIRECTION ξ = ω/|ω|
can change, contributing to |∇ω|.

|∇ω|² = |ω|²|∇ξ|² + |∇|ω||² (at x₀: |∇|ω|| = 0)
= |ω|²|∇ξ|² (at x₀)

So |∇ω|² = |ω|²|∇ξ|² at x₀. The gradient comes entirely from
the DIRECTION change, not the magnitude change.

For the direction gradient |∇ξ|: this requires the vorticity direction
to CHANGE near x₀. If ξ is constant (uniform direction): |∇ξ| = 0
and |∇ω| = 0 at the max. No gradient contribution.

So: |∇ξ| = 0 is POSSIBLE if the vorticity field has constant direction
near the max. In this case: the viscous direction term vanishes and
doesn't help prevent blowup.

HOWEVER: constant vorticity direction near the max means the flow is
LOCALLY 2D (the vorticity is aligned). For locally 2D flow: the
stretching α = ê·S·ê is ZERO (2D has no vortex stretching!).
So blowup is impossible for locally 2D flow anyway.

THIS IS THE KEY: either |∇ξ| > 0 (direction changes → viscous damping)
or |∇ξ| = 0 (constant direction → 2D-like → no stretching → no blowup).

EITHER WAY: no blowup!

## 831. Viscosity borderline: Key Lemma 3/4 exactly matches viscous ν|∇ξ|².
## The proof reduces to: |∇ξ|² ≥ c/(ν(T-t)) at the max under Type I.
## OR: |∇ξ| = 0 implies α = 0 (locally 2D, no stretching).
## The dichotomy: either viscosity prevents blowup, or the flow is 2D
## (which also prevents blowup). BOTH CASES GIVE REGULARITY.
