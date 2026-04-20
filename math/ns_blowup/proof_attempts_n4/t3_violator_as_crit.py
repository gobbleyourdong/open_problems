"""
t3_violator_as_crit.py — follow-up: is Agent C's violator realizable as
a TRUE local maximum of |omega(x)|^2 on R^3?

Approach:
  1. Find a specific x* achieving the best match of (c, s) to Agent C's violator.
  2. Check: is grad_x |omega|^2 = 0 at x*? (first-order condition)
  3. If yes, is the Hessian NSD (second-order max condition)?
  4. Compute |omega|^2 and ratio there, compare to 9/8.

If x* fails (2) or (3), then Agent C's violator is NOT a T^3-realizable
local max; it's only a point where the first-order equations (as formulated
in the 8-variable system) are satisfied because c_4 has been DETACHED from
the angle-link.
"""

import numpy as np
from itertools import product

SQ2 = np.sqrt(2.0); SQ3 = np.sqrt(3.0)
k1 = np.array([1.0,0,0]); k2 = np.array([0,1.0,0]); k3 = np.array([0,0,1.0])
k4 = np.array([1.0,1.0,1.0]) / SQ3
v1 = np.array([0,1.0,0]); v2 = np.array([0,0,1.0]); v3 = np.array([1.0,0,0])
v4 = np.array([1.0,-1.0,0]) / SQ2
K = np.stack([k1,k2,k3,k4]); V = np.stack([v1,v2,v3,v4])
W = np.cross(K, V)
S_stack = np.empty((4,3,3))
for j in range(4):
    S_stack[j] = -0.5 * (np.outer(K[j], W[j]) + np.outer(W[j], K[j]))
T_gram = np.einsum('jab,kab->jk', S_stack, S_stack)
Mv = V @ V.T


def omega_sq(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    return float(om @ om)


def grad(x):
    phi = K @ x; c = np.cos(phi); s = np.sin(phi)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    ov = V @ om
    return -2.0 * (K.T @ (s * ov))


def hessian(x):
    phi = K @ x; c = np.cos(phi); s = np.sin(phi)
    a = c * (Mv @ c)
    A = -2.0 * np.einsum('j,jn,jm->nm', a, K, K)
    B = 2.0 * (K.T * s) @ Mv @ (s[:, None] * K)
    return A + B


def ratio_at(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(om @ om)
    sf_sq = float(c @ T_gram @ c)
    return om_sq, sf_sq, (sf_sq / om_sq if om_sq > 1e-14 else float('nan'))


# Agent C's violator
C_target = np.array([-0.9993, -0.0109,  0.9993, -0.9990])
S_target = np.array([ 0.037,   1.0,    -0.037,   0.046])

# From t3_check_violator.py [3]: best match is at
# x* with base (c,s) using epsilons (-1,+1,+1) and integer shifts (n1,n2,n3)=(4,20,10)
# Let me re-derive cleanly.

# Base x: solve x_j = arctan2(s_j, c_j) with chosen sign for s_j.
def make_x_base(c1,s1,c2,s2,c3,s3):
    return np.array([np.arctan2(s1,c1), np.arctan2(s2,c2), np.arctan2(s3,c3)])

phi4_target = np.arctan2(S_target[3], C_target[3])

c1, c2, c3 = C_target[0], C_target[1], C_target[2]
s1_mag = np.sqrt(max(0.0, 1.0 - c1**2))
s2_mag = np.sqrt(max(0.0, 1.0 - c2**2))
s3_mag = np.sqrt(max(0.0, 1.0 - c3**2))

best = None
# Only use eps matching the target signs of (s_1, s_2, s_3):
# target s = (+0.037, +1.0, -0.037) -> eps = (+1, +1, -1)
for (e1,e2,e3) in product([-1,+1], repeat=3):
    # match target s signs preferentially
    sign_ok = (e1 == int(np.sign(S_target[0])) and
               e2 == int(np.sign(S_target[1])) and
               e3 == int(np.sign(S_target[2])))
    s1 = e1*s1_mag; s2 = e2*s2_mag; s3 = e3*s3_mag
    xb = make_x_base(c1,s1,c2,s2,c3,s3)
    # find integer shift (n1,n2,n3) so that phi4 matches phi4_target mod 2pi
    for n1, n2, n3 in product(range(-30, 31), repeat=3):
        x = xb + 2*np.pi*np.array([n1,n2,n3])
        phi4 = (x[0]+x[1]+x[2]) / SQ3
        d = np.mod(phi4 - phi4_target + np.pi, 2*np.pi) - np.pi
        # Score: prefer sign-match, then proximity
        score = abs(d) + (0 if sign_ok else 10.0)
        if best is None or score < best[0]:
            best = (score, e1,e2,e3, n1,n2,n3, x.copy(), phi4, abs(d), sign_ok)

print(f"    (debug: sign_ok = {best[-1]}, angle delta = {best[-2]:.6f} rad)")

print("=" * 72)
print(" t3_violator_as_crit.py — classify Agent C's violator as R^3 critical point?")
print("=" * 72)
_, e1,e2,e3, n1,n2,n3, x_star, phi4, d, _ = best
print(f"\n[1] Best-matching x*: eps=({e1:+d},{e2:+d},{e3:+d}), n=({n1},{n2},{n3})")
print(f"    x* = {x_star}")
print(f"    phi_4(x*) = {phi4:.6f}  (target {phi4_target:.6f}, delta in [-pi,pi]: {d:.6f} rad)")

# Evaluate (c, s) at x*
phi = K @ x_star
c_real = np.cos(phi); s_real = np.sin(phi)
print(f"    c_real = {c_real}")
print(f"    s_real = {s_real}")
print(f"    target c = {C_target}")
print(f"    target s = {S_target}")
print(f"    max |c_real - target c| = {np.max(np.abs(c_real - C_target)):.6f}")
print(f"    max |s_real - target s| = {np.max(np.abs(s_real - S_target)):.6f}")

# Check first-order condition
g = grad(x_star)
gn = float(np.linalg.norm(g))
print(f"\n[2] First-order: grad |omega|^2 at x* = {g}")
print(f"    ||grad|| = {gn:.6e}")

# Check second-order condition
H = hessian(x_star)
eigs = np.linalg.eigvalsh(H)
print(f"\n[3] Hessian of |omega|^2 at x*: eigenvalues = {eigs}")
print(f"    max eig = {np.max(eigs):.6e}")
print(f"    is NSD (local max)? {'YES' if np.max(eigs) <= 1e-6 else 'NO'}")

# Compute |omega|^2 and ratio
om_sq, sf_sq, rat = ratio_at(x_star)
print(f"\n[4] |omega(x*)|^2 = {om_sq:.8f}")
print(f"    ||S(x*)||_F^2 = {sf_sq:.8f}")
print(f"    ratio = {rat:.8f}")
print(f"    9/8 = {9.0/8.0:.8f}")

print("\n[5] Verdict")
if gn > 1e-4:
    print("    x* is NOT a critical point of |omega|^2 (||grad|| large).")
    print("    => Agent C's violator does NOT correspond to a vorticity maximum on T^3.")
    print("    It lives only in the SOS-relaxation where c_4 is detached from the angle-link.")
elif np.max(eigs) > 1e-6:
    print("    x* IS a critical point but Hessian has positive eigenvalue.")
    print("    => x* is a saddle / min of |omega|^2, not a maximum.")
    print("    => Agent C's violator does NOT correspond to a vorticity maximum.")
elif rat >= 9.0/8.0:
    print("    x* IS a true local max of |omega|^2 AND ratio >= 9/8 => KILL!")
else:
    print(f"    x* IS a true local max with ratio = {rat:.6f} < 9/8.")
print("=" * 72)
