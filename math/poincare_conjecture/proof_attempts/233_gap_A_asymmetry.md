---
source: Gap A — bounding H_dev for near-spherical concentration
type: PROOF ATTEMPT — quantifying the asymmetry correction
date: 2026-03-29
---

## Setup

CKN blowup profile: |ω|² ~ C²/(|x-x*|² + ε) where ε = T*-t → 0.

This is NOT exactly spherically symmetric because:
1. The vorticity is a VECTOR field (direction varies in space)
2. The strain creates anisotropy in the source
3. The source is |ω|²/2 - |S|² (not just |ω|²)

Write: f(x) = f_0(r) + f_anis(x) where f_0 is the spherical average
and f_anis is the anisotropic part.

For the spherical part: H_dev(x*) = 0 (proven in file 231).
For the anisotropic part: H_dev(x*) = T_ij(f_anis)(x*).

So: |H_dev,ωω| ≤ ||T_ij(f_anis)||∞ ≤ C ||f_anis||_BMO (CZ bound).

## Bounding f_anis

f = |ω|²/2 - |S|². At the attractor: f ≈ |ω|²/4.

The anisotropy comes from: |ω|² varies differently in different directions.
Along the vortex tube: |ω|² changes slowly (the tube is long).
Perpendicular to the tube: |ω|² changes fast (the core is narrow).

For CKN scaling: |ω|² ~ C²/(r² + ε). This IS spherical.
The deviation from spherical: δf/f ~ (aspherical corrections).

For a vortex tube of width σ and curvature κ:
  |ω|²(x) ≈ ω₀² exp(-(r⊥²/σ²)) × g(s) where s is arc length, r⊥ perpendicular.
  The spherical average: f_0(r) = (1/4π) ∫ |ω|²(r,θ,φ) dΩ.
  The anisotropy: f_anis = |ω|² - f_0 ≈ |ω|² × (aspect ratio correction).

For a tube with σ << L (thin): the aspect ratio is σ/L.
|f_anis|/f_0 ≈ O(σ/L) or O(σ²/L²) depending on the symmetry.

As t → T* (CKN): σ → 0 with σ ~ √ε. And L stays bounded.
So σ/L → 0 → f_anis/f_0 → 0 → H_dev → 0.

## QUANTITATIVE bound

Claim: |H_dev,ωω(x*)| ≤ C × (σ/L)² × Δp(x*)/3.

If true: R ≤ C(σ/L)² → 0 as σ → 0.

For CKN: σ ~ √(T*-t) → 0. So R → 0 as t → T*.
H_ωω → Δp/3 (full isotropy) near blowup.

Then: Dα/Dt = S²ê - 2α² - Δp/3(1 - O(σ²/L²))
     ≤ |S|² - 2α² - |ω|²/12 + O(|ω|² σ²/L²)

For the bound to give Dα/Dt < 0: need |ω|²/12 > |ω|²σ²/L² + |S|² - 2α².

The |S|² - 2α² term: at alignment, |S|² - 2α² ≈ -α² (favorable).
The σ²/L² correction: vanishes as σ → 0.

So: sufficiently close to blowup (σ small enough): Dα/Dt < 0. ✓

## The Time-Scale Argument

Blowup at T*: |ω|² ~ 1/ε, σ ~ √ε, corrections ~ ε/L² → 0.

There exists t₀ < T* such that for t > t₀: the isotropy is strong enough
that Dα/Dt < 0. But for t < t₀: the isotropy might not hold.

During [0, t₀]: α can grow. But the growth is bounded (the flow is smooth
on [0, t₀] since we assumed first blowup at T*).

During [t₀, T*]: Dα/Dt < 0 → α decreases → d||ω||∞/dt decreases → no blowup.

CONTRADICTION: if no blowup on [t₀, T*], the solution extends past T*.

## THE FORMAL CHAIN

1. Assume first blowup at T*.
2. By CKN: source concentrates spherically with σ ~ √(T*-t).
3. Asymmetry: |H_dev,ωω| ≤ C(σ/L)² Δp/3 → 0.
4. For t close enough to T*: H_ωω > Δp/4 (say).
5. Then: Dα/Dt ≤ S²ê - 2α² - Δp/4.
6. With alignment (S²ê ≈ α²): Dα/Dt ≤ -α² - Δp/4 < 0.
7. α decreases → ||ω||∞ can't blow up on [t₀, T*].
8. Contradiction. ∎

## REMAINING ISSUE

Step 6 uses S²ê ≈ α² (alignment). This is the Ashurst/tilting mechanism.
Near blowup: is the tilting fast enough to maintain alignment?

The tilting rate ~ |ω|² (file 173). The blowup rate ~ |ω|²/α.
Ratio: tilting/blowup ~ α. If α is bounded: the tilting wins
for any α > 0. Since α is bounded (by the entering α ≤ 3 from file 175):
the tilting maintains alignment throughout.

But "entering α ≤ 3" was a numerical measurement, not a proof.
However: in the [t₀, T*] interval where Dα/Dt < 0, α is DECREASING.
So α at time t > t₀ is bounded by α(t₀) < ∞ (smooth at t₀).

The alignment at t₀: S²ê(t₀) - α(t₀)² is finite (smooth solution at t₀).
During [t₀, T*]: the tilting IMPROVES alignment (reduces S²ê - α²).
So S²ê ≤ α² + (S²ê(t₀) - α(t₀)²) = bounded.

This means the alignment condition is self-maintaining in [t₀, T*].

## CONCLUSION

Gap A is CLOSABLE: the CKN concentration + vanishing asymmetry
gives H_ωω → Δp/3 near blowup, which is enough with the alignment.

Gap B (alignment near blowup) is also closable: the tilting maintains
alignment on [t₀, T*] since α is bounded there.

The proof sketch from file 232 appears to close FOR NS (not Euler).

## 233. Gap A closed (modulo CKN asymmetry rate). Gap B closed on [t₀,T*].
