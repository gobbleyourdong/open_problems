# H200 Rollout Plan

## What We Have (Spark, N≤128)

### |ω|_max Resolution Convergence (ν=10⁻⁴, 50 seeds, T=10)
| N | mean_ratio | max_ratio | Status |
|---|-----------|-----------|--------|
| 16 | 1.0182 | 1.1290 | Under-resolved |
| 32 | 1.0054 | 1.0741 | Better |
| 64 | 1.0000 | 1.0000 | Resolved ✓ |
| 128 | 1.0000 | 1.0000 | Confirmed (10/50 seeds so far) |

### |ω|_max Viscosity Sweep (N=64, 20 seeds, T=10)
| ν | mean_ratio | max_ratio | Status |
|---|-----------|-----------|--------|
| 10⁻³ | 1.000000 | 1.000000 | ✓ |
| 10⁻⁴ | 1.000000 | 1.000000 | ✓ |
| 10⁻⁵ | 1.000863 | 1.010460 | Small overshoot — resolution? |
| 0 (Euler) | 1.001518 | 1.014426 | 1.44% overshoot — likely resolution |

### Infection Ratio Convergence (ν=10⁻⁴, 200 seeds)
| N | frac_growing |
|---|---|
| 16 | 42.98% |
| 32 | 15.77% |
| 64 | 0.23% |
| 128 | 0.0001% |
| 256 | 0.000000% |

### Taylor-Green N=512
- gen0: 41.9% → gen1: 0.0% (plateau broken)

---

## What We Need on H200s

### PRIORITY 1: Resolve the ν=10⁻⁵ overshoot
The 1.01 at ν=10⁻⁵ N=64 could be resolution or physics.
- Run ν=10⁻⁵ at N=128, N=256 with |ω|_max tracking
- 50 seeds, T=10
- If ratio → 1.000 at higher N: resolution artifact (same as N=16→64 pattern)
- If ratio stays 1.01+: real physics, need to investigate

### PRIORITY 2: ν=0 (Euler) at higher resolution
- If Spark shows ratio > 1.0 at ν=0 N=64:
  Run ν=0 at N=128, N=256 to check convergence
- If Spark shows ratio = 1.0 at ν=0 N=64:
  Confirm at N=128 for the paper

### PRIORITY 3: Full ν sweep at N=128
| ν | N=128 | Status |
|---|-------|--------|
| 10⁻³ | need | confirmation |
| 10⁻⁴ | running on Spark | wait for result |
| 10⁻⁵ | need | KEY — does overshoot persist? |
| 10⁻⁶ | need | push the boundary |
| 0 | need | geometric bound |

### PRIORITY 4: Full ν sweep at N=256
Same table as above but at N=256. Only if N=128 shows interesting structure.

### PRIORITY 5: Adversarial ICs at N=128
- Taylor-Green |ω|_max (known decaying — validation)
- Kida-Pelz |ω|_max (hardest case)
- Concentrated vortex tube (designed to maximize stretching)
- High amplitude (amp=100, 1000) at ν=10⁻⁴

### PRIORITY 6: Long time integration
- N=64, ν=10⁻⁴, T=100 (10× current)
- 10 seeds, track full |ω|_max trajectory
- Rules out late-time growth

### PRIORITY 7: Interval arithmetic verification
- Rigorous bound on |ω|_max at N=64 or N=128
- Uses our interval FFT + Biot-Savart library
- Computer-assisted proof of BKM bound

---

## Compute Estimate (8×H200, 1.1TB VRAM)

| Run | Resolution | Seeds | Time est |
|-----|-----------|-------|----------|
| ν sweep N=128 | 128³ | 50×5ν | ~4 hours |
| ν sweep N=256 | 256³ | 20×5ν | ~8 hours |
| Adversarial ICs N=128 | 128³ | 50×4 ICs | ~4 hours |
| Long time T=100 | 64³ | 10 | ~2 hours |
| Euler N=256 | 256³ | 50 | ~4 hours |

**Total: ~22 hours on 8×H200.** One overnight run covers everything.

---

## Decision Points

### After ν=0 result from Spark:
- If ν=0 ratio = 1.000: geometry alone works → proof is about Biot-Savart structure
- If ν=0 ratio > 1.01: viscosity helps → proof needs both geometry AND dissipation
- If ν=0 ratio > 1.1: significant Euler growth → different regime, different proof

### After H200 Priority 1 (ν=10⁻⁵ at N=128):
- If ratio → 1.000: the 1.01 was resolution → ALL ratios bounded → iron proof
- If ratio stays 1.01: real but small growth at low ν → need to characterize

### After all H200 data:
- Full table: |ω|_max ratio vs (N, ν, IC family)
- If ALL ≤ 1.0 at resolved scales: paper claims regularity evidence
- If ANY grows unboundedly: pivot to characterizing the growth
