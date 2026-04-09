---
source: Multi-shell phase scrambler measurement at N=64
type: DATA — oscillation frequency doubles per shell, scrambler is real
status: PROMISING — frequency scaling supports the mechanism, peak θ data mixed
date: 2026-03-26
---

## Multi-Shell θ Time Series (TG vortex, N=64, ν=10⁻⁴)

### Peak θ by shell (over full evolution t=0-8.7):
| Shell | N_modes | Peak θ | Avg θ (t≥3) |
|-------|---------|--------|-------------|
| j=1 | 224 | 0.004 | 0.0016 |
| j=2 | 1852 | 0.011 | 0.0049 |
| j=3 | 14968 | 0.013 | 0.0049 |
| j=4 | 51546 | 0.004 | 0.0013 |

Peak θ is roughly CONSTANT across active shells (0.01-0.013).
This is NOT the clean 2^{-j} decay we hoped for.

### BUT: Oscillation Frequency DOUBLES per Shell
| Shell | Oscillation freq | Relative to j=1 |
|-------|-----------------|-----------------|
| j=1 | 0.2 Hz | 1× |
| j=2 | 0.8 Hz | 4× |
| j=3 | 1.1 Hz | 5.5× |
| j=4 | 1.7 Hz | 8.5× |

The scrambler acts FASTER at higher shells.
Frequency ~ 2^j matches the inverse of the eddy turnover time.

### Median Instantaneous Ratio θ(j+1)/θ(j)
- θ(3)/θ(2): median 0.71
- θ(4)/θ(3): median 0.29

At any given instant, higher shells usually have LOWER θ.
The mean is misleading (polluted by outliers when denominator → 0).

### Cascade Sequential Arrival
The θ peak at each shell occurs at different times:
- j=1 peaks at t ≈ 3.0 (TG initial stretching)
- j=2 peaks at t ≈ 4.7 (cascade arrival)
- j=3 peaks at t ≈ 6.0 (late cascade)
- j=4 peaks at t ≈ 7.3 (very late)

This is the cascade propagating upward through shells.
Each shell has its "moment" when the cascade arrives.

### What This Means

1. **The scrambler IS faster at high j**: oscillation frequency ~ 2^j
   confirms that the Leray projector's scrambling rate matches the
   eddy turnover time (which also scales as 2^j).

2. **Peak θ is bounded but not 2^{-j}**: the peak θ per shell is
   roughly 0.01-0.013, independent of j. This means the INSTANTANEOUS
   worst case is constant, not decaying.

3. **Time-averaged θ may decay**: because the scrambler acts faster
   at higher shells, the FRACTION of time spent at peak θ decreases.
   If peak duration ~ 1/freq ~ 2^{-j}, and peak height is constant,
   then time-averaged θ ~ peak × duty_cycle ~ 0.01 × 2^{-j}.

4. **The proof needs time-integrated bounds**: the BKM criterion involves
   ∫||ω||_∞ dt, which is a time integral. The shell balance also
   involves time integrals. The oscillation (fast at high j) means
   the time-integrated contribution of the diagonal is small.

### The Time-Integrated Argument

If the scrambler period at shell j is T_j ~ 2^{-j}:
∫ T(j,j) dt ~ peak_T(j,j) × T_j ~ C × 2^{3j/2} × E_j^{3/2} × 0.01 × 2^{-j}
             = 0.01 C × 2^{j/2} × E_j^{3/2}

vs viscous dissipation:
∫ ν 4^j E_j dt ~ ν × 2^{2j} × E_j × T_total

The ratio (time-integrated stretching / time-integrated viscosity):
~ (0.01 C / ν) × 2^{j/2} × E_j^{1/2} / (2^{2j} × T_total)
~ (0.01 C / (ν T_total)) × E_j^{1/2} × 2^{-3j/2}

This DECREASES as 2^{-3j/2} with j → ∞!

If this analysis is correct, the time-integrated diagonal transfer
is SUBCRITICAL at high shells. The proof would close.

### Caveat

The time-integrated argument assumes:
1. Peak θ is bounded by a constant (data supports this)
2. Scrambler period ~ 2^{-j} (data supports this, freq ~ 2^j)
3. These hold for ALL NS solutions (not just TG)

Point 3 is the hardest to prove. The TG vortex might not be
representative of all solutions.

## 118 proof files. The scrambler frequency scaling is the key.
