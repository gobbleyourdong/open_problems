"""
N=4 Key Lemma Frobenius target (R*) - sampling falsifier search.

Target polynomial inequality:
    P(a,b,c2,c4) := (5/8)*(a^2 + b^2 + c2^2) - (sqrt(2)/3)*c4*(a + c2 - 2b) - c4^2  >=  0

Semialgebraic set S:
  (F1')  (1 - (a + c4/sqrt(2))^2) * a^2 <= 1/4
  (F3')  (1 - (b - c4/sqrt(2))^2) * b^2 <= 1/4
  (F')   (1 - c4^2) * (b - a)^2 <= 3/2
  box:   |a + c4/sqrt(2)| <= 1, |b - c4/sqrt(2)| <= 1, |c2| <= 1, |c4| <= 1
  (NON-DEG) a^2 + b^2 + c2^2 + 2*c4^2 + sqrt(2)*c4*(a - b) > 0   (strict)

Task: find a feasible point where P < 0  (a falsifier), or report the minimum LHS over samples.
"""
import numpy as np

np.random.seed(20260419)

SQRT2 = np.sqrt(2.0)

def target(a, b, c2, c4):
    """Return P = (5/8)*(a^2+b^2+c2^2) - (sqrt(2)/3)*c4*(a+c2-2b) - c4^2.
    R* claims P >= 0 on the feasible set."""
    return (5.0/8.0)*(a*a + b*b + c2*c2) - (SQRT2/3.0)*c4*(a + c2 - 2.0*b) - c4*c4

def feasible(a, b, c2, c4, tol=1e-12):
    """Check if point is in S (with strict NON-DEG)."""
    c1 = a + c4/SQRT2
    c3 = b - c4/SQRT2
    if abs(c1) > 1.0 + tol: return False
    if abs(c3) > 1.0 + tol: return False
    if abs(c2) > 1.0 + tol: return False
    if abs(c4) > 1.0 + tol: return False
    # F1'
    if (1.0 - c1*c1) * a*a > 0.25 + tol: return False
    # F3'
    if (1.0 - c3*c3) * b*b > 0.25 + tol: return False
    # F'
    if (1.0 - c4*c4) * (b - a)**2 > 1.5 + tol: return False
    # NON-DEG (strict > 0)
    nd = a*a + b*b + c2*c2 + 2.0*c4*c4 + SQRT2*c4*(a - b)
    if nd <= tol: return False
    return True

def nondeg_value(a, b, c2, c4):
    return a*a + b*b + c2*c2 + 2.0*c4*c4 + SQRT2*c4*(a - b)

# ========== Uniform box sampling ==========
N = 2_000_000
# Sample c1, c3, c2, c4 in [-1,1], derive a, b
c1s = np.random.uniform(-1, 1, N)
c3s = np.random.uniform(-1, 1, N)
c2s = np.random.uniform(-1, 1, N)
c4s = np.random.uniform(-1, 1, N)
aas = c1s - c4s/SQRT2
bbs = c3s + c4s/SQRT2

# Feasibility masks (vectorized)
F1 = (1.0 - c1s*c1s) * aas*aas <= 0.25
F3 = (1.0 - c3s*c3s) * bbs*bbs <= 0.25
Fp = (1.0 - c4s*c4s) * (bbs - aas)**2 <= 1.5
ND = (aas*aas + bbs*bbs + c2s*c2s + 2.0*c4s*c4s + SQRT2*c4s*(aas - bbs)) > 1e-10
feas = F1 & F3 & Fp & ND

n_feas = int(np.sum(feas))
print(f"Samples: {N}, feasible: {n_feas} ({100*n_feas/N:.2f}%)")

if n_feas > 0:
    a_f = aas[feas]; b_f = bbs[feas]; c2_f = c2s[feas]; c4_f = c4s[feas]
    P = target(a_f, b_f, c2_f, c4_f)
    nd = nondeg_value(a_f, b_f, c2_f, c4_f)
    # Scale-invariant: P / nd (since target inequality really lives at |omega|^2 > 0)
    Pratio = P / nd

    idx_min_P = int(np.argmin(P))
    idx_min_Pratio = int(np.argmin(Pratio))
    print()
    print("=== Minimum raw P = (5/8)*(a^2+b^2+c2^2) - (sqrt2/3)*c4*(a+c2-2b) - c4^2 ===")
    print(f"  min P = {P[idx_min_P]:.6f}  (negative => violates R*)")
    print(f"    at (a,b,c2,c4) = ({a_f[idx_min_P]:.6f}, {b_f[idx_min_P]:.6f}, {c2_f[idx_min_P]:.6f}, {c4_f[idx_min_P]:.6f})")
    print(f"    c1 = {a_f[idx_min_P] + c4_f[idx_min_P]/SQRT2:.6f}, c3 = {b_f[idx_min_P] - c4_f[idx_min_P]/SQRT2:.6f}")
    print(f"    |omega|^2 ~ nd = {nd[idx_min_P]:.6f}")

    print()
    print("=== Minimum scale-invariant P/|omega|^2 ===")
    print(f"  min P/|omega|^2 = {Pratio[idx_min_Pratio]:.6f}")
    print(f"    at (a,b,c2,c4) = ({a_f[idx_min_Pratio]:.6f}, {b_f[idx_min_Pratio]:.6f}, {c2_f[idx_min_Pratio]:.6f}, {c4_f[idx_min_Pratio]:.6f})")
    print(f"    c1 = {a_f[idx_min_Pratio] + c4_f[idx_min_Pratio]/SQRT2:.6f}, c3 = {b_f[idx_min_Pratio] - c4_f[idx_min_Pratio]/SQRT2:.6f}")
    print(f"    |omega|^2 ~ nd = {nd[idx_min_Pratio]:.6f}")
    print(f"    raw P at this point = {P[idx_min_Pratio]:.6f}")

    n_viol = int(np.sum(P < 0))
    print()
    print(f"Feasible points with P < 0: {n_viol} / {n_feas} ({100*n_viol/n_feas:.2f}%)")

    n_viol_strict = int(np.sum((P < 0) & (nd > 0.01)))
    print(f"Feasible points with P < 0 AND |omega|^2 > 0.01: {n_viol_strict}")

    # If violators, print a few distant-from-degenerate ones
    if n_viol_strict > 0:
        viol_mask = (P < 0) & (nd > 0.01)
        viol_idx = np.where(viol_mask)[0]
        # Sort by how deep the violation (most negative P)
        P_viol = P[viol_idx]
        sort_by_depth = viol_idx[np.argsort(P_viol)[:5]]
        print()
        print("Top 5 violators away from |omega|=0 boundary (sorted by most negative P):")
        for k in sort_by_depth:
            print(f"  (a,b,c2,c4) = ({a_f[k]:.5f}, {b_f[k]:.5f}, {c2_f[k]:.5f}, {c4_f[k]:.5f})  P={P[k]:.5f}  |omega|^2={nd[k]:.5f}")

else:
    print("No feasible samples found - feasible set may be very small.")
