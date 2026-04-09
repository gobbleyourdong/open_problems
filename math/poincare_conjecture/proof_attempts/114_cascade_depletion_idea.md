---
source: Cascade depletion idea — does (2/3)^j change the scaling?
type: EXPLORATION — promising but needs formalization
status: OPEN — the argument has a plausible structure but gaps remain
date: 2026-03-26
---

## The Idea: Cascade Depletion

At each shell j, the intra-shell transfer is depleted by factor θ₀ = 2/3.
After j steps of the cascade, the ACCUMULATED depletion is (2/3)^j.

This modifies the effective stretching exponent:
```
Without depletion: 2^{3j/2} × E_j^{3/2}  (standard supercritical)
With cascade depletion: (2/3)^j × 2^{3j/2} × E_j^{3/2}
                      = 2^{j(3/2 - log₂(3/2))} × E_j^{3/2}
                      = 2^{0.915j} × E_j^{3/2}
```

Since 0.915 < 2 (the viscous exponent), viscosity wins at high j.
**This would make the problem SUBCRITICAL.**

## The Problem

The depletion θ₀ = 2/3 applies to the DIAGONAL transfer T(j,j),
which is the self-interaction within shell j. But the enstrophy
CASCADE goes through the OFF-DIAGONAL transfer T(j,j+1).

The cascade depletion assumes each shell "loses" a factor of 2/3
when enstrophy passes through it. But:
- The incoming enstrophy arrives via T(j,j-1) (off-diagonal)
- The self-amplification is via T(j,j) (diagonal, depleted by 2/3)
- The outgoing enstrophy leaves via T(j,j+1) (off-diagonal)

Only the MIDDLE step is depleted. The in/out transfers are different.

## Why It Might Still Work

The enstrophy production within shell j comes from T(j,j) (the diagonal).
If T(j,j) < ν 4^j E_j (dissipation), then the shell is a NET SINK:
- enstrophy arrives from below
- some is dissipated
- the rest cascades upward

The key: T(j,j) < ν 4^j E_j iff E_j^{1/2} < (3ν/C) 2^{j/2}

For smooth initial data: E_j(0) → 0 rapidly, so this holds initially.
The question: can E_j CROSS the threshold?

At the threshold: T(j,j) = ν 4^j E_j, so dE_j/dt = Π(j-1) - Π(j).
The incoming flux Π(j-1) ~ C 2^{j-1} √(E_{j-1} E_j).
At the threshold: E_j ~ (3ν/C)² 2^j.

For E_j to cross: Π(j-1) must supply enough enstrophy.
But Π(j-1) ~ 2^j √E_{j-1} × √(threshold) ~ 2^j × √E_{j-1} × ν 2^{j/2}
~ ν 2^{3j/2} √E_{j-1}

For this to push E_j above threshold:
ν 2^{3j/2} √E_{j-1} > ν 4^j × threshold
2^{3j/2} √E_{j-1} > 2^{2j} × (3ν/C)² 2^j = (3ν/C)² 2^{3j}
√E_{j-1} > (3ν/C)² 2^{3j/2}

But E_{j-1} at ITS threshold is (3ν/C)² 2^{j-1}:
√E_{j-1} = (3ν/C) 2^{(j-1)/2}

So: (3ν/C) 2^{(j-1)/2} > (3ν/C)² 2^{3j/2}
1/(3ν/C) > 2^j

For large j: this is IMPOSSIBLE. The incoming flux cannot sustain
E_j above the threshold for j > log₂(C/(3ν)).

## The Bootstrap

This suggests a bootstrap argument:
1. For low shells (j ≤ j*): E_j is bounded by initial data + finite cascading
2. For high shells (j > j*): the incoming flux is too weak to push E_j
   above the threshold, so dissipation always dominates
3. j* ~ log₂(C/(3ν)) = log of Reynolds number

The θ₀ = 2/3 enters through the threshold: E_j^* = (3ν/(2C/3×C'))² 2^j.
With θ₀ = 2/3 instead of 1, the threshold is 9/4 times higher.
The higher threshold means more room for the bootstrap to close.

## What Needs To Be Formalized

1. Make the flux balance rigorous (not just heuristic)
2. Show E_j stays below threshold for all j and all time
3. Handle the low-shell region (j ≤ j*) where cascade is active
4. Prove the bootstrap closes with θ₀ = 2/3 specifically

## Connection to Data

The data shows θ(j) ~ 0.003-0.047, much smaller than 2/3.
The actual cascade depletion is much stronger than (2/3)^j.
But even (2/3)^j might suffice if the bootstrap argument works.

## 114 proof files. The cascade depletion is a promising direction.
