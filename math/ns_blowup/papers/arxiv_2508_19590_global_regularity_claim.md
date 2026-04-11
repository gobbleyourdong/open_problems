# arxiv 2508.19590 — Global regularity of Leray-Hopf weak solutions to 3D NS

> Author: Myong-Hwan Ri (Institute of Mathematics, State Academy of Sciences, DPR Korea)
> Date: August 27, 2025
> Status: arxiv only, NOT peer-reviewed, NOT accepted

## Claim
Every Leray-Hopf weak solution to 3D NS on R³ with u₀ ∈ H^{1/2} belongs to L^∞(0,∞; H^{1/2}) ∩ L²(0,∞; H^{3/2}), therefore globally regular. Would resolve the Clay Millennium Prize.

## Technique
Three-step frequency-space argument:
1. Custom "supercritical space" X₁ with sparse inverse-logarithmic weights a(j)⁻¹ in Littlewood-Paley decomposition
2. Energy estimates for high-frequency parts u^k, nonlinear RHS involves X₁ norm × ||∇u^{k/2}||²
3. Rescaling u → λu(λ²t, λx) makes X₁ norm uniformly small, closing Gronwall

## Where it likely fails
- **Summation (3.12)-(3.13):** combinatorial counting of sparse set S(n). Bound Σb(j₀(2k)) ≤ 3n for large n needs careful verification.
- **Rescaling closure (3.21)-(3.24):** transition from X₁-smallness (supercritical) to controlling critical H^{1/2} norm. Works only because X₁ is "barely" supercritical. Historically, EVERY attempt to bridge critical/supercritical with log corrections has failed.
- **Continuity assumption:** u ∈ C([0,T]; H^{1/2}) cited without proof.

## Relevance to our campaign
- **Different path entirely** — no blowup analysis, no ancient solutions, no Liouville
- If correct: obviates our approach
- If wrong: the sparse logarithmic weight technique is novel and could apply to our backward entry argument (L^∞ supercriticality is our gap)
- The "barely supercritical" norm idea might be what we need for the small-data regime entry

## Assessment
Extreme skepticism warranted. History of NS regularity claims on arxiv is long and almost uniformly negative. But the technique (sparse log weights in frequency space) represents a genuinely new idea worth understanding.
