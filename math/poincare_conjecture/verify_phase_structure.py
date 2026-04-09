"""
VERIFY: Does S(x) involve sin(k·x) or cos(k·x)?

File 518 claims: ω ~ cos(k·x), S ~ sin(k·x).
My derivation says: both involve cos(k·x).

Let's check numerically.
"""
import numpy as np

def test_phase():
    """For ω = v cos(k·x), verify whether S involves sin or cos."""
    k = np.array([1, 0, 0.])
    v = np.array([0, 0, 1.])  # v ⊥ k, div-free
    a = 1.0

    # Vorticity at point x
    def omega(x):
        return v * np.cos(k @ x)

    # Velocity from Biot-Savart: u = -(k×v)/|k|² sin(k·x)
    kxv = np.cross(k, v)  # = (0, -1, 0)
    k2 = k @ k

    def u(x):
        return -kxv * np.sin(k @ x) / k2

    # Strain S = sym(∇u) computed numerically
    def S_numerical(x, h=1e-7):
        S = np.zeros((3,3))
        for j in range(3):
            xp = x.copy(); xp[j] += h
            xm = x.copy(); xm[j] -= h
            du = (u(xp) - u(xm)) / (2*h)
            S[:, j] = du
        return (S + S.T) / 2

    # Strain from analytical formula
    # S_k = -(a/2)(ζ⊗k̂ + k̂⊗ζ) where ζ = kxv/|kxv|
    zeta = kxv / np.linalg.norm(kxv)
    khat = k / np.linalg.norm(k)
    S_matrix = -(a/2) * (np.outer(zeta, khat) + np.outer(khat, zeta))

    print("Mode: k=(1,0,0), v=(0,0,1)")
    print(f"  kxv = {kxv}")
    print(f"  ζ = {zeta}")
    print()

    # Test at several points
    for x_test in [np.array([0.5, 0.3, 0.7]),
                    np.array([0.0, 0.0, 0.0]),
                    np.array([np.pi/2, 0, 0]),
                    np.array([1.0, 0.5, 0.2])]:
        S_num = S_numerical(x_test)
        cos_val = np.cos(k @ x_test)
        sin_val = np.sin(k @ x_test)

        # Check if S(x) = S_matrix × cos(k·x) or sin(k·x)
        S_cos = S_matrix * cos_val
        S_sin = S_matrix * sin_val

        err_cos = np.max(np.abs(S_num - S_cos))
        err_sin = np.max(np.abs(S_num - S_sin))

        print(f"  x={x_test}: cos={cos_val:.4f}, sin={sin_val:.4f}")
        print(f"    S matches cos: error={err_cos:.2e}")
        print(f"    S matches sin: error={err_sin:.2e}")
        print(f"    → S(x) = S_matrix × {'cos' if err_cos < err_sin else 'sin'}(k·x)")

    print()
    print("=" * 60)
    print("CONCLUSION: Does S involve cos or sin?")
    print()

    # Multi-mode test
    print("Multi-mode test:")
    ks = [np.array([1,0,0.]), np.array([0,1,0.]), np.array([1,1,0.])]
    vs = [np.array([0,1,0.]), np.array([0,0,1.]), np.array([-1,1,0.])/np.sqrt(2)]

    x_test = np.array([0.3, 0.7, 1.2])

    # ω(x) = Σ v_k cos(k·x)
    om = sum(v * np.cos(k @ x_test) for k, v in zip(ks, vs))

    # S(x) from Biot-Savart
    def u_multi(x):
        return sum(-np.cross(k, v) * np.sin(k @ x) / (k@k) for k, v in zip(ks, vs))

    S_num = np.zeros((3,3))
    h = 1e-7
    for j in range(3):
        xp = x_test.copy(); xp[j] += h
        xm = x_test.copy(); xm[j] -= h
        du = (u_multi(xp) - u_multi(xm)) / (2*h)
        S_num[:, j] = du
    S_num = (S_num + S_num.T) / 2

    # Compute S analytically using cos
    S_ana = np.zeros((3,3))
    for k, v in zip(ks, vs):
        w = np.cross(k, v)
        k2 = k @ k
        S_ana -= (np.outer(w, k) + np.outer(k, w)) * np.cos(k @ x_test) / (2*k2)

    print(f"  S (numerical): \n{S_num}")
    print(f"  S (cos formula): \n{S_ana}")
    print(f"  Max error: {np.max(np.abs(S_num - S_ana)):.2e}")

    # Now check if it's really cos or sin
    # If S ~ sin: S should be zero when all sin(k·x) = 0
    # At x = 0: all sin = 0
    x_zero = np.zeros(3)
    S_at_zero_num = np.zeros((3,3))
    for j in range(3):
        xp = x_zero.copy(); xp[j] += h
        xm = x_zero.copy(); xm[j] -= h
        du = (u_multi(xp) - u_multi(xm)) / (2*h)
        S_at_zero_num[:, j] = du
    S_at_zero_num = (S_at_zero_num + S_at_zero_num.T) / 2

    S_at_zero_ana = np.zeros((3,3))
    for k, v in zip(ks, vs):
        w = np.cross(k, v)
        k2 = k @ k
        S_at_zero_ana -= (np.outer(w, k) + np.outer(k, w)) * np.cos(k @ x_zero) / (2*k2)

    print()
    print(f"  S at x=0 (numerical): norm = {np.linalg.norm(S_at_zero_num):.6f}")
    print(f"  S at x=0 (cos formula): norm = {np.linalg.norm(S_at_zero_ana):.6f}")

    if np.linalg.norm(S_at_zero_ana) > 0.01:
        print(f"  → S(0) ≠ 0! S involves cos(k·x), NOT sin(k·x)!")
        print(f"  → File 518's sin-cos decoupling claim is WRONG")
    else:
        print(f"  → S(0) = 0. S involves sin(k·x)")

    # ω at x=0
    om_zero = sum(v * np.cos(k @ x_zero) for k, v in zip(ks, vs))
    print(f"\n  ω at x=0: norm = {np.linalg.norm(om_zero):.6f}")
    print(f"  This is |ω| at x=0 (should be max if phases align)")

if __name__ == '__main__':
    test_phase()
