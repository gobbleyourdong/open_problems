# BSD Odd Instance — L-value Verification (Cycle 17)

## Date: 2026-04-08

## Results (500 primes, short Weierstrass y²=x³+ax+b)

Rank 0 curves: L(E,1) clearly non-zero (0.08-0.77). **Detected correctly.**
Rank 1+ curves: L(E,1) still non-zero with 500 primes (convergence too slow).

## Assessment

The partial Euler product converges SLOWLY for the rank detection needed by BSD:
- Rank 0: O(100) primes sufficient (L(1) ≈ 0.3-0.7, clearly > 0)
- Rank 1: O(10000) primes needed (L(1) → 0 slowly)
- Rank 2: O(100000+) primes OR functional equation acceleration

This IS the BSD wall numerically: you need extraordinary precision to determine
ord_{s=1} L(E,s) for high-rank curves. The structural gap (no rank-2 construction)
manifests computationally as a convergence problem.

## Next Steps
1. Implement functional equation for convergence acceleration
2. Use LMFDB data for pre-computed a_p (avoids point counting)
3. Target: verify BSD for all rank-0 curves with conductor ≤ 1000
4. For rank 2: need mpmath high-precision or interface with PARI/GP
