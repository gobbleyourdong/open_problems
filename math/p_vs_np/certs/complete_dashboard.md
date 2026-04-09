# P vs NP: Complete Empirical Dashboard

## The Gap (n=16)
| Domain | Check | Find | Ratio |
|--------|-------|------|-------|
| Subset Sum | 0.5μs | 9μs | 17× |
| 3-SAT | 68μs | 131ms | 1916× |
| 3-Coloring | 0.6μs | 4.6ms | 8004× |

## Smart vs Brute (n=20)
Meet-in-middle: O(2^{n/2}) vs O(2^n). Still exponential.

## Phase Transition (3-SAT, n=18)
Hardest at α≈4.0: 159ms average. Easy at α=2: 8ms.

## The Boundary (Subset Sum DP crossover)
DP wins at b=4 (small integers). Brute wins at b≥8.
Crossover at b≈6-8 = log₂(n).

## The SOS Parallel
NS: c(N) ≈ 1.2/N → 0 (provable)
P vs NP: c(b) ≈ 2^b → ∞ (blocked by barriers)
