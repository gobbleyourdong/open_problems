"""Diagnose what's happening with refinement."""
import numpy as np
from scipy.optimize import minimize
from scipy.ndimage import maximum_filter

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
    A = 2.0 * np.einsum('j,jn,jm->nm', a, K, K)
    B = 2.0 * (K.T * s) @ Mv @ (s[:, None] * K)
    return A + B


def ratio_at(x):
    c = np.cos(K @ x)
    om = c[0]*v1 + c[1]*v2 + c[2]*v3 + c[3]*v4
    om_sq = float(om @ om)
    sf_sq = float(c @ T_gram @ c)
    return om_sq, sf_sq, (sf_sq / om_sq if om_sq > 1e-14 else float('nan'))


# Start from the 13 grid-level maxima at N=128
L = 2.0 * np.pi
N = 256
xs = np.linspace(0, L, N, endpoint=False)
X1, X2, X3 = np.meshgrid(xs, xs, xs, indexing='ij')
phi4 = (X1 + X2 + X3) / SQ3
c1 = np.cos(X1); c2 = np.cos(X2); c3 = np.cos(X3); c4 = np.cos(phi4)
omx = c3 + c4/SQ2; omy = c1 - c4/SQ2; omz = c2
osq = omx*omx + omy*omy + omz*omz

nbhd = maximum_filter(osq, size=3, mode='wrap')
lmask = (osq == nbhd)
lidx = np.argwhere(lmask)
# Take only nontrivial
lidx = [tuple(p) for p in lidx if osq[tuple(p)] > 1.0]
print(f"# grid local maxima w/ |om|^2 > 1: {len(lidx)}")

for (i,j,k) in lidx[:20]:
    x0 = np.array([xs[i], xs[j], xs[k]])
    # Very careful L-BFGS-B with tight tolerances
    res = minimize(lambda y: -omega_sq(y), x0, jac=lambda y: -grad(y),
                   method='L-BFGS-B',
                   options={'gtol': 1e-15, 'ftol': 1e-16, 'maxiter': 5000})
    x = res.x
    g = grad(x)
    gn = np.linalg.norm(g)
    om_sq, sf_sq, rat = ratio_at(x)
    H = hessian(x)
    eigs = np.linalg.eigvalsh(H)
    print(f"  seed ({x0[0]:.3f},{x0[1]:.3f},{x0[2]:.3f}) -> "
          f"({x[0]:.5f},{x[1]:.5f},{x[2]:.5f}) "
          f"|om|^2={om_sq:.4f} ratio={rat:.4f} gn={gn:.2e} eigs=[{eigs[0]:.2e},{eigs[1]:.2e},{eigs[2]:.2e}]")
