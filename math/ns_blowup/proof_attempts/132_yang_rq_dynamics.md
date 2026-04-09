---
source: Yang et al. (R,Q) dynamics — DIRECT route to compression
type: SECOND PROOF ROUTE — bypasses alignment balance entirely
date: 2026-03-26
---

## The (R,Q) Route (from Yang et al. 2024, Eqs. 4.1-4.6)

### Definitions
Q = (1/2)(|ω|²/2 - |S|²)  — vorticity vs strain balance
R = -(1/3)tr(S³) - (1/4)ω·S·ω  — includes the stretching term

### The Restricted Euler prediction (H_dev = 0)
dR/dt = (2/3)Q²  — ALWAYS POSITIVE → stretching grows → blowup

### Yang's correction (H_dev = -(1/4)(ω⊗ω - |ω|²I/3))
From Eq. (4.6): the pressure Hessian contribution to dR/dt is:

m_ij m_jk H̄^p_ki = -(2/3)Q² - (1/12)|ω|²|S|² + (1/6)(|S|²)² - (1/4)ω_i s_ik s_kj ω_j

**The leading term -(2/3)Q² EXACTLY CANCELS the RE prediction.**

The sub-leading remainder is:
-(1/12)|ω|²|S|² + (1/6)|S|⁴ - (1/4)ω_i s_ik s_kj ω_j

In vorticity-dominated regions (|ω|² >> |S|²):
The -(1/12)|ω|²|S|² term dominates → dR/dt < 0.

### Why dR/dt < 0 means compression

R = -(1/3)tr(S³) - (1/4)ω·S·ω

If dR/dt < 0: R decreases (becomes more negative).
In vorticity-dominated regions: R ≈ -(1/4)ω·S·ω (stretching term dominates).
So ω·S·ω is being pushed MORE POSITIVE...

Wait — negative R means POSITIVE ω·S·ω (stretching). dR/dt < 0 means R becomes
more negative, meaning ω·S·ω becomes more positive? That's stretching, not compression!

Let me re-examine. R < 0 corresponds to the "vortex stretching dominated" region
(page 6: "R < 0 corresponds to the vortex stretching dominated region").

Actually, R = -(1/3)tr(S³) - (1/4)ω·S·ω.
If ω·S·ω > 0 (stretching): R gets a NEGATIVE contribution from -(1/4)ω·S·ω.
If ω·S·ω < 0 (compression): R gets a POSITIVE contribution.

So R < 0 means stretching dominates: ω·S·ω > 0.
And dR/dt < 0 means R is getting MORE negative: stretching is INCREASING.

This is the OPPOSITE of what we want!

### Correction: Yang's result is about R staying in the stretching region

Actually, re-reading Yang: "dR/dt < 0" means the flow STAYS in the R < 0
(stretching) region rather than transitioning to R > 0. This is about the
TOPOLOGY of the (R,Q) dynamics, not about ω·S·ω going negative.

The RE prediction (dR/dt = (2/3)Q² > 0) would push R toward POSITIVE values
(away from stretching), which eventually leads to a finite-time singularity
through the Vieillefosse tail. Yang's correction prevents this by keeping
dR/dt < 0, which keeps the flow in the stretching region.

But this means the flow keeps stretching — it just doesn't blow up through
the Vieillefosse mechanism. The compression we observed must come from a
DIFFERENT mechanism than the (R,Q) dynamics.

### Resolution

The (R,Q) route does NOT directly give ω·S·ω < 0 (compression).
It gives: the Vieillefosse finite-time singularity is prevented.
This is a REGULARITY result, but it operates through a different
mechanism than the alignment-based compression we discovered.

The TWO mechanisms are complementary:
1. Yang (R,Q): pressure prevents the Vieillefosse blowup
2. Our alignment decay: pressure prevents sustained stretching

Both contribute to regularity but through different channels.

### What this means for the proof

The (R,Q) route is an ALTERNATIVE path to regularity, not a
shortcut for our alignment-based proof. Yang's result is already
published and validated by DNS. If we can formalize it, it provides
a second independent argument.

However, the (R,Q) route has the SAME gap as ours: Yang's formula
is asymptotic. The cancellation of the RE term is exact at leading
order, but the sub-leading correction being negative needs to be
proved rigorously for the full NS PDE, not just the restricted model.

## 132 proof files. The (R,Q) route is complementary, not a shortcut.
