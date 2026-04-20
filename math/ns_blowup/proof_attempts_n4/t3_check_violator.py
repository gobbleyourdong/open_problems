"""
t3_check_violator.py  — attempt 855

Tests whether Agent C's SOS violator (from attempt_854) lies in the T^3 image.

Agent C's violator (8-variable SOS at degree 6):
  c1 ~ -0.9993
  c2 ~ -0.0109
  c3 ~ +0.9993
  c4 ~ -0.9990
  s1 ~ +0.037
  s2 ~ +1.0
  s3 ~ -0.037
  s4 ~ +0.046

Under the T^3 parametrization of attempt_851,
  c_j = cos(k_j . x),  s_j = sin(k_j . x),
with k_1 = e_1, k_2 = e_2, k_3 = e_3, k_4 = (1,1,1)/sqrt(3).

So k_j.x = x_j for j=1..3 and k_4.x = (x_1+x_2+x_3)/sqrt(3).

Given (c_1, c_2, c_3) = (-0.9993, -0.0109, +0.9993), solve for x_1, x_2, x_3.
Then compute the REAL c_4 = cos((x_1+x_2+x_3)/sqrt(3)) and compare to the
claimed -0.9990.

There are 4 sign ambiguities (s_j = ± sqrt(1-c_j^2) for j=1,2,3) and a
continuum of branches (mod 2*pi). We enumerate all nearby ones and report
the best match.
"""

import numpy as np
from itertools import product

SQ3 = np.sqrt(3.0)

# Agent C's violator
C_target = np.array([-0.9993, -0.0109,  0.9993, -0.9990])
S_target = np.array([ 0.037,   1.0,    -0.037,   0.046])

def wrap(x):
    return np.mod(x, 2.0 * np.pi)

def solve_x_from_c_s(c1, s1, c2, s2, c3, s3):
    """Return x_j = arctan2(s_j, c_j)."""
    x1 = np.arctan2(s1, c1)
    x2 = np.arctan2(s2, c2)
    x3 = np.arctan2(s3, c3)
    return x1, x2, x3

def eval_c4(x1, x2, x3):
    phi4 = (x1 + x2 + x3) / SQ3
    return np.cos(phi4), np.sin(phi4), phi4

# Primary check: use target (c_j, s_j) directly.
print("=" * 72)
print(" t3_check_violator.py — is Agent C's violator in T^3 image?")
print("=" * 72)

print("\nAgent C's claimed violator:")
print(f"  c = {C_target}")
print(f"  s = {S_target}")

print("\n[1] Primary: use target signs of s directly")
x1 = np.arctan2(S_target[0], C_target[0])
x2 = np.arctan2(S_target[1], C_target[1])
x3 = np.arctan2(S_target[2], C_target[2])
c4_real, s4_real, phi4 = eval_c4(x1, x2, x3)

print(f"  x_1 = arctan2(s_1, c_1) = arctan2({S_target[0]:.4f}, {C_target[0]:.4f}) = {x1:.6f}")
print(f"  x_2 = arctan2(s_2, c_2) = arctan2({S_target[1]:.4f}, {C_target[1]:.4f}) = {x2:.6f}")
print(f"  x_3 = arctan2(s_3, c_3) = arctan2({S_target[2]:.4f}, {C_target[2]:.4f}) = {x3:.6f}")
print(f"  phi_4 = (x_1+x_2+x_3)/sqrt(3) = {phi4:.6f}")
print(f"  c_4 (REAL, from T^3) = cos(phi_4) = {c4_real:.6f}")
print(f"  s_4 (REAL, from T^3) = sin(phi_4) = {s4_real:.6f}")
print(f"  c_4 (TARGET from Agent C) = {C_target[3]:.6f}")
print(f"  s_4 (TARGET from Agent C) = {S_target[3]:.6f}")
print(f"  |c_4_real - c_4_target|  = {abs(c4_real - C_target[3]):.6f}")
print(f"  |s_4_real - s_4_target|  = {abs(s4_real - S_target[3]):.6f}")

# Try all sign combinations of s_1, s_2, s_3 (c_j is fixed)
print("\n[2] Enumerate all 8 sign combinations for s_1, s_2, s_3")
c1, c2, c3 = C_target[0], C_target[1], C_target[2]
# Given c, s can be ±sqrt(1-c^2)
s1_mag = np.sqrt(max(0.0, 1.0 - c1**2))
s2_mag = np.sqrt(max(0.0, 1.0 - c2**2))
s3_mag = np.sqrt(max(0.0, 1.0 - c3**2))

print(f"  |s_1| = sqrt(1 - c_1^2) = sqrt(1 - {c1**2:.6f}) = {s1_mag:.6f}  (target |s_1| = {abs(S_target[0]):.4f})")
print(f"  |s_2| = sqrt(1 - c_2^2) = sqrt(1 - {c2**2:.6f}) = {s2_mag:.6f}  (target |s_2| = {abs(S_target[1]):.4f})")
print(f"  |s_3| = sqrt(1 - c_3^2) = sqrt(1 - {c3**2:.6f}) = {s3_mag:.6f}  (target |s_3| = {abs(S_target[2]):.4f})")

print("\n  sign  s_1    s_2    s_3      x_1     x_2     x_3     phi_4    c_4_real    c_4_target  |delta|")
results = []
for (eps1, eps2, eps3) in product([-1, +1], repeat=3):
    s1 = eps1 * s1_mag; s2 = eps2 * s2_mag; s3 = eps3 * s3_mag
    x1, x2, x3 = solve_x_from_c_s(c1, s1, c2, s2, c3, s3)
    c4r, s4r, phi4 = eval_c4(x1, x2, x3)
    delta_c = c4r - C_target[3]
    results.append((eps1, eps2, eps3, x1, x2, x3, phi4, c4r, delta_c))
    print(f"  {eps1:+d}{eps2:+d}{eps3:+d}  {s1:+6.3f} {s2:+6.3f} {s3:+6.3f}  "
          f"{x1:+7.3f} {x2:+7.3f} {x3:+7.3f}  {phi4:+7.3f}  {c4r:+9.5f}  {C_target[3]:+9.5f}  {abs(delta_c):.6f}")

best = min(results, key=lambda t: abs(t[8]))
print(f"\n  Best-matching sign (minimizing |c_4_real - c_4_target|): eps = ({best[0]:+d},{best[1]:+d},{best[2]:+d})")
print(f"     phi_4 = {best[6]:.6f}, c_4_real = {best[7]:.6f}, delta = {best[8]:.6f}")

print("\n[3] Also sweep over integer shifts of (x_1, x_2, x_3) by 2*pi")
print("    (Note: adding 2*pi to x_j doesn't change c_j or s_j, but shifts phi_4 by 2*pi/sqrt(3))")
print("    Since sqrt(3) is irrational, (c_4, s_4) lands densely on S^1 as we vary shifts.")
print("    We match BOTH c_4 AND s_4 simultaneously (equivalent to matching phi_4 mod 2*pi).")
# Target phi_4 from Agent C's (c_4, s_4)
phi4_target = np.arctan2(S_target[3], C_target[3])
print(f"    phi_4_target = arctan2(s_4_target, c_4_target) = arctan2({S_target[3]:.4f}, {C_target[3]:.4f}) = {phi4_target:.6f}")

best_overall = None
for (eps1, eps2, eps3, x1b, x2b, x3b, phi4b, c4rb, dc) in results:
    for n1, n2, n3 in product(range(-20, 21), repeat=3):
        xx1 = x1b + 2*np.pi*n1
        xx2 = x2b + 2*np.pi*n2
        xx3 = x3b + 2*np.pi*n3
        phi4_shifted = (xx1 + xx2 + xx3) / SQ3
        c4_shifted = np.cos(phi4_shifted)
        s4_shifted = np.sin(phi4_shifted)
        # Delta in (c_4, s_4)-plane (which is the same as phi_4 mod 2*pi distance)
        delta_phi = np.mod(phi4_shifted - phi4_target + np.pi, 2*np.pi) - np.pi
        d = abs(delta_phi)
        if best_overall is None or d < best_overall[-1]:
            best_overall = (n1, n2, n3, eps1, eps2, eps3, phi4_shifted, c4_shifted, s4_shifted, d)

if best_overall is not None:
    n1, n2, n3, eps1, eps2, eps3, phi4s, c4s, s4s, d = best_overall
    print(f"  best integer shift in [-20,20]^3: n = ({n1},{n2},{n3}), eps = ({eps1:+d},{eps2:+d},{eps3:+d})")
    print(f"     phi_4 = {phi4s:.6f}  (target {phi4_target:.6f})")
    print(f"     phi_4 - phi_4_target (mod 2pi) = {d:.6f}")
    print(f"     c_4_real = {c4s:.6f}  (target {C_target[3]:.6f}, delta {c4s - C_target[3]:+.6f})")
    print(f"     s_4_real = {s4s:.6f}  (target {S_target[3]:.6f}, delta {s4s - S_target[3]:+.6f})")

    if d < 0.01:
        print("     -> Can be matched to within 0.01 rad in phi_4 (T^3 image is dense here)")
    elif d < 0.1:
        print("     -> Within 0.1 rad; could match more closely with larger integer range")
    else:
        print("     -> outside with n in [-20,20]; would need larger range (equidistribution)")

# NOW: even if (c_4, s_4) can be matched by equidistribution, the question is whether
# there's a T^3 point x* where ALL 4 of (c, s) match AND x* is a local max of |omega|^2.
# First requirement fails: at Agent C's violator, the first-order constraint is satisfied
# (per attempt_854's SOS setup) but that doesn't guarantee x* is a local MAX; it only
# guarantees x* is a critical point. And even that needed the T^3 angle-link to hold.

print("\n[4] Conclusion")
print("  Agent C's SOS violator (from the 8-var system with sphere + 3 first-order eqs)")
print("  has c_4 = -0.9990.  The T^3 IMAGE gives c_4 determined by the angle-link")
print("  phi_4 = (x_1+x_2+x_3)/sqrt(3).")
if best_overall is not None:
    print(f"  Numerical answer: best-case T^3-realized c_4 = {c4s:.6f}")
    print(f"  Gap to Agent C's claimed c_4 = {abs(dc):.6f}")
print("="*72)
