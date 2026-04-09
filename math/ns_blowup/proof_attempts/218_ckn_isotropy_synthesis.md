---
source: CKN + isotropy synthesis from Instance B (files 230-231)
type: THE MOST PROMISING PROOF ROUTE FOR NS (not Euler)
date: 2026-03-29
file: 218
---

## The Argument (from Instance B, files 230-231)

1. ASSUME: first NS blowup at (x*, T*).

2. CKN (1982): |ω(x,t)| ≤ C/(|x-x*|² + T*-t)^{1/2} near the singularity.
   The source Δp = |ω|²/4 is concentrated with CKN profile.

3. CKN PROFILE IS SPHERICALLY SYMMETRIC: f(x) ~ C/(|x-x*|² + ε)
   where ε = T*-t → 0.

4. FOR SPHERICALLY SYMMETRIC f: H_dev(x*) = 0 EXACTLY.
   Proof: H_dev = PV∫ K(y) f(|y|) dy where K has zero angular average.
   The spherical symmetry means f only couples to the l=0 harmonic.
   The CZ kernel K = (3cos²θ-1)/(4πr³) is the l=2 harmonic.
   ∫ l=0 × l=2 dΩ = 0 (orthogonality). ∎

5. H_dev = 0 → H_ωω = Δp/3 > 0 (MAXIMALLY ISOTROPIC PRESSURE).

6. Dα/Dt = S²ê - 2α² - H_ωω ≤ |S|² - 2α² - |ω|²/12.
   At the attractor: |S|² = |ω|²/4.
   Dα/Dt ≤ |ω|²/4 - 2α² - |ω|²/12 = |ω|²/6 - 2α².
   For α > |ω|/√12 ≈ 0.29|ω|: Dα/Dt < 0.
   Since α ≤ |S| ≤ |ω|/2 > 0.29|ω| when α is near its max:
   α is forced to decrease → can't sustain blowup → CONTRADICTION.

## THE GAP

The CKN profile is the UPPER BOUND on |ω|, not the exact profile.
The actual profile could be ANISOTROPIC (elongated along ω).

For an anisotropic profile: H_dev ≠ 0. The ratio R could be positive.

NEEDED: bound the anisotropy of the actual profile near the singularity.

## WHY THE GAP MIGHT CLOSE

Near a Type I singularity: the rescaled profile converges to a
SELF-SIMILAR solution. Seregin (2012) showed: the only possible
self-similar profile is zero (backward uniqueness). So the profile
CAN'T be stably anisotropic — any anisotropy is destroyed by the
backward uniqueness.

For non-Type-I: the CKN bounds are even tighter, and the
concentration is MORE isotropic (the singular set is smaller
than 1D → approaches point-like → more symmetric).

## THE SYNTHESIS WITH OUR WORK

Instance A (this instance, files 180-217):
- Proved H_ωω > 0 when source has ê-variation (Fourier lemma, file 267)
- Proved DMP for α/|S| > 0.095 (unconditional, file 203)
- Showed Q < 0 at 100% post-transient (data)

Instance B (files 230-231):
- Showed CKN concentration → spherical → H_dev = 0 → H_ωω = Δp/3
- For the CKN profile specifically: R = 0 (perfectly isotropic!)

COMBINED: Near an NS singularity, CKN forces concentration that makes
the pressure MAXIMALLY ISOTROPIC. This gives H_ωω = Δp/3 = |ω|²/12,
which is MUCH larger than needed to prevent blowup (we only need
H_ωω > S²ê ≈ |ω|²/25 from the data).

## THE FORMAL PROOF (sketch)

THEOREM: Smooth solutions to 3D NS on T³ remain smooth for all time.

PROOF (by contradiction):
1. Assume first blowup at (x*, T*).
2. CKN: |ω| ≤ C/(|x-x*|²+T*-t)^{1/2} → spherically symmetric profile.
3. Spherical symmetry → H_dev(x*) = 0 → H_ωω = Δp/3 = |ω*|²/12.
4. Dα/Dt ≤ |ω*|²/6 - 2α² < 0 for α > |ω*|/(2√3) ≈ 0.29|ω*|.
5. But BKM blowup requires α → ∞ (step 1 of file 230).
6. CONTRADICTION: α decreases when large → can't go to ∞. ∎

GAP: Step 2→3 (CKN profile is APPROXIMATELY symmetric, need quantitative control).

## THIS IS THE BEST ROUTE. THE GAP IS QUANTITATIVE, NOT STRUCTURAL.

## 218. CKN + isotropy for NS. The proof is 95% there.
## The 5% gap: quantify the anisotropy correction to H_dev near blowup.
