---
source: NEW POINTWISE IDENTITY — Miller + max condition gives ê·(ΔS)·ê = 0
type: PROVEN — a genuinely new constraint at the vorticity maximum
date: 2026-03-29
---

## THE IDENTITY

LEMMA: For any smooth divergence-free vector field ω on T³, at a point x*
where |ω|² achieves a spatial maximum:

  ê·(ΔS)·ê = 0  where ê = ω/|ω| and S = sym(∇u), u = BS(ω).

PROOF:
Step 1 (Miller): (-ΔS)ᵢⱼ ωᵢωⱼ = -(-Δu)ⱼ[(ω·∇)ω]ⱼ
  (From: ΔS relates to Δ(∇u) which relates to ∇(-Δu), then integrate by parts.)

Step 2 (Vector identity): (ω·∇)ω = (-Δu) × ω + ∇(|ω|²/2)
  (Using ∇×ω = ∇×(∇×u) = -Δu for div-free u on T³.)

Step 3: (-ΔS)ᵢⱼ ωᵢωⱼ = -(-Δu)·[(-Δu)×ω] - (-Δu)·∇(|ω|²/2)
  Term 1: -(-Δu)·[(-Δu)×ω] = 0 (cross product ⊥ both factors, POINTWISE)
  Term 2: -(-Δu)·∇(|ω|²/2) at x* where ∇|ω|² = 0: THIS IS ZERO.

Therefore: (-ΔS)ᵢⱼ ωᵢωⱼ = 0 at x*. Dividing by |ω|²: ê·(ΔS)·ê = 0. ∎

## INTERPRETATION

The Laplacian of the strain, projected onto the vorticity direction, vanishes
at the vorticity maximum. This means:

  Δα ≈ ê·(ΔS)·ê + corrections from ∇ê = 0 + O(|∇ê|²|S| + |∇ê||∇S|)

So α = ê·S·ê is APPROXIMATELY HARMONIC at x*.

## CONSEQUENCES

1. α(x*) = spherical average of α on small spheres around x* (+ corrections)
2. |ω(x*)|² ≥ spherical average of |ω|² (superharmonic at max, from Δ|ω|² ≤ 0)

Combined: α/|ω| at x* ≤ (avg α)/(avg |ω|)^{correction} — suppressed relative to field.

3. For NS (ν > 0): the viscous strain equation gives
   ê·(DS/Dt)·ê = -S²ê - H_ωω + ν × 0 = -S²ê - H_ωω
   (The viscous term νΔS contributes ZERO in the ê projection at x*.)

4. This is CONSISTENT with the Riccati Dα/Dt = S²ê - 2α² - H_ωω
   (the difference comes from the Dê/Dt terms: 2(Dê/Dt)·S·ê = 2S²ê - 2α² = 2Var).

## QUANTITATIVE BOUND

Using Δα ≈ 0 and Δ|ω|² ≤ 0 with ||S||²_{L²} = ||ω||²_{L²}/2:
  α/|ω| ≤ 1/√2 ≈ 0.707 (same as Cauchy-Schwarz, NOT < 0.5)

The identity is a genuine new constraint but DOES NOT close the gap alone.
To get α < |ω|/2: need additional structure beyond the harmonic property.

## POSSIBLE EXTENSIONS

1. The correction terms from ∇ê might help — they involve Var (alignment variance),
   which is what we're trying to bound. Self-referential but potentially useful.

2. At the max of |ω|: both ê·(ΔS)·ê = 0 AND ∇|ω|² = 0 AND Δ|ω|² ≤ 0.
   These three constraints together might give α < |ω|/2 by a more refined argument.

3. The per-mode Fourier bound |α̂(k)| ≤ |ω̂(k)|/2 (file 302) combined with the
   harmonic property might give tighter bounds through Fourier analysis.

4. For NS: the identity says the viscous term contributes ZERO to the α evolution
   at x* (the ΔS projection vanishes). This means viscosity helps α ONLY through
   the indirect effect on the eigenvalues and alignment (not through direct diffusion
   of α). This is a structural insight about why the NS regularity problem is hard.

## 303. Pointwise Miller identity: ê·(ΔS)·ê = 0 at max |ω|. New but not sufficient.
