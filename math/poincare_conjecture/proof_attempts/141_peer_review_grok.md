---
source: Peer review #1 — Grok (PhD-level)
type: EXTERNAL REVIEW
date: 2026-03-27
verdict: "Not yet publishable, highly promising, worthy future submission"
---

## Verdict
"Yes, this is a worthy future submission — potentially to JFM, CPAM, or ARMA
— once the gaps are closed or reframed."

## Strengths Identified
1. Bilinear symbol f(α) = cos(α/2)/2 is "clean and Lean-verified"
2. Lean formalization "sets a high bar" for fluid mechanics
3. Phase scrambler is "physically insightful and backed by clean numerics"
4. "Turbulence is the regularity mechanism" is "memorable and constructive"
5. Transparency with red boxes "raises credibility rather than diminishing it"

## Major Concerns
1. **Normal form gap**: commutator estimates missing (Pillar 2 heuristic)
2. **Alignment condition**: "proving cos²<1/3 is essentially as difficult
   as the full regularity problem" — the conditional theorem is a REDUCTION
3. **Title/abstract**: should say "mechanism/framework" not "proof"
4. **Domain independence section**: too brief
5. **Computational methods**: need more detail (time-stepping, dealiasing)

## Actionable Items

### Must fix before sharing more widely:
- [ ] Soften "proof architecture" language → "mechanistic framework"
- [ ] Add DNS methodology appendix (dt, dealiasing, IC robustness)
- [ ] Expand domain independence discussion
- [ ] Add more ICs to alignment figure (random seeds)

### Should fix:
- [ ] Equation (4): explicitly note strain-rate projection
- [ ] Include GitHub/code availability link
- [ ] Consider reframing title: "A Mechanistic Framework and
      Computer-Assisted Evidence for Self-Limiting Vortex Stretching"

### Can ignore for now:
- Budden citations "feel speculative" — we already softened this
- "arXiv (Author 2026, SIREN)" — reviewer confused us with someone else

## Key Quote
"One of the most creative hybrid attacks on the Navier-Stokes regularity
problem I have seen."

## Targets Suggested
- arXiv first
- Then JFM or CPAM

## 141 proof files. First external review received.
