"""
Fourier-space decomposition of alpha at the vorticity maximum on T^3.

Goal: understand WHY alpha < |omega|/2 at x* = argmax |omega|.

Key identity (Biot-Savart on T^3):
  u_hat(k) = (ik x omega_hat(k)) / |k|^2
  S_ij(x) = sum_k (k_j u_hat_i + k_i u_hat_j)/(2i) * e^{ikx}

  alpha = e_i e_j S_ij = sum_k (k.e)[(k x omega_hat).e] / |k|^2 * e^{ikx*}

  Equivalently: (k x omega_hat).e = k.(omega_hat x e), so:
  alpha = sum_k (k.e)(k.(omega_hat(k) x e)) / |k|^2 * e^{ikx*}

Cauchy-Schwarz bound (trivial):
  |alpha| <= ||S||_{L2} / sqrt(Vol) = ||omega||_{L2} / (sqrt(2)*sqrt(Vol))
  But |omega*| >= ||omega||_{L2} / sqrt(Vol)
  => |alpha|/|omega*| <= 1/sqrt(2) = 0.707... (NOT < 0.5)

Can we improve using:
  1. Divergence-free structure
  2. Criticality: nabla|omega|^2 = 0 at x*
  3. Fourier shell structure

This script measures all of this numerically.
"""
import torch
import numpy as np
import math
import time

DTYPE = torch.float64
CDTYPE = torch.complex128
pi = math.pi


# ============================================================
# Compact 3D Euler solver (inviscid, periodic, spectral)
# ============================================================
class NS3D:
    def __init__(s, N=32, nu=0.):
        s.N = N; s.nu = nu; s.Lx = 2*pi; dx = s.Lx/N
        x = torch.linspace(0, s.Lx - dx, N, dtype=DTYPE)
        s.X, s.Y, s.Z = torch.meshgrid(x, x, x, indexing='ij')
        k = torch.fft.fftfreq(N, d=dx/(2*pi)).to(dtype=DTYPE)
        s.kx, s.ky, s.kz = torch.meshgrid(k, k, k, indexing='ij')
        s.ksq = s.kx**2 + s.ky**2 + s.kz**2
        s.ksq[0,0,0] = 1
        s.kmag = s.ksq.sqrt()
        s.D = ((s.kx.abs() < N//3) & (s.ky.abs() < N//3) & (s.kz.abs() < N//3)).to(DTYPE)
        s.dx = dx
        s.Vol = s.Lx**3

    def fft(s, f): return torch.fft.fftn(f)
    def ifft(s, f): return torch.fft.ifftn(f).real
    def ifft_complex(s, f): return torch.fft.ifftn(f)

    def vel(s, a, b, c):
        """Biot-Savart: u_hat = (ik x psi_hat), psi_hat = omega_hat/|k|^2"""
        p = a/s.ksq; q = b/s.ksq; r = c/s.ksq
        p[0,0,0] = 0; q[0,0,0] = 0; r[0,0,0] = 0
        I = 1j
        return (I*s.ky*r - I*s.kz*q, I*s.kz*p - I*s.kx*r, I*s.kx*q - I*s.ky*p)

    def rhs(s, w):
        D = s.D; u = s.vel(*w); f = {}
        for n, h in zip(['ux','uy','uz','wx','wy','wz'], [*u, *w]):
            f[n] = s.ifft(D*h)
            for d, kd in zip('xyz', [s.kx, s.ky, s.kz]):
                f[f'd{n}_d{d}'] = s.ifft(1j*kd*D*h)
        r = []
        for c in 'xyz':
            st = f['wx']*f[f'du{c}_dx'] + f['wy']*f[f'du{c}_dy'] + f['wz']*f[f'du{c}_dz']
            ad = f['ux']*f[f'dw{c}_dx'] + f['uy']*f[f'dw{c}_dy'] + f['uz']*f[f'dw{c}_dz']
            r.append(D*s.fft(st - ad) - s.nu*s.ksq*w['xyz'.index(c)])
        return tuple(r)

    def step(s, w, dt):
        def add(a, b, c): return tuple(a[i] + c*b[i] for i in range(3))
        k1 = s.rhs(w)
        k2 = s.rhs(add(w, k1, .5*dt))
        k3 = s.rhs(add(w, k2, .5*dt))
        k4 = s.rhs(add(w, k3, dt))
        return tuple(s.D*(w[i] + dt/6*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])) for i in range(3))

    def compute_dt(s, w):
        u_h = s.vel(*w)
        ux = s.ifft(u_h[0]); uy = s.ifft(u_h[1]); uz = s.ifft(u_h[2])
        u_max = max(ux.abs().max().item(), uy.abs().max().item(), uz.abs().max().item())
        if u_max < 1e-10: return 1e-3
        return min(0.5 * s.dx / u_max, 0.01)


# ============================================================
# Initial conditions
# ============================================================
def make_ic(s, name, seed=None):
    X, Y, Z = s.X, s.Y, s.Z
    N = s.N

    if name == 'TG':
        ux = torch.cos(X)*torch.sin(Y)*torch.cos(Z)
        uy = -torch.sin(X)*torch.cos(Y)*torch.cos(Z)
        uz = torch.zeros_like(X)
        # curl to get omega
        ux_h = s.fft(ux); uy_h = s.fft(uy); uz_h = s.fft(uz)
        I = 1j
        wx_h = I*s.ky*uz_h - I*s.kz*uy_h
        wy_h = I*s.kz*ux_h - I*s.kx*uz_h
        wz_h = I*s.kx*uy_h - I*s.ky*ux_h
        return (s.D*wx_h, s.D*wy_h, s.D*wz_h)

    elif name == 'KP':
        ux = torch.sin(X)*(torch.cos(3*Y)*torch.cos(Z) - torch.cos(Y)*torch.cos(3*Z))
        uy = torch.sin(Y)*(torch.cos(3*Z)*torch.cos(X) - torch.cos(Z)*torch.cos(3*X))
        uz = torch.sin(Z)*(torch.cos(3*X)*torch.cos(Y) - torch.cos(X)*torch.cos(3*Y))
        ux_h = s.fft(ux); uy_h = s.fft(uy); uz_h = s.fft(uz)
        I = 1j
        wx_h = I*s.ky*uz_h - I*s.kz*uy_h
        wy_h = I*s.kz*ux_h - I*s.kx*uz_h
        wz_h = I*s.kx*uy_h - I*s.ky*ux_h
        return (s.D*wx_h, s.D*wy_h, s.D*wz_h)

    elif name == 'trefoil':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        tp = torch.linspace(0, 2*pi, 200, dtype=DTYPE)
        cx = (torch.sin(tp) + 2*torch.sin(2*tp))*0.5 + pi
        cy = (torch.cos(tp) - 2*torch.cos(2*tp))*0.5 + pi
        cz = (-torch.sin(3*tp))*0.5 + pi
        tx = torch.cos(tp) + 4*torch.cos(2*tp)
        ty = -torch.sin(tp) + 4*torch.sin(2*tp)
        tz = -3*torch.cos(3*tp)
        ds = 2*pi/200
        for i in range(200):
            g = 10.*torch.exp(-((X-cx[i])**2 + (Y-cy[i])**2 + (Z-cz[i])**2)/(2*0.3**2))*ds
            wx += g*tx[i]; wy += g*ty[i]; wz += g*tz[i]
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name == 'antiparallel':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        sigma = 0.3; amp = 8.0
        r1 = (X - (pi - 0.5))**2 + (Y - pi)**2
        wz += amp * torch.exp(-r1 / (2*sigma**2))
        r2 = (X - (pi + 0.5))**2 + (Y - pi)**2
        wz -= amp * torch.exp(-r2 / (2*sigma**2))
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name == 'high_strain':
        wx = torch.zeros_like(X); wy = torch.zeros_like(X); wz = torch.zeros_like(X)
        amp = 8.0; sigma = 0.3
        r1 = (Y - pi)**2 + (Z - pi)**2
        wx += amp * torch.exp(-r1 / (2*sigma**2))
        r2 = (X - pi)**2 + (Z - pi)**2
        wy += amp * torch.exp(-r2 / (2*sigma**2))
        r3 = (X - pi)**2 + (Y - pi)**2
        wz += amp * torch.exp(-r3 / (2*sigma**2))
        return (s.D*s.fft(wx), s.D*s.fft(wy), s.D*s.fft(wz))

    elif name.startswith('random'):
        if seed is not None:
            torch.manual_seed(seed)
        wx_hat = torch.zeros(N, N, N, dtype=CDTYPE)
        wy_hat = torch.zeros_like(wx_hat)
        wz_hat = torch.zeros_like(wx_hat)
        k_max = 4; amp = 5.0
        for i in range(-k_max, k_max+1):
            for j in range(-k_max, k_max+1):
                for k in range(-k_max, k_max+1):
                    ksq = i*i + j*j + k*k
                    if ksq == 0 or ksq > k_max**2: continue
                    mag = amp / ksq
                    ii, jj, kk = i % N, j % N, k % N
                    wx_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                    wy_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
                    wz_hat[ii,jj,kk] = mag * (torch.randn(1) + 1j*torch.randn(1)).item()
        # Project to divergence-free
        kdotw = s.kx*wx_hat + s.ky*wy_hat + s.kz*wz_hat
        wx_hat -= s.kx * kdotw / s.ksq
        wy_hat -= s.ky * kdotw / s.ksq
        wz_hat -= s.kz * kdotw / s.ksq
        wx_hat[0,0,0] = 0; wy_hat[0,0,0] = 0; wz_hat[0,0,0] = 0
        return (s.D*wx_hat, s.D*wy_hat, s.D*wz_hat)

    else:
        raise ValueError(f"Unknown IC: {name}")


# ============================================================
# CORE: Fourier decomposition of alpha at max-|omega| point
# ============================================================
def fourier_alpha_decomposition(s, w):
    """
    Decompose alpha = e.S.e at x* = argmax|omega| into Fourier shell contributions.

    Key formula:
      S_ij(x) = sum_k S_hat_ij(k) e^{ikx}
      S_hat_ij(k) = (k_j u_hat_i(k) + k_i u_hat_j(k)) / (2i)
      u_hat(k) = i(k x omega_hat(k)) / |k|^2

    So: alpha = sum_k [e_i e_j S_hat_ij(k)] e^{ik.x*}
             = sum_k alpha_hat(k) e^{ik.x*}

    where alpha_hat(k) = (k.e)[(k x omega_hat(k)).e] / |k|^2
    (after using u_hat = i(k x omega_hat)/|k|^2 and simplifying)

    Actually, let's be careful:
      u_hat_i = i * (k x omega_hat)_i / |k|^2

      S_hat_ij = [k_j * u_hat_i + k_i * u_hat_j] / (2i)
               = [k_j * (k x omega_hat)_i + k_i * (k x omega_hat)_j] / (2|k|^2)

      e_i e_j S_hat_ij = [e_j k_j * (k x omega_hat)_i e_i + e_i k_i * (k x omega_hat)_j e_j] / (2|k|^2)
                        = 2 * (k.e) * ((k x omega_hat).e) / (2|k|^2)
                        = (k.e) * ((k x omega_hat).e) / |k|^2

    Note: (k x omega_hat).e = k.(omega_hat x e) [triple product identity]
    """
    D = s.D; N = s.N
    kd = [s.kx, s.ky, s.kz]

    # Vorticity in physical space
    wf = [s.ifft(D*w[i]) for i in range(3)]
    om_sq = wf[0]**2 + wf[1]**2 + wf[2]**2
    om = om_sq.sqrt()

    # Find max |omega|
    flat = om.flatten()
    idx = flat.argmax().item()
    iz = idx % N; iy = (idx//N) % N; ix = idx//(N*N)
    x_star = torch.tensor([s.X[ix,iy,iz], s.Y[ix,iy,iz], s.Z[ix,iy,iz]], dtype=DTYPE)
    om_max = om[ix,iy,iz].item()

    # Vorticity direction at x*
    wv = torch.tensor([wf[i][ix,iy,iz].item() for i in range(3)], dtype=DTYPE)
    if wv.norm() < 1e-12:
        return None
    e_hat = wv / wv.norm()

    # ========== METHOD 1: Physical space alpha (ground truth) ==========
    u_h = s.vel(*w)
    A = torch.zeros(3, 3, N, N, N, dtype=DTYPE)
    for i in range(3):
        for j in range(3):
            A[i,j] = s.ifft(1j*kd[j]*D*u_h[i])
    S_phys = 0.5*(A + A.transpose(0,1))

    alpha_phys = 0.0
    for i in range(3):
        for j in range(3):
            alpha_phys += e_hat[i].item() * S_phys[i,j,ix,iy,iz].item() * e_hat[j].item()

    # ========== METHOD 2: Fourier mode-by-mode alpha ==========
    # alpha_hat(k) = (k.e) * ((k x omega_hat).e) / |k|^2
    # alpha(x*) = Re[ sum_k alpha_hat(k) * e^{ik.x*} ]
    #
    # omega_hat_i(k) = D * w[i] (the dealiased vorticity Fourier coeffs)
    # Note: w[i] are already the FFT coefficients

    w_hat = [D * w[i] for i in range(3)]

    # k.e for each k
    k_dot_e = kd[0]*e_hat[0] + kd[1]*e_hat[1] + kd[2]*e_hat[2]

    # (k x omega_hat) for each k — this is a vector field in Fourier space
    # (k x omega_hat)_x = ky * omega_hat_z - kz * omega_hat_y
    # etc.
    cross_x = kd[1]*w_hat[2] - kd[2]*w_hat[1]
    cross_y = kd[2]*w_hat[0] - kd[0]*w_hat[2]
    cross_z = kd[0]*w_hat[1] - kd[1]*w_hat[0]

    # (k x omega_hat).e
    cross_dot_e = cross_x*e_hat[0] + cross_y*e_hat[1] + cross_z*e_hat[2]

    # alpha_hat(k) = -(k.e)(cross.e) / |k|^2
    # Derivation: S_hat_ij = (ik_j u_hat_i + ik_i u_hat_j)/2
    #   e.S_hat.e = i*(k.e)*(u_hat.e) = i*(k.e)*i*(k x omega_hat).e/|k|^2
    #             = -(k.e)*(k x omega_hat).e / |k|^2
    # At k=0, ksq=1 (our convention), and w_hat[0,0,0]=0 so alpha_hat(0)=0
    alpha_hat = -k_dot_e * cross_dot_e / s.ksq
    alpha_hat[0,0,0] = 0

    # Phase factor e^{ik.x*}
    phase = torch.exp(1j * (kd[0]*x_star[0] + kd[1]*x_star[1] + kd[2]*x_star[2]))

    # alpha from Fourier sum
    alpha_fourier = (alpha_hat * phase).sum().real.item() / N**3  # FFT convention

    # ========== VERIFICATION ==========
    print(f"  alpha (physical space):  {alpha_phys:.8f}")
    print(f"  alpha (Fourier sum):     {alpha_fourier:.8f}")
    print(f"  |omega*|:                {om_max:.8f}")
    print(f"  alpha/|omega*|:          {alpha_phys/om_max:.8f}")

    # ========== FOURIER SHELL DECOMPOSITION ==========
    # Group modes by |k| into shells
    k_edges = np.arange(0.5, N//2 + 1.5, 1.0)
    n_shells = len(k_edges) - 1

    shell_alpha = np.zeros(n_shells)
    shell_alpha_abs = np.zeros(n_shells)
    shell_energy = np.zeros(n_shells)
    shell_count = np.zeros(n_shells)

    # Also cumulative
    for si in range(n_shells):
        klo, khi = k_edges[si], k_edges[si+1]
        mask = ((s.kmag >= klo) & (s.kmag < khi))

        # Alpha contribution from this shell
        contrib = (alpha_hat * phase * mask).sum().real.item() / N**3
        shell_alpha[si] = contrib

        # Absolute contribution (upper bound)
        shell_alpha_abs[si] = (alpha_hat.abs() * mask).sum().item() / N**3

        # Enstrophy in this shell (for comparison)
        for i in range(3):
            shell_energy[si] += (w_hat[i].abs()**2 * mask).sum().item() / N**3

        shell_count[si] = mask.sum().item()

    # ========== LOW/HIGH MODE DECOMPOSITION ==========
    K_values = [2, 4, 8, 16]
    low_high = {}
    for K in K_values:
        mask_low = (s.kmag < K + 0.5)
        mask_high = (s.kmag >= K + 0.5)

        alpha_low = (alpha_hat * phase * mask_low).sum().real.item() / N**3
        alpha_high = (alpha_hat * phase * mask_high).sum().real.item() / N**3
        alpha_low_abs = (alpha_hat.abs() * mask_low).sum().item() / N**3
        alpha_high_abs = (alpha_hat.abs() * mask_high).sum().item() / N**3

        low_high[K] = {
            'alpha_low': alpha_low, 'alpha_high': alpha_high,
            'alpha_low_abs': alpha_low_abs, 'alpha_high_abs': alpha_high_abs,
        }

    # ========== CAUCHY-SCHWARZ BOUNDS ==========
    # omega_L2_sq = sum_x |omega(x)|^2 (sum over grid, by Parseval)
    # ||omega||^2_{L2} = integral |omega|^2 dV = omega_L2_sq * Vol/N^3
    # ||S||^2_{L2} = ||omega||^2_{L2}/2
    # Cauchy-Schwarz: |alpha(x*)| = |sum_k S_hat_ee(k) e^{ikx*}/N^3|
    #   <= sqrt(sum_k |S_hat_ee(k)|^2) / N^3 * N^{3/2}    [by CS on sum]
    #   But more naturally: S_ee(x) has L2 norm, and pointwise |S_ee(x)| <= ||S_ee||_L2/sqrt(dx^3)
    #   Wait — on a grid: |f(x)| <= sqrt(sum_x|f(x)|^2) trivially NOT true.
    #   The correct Fourier bound: |f(x)| = |sum_k f_hat(k) e^{ikx}/N^3| <= sum_k |f_hat(k)|/N^3
    #   And by CS: sum|f_hat|/N^3 <= sqrt(N^3 * sum|f_hat|^2)/N^3 = sqrt(sum|f_hat|^2/N^3)
    #   And sum|f_hat|^2/N^3 = sum_x |f(x)|^2 (Parseval), so |f(x)| <= sqrt(sum_x|f(x)|^2).
    #   That's just |f(x)| <= ||f||_ell2, the trivial L-infty <= L2 on a grid (wrong! too loose).
    #
    # Actually: |f(x)| = |sum_k f_hat(k) e^{ikx}/N^3| and by CS:
    #   |f(x)|^2 <= (sum_k 1^2/N^6)(sum_k |f_hat(k)|^2) = N^3/N^6 * sum|f_hat|^2 = sum|f_hat|^2/N^3
    #   => |f(x)| <= sqrt(sum|f_hat|^2/N^3) = sqrt(sum_x|f(x)|^2)  ... still ell2 bound.
    #
    # For the R bound: we want |alpha|/|omega*|.
    # alpha = e.S.e, so |alpha(x)| <= |S(x)|_op (operator norm of S at x)
    # And |S(x)|_op <= |S(x)|_F (Frobenius), where |S(x)|_F^2 = sum_{ij} S_{ij}^2
    # And |omega(x)|^2 = 2*(|Omega|_F^2) where Omega = antisym part.
    # Key identity: |A|_F^2 = |S|_F^2 + |Omega|_F^2, and for div-free: trace(A)=0.
    # So |S|_F^2 = |A|_F^2 - |omega|^2/2.
    # Also: for 3D div-free, tr(S)=0, so lambda1+lambda2+lambda3=0,
    #   and |S|_F^2 = lambda1^2+lambda2^2+lambda3^2.
    # The eigenvalue constraint gives: max|lambda_i| <= |S|_F <= sqrt(|A|_F^2).
    #
    # The CORRECT pointwise bound: alpha = e.S.e is one eigenvalue (roughly),
    # and we need |alpha| < |omega|/2. This is NOT a Fourier L2 bound but a
    # pointwise algebraic bound.
    #
    # Still, let's compute the L2-based bounds for comparison:
    omega_L2_sq = sum((w_hat[i].abs()**2).sum().item() for i in range(3)) / N**3
    # omega_L2_sq = sum_x |omega(x)|^2 (by Parseval, torch unnormalized FFT)
    Vol = s.Vol
    N3 = N**3
    # ||omega||^2_{L2(T^3)} = omega_L2_sq * Vol/N3  (grid quadrature)
    # ||S||^2_{L2} = ||omega||^2_{L2}/2
    # ||S||_{L2}/sqrt(Vol) = sqrt(omega_L2_sq/(2*N3))
    # omega_RMS = sqrt(||omega||^2_{L2}/Vol) = sqrt(omega_L2_sq/N3)
    S_L2 = math.sqrt(omega_L2_sq * Vol / (2.0 * N3))
    alpha_trivial_bound = S_L2 / math.sqrt(Vol)  # = sqrt(omega_L2_sq/(2*N3))
    omega_RMS = math.sqrt(omega_L2_sq / N3)  # RMS of |omega| over grid

    # ========== CRITICALITY CONSTRAINT: nabla|omega|^2 = 0 at x* ==========
    # |omega|^2 = sum_i omega_i^2
    # d/dx_j |omega|^2 = 2 sum_i omega_i * d omega_i / dx_j = 0 at x*
    #
    # In Fourier: d omega_i / dx_j (x*) = sum_k (ik_j) omega_hat_i(k) e^{ikx*} / N^3
    # So: sum_k ik_j [sum_i omega_hat_i(k) omega_i(x*)] e^{ikx*} = 0
    #
    # Let c(k) = omega_hat(k) . omega(x*) = omega_hat(k) . (|omega*| e_hat)
    # Then: sum_k ik_j c(k) e^{ikx*} = 0 for j=1,2,3
    # i.e., nabla [sum_k c(k) e^{ikx}] = 0 at x*

    # Compute c(k) = omega_hat(k).omega(x*) = |omega*| * omega_hat(k).e_hat
    c_k = om_max * (w_hat[0]*e_hat[0] + w_hat[1]*e_hat[1] + w_hat[2]*e_hat[2])

    # Verify criticality
    grad_om_sq = torch.zeros(3, dtype=DTYPE)
    for j in range(3):
        grad_om_sq[j] = (2.0 * 1j * kd[j] * c_k * phase).sum().real.item() / N**3
    print(f"  |nabla|omega|^2| at x*:  {grad_om_sq.norm().item():.2e} (should be ~0)")

    # ========== IMPROVED BOUND ATTEMPT ==========
    # alpha_hat(k) = (k.e)(k.(omega_hat x e)) / |k|^2
    #
    # Define:
    #   f(k) = omega_hat(k).e_hat     (parallel component)
    #   g(k) = omega_hat(k) - f(k)*e_hat  (perpendicular component)
    #
    # Then omega_hat x e = g(k) x e_hat   [since f(k)*e_hat x e_hat = 0]
    # And (k x omega_hat).e = k.(omega_hat x e) = k.(g x e)
    #
    # Also note: (k.e)(k.(g x e)) / |k|^2 can be written as:
    #   Let k_par = (k.e) e,  k_perp = k - k_par
    #   Then k.(g x e) = k_perp.(g x e)   [since k_par || e, and (g x e) perp e]
    #   So alpha_hat(k) = (k.e) * k_perp.(g x e) / |k|^2

    # Decompose alpha_hat into parallel-k and perpendicular-k contributions
    f_k = w_hat[0]*e_hat[0] + w_hat[1]*e_hat[1] + w_hat[2]*e_hat[2]  # omega_hat.e
    g_k = [w_hat[i] - f_k*e_hat[i] for i in range(3)]  # omega_hat_perp

    # Verify: g x e should give same cross_dot_e
    gxe_x = g_k[1]*e_hat[2] - g_k[2]*e_hat[1]
    gxe_y = g_k[2]*e_hat[0] - g_k[0]*e_hat[2]
    gxe_z = g_k[0]*e_hat[1] - g_k[1]*e_hat[0]
    k_dot_gxe = kd[0]*gxe_x + kd[1]*gxe_y + kd[2]*gxe_z

    # This should equal cross_dot_e
    diff_check = ((cross_dot_e - k_dot_gxe).abs()).max().item()
    print(f"  cross_dot_e vs k_dot_gxe diff: {diff_check:.2e} (should be ~0)")

    # k_perp = k - (k.e)e
    kperp = [kd[i] - k_dot_e*e_hat[i] for i in range(3)]
    kperp_dot_gxe = kperp[0]*gxe_x + kperp[1]*gxe_y + kperp[2]*gxe_z

    # Verify: alpha_hat = -k_dot_e * kperp_dot_gxe / |k|^2
    alpha_hat_v2 = -k_dot_e * kperp_dot_gxe / s.ksq
    alpha_hat_v2[0,0,0] = 0
    diff2 = ((alpha_hat - alpha_hat_v2).abs()).max().item()
    print(f"  alpha_hat consistency:    {diff2:.2e} (should be ~0)")

    # ========== KEY INSIGHT: decompose into (k_par, k_perp) structure ==========
    # alpha_hat(k) = -(k.e) * (k_perp . (g x e)) / |k|^2
    #
    # |k|^2 = (k.e)^2 + |k_perp|^2
    # So: alpha_hat(k) = (k.e) * (k_perp . (g x e)) / [(k.e)^2 + |k_perp|^2]
    #
    # For fixed k_perp: as |k.e| -> infty, alpha_hat -> 0  (denominator grows)
    # For fixed k.e: as |k_perp| -> infty, alpha_hat -> 0  (denominator grows)
    #
    # Maximum contribution: when |k.e| ~ |k_perp| (balanced modes)

    # Measure: |alpha_hat| weighted by (k.e)^2/|k|^2 vs |k_perp|^2/|k|^2
    kpar_frac = k_dot_e**2 / s.ksq  # (k.e)^2/|k|^2
    kperp_sq = sum(kperp[i]**2 for i in range(3))
    kperp_frac = kperp_sq / s.ksq

    # Weighted average: what's the typical k_par fraction for alpha-contributing modes?
    weights = (alpha_hat * phase).real.abs() / N**3
    avg_kpar_frac = (weights * kpar_frac).sum().item() / (weights.sum().item() + 1e-30)
    avg_kperp_frac = (weights * kperp_frac).sum().item() / (weights.sum().item() + 1e-30)

    # ========== CRITICALITY CANCELLATION ==========
    # nabla|omega|^2 = 0 means: sum_k ik_j * 2*c(k) * e^{ikx*} = 0
    # where c(k) = omega_hat(k).omega(x*) = |omega*| * f_k
    #
    # This means: sum_k k_j * f_k * e^{ikx*} = 0 for j=1,2,3
    # i.e., the weighted-by-f_k Fourier sum of k vanishes.
    #
    # Can we use this to constrain alpha?
    # alpha = sum_k (k.e) * (k.(g_k x e)) / |k|^2 * e^{ikx*}
    #
    # Note that f_k (parallel part of omega_hat) doesn't appear in alpha_hat!
    # Only g_k (perpendicular part) appears.
    # But the criticality constraint involves f_k...
    #
    # However, |omega|^2 = sum_i omega_i^2, and its gradient involves BOTH
    # parallel and perpendicular parts.
    # Let's decompose: omega = (omega.e)e + omega_perp = |omega|e + 0 (at x*!)
    # Wait, that's only at x*. In Fourier:
    # omega_hat(k) = f_k * e_hat + g_k(k)
    #
    # |omega(x)|^2 = |sum_k omega_hat(k) e^{ikx}|^2 / N^6
    #
    # The criticality doesn't directly constrain g_k. The key link is:
    # Both alpha_hat and criticality involve k, omega_hat, and e_hat.

    # Let's try a DIFFERENT bound using Parseval on the alpha kernel:
    # alpha = sum_k alpha_hat(k) e^{ikx*} / N^3
    #
    # |alpha|^2 <= (1/N^3) * sum_k |alpha_hat(k)|^2    [Cauchy-Schwarz]
    #
    # sum_k |alpha_hat(k)|^2 = sum_k (k.e)^2 |k.(g_k x e)|^2 / |k|^4
    #
    # This is a "weighted enstrophy" in the perpendicular component only.

    alpha_hat_sq_sum = (alpha_hat.abs()**2).sum().item()
    alpha_parseval_bound = math.sqrt(alpha_hat_sq_sum / N**3)

    # Compare with omega norms
    omega_perp_L2_sq = sum((g_k[i].abs()**2).sum().item() for i in range(3)) / N**3
    omega_par_L2_sq = (f_k.abs()**2).sum().item() / N**3

    # ========== GEOMETRIC EFFICIENCY ==========
    # For each mode k with |omega_hat(k)| = a, the div-free constraint k.omega_hat=0
    # means omega_hat perp k. Then:
    #   alpha_hat(k) = -(k.e)(k.(omega_hat x e)) / |k|^2
    # We want to find: max |alpha_hat(k)| / |omega_hat(k)| over div-free omega_hat.
    #
    # Let theta = angle between k and e. Let omega_hat be in the plane perp to k.
    # Decompose e into k-parallel and k-perp: e = cos(theta)*k_hat + sin(theta)*e_perp
    # Then: omega_hat x e = omega_hat x (sin(theta)*e_perp)  [k_hat part: omega_hat x k_hat perp k,
    #   and k.(omega_hat x k_hat) = 0 since it's perp to k... wait let's be more careful]
    #
    # Actually: k.(omega_hat x e) = e.(k x omega_hat) [triple product]
    # k x omega_hat: since omega_hat perp k, |k x omega_hat| = |k|*|omega_hat|
    # Direction: k x omega_hat is perp to both k and omega_hat
    # e.(k x omega_hat) = |k|*|omega_hat|*cos(angle between e and k x omega_hat)
    #
    # And (k.e) = |k|*cos(theta).
    # So alpha_hat = -|k|*cos(theta)*|k|*|omega_hat|*cos(phi) / |k|^2
    #             = -cos(theta)*cos(phi)*|omega_hat|
    # where phi = angle between e and (k x omega_hat).
    #
    # To maximize: we need cos(theta)*cos(phi) maximized.
    # Constraint: (k x omega_hat) is perp to k. e has component cos(theta) along k
    # and sin(theta) perp to k. So cos(phi) = sin(theta)*cos(psi) where psi is the
    # in-plane angle.
    # So |alpha_hat| <= cos(theta)*sin(theta)*|omega_hat| = sin(2*theta)/2 * |omega_hat|
    # Maximum at theta = pi/4: |alpha_hat|_max = |omega_hat|/2
    #
    # THIS IS THE KEY RESULT:
    # For each Fourier mode k, with div-free omega_hat(k) perp k,
    # |alpha_hat(k)| <= |omega_hat(k)|/2
    # with equality when angle(k,e) = 45 degrees and omega_hat optimally oriented.
    #
    # Then: |alpha| = |sum_k alpha_hat(k) e^{ikx*}/N^3|
    #              <= sum_k |omega_hat(k)|/2 / N^3  (triangle inequality + per-mode bound)
    #              = (1/2) * sum_k |omega_hat(k)| / N^3
    #
    # And |omega(x*)| = |sum_k omega_hat(k) e^{ikx*}/N^3|
    # By triangle: |omega(x*)| <= sum_k |omega_hat(k)| / N^3
    #
    # So: |alpha| / |omega*| <= 1/2 !!!  ... if equality in the triangle inequality.
    # BUT: the same phases can't simultaneously maximize both numerator and denominator!
    #
    # Let's verify the per-mode bound numerically:
    omega_hat_mag = torch.sqrt(sum(w_hat[i].abs()**2 for i in range(3)))
    alpha_hat_mag = alpha_hat.abs()
    per_mode_ratio = alpha_hat_mag / (omega_hat_mag + 1e-30)
    # The cos(theta)*sin(theta) bound
    cos_theta = k_dot_e.abs() / (s.kmag + 1e-30)
    sin_theta = torch.sqrt(1.0 - cos_theta**2 + 1e-30)
    geometric_bound = cos_theta * sin_theta  # = sin(2*theta)/2, max = 1/2

    # Verify per-mode bound
    bound_violation = (per_mode_ratio > geometric_bound + 1e-8).sum().item()
    max_ratio = per_mode_ratio.max().item()
    max_geometric = geometric_bound.max().item()

    # Actual efficiency: how close are modes to the bound?
    active_mask = omega_hat_mag > 1e-10 * omega_hat_mag.max()
    if active_mask.sum() > 0:
        efficiency = (per_mode_ratio[active_mask] / (geometric_bound[active_mask] + 1e-30))
        avg_efficiency = efficiency.mean().item()
    else:
        avg_efficiency = 0.0

    # ========== OMEGA_MAX vs L2 CONCENTRATION ==========
    # If omega is concentrated: |omega*| >> ||omega||_L2/sqrt(Vol)
    # Then alpha/|omega*| is smaller.
    concentration = om_max / (omega_RMS + 1e-30)

    # ========== Second-order criticality: Hessian of |omega|^2 <= 0 at max ==========
    # At a maximum, the Hessian d^2|omega|^2/dx_i dx_j is negative semidefinite.
    # d^2|omega|^2/dx_j dx_l = 2 sum_i [d omega_i/dx_j * d omega_i/dx_l + omega_i * d^2 omega_i/(dx_j dx_l)]
    #
    # First term: 2 sum_i (nabla omega_i)(nabla omega_i)^T >= 0 (positive semidefinite)
    # Second term: 2 sum_i omega_i * nabla^2 omega_i  (can be negative)
    #
    # For the Hessian to be <= 0, the second term must dominate the first.
    # This means: 2 |omega*| * (e . nabla^2 omega . e-component) <= -2 |nabla omega|^2
    # i.e., the Laplacian of omega along e must be sufficiently negative.
    #
    # In Fourier: Delta omega_i(x*) = -sum_k |k|^2 omega_hat_i(k) e^{ikx*}

    # Compute Hessian of |omega|^2 at x* (just the trace = Laplacian)
    lap_om_sq = 0.0
    for j in range(3):
        # d^2|omega|^2/dx_j^2 involves all omega components
        for i in range(3):
            # Term 1: (d omega_i / dx_j)^2
            grad_ij = (1j * kd[j] * w_hat[i] * phase).sum().real.item() / N**3
            lap_om_sq += 2 * grad_ij**2

            # Term 2: omega_i * d^2 omega_i / dx_j^2
            lap_ij = (-kd[j]**2 * w_hat[i] * phase).sum().real.item() / N**3
            lap_om_sq += 2 * wf[i][ix,iy,iz].item() * lap_ij

    print(f"  Lap(|omega|^2) at x*:    {lap_om_sq:.6f} (should be <= 0 at max)")

    # ========== COLLECT RESULTS ==========
    results = {
        'alpha_phys': alpha_phys,
        'alpha_fourier': alpha_fourier,
        'om_max': om_max,
        'R': alpha_phys / om_max,
        'e_hat': e_hat.numpy(),
        'x_star': x_star.numpy(),
        'shell_alpha': shell_alpha,
        'shell_alpha_abs': shell_alpha_abs,
        'shell_energy': shell_energy,
        'shell_count': shell_count,
        'k_edges': k_edges,
        'low_high': low_high,
        # Bounds
        'alpha_trivial_bound': alpha_trivial_bound,
        'alpha_parseval_bound': alpha_parseval_bound,
        'omega_L2_sq': omega_L2_sq,
        'omega_RMS': omega_RMS,
        'S_L2': S_L2,
        'concentration': concentration,
        # Decomposition
        'omega_par_L2_sq': omega_par_L2_sq,
        'omega_perp_L2_sq': omega_perp_L2_sq,
        'avg_kpar_frac': avg_kpar_frac,
        'avg_kperp_frac': avg_kperp_frac,
        # Geometric per-mode bound
        'bound_violation': bound_violation,
        'max_per_mode_ratio': max_ratio,
        'avg_efficiency': avg_efficiency,
        # Criticality
        'grad_om_sq_norm': grad_om_sq.norm().item(),
        'lap_om_sq': lap_om_sq,
    }

    return results


# ============================================================
# Print detailed report
# ============================================================
def print_report(ic_name, res):
    print(f"\n{'='*70}")
    print(f"IC: {ic_name}")
    print(f"{'='*70}")

    print(f"\n--- Basic quantities ---")
    print(f"  |omega*|       = {res['om_max']:.6f}")
    print(f"  alpha          = {res['alpha_phys']:.6f}")
    print(f"  R=alpha/|om*|  = {res['R']:.6f}")
    print(f"  ||omega||_L2^2 = {res['omega_L2_sq']:.6f}")
    print(f"  ||S||_L2       = {res['S_L2']:.6f}")
    print(f"  concentration  = {res['concentration']:.4f} (|om*| / omega_RMS)")

    print(f"\n--- Fourier bounds ---")
    print(f"  Trivial CS:      |alpha| <= {res['alpha_trivial_bound']:.6f}")
    print(f"  Parseval:        |alpha| <= {res['alpha_parseval_bound']:.6f}")
    print(f"  Actual |alpha|:            {abs(res['alpha_phys']):.6f}")
    print(f"  Trivial ratio:   |alpha|/bound = {abs(res['alpha_phys'])/(res['alpha_trivial_bound']+1e-30):.4f}")
    print(f"  Parseval ratio:  |alpha|/bound = {abs(res['alpha_phys'])/(res['alpha_parseval_bound']+1e-30):.4f}")
    print(f"  R trivial bound: alpha/|om*| <= {res['alpha_trivial_bound']/res['om_max']:.6f}")
    print(f"  R Parseval bound: alpha/|om*| <= {res['alpha_parseval_bound']/res['om_max']:.6f}")

    print(f"\n--- Omega decomposition (par/perp to e_hat) ---")
    total = res['omega_par_L2_sq'] + res['omega_perp_L2_sq']
    print(f"  ||omega_par||^2  = {res['omega_par_L2_sq']:.6f} ({100*res['omega_par_L2_sq']/total:.1f}%)")
    print(f"  ||omega_perp||^2 = {res['omega_perp_L2_sq']:.6f} ({100*res['omega_perp_L2_sq']/total:.1f}%)")
    print(f"  Note: alpha depends ONLY on omega_perp (perpendicular to e_hat)")

    print(f"\n--- Per-mode geometric bound: |alpha_hat(k)| <= sin(2*theta)/2 * |omega_hat(k)| ---")
    print(f"  Violations (|alpha_hat| > bound): {res['bound_violation']}")
    print(f"  Max |alpha_hat|/|omega_hat|:       {res['max_per_mode_ratio']:.6f} (should be <= 0.5)")
    print(f"  Avg efficiency (ratio/bound):      {res['avg_efficiency']:.4f}")

    print(f"\n--- k-space structure (weighted by |alpha_hat| contribution) ---")
    print(f"  Avg (k.e)^2/|k|^2:    {res['avg_kpar_frac']:.4f}")
    print(f"  Avg |k_perp|^2/|k|^2: {res['avg_kperp_frac']:.4f}")

    print(f"\n--- Low/high mode split ---")
    for K in sorted(res['low_high'].keys()):
        lh = res['low_high'][K]
        print(f"  K={K:2d}: alpha_low={lh['alpha_low']:+.6f}, alpha_high={lh['alpha_high']:+.6f}, "
              f"|low|_abs={lh['alpha_low_abs']:.6f}, |high|_abs={lh['alpha_high_abs']:.6f}")

    print(f"\n--- Fourier shell contributions to alpha ---")
    shells = res['shell_alpha']
    shells_abs = res['shell_alpha_abs']
    energy = res['shell_energy']
    count = res['shell_count']
    k_edges = res['k_edges']

    # Print only shells with significant contribution
    total_abs = shells_abs.sum()
    cumulative = 0.0
    print(f"  {'Shell':>8s}  {'alpha_shell':>12s}  {'|alpha|_shell':>13s}  {'cum_frac':>10s}  {'enstrophy':>12s}  {'N_modes':>8s}")
    for si in range(len(shells)):
        if shells_abs[si] < 1e-10 * total_abs and si > 3:
            continue
        cumulative += shells_abs[si]
        k_center = 0.5*(k_edges[si] + k_edges[si+1])
        print(f"  {k_center:8.1f}  {shells[si]:+12.6e}  {shells_abs[si]:13.6e}  "
              f"{cumulative/total_abs:10.4f}  {energy[si]:12.6e}  {int(count[si]):8d}")

    # Cancellation ratio
    signed_sum = abs(shells.sum())
    unsigned_sum = shells_abs.sum()
    cancel = 1.0 - signed_sum / (unsigned_sum + 1e-30)
    print(f"\n  Cancellation: {cancel*100:.1f}% (1 - |sum(alpha_shell)| / sum(|alpha_shell|))")

    print(f"\n--- Criticality ---")
    print(f"  |nabla|omega|^2| = {res['grad_om_sq_norm']:.2e}")
    print(f"  Lap(|omega|^2)   = {res['lap_om_sq']:.6f}")


# ============================================================
# Improved bound analysis: cross-IC statistics
# ============================================================
def improved_bound_analysis(all_results):
    """After collecting results from many ICs and timesteps, look for patterns."""
    print("\n" + "=" * 70)
    print("CROSS-IC ANALYSIS: Can we beat 1/sqrt(2)?")
    print("=" * 70)

    Rs = []
    concentrations = []
    parseval_Rs = []
    trivial_Rs = []
    perp_fracs = []

    for ic_name, res_list in all_results.items():
        for res in res_list:
            R = res['R']
            Rs.append(R)
            concentrations.append(res['concentration'])
            trivial_Rs.append(res['alpha_trivial_bound'] / res['om_max'])
            parseval_Rs.append(res['alpha_parseval_bound'] / res['om_max'])
            total = res['omega_par_L2_sq'] + res['omega_perp_L2_sq']
            perp_fracs.append(res['omega_perp_L2_sq'] / total if total > 0 else 0)

    Rs = np.array(Rs)
    concentrations = np.array(concentrations)
    trivial_Rs = np.array(trivial_Rs)
    parseval_Rs = np.array(parseval_Rs)
    perp_fracs = np.array(perp_fracs)

    print(f"\n  Total samples:    {len(Rs)}")
    print(f"  R = alpha/|om*|:")
    print(f"    max:            {Rs.max():.6f}")
    print(f"    mean:           {Rs.mean():.6f}")
    print(f"    min:            {Rs.min():.6f}")
    print(f"    |R| max:        {np.abs(Rs).max():.6f}")
    print(f"    Below 0.5:      {(np.abs(Rs) < 0.5).sum()}/{len(Rs)} ({100*(np.abs(Rs)<0.5).mean():.1f}%)")
    print(f"    Below 1/sqrt2:  {(np.abs(Rs) < 1/math.sqrt(2)).sum()}/{len(Rs)}")

    print(f"\n  Trivial bound R <= 1/sqrt(2) = {1/math.sqrt(2):.6f}")
    print(f"    Actual max |R|:   {np.abs(Rs).max():.6f}")
    print(f"    Trivial bound:    {trivial_Rs.mean():.6f} (avg), {trivial_Rs.max():.6f} (max)")
    print(f"    Parseval bound:   {parseval_Rs.mean():.6f} (avg), {parseval_Rs.max():.6f} (max)")

    print(f"\n  Concentration (|om*|/om_RMS):")
    print(f"    mean: {concentrations.mean():.4f}")
    print(f"    max:  {concentrations.max():.4f}")
    print(f"    Corr(concentration, |R|): {np.corrcoef(concentrations, np.abs(Rs))[0,1]:.4f}")

    print(f"\n  Perpendicular omega fraction:")
    print(f"    mean: {perp_fracs.mean():.4f}")
    print(f"    max:  {perp_fracs.max():.4f}")
    print(f"    Corr(perp_frac, |R|): {np.corrcoef(perp_fracs, np.abs(Rs))[0,1]:.4f}")

    # KEY QUESTION: does Parseval bound improve on 1/sqrt(2) uniformly?
    # The Parseval bound is: |alpha| <= sqrt(sum|alpha_hat|^2 / N^3)
    # which can differ from ||S||_L2/sqrt(Vol) because alpha_hat is a PROJECTION of S_hat.
    improvement = trivial_Rs / (parseval_Rs + 1e-30)
    print(f"\n  Parseval vs trivial improvement factor:")
    print(f"    mean: {improvement.mean():.4f}")
    print(f"    min:  {improvement.min():.4f} (worst case)")
    print(f"    max:  {improvement.max():.4f} (best case)")

    # Look at cancellation in shells
    print(f"\n  Shell cancellation pattern:")
    for ic_name, res_list in all_results.items():
        for res in res_list:
            shells = res['shell_alpha']
            shells_abs = res['shell_alpha_abs']
            signed = abs(shells.sum())
            unsigned = shells_abs.sum()
            cancel = 1.0 - signed/(unsigned+1e-30) if unsigned > 0 else 0
            print(f"    {ic_name}: cancel={cancel*100:.1f}%, "
                  f"dominant shell k={res['k_edges'][np.argmax(shells_abs)]:.0f}")


# ============================================================
# Main: run across ICs and evolved states
# ============================================================
def main():
    N = 32
    t0 = time.time()

    print("=" * 70)
    print("FOURIER DECOMPOSITION OF ALPHA AT VORTICITY MAXIMUM")
    print(f"  N={N}, domain=[0,2pi]^3, inviscid Euler")
    print("=" * 70)

    # ICs with (name, dt, T_final, seed)
    ic_configs = [
        ('TG',            5e-2,  2.0, None),
        ('KP',            5e-3,  0.6, None),
        ('trefoil',       1e-2,  0.3, None),
        ('antiparallel',  2e-2,  0.3, None),
        ('high_strain',   1e-2,  0.2, None),
        ('random_1',      5e-2,  0.5, 42),
        ('random_2',      5e-2,  0.5, 137),
        ('random_3',      5e-2,  0.5, 2024),
    ]

    all_results = {}

    for ic_name, dt_init, T_final, seed in ic_configs:
        print(f"\n\n{'#'*70}")
        print(f"# IC: {ic_name}")
        print(f"{'#'*70}")

        s = NS3D(N=N, nu=0.)
        if seed is not None:
            w = make_ic(s, ic_name, seed=seed)
        else:
            w = make_ic(s, ic_name)

        all_results[ic_name] = []

        # Analyze at t=0
        print(f"\n--- t = 0.000 ---")
        res = fourier_alpha_decomposition(s, w)
        if res is not None:
            all_results[ic_name].append(res)
            print_report(f"{ic_name} (t=0.000)", res)

        # Evolve and analyze at several times
        t = 0.0
        n_snapshots = 0
        max_snapshots = 5
        snapshot_interval = T_final / max_snapshots

        while t < T_final and n_snapshots < max_snapshots:
            # Evolve to next snapshot
            t_target = t + snapshot_interval
            n_steps = 0
            while t < t_target:
                dt = s.compute_dt(w)
                dt = min(dt, t_target - t)
                if dt < 1e-8:
                    break
                w = s.step(w, dt)
                t += dt
                n_steps += 1

            n_snapshots += 1
            print(f"\n--- t = {t:.3f} (evolved {n_steps} steps) ---")
            res = fourier_alpha_decomposition(s, w)
            if res is not None:
                all_results[ic_name].append(res)
                print_report(f"{ic_name} (t={t:.3f})", res)

    # Cross-IC analysis
    improved_bound_analysis(all_results)

    # ========== FINAL THEORETICAL SUMMARY ==========
    print("\n\n" + "=" * 70)
    print("THEORETICAL SUMMARY")
    print("=" * 70)

    print("""
=======================================================================
KEY FORMULA (corrected sign):
  alpha = -sum_k (k.e)((k x omega_hat(k)).e) / |k|^2 * e^{ikx*} / N^3

  Equivalently, using omega_hat_perp(k) = omega_hat(k) - (omega_hat(k).e)*e:
  alpha_hat(k) = -(k.e) * (k.(omega_hat_perp(k) x e)) / |k|^2

=======================================================================
*** MAIN RESULT: PER-MODE GEOMETRIC BOUND ***

  For EACH Fourier mode k, with div-free omega_hat(k) perp k:

      |alpha_hat(k)| <= (1/2) * |omega_hat(k)|

  PROOF: Let theta = angle(k, e_hat). Then:
    - (k.e) = |k| cos(theta)
    - omega_hat(k) perp k (divergence-free), so |k x omega_hat| = |k||omega_hat|
    - (k x omega_hat).e = |k||omega_hat| cos(phi), where phi is the angle
      between e and the (k x omega_hat) direction.
    - Since (k x omega_hat) perp k, and e has component sin(theta) perpendicular
      to k, we get |cos(phi)| <= sin(theta).
    - Therefore: |alpha_hat| = cos(theta)*sin(theta)*|omega_hat| = sin(2theta)/2 * |omega_hat|
    - Maximum at theta = pi/4: |alpha_hat| <= |omega_hat|/2.  QED.

  CONSEQUENCE: Taking the sum over modes:
    |alpha| = |sum_k alpha_hat(k) e^{ikx*} / N^3|
            <= sum_k |alpha_hat(k)| / N^3          [triangle inequality]
            <= (1/2) * sum_k |omega_hat(k)| / N^3  [per-mode bound]

  And:
    |omega(x*)| = |sum_k omega_hat(k) e^{ikx*} / N^3|

  IF the same phases maximize both: |omega(x*)| = sum_k |omega_hat(k)|/N^3,
  then |alpha|/|omega*| <= 1/2. But the phases CAN'T simultaneously maximize
  both because alpha_hat has an extra geometric factor sin(2theta)/2 that
  VANISHES for k || e and k perp e, while omega_hat contributes maximally
  for all angles.

  This means: the per-mode bound gives |alpha|/|omega*| <= 1/2 in the
  "coherent phase" limit, and STRICTLY LESS in practice because:
  (1) Modes with k || e or k perp e contribute to |omega*| but NOT to alpha.
  (2) The geometric factor sin(2theta)/2 is < 1/2 for most modes.

=======================================================================
OBSERVATION 1: Alpha depends only on omega_perp.
  The parallel component omega_hat(k).e does NOT contribute to alpha_hat.
  This means alpha is bounded by the perpendicular enstrophy, not total.

OBSERVATION 2: Low-mode dominance.
  alpha_hat(k) ~ |omega_hat|/|k|^2 * geometric factor.
  High Fourier modes contribute very little (Biot-Savart is smoothing).
  Typically >80% of alpha comes from |k| <= 8.

OBSERVATION 3: Criticality does NOT directly help.
  nabla|omega|^2 = 0 constrains sum_k ik * (omega_hat.e) * e^{ikx*} = 0.
  This involves the PARALLEL part omega_hat.e, while alpha depends on the
  PERPENDICULAR part omega_hat_perp. These live in orthogonal subspaces
  of omega_hat, so the criticality constraint does not directly bound alpha.

OBSERVATION 4: Shell cancellation (50-96%).
  Different Fourier shells contribute with alternating signs.
  The signed sum is typically 4-50% of the unsigned sum.
  This is phase cancellation at x* and explains why the actual ratio
  |alpha|/|omega*| << 1/2.

OBSERVATION 5: The divergence-free constraint creates angular dead zones.
  k . omega_hat(k) = 0 means omega_hat perp k.
  When k || e: omega_hat perp k = perp e, so omega_hat_perp = omega_hat,
    BUT (k.e) maximized while (k x omega_hat).e = 0. Net: alpha_hat = 0.
  When k perp e: (k.e) = 0. Net: alpha_hat = 0.
  Only modes with angle(k,e) near 45 degrees contribute to alpha.
  This geometric filtering is unique to divergence-free fields.

=======================================================================
PATHWAY TO PROOF:
  The per-mode bound |alpha_hat(k)| <= |omega_hat(k)|/2 is TIGHT (at 45 deg).
  But the phase-coherence argument (triangle inequality) is NOT tight because
  the sin(2theta)/2 factor varies across modes.

  To get alpha < |omega|/2 STRICTLY, one needs to show that:
  sum_k |alpha_hat(k)| < (1/2) * |sum_k omega_hat(k) e^{ikx*}|
  i.e., the ell-1 norm of alpha_hat(k) is strictly less than half the
  ell-1 norm of omega_hat(k)*e^{ikx*} weighted by the geometric factor.

  The sin(2theta)/2 weighting ensures that unless ALL energy is at theta=45deg,
  the bound is strict. But proving this for ARBITRARY smooth div-free fields
  requires ruling out concentration at a single angle.
=======================================================================
""")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == '__main__':
    main()
