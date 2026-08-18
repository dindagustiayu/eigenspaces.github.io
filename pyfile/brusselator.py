# Parameters
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

def deriv(t, X, a, b):
    """return the derivatives dx/dtau and dy/dtau"""
    x, y = X
    dxdtau = 1 + a* x**2 *y - (b+1)*x
    dydtau = -a *x**2 *y + b*x
    return dxdtau, dydtau

def plot_brusselator(a, b, irow, axes): #set functions a, b are reactant concentrations, irow is the 2D array of matplotlib
    """
    Integrate the Brusselator equations for reactant concentrations a, b
    and plot on the row indexed at irow of the figure axes.
    """
    #Initial and final (scaled) time points
    taui, tauf = 0, 100

    #intitial (scaled) concentrations of the intermediates.
    x0, y0 = 0, 0

    # Solving the Oder Differential Equation
    soln = solve_ivp(deriv, (taui, tauf), (x0, y0), dense_output =True, args=(a, b))

    tau = np.linspace(taui, tauf, 1000)
    x, y = soln.sol(tau)

    # time series -left plot
    axes[irow][0].plot(tau, x, lw=1)
    axes[irow][0].plot(tau, y, lw=1)
    axes[irow][0].legend((r'$x$', r'$y$'), loc='upper right')
    axes[irow][0].set_xlabel(r'$\tau$')
    text_hpos = (tauf -taui) /2

    axes[irow][0].text(text_hpos, 0.1, f'$a={a}, b={b}$', ha='center')
    # phase portrait shape spiral, limit or cycle (right plot)
    axes[irow][1].plot(x, y, lw =1)
    axes[irow][1].set_xlabel(r'$x$')
    axes[irow][1].set_ylabel(r'$y$')

fig, axes = plt.subplots(nrows =3, ncols = 2, figsize=(6, 8))
# Plot the Brusselator solutions for different reactant concentrations, a and b.

plot_brusselator(1, 0.7, 0, axes)
plot_brusselator(1, 1.8, 1, axes)
plot_brusselator(1, 2.05, 2, axes)

fig.tight_layout()
plt.savefig("brusselator.svg")
plt.show()