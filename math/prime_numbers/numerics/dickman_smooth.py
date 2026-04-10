"""
Dickman's ρ function and the density of smooth numbers.

An integer n is y-smooth if all its prime factors are ≤ y. Let
    ψ(x, y) = #{n ≤ x : n is y-smooth}
be the count. Dickman (1930) proved:
    ψ(x, y) / x → ρ(u),    where u = log x / log y.

Dickman's ρ is the unique continuous function [0, ∞) → [0, 1] with
    ρ(u) = 1          for 0 ≤ u ≤ 1
    u ρ'(u) = -ρ(u-1) for u > 1

Equivalently, u · ρ(u) = ∫_{u-1}^u ρ(v) dv.

Classical values:
    ρ(1) = 1
    ρ(2) = 1 - log 2 ≈ 0.30685281944005469...
    ρ(3) ≈ 0.04860838568...
    ρ(4) ≈ 0.00491092564...
    ρ(5) ≈ 0.00035472470...
    ρ(6) ≈ 0.00001964968...

Smooth numbers are the workhorse of integer factorization:
 - Quadratic Sieve uses B-smooth relations
 - Number Field Sieve uses smoothness in algebraic number rings
 - Pollard's p-1 method uses B-smoothness of p-1
 - ρ(u) gives the probability a random integer is smooth
"""
import numpy as np
from math import log
from sieve_core import sieve, primes_up_to


def compute_lpf(N):
    """Largest prime factor array lpf[n] for n ≤ N.
    lpf[1] = 0 (convention: 1 is 0-smooth).
    For n ≥ 2, lpf[n] = largest prime dividing n."""
    lpf = np.zeros(N + 1, dtype=np.int64)
    is_prime = sieve(N)
    for p in range(2, N + 1):
        if is_prime[p]:
            # For every multiple of p, tentatively set lpf to p.
            # Since we iterate p in increasing order, larger primes overwrite.
            lpf[p::p] = p
    return lpf


def dickman_rho_table(u_max=8.0, du=0.0001):
    """Numerically solve ρ'(u) = -ρ(u-1)/u on a uniform grid using RK4.

    Initial: ρ(u) = 1 for u ∈ [0, 1].
    Step forward from u = 1 using classical RK4 for the DDE:
        k1 = -ρ(u - 1)/u
        k2 = -ρ(u + du/2 - 1)/(u + du/2)
        k3 = -ρ(u + du/2 - 1)/(u + du/2)  [same as k2]
        k4 = -ρ(u + du - 1)/(u + du)
        ρ(u + du) = ρ(u) + (du/6)(k1 + 2k2 + 2k3 + k4)
    The delayed values at (u - 1), (u + du/2 - 1), (u + du - 1) are always
    already computed (they lie strictly below u), so no implicit step."""
    n_steps = int(u_max / du) + 1
    us = np.arange(n_steps) * du
    rho = np.ones(n_steps)
    i1 = int(round(1.0 / du))  # index of u = 1

    def rho_shifted(i_current):
        """ρ(u - 1) at step i_current, i.e. rho[i_current - i1]."""
        idx = i_current - i1
        return rho[idx] if idx >= 0 else 1.0

    for i in range(i1, n_steps - 1):
        u = us[i]
        u_half = u + 0.5 * du
        u_full = u + du
        # RK4 on ρ'(u) = -ρ(u-1)/u
        # Delayed values at u-1, u-1+du/2, u-1+du (all less than u, so known)
        r_u_minus_1 = rho_shifted(i)
        # At half-step: need rho(u - 1 + du/2); interpolate between rho[i-i1] and rho[i-i1+1]
        r_u_half_minus_1 = 0.5 * (rho[i - i1] + rho[min(i - i1 + 1, n_steps - 1)])
        r_u_full_minus_1 = rho[min(i - i1 + 1, n_steps - 1)]
        k1 = -r_u_minus_1 / u
        k2 = -r_u_half_minus_1 / u_half
        k3 = k2
        k4 = -r_u_full_minus_1 / u_full
        rho[i + 1] = rho[i] + (du / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
    return us, rho


def rho_at(u_vals, us_table, rho_table):
    """Linear interpolation into the tabulated ρ."""
    return np.interp(u_vals, us_table, rho_table)


def main():
    N = 10**7
    print(f"Dickman ρ & smooth numbers — ψ(x, y) for x ≤ {N}")
    print("=" * 76)

    # Build Dickman table
    print("Building Dickman ρ table (grid 0.001)...")
    us, rho = dickman_rho_table(u_max=8.0, du=0.001)

    # Sanity: print classical values
    print("Dickman ρ(u) at integers u = 1..6:")
    classical = {
        1: 1.0,
        2: 1 - log(2),                # 0.30685281944005469
        3: 0.04860838568756097,       # from literature
        4: 0.00491092564776083,
        5: 0.00035472470179229,
        6: 0.00001964968304849,
    }
    for u_int in range(1, 7):
        ours = rho_at(np.array([float(u_int)]), us, rho)[0]
        ref = classical[u_int]
        rel_err = abs(ours - ref) / ref if ref > 0 else 0
        print(f"  ρ({u_int}) = {ours:.10f}  (ref {ref:.10f}, rel err {rel_err:.2e})")
    print()

    # Compute lpf and smooth counts
    print(f"Computing lpf(n) for n ≤ {N}...")
    lpf = compute_lpf(N)
    lpf = lpf[2:]  # drop 0 and 1

    # Pick (x, y) pairs with diverse u = log x / log y
    x_test = N  # fix x = 10^7
    # Choose y values to hit u = 1.5, 2, 2.5, 3, 4, 5
    log_x = log(x_test)
    target_us = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]
    print(f"Testing x = {x_test}, varying y to hit u = log x / log y = target:")
    print("(HT = Hildebrand-Tenenbaum refinement: ρ(u)·(1 + correction))")
    print()
    print(f"{'u':>6} {'y':>8} {'ψ/x':>12} {'ρ(u)':>12} "
          f"{'HT refined':>12} {'err vs ρ':>10} {'err vs HT':>10}")
    print("-" * 82)

    for u_target in target_us:
        y = int(np.exp(log_x / u_target))
        count = int(np.sum(lpf <= y))
        density = count / (x_test - 1)
        u_exact = log_x / log(y)
        rho_val = rho_at(np.array([u_exact]), us, rho)[0]
        # Hildebrand-Tenenbaum refinement:
        # ψ(x,y)/x ≈ ρ(u) · (1 + (1 - γ) · u / log y)
        # Leading finite-size correction.
        gamma = 0.5772156649
        ht_refined = rho_val * (1 + (1 - gamma) * u_exact / log(y))
        err_rho = (density - rho_val) / rho_val if rho_val > 0 else 0
        err_ht = (density - ht_refined) / ht_refined if ht_refined > 0 else 0
        print(f"{u_exact:>6.3f} {y:>8} {density:>12.6f} {rho_val:>12.6f} "
              f"{ht_refined:>12.6f} {err_rho:>+9.2%} {err_ht:>+9.2%}")
    print()

    # Alternative: fix y, vary x
    print(f"Fix y = {int(np.sqrt(N))}, vary x:")
    y_fix = int(np.sqrt(N))  # sqrt(10^7) ≈ 3162
    log_y = log(y_fix)
    print(f"{'x':>10} {'u':>6} {'ψ(x,y)':>12} {'ψ/x':>14} "
          f"{'ρ(u)':>14} {'rel err':>12}")
    print("-" * 76)
    for x in [10**k for k in range(4, 8)]:
        u = log(x) / log_y
        # Need count of n ≤ x with lpf(n) ≤ y_fix
        count = int(np.sum(lpf[:x - 1] <= y_fix))
        density = count / (x - 1)
        rho_val = rho_at(np.array([u]), us, rho)[0]
        rel_err = abs(density - rho_val) / rho_val if rho_val > 0 else 0
        print(f"{x:>10} {u:>6.3f} {count:>12} {density:>14.6f} "
              f"{rho_val:>14.6f} {rel_err:>11.2%}")
    print()

    # Practical: what fraction of [1, 10^7] is 100-smooth? 1000-smooth?
    print("Practical smoothness fractions at x = 10^7:")
    for y in [10, 50, 100, 500, 1000, 10000, 100000]:
        u = log(N) / log(y)
        count = int(np.sum(lpf <= y))
        density = count / (N - 1)
        rho_val = rho_at(np.array([u]), us, rho)[0]
        print(f"  y = {y:>6}: u = {u:.3f}, ψ/x = {density:.6f}, "
              f"ρ(u) = {rho_val:.6f}, count = {count}")


if __name__ == '__main__':
    main()
