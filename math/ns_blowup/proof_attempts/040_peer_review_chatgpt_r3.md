---
source: ChatGPT adversarial review Round 3
type: H200 plan review
status: ACTIONABLE — 80% right, 20% missing
---

## Summary
ChatGPT says: plan is good engineering but missing three things that
reviewers will attack. Recommends spending some budget on robustness
instead of all on resolution.

## MUST DO BEFORE H200 (cheap, on Spark):
1. **ν=10⁻⁶ at N=64** — tests if overshoot continues growing
2. **Half timestep test** — CFL robustness check
3. **Alternative dealiasing** — method independence

## MUST ADD TO H200:
4. **Anti-parallel vortex tube IC** — known for extreme stretching
5. **One long-time run T=500+** — rules out slow accumulation

## Revised GPU Allocation (ChatGPT's suggestion):

| GPU | Job | Change |
|-----|-----|--------|
| 0 | ν sweep N=128 (10⁻³, 10⁻⁴) | keep |
| 1 | ν sweep N=128 (10⁻⁵, 10⁻⁶) | keep |
| 2 | Euler N=128 | keep |
| 3 | ν sweep N=256 (10⁻⁴, 10⁻⁵) | keep |
| 4 | Euler N=256 | keep |
| 5 | **Anti-parallel vortex tube** N=128 | CHANGED from TG/KP |
| 6 | **Method variation** (3/2 dealiasing, RK3) | CHANGED from tube/high-amp |
| 7 | **Long time T=500** N=64 | CHANGED from T=100 |

## Key Insight
"You're overspending on resolution and underspending on robustness."

Valid. Resolution convergence we already see the trend. Method independence
and adversarial ICs are the gaps reviewers will exploit.

## Pre-H200 Checklist (Spark, cheap):
- [ ] ν=10⁻⁶ at N=64 (minutes)
- [ ] Half dt test at N=64 ν=10⁻⁴ (minutes)
- [ ] 3/2 dealiasing at N=64 ν=10⁻⁴ (requires code change)
