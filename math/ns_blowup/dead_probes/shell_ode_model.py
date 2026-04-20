"""
Shell ODE Model — Does θ₀ < 1 prevent blowup?

Simulates the Littlewood-Paley shell enstrophy balance:

  dE_j/dt = -ν 4^j E_j + θ₀ C 2^{3j/2} E_j^{3/2}
            + C 2^j [√(E_{j-1} E_j) + √(E_j E_{j+1})]

with initial data E_j(0) = A 2^{-2sj} (smooth data, s > 0).

Tests:
1. θ₀ = 1 (no depletion): does it blow up?
2. θ₀ = 2/3 (our Schur bound): does it stay bounded?
3. θ₀ = 0 (perfect depletion): definitely bounded?
4. Sweep θ₀ from 0 to 1: where is the transition?

If blowup with θ₀ = 1 but bounded with θ₀ = 2/3, the depletion
is the critical ingredient.
"""
import numpy as np
from scipy.integrate import solve_ivp
import sys

def shell_ode(t, E, nu, C, theta0, n_shells):
    """RHS of shell enstrophy balance ODE."""
    dEdt = np.zeros(n_shells)
    for j in range(n_shells):
        # Viscous damping
        dEdt[j] = -nu * 4**j * E[j]

        # Diagonal (intra-shell) transfer with depletion
        dEdt[j] += theta0 * C * 2**(3*j/2) * E[j]**1.5

        # Off-diagonal (inter-shell) transfer
        if j > 0:
            dEdt[j] += C * 2**j * np.sqrt(max(0, E[j-1]) * max(0, E[j]))
        if j < n_shells - 1:
            dEdt[j] += C * 2**j * np.sqrt(max(0, E[j]) * max(0, E[j+1]))

    return dEdt


def run_shell_model(theta0, nu=1e-4, C=1.0, n_shells=12, A=10.0, s=1.0,
                    T_max=10.0, label=""):
    """Run the shell model and return max enstrophy over time."""
    # Initial data: E_j(0) = A × 2^{-2sj}
    E0 = np.array([A * 2**(-2*s*j) for j in range(n_shells)])

    # Total initial enstrophy
    Omega0 = E0.sum()

    def rhs(t, E):
        return shell_ode(t, np.maximum(E, 0), nu, C, theta0, n_shells)

    # Event: detect blowup (enstrophy > 1e10)
    def blowup_event(t, E):
        return 1e10 - np.sum(np.maximum(E, 0))
    blowup_event.terminal = True

    sol = solve_ivp(rhs, [0, T_max], E0, method='RK45',
                    max_step=0.001, events=blowup_event,
                    rtol=1e-8, atol=1e-12)

    total_enstrophy = np.sum(np.maximum(sol.y, 0), axis=0)
    max_enstrophy = np.max(total_enstrophy)
    blew_up = sol.t_events[0].size > 0

    if label:
        status = "BLOWUP" if blew_up else f"bounded (max={max_enstrophy:.2f})"
        t_end = sol.t_events[0][0] if blew_up else sol.t[-1]
        print(f"  θ₀={theta0:.3f}: {status} at t={t_end:.4f}")

    return max_enstrophy, blew_up, sol


def main():
    print("SHELL ODE MODEL — Does θ₀ < 1 prevent blowup?")
    print("="*60)

    # Parameters
    nu = 1e-4
    C = 1.0
    n_shells = 15
    A = 100.0  # large initial enstrophy
    s = 0.5  # moderate smoothness

    print(f"ν={nu}, C={C}, {n_shells} shells, A={A}, s={s}")
    print(f"Initial enstrophy: {sum(A * 2**(-2*s*j) for j in range(n_shells)):.1f}")
    print()

    # Test 1: θ₀ = 0 (no self-interaction)
    print("Test 1: θ₀ = 0 (no diagonal transfer)")
    run_shell_model(0.0, nu=nu, C=C, n_shells=n_shells, A=A, s=s, label="no diag")

    # Test 2: θ₀ = 2/3 (our bound)
    print("\nTest 2: θ₀ = 2/3 (Schur bound)")
    run_shell_model(2/3, nu=nu, C=C, n_shells=n_shells, A=A, s=s, label="Schur")

    # Test 3: θ₀ = 1 (no depletion)
    print("\nTest 3: θ₀ = 1 (no depletion)")
    run_shell_model(1.0, nu=nu, C=C, n_shells=n_shells, A=A, s=s, label="full")

    # Sweep θ₀ to find transition
    print(f"\n{'='*60}")
    print("SWEEP: θ₀ from 0 to 2")
    print(f"{'='*60}")
    for theta0 in [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 2/3, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.5, 2.0]:
        run_shell_model(theta0, nu=nu, C=C, n_shells=n_shells, A=A, s=s,
                       label=f"θ₀={theta0:.2f}")

    # Test with different initial conditions
    print(f"\n{'='*60}")
    print("INITIAL DATA SWEEP at θ₀ = 2/3")
    print(f"{'='*60}")
    for A_test in [1, 10, 100, 1000, 10000]:
        run_shell_model(2/3, nu=nu, C=C, n_shells=n_shells, A=A_test, s=s,
                       label=f"A={A_test}")

    # Test with different viscosity
    print(f"\n{'='*60}")
    print("VISCOSITY SWEEP at θ₀ = 2/3, A=100")
    print(f"{'='*60}")
    for nu_test in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        run_shell_model(2/3, nu=nu_test, C=C, n_shells=n_shells, A=100, s=s,
                       label=f"ν={nu_test:.0e}")

    # Critical test: does θ₀ = 2/3 ALWAYS prevent blowup?
    print(f"\n{'='*60}")
    print("STRESS TEST: θ₀ = 2/3, extreme parameters")
    print(f"{'='*60}")
    # Very large initial data, very small viscosity
    for A_test, nu_test in [(1e6, 1e-6), (1e4, 1e-8), (1e8, 1e-4)]:
        run_shell_model(2/3, nu=nu_test, C=C, n_shells=20, A=A_test, s=0.5,
                       T_max=1.0, label=f"A={A_test:.0e},ν={nu_test:.0e}")


if __name__ == '__main__':
    main()
