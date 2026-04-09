---
source: Manus adversarial review Round 3
type: H200 plan review
status: MOST DETAILED — changes 3 GPUs, adds 3 missing experiments
---

## Key Insight from Manus
"If the Euler overshoot is real physics, the Euler ratio at N=128 should
INCREASE. If it's resolution, it should DECREASE. This single distinction
determines whether your paper claims regularity or discovers Euler blowup."

## GPU Changes Recommended

### GPU 0: Replace ν=10⁻³ with ν=10⁻⁶
Already know ν=10⁻³ is 1.000. Push the boundary instead.

### GPU 3: Replace ν=10⁻⁴ with ν=10⁻⁶ at N=256
Same logic — confirm what's known, push what isn't.

### GPU 5: Replace TG/KP with anti-parallel tubes + perturbed KP
"Symmetric ICs make blowup HARDER, not easier." Valid.

### GPU 7: T=200 with 5 seeds instead of T=100 with 10 seeds
Longer horizon more valuable than more seeds.

## Three Missing Experiments (cheap, do on Spark)

### 1. Convergence test: same seed, N=32/64/128/256
Plot |ω|_max(t) for same IC at all 4 resolutions on same graph.
Do the curves converge? If not, can't trust the ratio.
**Cost: 4 runs, 1 seed. Minutes.**

### 2. Energy spectrum at peak vorticity
Is energy piling up at k_max (under-resolved) or decaying (smooth)?
**Cost: zero — just save spectrum at checkpoint.**

### 3. Strain-vorticity alignment at the max point
At the point where |ω|_max occurs, what's the angle between ω and S?
Is depletion of nonlinearity active at the point that matters most?
**Cost: zero — compute at existing checkpoints.**

## PySR Adversarial IC (Manus's strongest suggestion)
"Parameterize IC as ω₀ = Σ a_k exp(ikx) with div=0 constraint.
Optimize a_k to maximize |ω|_max(T=1)/|ω|_max(0) at N=32.
If PySR CAN'T find one where ratio > 1.1, that's your strongest
adversarial evidence."

THIS IS BRILLIANT. Let the machine find the worst case. If it can't
find blowup, nobody can argue we didn't look hard enough.

## Manus's Bottom Line
"Run ν=10⁻⁶ at N=64 on Spark before committing to H200."

Same as ChatGPT. Both reviewers agree: one cheap test first.

## Consensus Between ChatGPT and Manus

Both agree on:
1. Run ν=10⁻⁶ at N=64 first (cheap, decisive)
2. Replace symmetric ICs with anti-parallel tubes
3. Extend long-time runs beyond T=100
4. Method independence test (ChatGPT only)
5. PySR adversarial IC search (Manus only)

## Updated Pre-H200 Checklist
- [ ] ν=10⁻⁶ at N=64 (RUNNING on CPU)
- [ ] Half-dt test (ChatGPT)
- [ ] Convergence test: same seed at N=32/64/128 (Manus)
- [ ] PySR adversarial IC search at N=32 (Manus)
