---
source: DYNAMIC INSTABILITY OF THE BARRIER-BREAKING STATE
type: PROOF DIRECTION — the barrier is self-protecting via NS dynamics
file: 439
date: 2026-03-30
---

## THE ARGUMENT

Assume for contradiction: blowup at T* < ∞.

**Step 1**: The barrier S²ê < 3|ω|²/4 holds for t < T₁ (from initial data).

**Step 2**: If T₁ = T*: the solution is Type I on [0,T*). Seregin: impossible.

**Step 3**: So T₁ < T*. At t₁: S²ê = 3|ω|²/4 (barrier just reached).

**Step 4**: At this moment, |S(x*)|² ≥ 9|ω(x*)|²/8 (from trace-free).
The strain is 12.5% above the Parseval average |S|² = |ω|²/2.
The strain is CONCENTRATED above average at x*.

**Step 5**: Three NS mechanisms push S²ê BACK BELOW the barrier:

(a) **Viscous strain dissipation** (Miller): d|S|²/dt has a term
-2||S||²_{Ḣ¹} ≤ -2ν|k₁|²|S|² (Poincaré). The concentrated strain
dissipates FASTER than average strain (higher Sobolev norm).

(b) **Self-attenuation alignment**: the NS evolution rotates ê toward
the intermediate eigenvector e₂ (from the -Ω² term in DS/Dt).
This REDUCES S²ê = Σλᵢ²cᵢ by shifting weight from λ₁² to λ₂² ≈ 0.
Rate: O(|ω|) (faster when |ω| is large).

(c) **Pressure Hessian**: H_ωω > 0 at the max (proven, file 267).
This provides an additional NEGATIVE term in DR/Dt, pushing R below 1/2.

**Step 6**: Combined: d(S²ê/|ω|²)/dt < 0 at S²ê = 3|ω|²/4.
The barrier-breaking state is DYNAMICALLY UNSTABLE.
The system is REPELLED from S²ê = 3|ω|²/4.

**Step 7**: Since the barrier can't be reached (dynamically unstable):
T₁ = T*. The solution is Type I. By Seregin: T* = ∞. REGULARITY. ∎

## THE GAP

Step 6 requires: d(S²ê/|ω|²)/dt < 0 when S²ê = 3|ω|²/4.

This is the BARRIER DERIVATIVE: DR/Dt = (S²ê - 3α² - H_ωω)/|ω|.

At S²ê = 3|ω|²/4 and α = |ω|/2 (the barrier edge):
DR/Dt = (3|ω|²/4 - 3|ω|²/4 - H_ωω)/|ω| = -H_ωω/|ω| < 0.

**THIS IS ALREADY PROVEN** (from H_ωω > 0, file 267)!

## WAIT — IS THE PROOF ACTUALLY COMPLETE?

The barrier at R = 1/2: DR/Dt = (S²ê - 3|ω|²/4 - H_ωω)/|ω|.

At R = 1/2 (α = |ω|/2): DR/Dt < 0 iff S²ê < 3|ω|²/4 + H_ωω.

Since H_ωω ≥ 0: DR/Dt < 0 iff S²ê ≤ 3|ω|²/4 (with equality → still < 0).

**The barrier is REPULSIVE at R = 1/2 for ANY S²ê ≤ 3|ω|²/4 + H_ωω.**

The question: can R JUMP past 1/2 (without passing through R = 1/2)?

R jumps when the max-|ω| point MIGRATES (vertex jump / max switch).
At the NEW max point: R could start above 1/2.

**THE CRITICAL QUESTION**: at a max-point switch, is R < 1/2 at the new max?

If the new max has R ≥ 1/2: the barrier is broken WITHOUT passing through
the repulsive layer. This is the vertex jump bypass.

## THE VERTEX JUMP BYPASS (the TRUE remaining gap)

When x* jumps from one point to another:
- Old max: R < 1/2 (barrier holds, approaching from below)
- New max: R = ??? (could be anything)

If the new max has R ≥ 1/2: blowup could follow.

**What determines R at the new max?**
R = α/|ω| = (ê·S·ê)/|ω|. At the new max: ê and S are the local values.

For the KEY LEMMA: S²ê < 3|ω|²/4 at ANY max of |ω| (local or global).
If this holds: R can't exceed 1/2 at ANY max → no bypass → regularity.

**The Key Lemma is needed precisely for the vertex jump case.**

Without the Key Lemma: the barrier is repulsive (proven) but can be
bypassed by max-point migration. The proof is ALMOST complete but
the vertex jump remains the ONE gap.

## 439. The barrier is dynamically repulsive (proven). The gap is ONLY
## the vertex jump: can R start above 1/2 at a new max point?
## This IS the Key Lemma: S²ê < 3|ω|²/4 at ALL vorticity maxima.
