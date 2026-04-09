---
source: da Veiga-Berselli (2002) + Constantin lecture notes (2006)
type: Literature extraction — the exact conditions for regularity
status: COMPLETE — critical insight about the a priori estimate
---

## The Killer Finding

Constantin already proved THIS a priori estimate exists for ALL NS solutions:

```
∫₀ᵀ ∫_ℝ³ |ω(x,t)| |∇ξ(x,t)|² dx dt ≤ (1/2ν²) ∫_ℝ³ |u₀|² dx
```

This is UNCONDITIONAL. It holds for every Leray solution. It says:
the space-time integral of |ω||∇ξ|² is bounded by initial energy / ν².

Physical meaning: vortex lines are "on average" straight in high-vorticity
regions. The bending |∇ξ| is CONTROLLED in an L¹-weighted average.

## What This Means for Our Measurement

Our CF ratio = |∇ξ(x*)|/|ω(x*)|^{1/2} growing with N is NOT necessarily
fatal. Here's why:

The a priori estimate bounds the INTEGRAL ∫|ω||∇ξ|² dx dt, not the
POINTWISE value |∇ξ(x*)|. At x* where |ω| is max, the pointwise
|∇ξ| could be large IF |ω| is small (the integral can still converge).

Our ICs have |ω|_max ~ 10⁻⁴ at N=128 (very weak). So |ω|^{1/2} ~ 0.01.
Even |∇ξ| ~ 1 gives CF ratio ~ 100. But this doesn't mean the CF
condition fails — it means our ICs are too WEAK to test it properly.

The real test: high-amplitude ICs where |ω|_max is O(1) or larger.
Then |ω|^{1/2} ~ 1, and CF ratio = |∇ξ| directly measures the
Hölder constant without the tiny denominator.

## da Veiga-Berselli: Exact Conditions

### Assumption A (½-Hölder coherence):
```
sin θ(x, x+y, t) ≤ g(t,x) |y|^{1/2}
```
in regions where |ω| > k, with g ∈ Lᵃ(0,T; Lᵇ), 2/a + 3/b = 0.

### Theorem 1.2: Assumption A → solution is regular.

### WHY ½-Hölder is critical:
The proof uses Hardy-Littlewood-Sobolev inequality. The sin θ ≤ g|y|^α
converts the CZ kernel 1/|y|³ to a fractional integral kernel 1/|y|^{3-α}.
HLS gives L^r → L^q mapping. The energy estimate closes via Gronwall
ONLY when α ≥ 1/2. Below 1/2, the integrability fails.

### The representation formula for α:
```
α(x) = (3/4π) PV ∫ D(ŷ, ξ(x+y), ξ(x)) |ω(x+y)| dy/|y|³
```
where D(v₁,v₂,v₃) = (v₁·v₃) det(v₁,v₂,v₃).

### Key property of D:
|D| ≤ |sin ∠(ξ(x), ξ(x+y))|
D = 0 when ξ(x) ∥ ξ(x+y) (parallel vorticity → zero stretching)

This is the physical-space version of our single-mode orthogonality.

## Constantin Lecture Notes: Physical Picture

Constantin interprets the a priori estimate:

> "This bound is consistent with the numerically observed fact that the
> region of high vorticity is made up of relatively straight vortex
> filaments separated by distances that vanish with viscosity. The process
> by which this separation is achieved is vortex reconnection. When vortex
> lines are locally aligned, geometric depletion occurs, and local
> production of enstrophy drops."

And on vortex reconnection:

> "NS equations have global smooth solutions if the vorticity direction
> field ω/|ω| is Lipschitz continuous in regions of high vorticity.
> So, vortex reconnection is a regularizing mechanism."

## The Gap (Precise Statement)

Known (a priori, unconditional):
```
∫₀ᵀ ∫ |ω| |∇ξ|² dx dt ≤ C(u₀, ν)
```

Need (for regularity via BdV):
```
sin θ(x, x+y, t) ≤ g(t,x) |y|^{1/2}  pointwise in {|ω| > k}
```

The gap: upgrading from space-time average to pointwise.

Our single-mode orthogonality provides a STRUCTURAL reason why the
pointwise bound should hold: the Biot-Savart structure forces each
mode's strain to be orthogonal to its own vorticity, creating geometric
depletion at every scale.

## Action Items

1. RE-RUN CF ratio measurement with HIGH AMPLITUDE ICs (amp=100)
   so |ω|_max ~ 1, eliminating the tiny-denominator artifact

2. Measure |∇ξ| at x* during TG evolution where |ω| actually grows
   — this tests the CF condition under genuine stretching

3. Compare our pointwise |∇ξ(x*)| with the a priori bound's prediction
   — if pointwise is within the average bound, the upgrade is plausible

4. The Lean formalization of the stretching decomposition should
   explicitly connect sin²(α_k) to the da Veiga kernel D

## Papers Still Needed
- Constantin 1990 (CMP 129, 241-266) — area of interfaces
- Constantin 2001 (CMP 216, 663-686) — Eulerian-Lagrangian approach
- Constantin 2003 (Handbook Vol 2, 117-141) — near identity transforms
