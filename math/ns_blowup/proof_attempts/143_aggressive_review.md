---
source: Peer review #3 — aggressive external (Claude analysis)
type: EXTERNAL REVIEW — found a REAL BUG
date: 2026-03-27
verdict: "not pure crank, absolutely not a solved millennium proof"
---

## Overall Verdict
"Not a legitimate solution. Exploratory draft with potentially interesting
algebraic and computational ideas, possibly publishable after claims are
drastically narrowed."

## THE BUG (Point #2 — Internal Inconsistency)

The main theorem `main_theorem_strong` assumes c2 ≤ c1.
But the physical interpretation (Ashurst alignment: ω aligns with e2)
gives c2 > c1. These CONTRADICT each other.

### The Counterexample
λ = (2, 1, -3), c = (0.25, 0.70, 0.05)

c1 = 0.25 < 1/3 ✓ (misaligned with e1)
BUT: 2(0.25) + 1(0.70) - 3(0.05) = 0.50 + 0.70 - 0.15 = 1.05 > 0

**Stretching is POSITIVE even with c1 < 1/3!**

Because c2 = 0.70 (aligned with e2) and λ2 = 1 > 0, the intermediate
eigenvalue contribution gives positive stretching.

### Why This Breaks Our Chain
- Our theorem needs c2 ≤ c1 AND c3 ≥ 1/3
- Ashurst alignment gives c2 >> c1 AND c3 << 1/3
- The hypotheses DON'T MATCH the physics
- The Lean theorems are CORRECT but INAPPLICABLE

### What Actually Happens with e2-alignment
If ω aligns with e2: stretching ≈ λ2 (intermediate eigenvalue)
- λ2 > 0 typically (eigenvalue ratio ~3:1:-4 in turbulence)
- So stretching is POSITIVE but REDUCED (λ2 < λ1)
- This gives PARTIAL depletion, not COMPRESSION

## Other Valid Criticisms

### Point 3: "On average" too weak for BKM
BKM requires ∫||ω||_∞ dt < ∞ (supremum, not average).
Mean alignment below 1/3 doesn't exclude points where cos²>1/3
and stretching is positive. Our own figure shows bins above 1/3.

### Point 4: Gaps are THE proof, not technicalities
The reviewer correctly identifies that the "technical gaps" are
actually the entire bridge from local algebra to PDE regularity.

### Point 5: Citation mismatches
- Chen-Hou described as "rigorous blowup for 3D Euler" but the
  cited result is narrower (Boussinesq + axi-symmetric Euler)
- Morrey/Besov citation doesn't match the specific estimate needed

### Point 6: Numerics thinner than rhetoric
- N=256 advertised but evidence mainly at N=64
- Sign flip table "mixed rather than cleanly monotone"
- PySR is conjecture generation, not proof

## Crank Concerns Flagged
- "Heavy reliance on prestige aura of Lean verification"
- "Overconfident framing of domain independence"
- "Emotionally and rhetorically leaning toward claiming"
- BUT: "would not file under classic incoherent-crank mathematics"

## What This Means

The compression theorem as stated (c1<1/3 AND c2≤c1 → compression)
does NOT apply to the e2-alignment case (where c2>c1).

We need EITHER:
A. A different theorem that works with c2 > c1 (e2-alignment)
B. Or prove that the e2-alignment itself prevents blowup (different mechanism)
C. Or accept that compression only works when ω is NOT aligned with e2
   (which contradicts the Ashurst phenomenology we're citing)

## 143 proof files. Real bug found. Must fix.
