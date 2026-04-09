---
source: Pressure Hessian lower bound — using NS structure for N ≥ 5
type: PROOF APPROACH — H_ωω ≥ c|ω|² would close the gap
file: 375
date: 2026-03-29
---

## THE GAP FOR N ≥ 5

The barrier at R = α/|ω| = 1/2:

    DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω|

For DR/Dt < 0: need S²ê < 3|ω|²/4 + H_ωω.

Currently:
- S²ê ≤ (N-1)|ω|²/4 (proven for N modes, file 363)
- H_ωω > 0 (proven when α > 0, file 267)
- For N ≤ 4: S²ê ≤ 3|ω|²/4, and H_ωω > 0 gives strict. CLOSED.
- For N ≥ 5: S²ê ≤ (N-1)|ω|²/4 > 3|ω|²/4. Need H_ωω to absorb the excess.

Required: H_ωω > S²ê - 3|ω|²/4 ≥ ((N-1)/4 - 3/4)|ω|² = (N-4)|ω|²/4.


## THE PRESSURE EQUATION

For incompressible NS on T³:

    Δp = -Tr(∇u ⊗ ∇u) = |ω|²/2 - |S|²    (standard identity)

At the global max x* of |ω|: the source |ω|²/2 - |S|² is POSITIVE
(since |ω|²/|S|² → 4 at the attractor, so |ω|²/2 > |S|²/2 typically).


## H_ωω FROM THE PRESSURE

H_ωω = -ê · ∇²p · ê = ê-component of the pressure Hessian.

From Δp = f where f = |ω|²/2 - |S|²:

    p(x) = -(Δ)⁻¹f(x) = -Σ_k f̂_k e^{ik·x}/|k|²

    ∂²p/∂ê² = -Σ_k (k·ê)²/|k|² × f̂_k e^{ik·x}

    H_ωω = Σ_k (k·ê)²/|k|² × f̂_k e^{ik·x*}

(where we use H_ωω = -∂²p/∂ê²... actually need to check sign convention.)


## THE FOURIER LEMMA (FROM FILE 267)

At x* where f = Δp has a POSITIVE value (f(x*) > 0):

The Fourier lemma says: for each k-mode with positive coefficient at x*,
the pressure coefficient has OPPOSITE sign (from the negative Laplacian inverse).

This gives H_ωω > 0 (each term in the sum is positive).


## LOWER BOUND ON H_ωω

The Fourier lemma gives H_ωω > 0 but not H_ωω ≥ c|ω|² for specific c > 0.

For a LOWER bound: need to control the pressure Fourier coefficients.

### Simple estimate:

f(x*) = |ω(x*)|²/2 - |S(x*)|². Using |S|² ≤ (some fraction)|ω|²:

From the attractor |ω|²/|S|² ≈ 4: |S|² ≈ |ω|²/4. So f ≈ |ω|²/4 > 0.

The k=0 mode of f: f̂₀ = <f> = <|ω|²/2 - |S|²> = <|ω|²>/2 - <|S|²>
= ||ω||²/(2(2π)³) - ||S||²/(2π)³ = 0 (using ||S||² = ||ω||²/2).

So f̂₀ = 0. The pressure has no zero-mode contribution. H_ωω comes from k ≠ 0.

### For the dominant mode k₁:

f̂_k₁ e^{ik₁·x*} = (Fourier coefficient of |ω|²/2 - |S|² at mode k₁)

At x*: f(x*) = |ω|²/2 - |S|² > 0. The dominant Fourier modes of f near x*
are the ones that peak at x*.

For |ω|² = Σa_j² + 2Σa_ja_k d_{jk} cos(difference phase): the quadratic terms
generate new Fourier modes at sum and difference frequencies.

The convolution structure makes this complex. But schematically:

f̂ ~ |ω̂|² (convolution) at low modes, giving f̂ ~ |ω|²/N for N modes.

Then: H_ωω ~ Σ (k·ê)²/|k|² × |ω|²/N ~ |ω|²/N × (some constant).

For N modes: H_ωω ~ C|ω|²/N. This decreases with N!

Required for closure: H_ωω > (N-4)|ω|²/4. So C/N > (N-4)/4 → C > N(N-4)/4.
For large N: need C > N²/4, but C is a fixed constant. FAILS.


## THE ISSUE: H_ωω DECREASES WITH N

For a field spread over many modes: the pressure curvature is small because
the pressure source f is smooth (slowly varying) at x*. The curvature of
a smooth function is bounded by its second derivatives, which scale as k²f̂.

For N modes at unit k: f̂ ~ 1/N per mode. k² ~ 1. H_ωω ~ 1/N × N = O(1).

But the excess to absorb is (N-4)/4. For large N: O(N) vs O(1). FAILS.


## ALTERNATIVE: COMBINE KINEMATIC + DYNAMIC

### Step 1: Use the per-mode bound for the DOMINANT modes
The M largest modes (M ≤ 4) contribute:
S²ê_dominant ≤ (M-1)|ω_dominant|²/4 ≤ 3|ω|²/4 (if M ≤ 4).

### Step 2: Bound the TAIL contribution
The remaining N-M modes have small amplitudes a_k. Their contribution to S²ê:
S²ê_tail ≤ (Σ_tail |ŝ_k|)² ≤ (Σ_tail a_k sin(2γ_k)/4 × |ω|)² ... hmm, the |ω| factor makes this ~ |ω|² × (Σ_tail a_k/|ω|)².

If Σ_tail a_k << |ω|: the tail contribution is small.

### Step 3: Cross-terms
S²ê = |Σ_dom ŝ_k + Σ_tail ŝ_k|² ≤ (|Σ_dom| + |Σ_tail|)²
= S²ê_dom + 2√(S²ê_dom × S²ê_tail) + S²ê_tail

For the cross: 2√(S²ê_dom × S²ê_tail) ≤ ... needs bounding.

### The energy split
At x*: |ω| = Σ p_k = Σ_dom p_k + Σ_tail p_k.

If the dominant 4 modes contribute fraction f of |ω|:
|ω_dom| = f|ω|. |ω_tail| = (1-f)|ω|.

S²ê_dom ≤ 3f²|ω|²/4.
S²ê_tail ≤ ... bounded by the per-mode approach for the tail.

S²ê ≤ (√S²ê_dom + √S²ê_tail)² ≤ (f√3/2 + (1-f)C_tail)² × |ω|²

For the total to be < 3|ω|²/4: need f√3/2 + (1-f)C_tail < √3/2.
→ (1-f)(C_tail - √3/2) < 0.
→ C_tail < √3/2 ≈ 0.866 (since 1-f > 0).

Is C_tail < 0.866? The tail modes have small amplitudes but many modes.
From the Parseval bound: S²ê_tail ≤ Σ_tail|ŝ_k|² ≤ |ω|²/4 (diagonal bound applies to tail too).
√(S²ê_tail/|ω|²) ≤ 1/2 = 0.5 < 0.866. ✓ BUT this uses the Parseval bound for
the tail (diagonal only, ignoring cross-terms within the tail).

Actually: for the tail, S²ê_tail = |Σ_tail ŝ_k|². The cross-terms within
the tail could be positive. By the (N_tail-1)/4 bound:
S²ê_tail ≤ (N_tail-1)|ω_tail|²/4.

But |ω_tail| = (1-f)|ω|. So S²ê_tail ≤ (N_tail-1)(1-f)²|ω|²/4.

For the overall bound:
S²ê ≤ (√(3f²/4) + √((N_tail-1)(1-f)²/4))² |ω|²
= (f√3/2 + (1-f)√(N_tail-1)/2)² |ω|²

For this < 3|ω|²/4:
f√3 + (1-f)√(N_tail-1) < √3 (dividing by |ω|/2)
(1-f)(√(N_tail-1)-√3) < 0

This requires √(N_tail-1) < √3 → N_tail < 4. So the tail must have at most 3 modes!

If the tail has ≥ 4 modes: √(N_tail-1) ≥ √3, and the inequality fails.

So: the split into dominant + tail doesn't help unless the tail is ≤ 3 modes.
This effectively requires N ≤ 7 (4 dominant + 3 tail) for this approach.

For N ≥ 8: need a different decomposition.


## WHAT ACTUALLY LIMITS THE TOTAL S²ê?

From all the analysis: the KINEMATIC bounds (per-mode, trace-free, Parseval)
all give S²ê ≤ f(N)|ω|² where f(N) grows with N. But the NUMERICAL
S²ê/|ω|² stays below 0.28 for all N.

The discrepancy: the bounds don't capture the DIRECTIONAL CANCELLATION
of the ŝ_k vectors. This cancellation is a consequence of:
1. The ŝ_k vectors live in 3D (limited directions)
2. The Biot-Savart structure constrains each ŝ_k to a specific 2D plane
3. The global max condition forces specific amplitude-angle relationships

A RIGOROUS proof of S²ê ≤ |ω|²/3 (or even < 3|ω|²/4) for general N
likely requires a new technique that captures these directional constraints.


## STATUS

The pressure Hessian approach (H_ωω ≥ c|ω|²) does NOT scale well with N
because H_ωω ~ O(1) while the excess ~ O(N). Not viable for large N.

The energy split approach works for N ≤ 7 but not beyond.

The fundamental challenge remains: prove directional cancellation in
|Σŝ_k|² for N ≥ 5 modes in R³.


## 375. Pressure Hessian approach doesn't scale with N (H_ωω ~ 1/N).
## Energy split works for N ≤ 7 only.
## The directional cancellation remains the core challenge.
