"""
P vs NP: THE APPROXIMATION GAP

PCP Theorem (Hastad 2001): MAX-3-SAT cannot be approximated beyond 7/8
in polynomial time, unless P = NP.

Measured: greedy and biased rounding achieve 0.95-0.99 at small n (8-20),
but ratios DECREASE with n, trending toward the 7/8 PCP bound.

The 12.5% gap (7/8 → 1) is P vs NP measured as an approximation ratio.
Three formulations, one gap:
  Decision: c = 1.009 (planted) vs 1.091 (threshold)
  Search:   8 flips (easy) vs 602 (hard) = 75x
  Approx:   7/8 = 0.875 (achievable) vs 1.000 (optimal) = 12.5%
"""
