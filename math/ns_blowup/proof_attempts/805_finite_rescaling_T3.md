---
source: FINITE RESCALING ON T³ — don't take λ→0, stay on a torus
type: NEW APPROACH — the most promising angle yet
file: 805
date: 2026-04-01
instance: MATHEMATICIAN (Opus)
---

## THE CORE INSIGHT

The KNSS argument: Type I blowup → rescale by λ→0 → ancient solution on R³.
The Liouville conjecture on R³ is OPEN.

BUT: at any FINITE λ > 0, the rescaled solution lives on T³/λ (a LARGER torus).
On any torus (no matter how large), there's a DIRECT argument:

**Ancient solutions on T³_L with Type I decay must be trivial.**

## THE T³ LIOUVILLE THEOREM

**Theorem (attempt)**: Let v be a mild bounded ancient solution of NS on
T³_L × (-∞, 0) with viscosity ν > 0 and Type I decay ||v||∞ ≤ C/√(-t).
Then v ≡ 0.

**Proof sketch:**

1. Type I decay: ||v(·,t)||∞ ≤ C/√(-t) → 0 as t → -∞.

2. Compact domain: ||v(·,t)||_{L²(T³_L)} ≤ ||v(·,t)||∞ · L^{3/2} → 0 as t → -∞.

3. Small-data threshold on T³_L:
   There exists ε(ν,L) > 0 such that if ||v₀||_{L²(T³_L)} < ε, the solution
   exists globally and decays: ||v(·,t)||_{L²} ≤ ||v₀||_{L²} e^{-νλ₁t}
   where λ₁ = (2π/L)² is the first eigenvalue of -Δ on T³_L.

   Standard: ε = cν/L (from the bilinear estimate scaling).

4. For t₀ negative enough: ||v(·,t₀)||_{L²} ≤ C·L^{3/2}/√|t₀| < cν/L.
   This requires |t₀| > C²L⁵/(c²ν²). Achievable for any fixed L.

5. From t₀ forward: ||v(·,t)||_{L²} ≤ ||v(·,t₀)||_{L²} · e^{-νλ₁(t-t₀)}

6. At t = 0: ||v(·,0)||_{L²} ≤ (cν/L) · e^{-νλ₁|t₀|} → 0 as |t₀| → ∞.

7. Therefore ||v(·,0)||_{L²} = 0, so v(·,0) = 0. By uniqueness, v ≡ 0. □

## THE CATCH: THE RESCALED SOLUTION IS NOT ANCIENT

Assume Type I blowup on T³ at time T*. Rescale:
u_λ(x,t) = λ u(x₀+λx, T*+λ²t) on T³_{2π/λ}

The original solution exists on [0, T*), so the rescaled solution exists on:
t ∈ [-T*/λ², 0)

For any FINITE λ > 0: u_λ has a FINITE starting time t_min = -T*/λ².
It is NOT an ancient solution (doesn't extend to t = -∞).

So the T³ Liouville theorem doesn't apply to u_λ.

## THE QUESTION

Can we modify the argument to work for solutions with FINITE but LONG
backward existence?

The key step was: choose t₀ < -t* such that ||v(·,t₀)||_{L²} < ε.
For u_λ: the earliest time is t_min = -T*/λ². We need:

||u_λ(·,t_min)||_{L²(T³/λ)} < ε(ν, 2π/λ) = cνλ

Now: ||u_λ(·,t_min)||_{L²(T³/λ)} = λ^{-1/2} ||u(·,0)||_{L²(T³)} = λ^{-1/2} ||u₀||

For this to be < cνλ: need λ^{-1/2} ||u₀|| < cνλ, i.e., λ > (||u₀||/(cν))^{2/3}.

**For large enough λ** (not too much rescaling): the initial data IS small
on the rescaled torus. Then the small-data theorem prevents blowup!

But wait — the rescaling makes the blowup at t = 0. If the initial data
at t_min is small (in the small-data regime), the small-data theorem says
the solution exists GLOBALLY past t = 0. But u_λ blows up at t = 0.
CONTRADICTION!

## THE RESOLUTION ATTEMPT

For λ > λ* = (||u₀||/(cν))^{2/3}:
||u_λ(·,-T*/λ²)||_{L²} = λ^{-1/2}||u₀|| < cνλ

The small-data global existence theorem on T³_{2π/λ} says: the solution
with this initial data exists for ALL t > -T*/λ² and remains smooth.

But u_λ blows up at t = 0. CONTRADICTION.

**Therefore: Type I blowup cannot occur on T³!**

## THE CRITICAL CHECK

Is the rescaled initial data really in the small-data regime?

Small-data threshold on T³_L: ||u₀||_{L²} < cν · (2π/L)^{1/2} = cν√λ₁(L)

Wait, I need to be precise about the small-data theorem on T³_L.

The standard result: If ||u₀||_{Ḣ^{1/2}(T³_L)} ≤ cν, then global existence.
Alternatively: If ||u₀||_{L²(T³_L)} · λ₁(L)^{-1/2} ≤ cν, then global.
This gives: ||u₀||_{L²} ≤ cν · λ₁^{1/2} = cν · 2π/L.

For T³_{2π/λ} (L = 2π/λ): threshold = cν · λ.

Rescaled initial data: ||u_λ(·,t_min)||_{L²} = λ^{-1/2} ||u₀||.

Need: λ^{-1/2} ||u₀|| < cνλ, i.e., λ^{3/2} > ||u₀||/(cν).
So: λ > (||u₀||/(cν))^{2/3}.

For FIXED ν and u₀: λ* = (||u₀||/(cν))^{2/3} is a FINITE positive number.

**For any λ > λ*: contradiction!**

But the rescaling parameter λ in the KNSS framework is taken to 0, not ∞.
We're using the rescaling in the OPPOSITE direction.

Actually: for λ > λ*, u_λ lives on a SMALLER torus T³_{2π/λ} (since λ is
large, L = 2π/λ is small). The initial data has SMALL L² norm on this
small torus. The small-data theorem applies.

But wait: u_λ is the rescaled solution. If the original u blows up at T*,
then u_λ blows up at t = 0 on T³_{2π/λ}. If the small-data theorem says
u_λ doesn't blow up: CONTRADICTION.

## THE POTENTIAL FLAW

The small-data theorem requires the initial data to be in L² with
||u₀||_{L²} < cν√λ₁. On T³_{2π/λ} with λ > λ*: this IS satisfied.

But the small-data theorem also requires the solution to be the UNIQUE
mild solution starting from that data. The rescaled u_λ IS the unique
mild solution (rescaling preserves the NS equation with same ν).

So if ||u_λ(·,t_min)||_{L²} < cνλ, the unique mild solution from this
data is global. Since u_λ IS this unique solution: u_λ is global.
But u_λ was supposed to blow up at t = 0. Contradiction. ∎

## STATUS: NEEDS VERIFICATION

The argument hinges on:
1. The small-data global existence theorem on T³_L with threshold cν√λ₁
2. The L² norm of the rescaled initial data: λ^{-1/2}||u₀|| vs cνλ
3. Uniqueness of mild solutions (standard)
4. NS invariance under the rescaling (verified: same ν)

THE KEY QUESTION: Does the small-data theorem on T³_L have threshold
cν√λ₁ = cν(2π/L), or is it cν (independent of L)?

If threshold = cν (independent of L): then for large λ, the threshold is
FIXED while the data norm λ^{-1/2}||u₀|| → 0. Works for λ > (||u₀||/(cν))^2.

If threshold = cνλ = cν(2π/L) → 0 as L → ∞: then the threshold SHRINKS
as the torus grows. The data norm λ^{-1/2}||u₀|| and threshold cνλ:
need λ^{-1/2}||u₀|| < cνλ, i.e., λ^{3/2} > ||u₀||/(cν). Works for large λ.

In BOTH cases: for λ large enough, the argument works!

## THE L² SCALING ISSUE

Wait — I need to double-check the L² scaling more carefully.

Original solution u on T³ = T³_{2π}. Rescaled u_λ on T³_{2π/λ}.

u_λ(x,t) = λ u(x₀ + λx, T* + λ²t)

At t_min = -T*/λ²: u_λ(x, t_min) = λ u(x₀ + λx, 0) = λ u₀(x₀ + λx)

||u_λ(·,t_min)||²_{L²(T³_{2π/λ})} = ∫_{T³_{2π/λ}} λ²|u₀(x₀+λx)|² dx
= λ² · λ^{-3} ∫_{T³} |u₀(y)|² dy  (substituting y = x₀+λx)
= λ^{-1} ||u₀||²_{L²(T³)}

So ||u_λ(·,t_min)||_{L²} = λ^{-1/2} ||u₀||_{L²}. ✓

For LARGE λ: this → 0. The initial data IS small.

BUT: the torus T³_{2π/λ} is SMALL for large λ (period = 2π/λ → 0).
The first eigenvalue λ₁ = (2π/(2π/λ))² = λ².
The small-data threshold: cν√λ₁ = cνλ.

Need: λ^{-1/2}||u₀|| < cνλ → λ^{3/2} > ||u₀||/(cν). ✓ for large λ.

THE ISSUE: for large λ, the rescaled torus is SMALL. The original blowup
at x₀ is being "zoomed OUT" (not zoomed in). We're looking at the solution
from far away, where it appears smooth (the blowup is at a single point).

In fact, for λ large: the rescaled solution u_λ on T³_{2π/λ} corresponds
to the original solution on T³ viewed at scale 2π/λ. The blowup at x₀
occupies a fraction λ^{-3} of the domain. For λ large, this fraction → 0.
The L² norm is dominated by the smooth bulk, not the singular point.

## THE SUBTLE ISSUE

When λ is large, the torus T³_{2π/λ} is small, and the rescaled solution
u_λ has LARGE derivatives (the blowup is compressed into a small domain).

Specifically: ||∇u_λ||_{L²(T³_{2π/λ})} = λ^{1/2} ||∇u₀||_{L²(T³)}.
This GROWS with λ.

The small-data theorem in L² requires: ||u₀||_{L²} < cν√λ₁.
But the H^{1/2} norm might be more relevant. Let me check.

The classical small-data result: ||u₀||_{Ḣ^{1/2}} < cν → global existence.

||u_λ(·,t_min)||²_{Ḣ^{1/2}(T³_{2π/λ})} = Σ_k |k|·|û_k|²

Under the rescaling: the Fourier coefficients transform, and...

Actually, the Ḣ^{1/2} norm is SCALE-INVARIANT (critical) for 3D NS!

||u_λ||_{Ḣ^{1/2}} = ||u||_{Ḣ^{1/2}} (invariant under the NS rescaling)

So: ||u_λ(·,t_min)||_{Ḣ^{1/2}} = ||u₀||_{Ḣ^{1/2}} for ALL λ.

The small-data theorem: ||u₀||_{Ḣ^{1/2}} < cν → global existence.

If ||u₀||_{Ḣ^{1/2}} < cν: the solution is ALREADY globally regular.
No blowup in the first place.

If ||u₀||_{Ḣ^{1/2}} ≥ cν: the rescaled data ALSO has Ḣ^{1/2} ≥ cν.
The small-data theorem DOESN'T apply.

**THE ARGUMENT FAILS BECAUSE Ḣ^{1/2} IS CRITICAL.**

The L² threshold argument worked because L² is subcritical (the rescaling
reduces the L² norm). But the ACTUAL small-data theorem uses the critical
norm Ḣ^{1/2}, which is preserved by rescaling.

## REFINED ANALYSIS

Can we use L² instead of Ḣ^{1/2} for the small-data theorem?

On T³_L: there IS a small-data result in L²:
||u₀||_{L²(T³_L)} < cν · λ₁(L)^{1/2} → global existence

But λ₁ = (2π/L)² = λ² for our rescaled torus. The threshold cνλ.
The data norm λ^{-1/2}||u₀||. For λ large: data < threshold. ✓

BUT: this L² small-data theorem is WEAKER than the Ḣ^{1/2} one.
It uses the Poincaré inequality ||u||_{Ḣ^{1/2}} ≤ C||u||_{L²}/√λ₁(L).

Wait: ||u||_{Ḣ^{1/2}(T³_L)} ≤ ||u||_{L²(T³_L)} · λ₁(L)^{1/4}
= λ^{-1/2}||u₀|| · λ^{1/2} = ||u₀||. Invariant. ✓

So: ||u₀||_{L²} < cνλ on T³_{2π/λ} iff ||u₀||_{Ḣ^{1/2}} < cν.
They're EQUIVALENT up to domain scaling.

The L² threshold IS the Ḣ^{1/2} threshold in disguise. The argument
is circular: it only works when the original data is already small.

## FINAL VERDICT

**THE ARGUMENT FAILS.** The critical (scale-invariant) norm Ḣ^{1/2}
is preserved by rescaling. The L² smallness for large λ is an illusion:
it's compensated by the shrinking domain (large λ₁), and the Ḣ^{1/2}
norm remains unchanged.

The rescaling trick works for SUBCRITICAL data but not CRITICAL data.
Type I blowup involves critical scaling, where subcritical norms can be
made arbitrarily small but critical norms are preserved.

This is the fundamental reason why critical NS regularity is hard: all
scale-invariant quantities are FIXED by the dynamics, and subcritical
quantities can be driven to zero without preventing blowup.

## LESSON

Any argument using L² or other subcritical norms combined with rescaling
will fail for the same reason. The proof must work at the CRITICAL level
(L³, Ḣ^{1/2}, or equivalent) where rescaling provides no benefit.

This is why the Liouville conjecture is so hard: it asks about bounded
ancient solutions in L∞ (supercritical), and the critical norms aren't
controlled by L∞ alone.

## 805. Finite rescaling on T³: λ^{-1/2}||u₀|| < cνλ for large λ.
## Initial data IS small in L², but Ḣ^{1/2} (critical norm) is INVARIANT.
## The L² threshold = Ḣ^{1/2} threshold in disguise. Circular.
## Lesson: scale-invariant norms cannot be beaten by rescaling.
