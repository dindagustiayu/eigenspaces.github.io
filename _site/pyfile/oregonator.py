# set environment
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# Calculate oregonator
def deriv(tau, X, alpha, beta, gamma, f):
    """ Return the derivatives dx/dtau, dy/dtau, and dz/dtau"""

    x, y, z = X
    dxdtau = (gamma*y - x*y + x*(1-x)) /alpha
    dydtau = (-gamma*y - x*y + f*z) /beta
    dzdtau = x - z
    return dxdtau, dydtau, dzdtau

# Substitute reactant concentrations A = 0.06 M, B = 0.02 M
def solve_oregonator(Hp= 0.8, f=1, A=0.06, B=0.02):
    """Integrate the Oregonator differential equations.

    Hp is the H+ concentration in M, f the stoichiometric parameter and A and B the constant reactant concentrations.

    """

    kp1, kp2, kp3, kp4 = 2.1, 3e6, 42, 3e3
    k1, k2, k3, k4 = kp1 * Hp**2, kp2 * Hp, kp3 * Hp, kp4 * Hp
    k5 = 1
    alpha = k5 * B / k3 / A
    beta = 2 * k4 * k5 * B /k2 /k3 / A
    gamma = 2 * k1 * k4 / k2 / k3

    # Initial and final (scaled) times for the integration.
    tau_i, tau_f = 0, 40

    # Initial conditions, x(0), y(0), z(0).
    x0 = (1, 1, 1)

    # Solve the differential equations, using the Radau method and
    # implicit Runge-Kutta algorithm suited to stiff ODEs
    soln = solve_ivp(deriv, (tau_i, tau_f), x0, dense_output=True, 
                     args = (alpha, beta, gamma, f), method='Radau')

    # Interpolate the solution onto a suitable grid of (scaled) times.
    tau = np.linspace(tau_i, tau_f, 10000)
    x, y, z = soln.sol(tau)
    return tau, x, y, z

# Plotting
def plot_oregonator(tau, x, y, z):
    """ Plot the scaled concentrations, x(tau), y(tau) and z(tau)"""

    fig, axes = plt.subplots(nrows=3, ncols=1)
    axes[0].plot(tau, np.log10(x), 'k')
    axes[1].plot(tau, np.log10(y), 'b')
    axes[2].plot(tau, np.log10(z), 'r', ls='--')
    axes[0].set_xticklabels([])
    axes[1].set_xticklabels([])
    axes[0].set_ylabel(r'$\log_{10} (x) \ (\mathrm{HBrO_2})$')
    axes[1].set_ylabel(r'$\log_{10} (y) \ (\mathrm{Br^-})$')
    axes[2].set_ylabel(r'$\log_{10} (z) \ (\mathrm{Ce^{4+}})$')
    axes[2].set_xlabel(r'scaled time, $\tau$')

tau, x, y, z = solve_oregonator(Hp=0.8, f=1)
plt.savefig("oregonator.svg", bbox_inches = 'tight')
plot_oregonator(tau, x, y, z)