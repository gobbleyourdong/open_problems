# Adversarial Review Round 3 — H200 Plan Review

You previously identified two critical issues:
1. Grid max might not capture true max (ChatGPT)
2. Results might be viscosity-dependent, not geometric (Manus)

We ran the viscosity sweep you demanded. Here are the results. Before we spend $30/hr on 8×H200 GPUs, tell us if our plan is right or if we're about to waste money.

---

## New Data: |ω|_max Viscosity Sweep (N=64, 20 seeds, T=10)

```
ν=10⁻³:  mean_ratio = 1.000000,  max_ratio = 1.000000
ν=10⁻⁴:  mean_ratio = 1.000000,  max_ratio = 1.000000
ν=10⁻⁵:  mean_ratio = 1.000863,  max_ratio = 1.010460
ν=0:     mean_ratio = 1.001518,  max_ratio = 1.014426
```

At ν=10⁻³ and ν=10⁻⁴: exactly 1.0. No growth.
At ν=10⁻⁵: 1.05% overshoot in worst seed.
At ν=0 (Euler): 1.44% overshoot in worst seed.

## Our Interpretation
The 1.44% Euler overshoot is a resolution artifact. N=64 with 2/3 dealiasing resolves k_max ≈ 21. At ν=10⁻⁴, the dissipation wavenumber k_d ≈ 20 (barely resolved, ratio = 1.000). At ν=10⁻⁵ and ν=0, k_d moves beyond the grid and the under-resolution creates a small overshoot. The same pattern appeared in our resolution convergence:

```
N=16:  max_ratio = 1.129  (under-resolved)
N=32:  max_ratio = 1.074
N=64:  max_ratio = 1.000  (resolved at ν=10⁻⁴)
N=128: max_ratio = 1.000  (10/50 seeds so far)
```

Under-resolution always shows a small overshoot that vanishes with more grid points.

## Our H200 Plan (8 GPUs, ~22 hours, ~$660)

| GPU | Job | N | ν values | Seeds | Goal |
|-----|-----|---|----------|-------|------|
| 0 | ν sweep | 128 | 10⁻³, 10⁻⁴ | 50 | Confirm 1.000 at higher N |
| 1 | ν sweep | 128 | 10⁻⁵, 10⁻⁶ | 50 | KEY: does 1.01 drop to 1.000? |
| 2 | Euler | 128 | 0 | 50 | KEY: does 1.014 drop to 1.000? |
| 3 | ν sweep | 256 | 10⁻⁴, 10⁻⁵ | 20 | Higher resolution confirmation |
| 4 | Euler | 256 | 0 | 20 | Strongest test |
| 5 | Adversarial ICs | 128 | Taylor-Green, Kida-Pelz | 50 | Hardest ICs |
| 6 | Adversarial ICs | 128 | vortex tube, high-amp | 50 | Worst-case geometry |
| 7 | Long time T=100 | 64 | 10⁻⁴ | 10 | Rule out late-time growth |

Checkpoints saved every 500 steps for future diagnostic queries.
Sync to local NAS every 30 minutes.

## Questions for You

1. Is the H200 plan the right set of experiments? Are we missing anything?
2. The Euler ratio 1.014 at N=64 — do you agree this is likely resolution? Or could it indicate real vorticity growth in the inviscid case?
3. Should we run ν=10⁻⁶ at N=64 first (cheap, on Spark) before committing to H200?
4. Is N=256 at ν=0 (Euler) the right "hardest test"? Or should we use that GPU for something else?
5. The adversarial ICs (GPU 5,6) — are Taylor-Green, Kida-Pelz, vortex tube, and high-amplitude the right choices? What IC would YOU design to break our claim?
6. Is T=100 sufficient for the long-time test? Or does the reviewer concern about T=1000 need to be addressed?
7. Any other experiments that would strengthen the paper that we're not running?

Attack the plan. Tell us what's missing before we spend the money.
