---
source: NS regularity via the Seregin Type I exclusion
type: PROOF ATTEMPT — bypasses the attractor entirely for NS
date: 2026-03-29
---

## The Seregin Result

THEOREM (Seregin 2012, Escauriaza-Seregin-Šverák 2003):
Smooth solutions to 3D NS on T³ cannot have Type I blowup:
  ||ω(t)||∞ ≤ C/(T*-t)^{1/2} is impossible.

Stronger: any blowup ||ω||∞ → ∞ requires SUPER-Type-I rate.

## Our Bound

If α/|ω| ≤ β for some β < 1/2 on a time interval [T₀, T*]:
  d||ω||∞/dt = α||ω||∞ ≤ β||ω||∞²
  → ||ω||∞ ≤ ||ω||∞(T₀)/(1 - β||ω||∞(T₀)(t-T₀))
  This is Type I (rate 1/(T*-t) with T* = T₀ + 1/(β||ω||∞(T₀))).

Seregin excludes Type I → no blowup → REGULARITY.

## Can We Prove α/|ω| < 1/2?

At the max of |ω| with c₁ = 1 (ω aligned with e₁):
  α = λ₁. And α/|ω| = λ₁/|ω|.

For α/|ω| = 1/2: need λ₁ = |ω|/2. Then |S| ≥ λ₁ = |ω|/2.

AT THIS CONFIGURATION: Q = Var - H_ωω = 0 - H_ωω = -H_ωω < 0.
(Fourier lemma: H_ωω > 0 when α > 0.)

So: D(α/|ω|)/Dt = Q/|ω| < 0. The ratio is STRICTLY DECREASING.

## The Maximum Principle Argument

CLAIM: α/|ω| < 1/2 at the max of |ω| for all t > T₀.

PROOF ATTEMPT:
Define R(t) = max_{x : |ω(x,t)| = ||ω||∞} α(x,t)/|ω(x,t)|.

R is upper-semicontinuous. If R(t₀) = 1/2 for some t₀:
  At the point achieving R = 1/2: c₁ = 1 (ω = e₁, maximum stretching).
  DR/Dt = Q/|ω| = -H_ωω/|ω| < 0.
  So R DECREASES at that instant.

PROBLEM: R might jump UP when the max-|ω| point moves to a new location.
At the NEW location: R could be > 1/2.

BUT: the NEW location also has |ω| maximal. If its α/|ω| > 1/2:
then its c₁ must be close to 1. And we just showed: at c₁ = 1, DR/Dt < 0.

The SUBTLETY: at the new location, c₁ might be < 1 (intermediate alignment)
while α/|ω| > 1/2. This requires α > |ω|/2 with c₁ < 1.

From α = Σλᵢcᵢ: α > |ω|/2 requires the WEIGHTED AVERAGE of eigenvalues
(weights cᵢ) to exceed |ω|/2. Since max eigenvalue λ₁ ≤ |S| ≤ |ω|/... hmm.

Actually: α ≤ λ₁. And λ₁ ≤ |S|. For the max point: |S| could be > |ω|/2
(this is the ATTRACTOR question — we can't bound |S| without it).

## THE NS-SPECIFIC ESCAPE

For NS: even if α/|ω| briefly exceeds 1/2:

1. The RATIO decreases at c₁ = 1 (proven).
2. The RATIO can increase at intermediate alignment, but only when α is
   comparable to the eigenvalue gaps (which are O(|S|) = O(|ω|)).
3. The GROWTH RATE d||ω||/dt = α||ω|| ≤ |S||ω|| ≤ C||ω||∞².

For NS with the CZ bound ||S||_∞ ≤ C||ω||∞(1+log...):
d||ω||/dt ≤ C||ω||²(1+log...).

The log correction is CRITICAL:
  ||S||∞ ≤ C||ω||∞(1 + log(||∇ω||_{L²}/||ω||_{L²}))  [BKM refinement]

For smooth solutions: the log is finite at each time.

If ||ω||∞ → ∞: the log grows (because ||∇ω||_{L²} grows with ||ω||∞).
But the growth is at most log-polynomial.

So: d||ω||/dt ≤ C||ω||² × (1+log(||ω||^a/||ω₀||)):
  This is BARELY super-Type-I. Seregin's result excludes Type I.
  What about this log-corrected Type I?

Actually, there are sharper results:
  Seregin-Šverák (2009): blowup requires ||ω||∞ ≥ C(T*-t)^{-1}.
  This IS Type I rate. And it's EXCLUDED.

So: for NS, d||ω||/dt ≤ C||ω||² gives ||ω|| ~ C/(T*-t) which IS excluded.

BUT: The CZ constant C might be > 1. Then d||ω||/dt ≤ C||ω||² with C > 1
still gives Type I rate (just with a different constant). Still excluded.

## THE PROOF (for NS)

THEOREM: Smooth solutions to 3D NS on T³ are globally regular.

PROOF:
1. Assume blowup at T*.
2. At the max of |ω|: α ≤ |S| ≤ C||ω||∞ [CZ bound, standard].
3. d||ω||∞/dt = α||ω||∞ ≤ C||ω||∞² [from step 2].
4. This gives ||ω||∞(t) ≤ ||ω||∞(T₀)/(1-C||ω||∞(T₀)(t-T₀)) [ODE comparison].
5. This is Type I: ||ω||∞ ~ C/(T*-t).
6. Seregin (2012): Type I is excluded for NS. Contradiction. ∎

WAIT. This can't be right. Step 2 uses ||S||∞ ≤ C||ω||∞, but the CZ
constant C could depend on the solution (through the log correction).

More precisely: ||S||∞ ≤ C₀||ω||∞(1 + log(||∇ω||_{L²}/||ω||_{L²}))
The log factor grows with the solution — it's NOT a fixed constant.

So d||ω||/dt ≤ C(t)||ω||² where C(t) grows. This is NOT pure Type I.

Seregin's exclusion applies to: ||ω||∞ ≤ M/(T*-t)^{1/2} (with FIXED M).
Our bound gives: ||ω||∞ ≤ C(t)/(T*-t) which is Type I with GROWING constant.
These are DIFFERENT. Seregin doesn't exclude the growing-constant case.

## REVISED STATUS

The NS-via-Seregin route FAILS because the CZ constant in ||S||∞ ≤ C||ω||∞
has a log correction that grows with the solution. The blowup rate could be
"log-corrected Type I" which Seregin doesn't exclude.

This is the SAME log correction that makes the NS problem hard. The BKM
refinement gives ||ω||∞ ~ C/(T*-t) × log... The log prevents applying
the fixed-rate exclusion theorems.

## 262. The NS-via-Seregin route doesn't close because of the log correction.
## The attractor remains the path forward.
