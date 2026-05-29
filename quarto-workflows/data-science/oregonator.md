---
title: "The Oscillatory Chemical Reactions"
date: "2026-5-6" 
---
[![](https://colab.research.google.com/assets/colab-badge.svg)](pyfile/oregonator.py)


# Oscillating Reactions

It should be clear by now that chemical kinetics is governed by the mathematics of systems of differential equations. Thus far, we have only looked at reaction systems that give rise to purely _linear_ differential equations, however, in many instances the rate equations are nonlinear. When the differential equations are nonlinear, the behaviour is considerably more complex. In particular, nonlinear equations can lead to oscillatory solutions and can also exhibit the phenomenon of _chaos_.

## Belousov-Zhabotinsky reaction
[Boris Belousov](https://en.wikipedia.org/wiki/Boris_Belousov_(chemist)) in the 1950's discovered that a mixture of malonic acid, potassium bromate, and cerium sulfate an acidic aqueous mixture in a batch reactor did not react directly to equilibrium. Instead, the composition and color of the solution oscillated for a significant period. His reports of this work were rejected by peer-reviewed journals becuase reviewers felt than an oscillating chemical reaction violates thermodynamic equilibrium and, thus, was not possible.

>The discovery of oscillating reactions revolutionized teh way taht scientist thought about chemical dynamics. Indeed, Ilya Prigogine who received the 1977 Nobel Prize in Chemistry, in part for demonstrating that chemical systems far from equilibrium can exhibit periodic oscillations, regarded the the Balousov-Zhabotinsky (BZ) reaction as the most important scientific discovery of the twentieth century, that the discovery of a "simple" chemical reaction that displays periodic temporal and spatial behaviour had far-reaching consequenches, even leading to a greater understanding of the processes that underlie life itself, such as biological clocks and morphogenesis.

Field, Koros and Noyes at the University of Oregon in the 1970's developed kinetic models of the reaction that were able to explain much of the experimental behaviour. The original model was the FKN model:


[![](http://www.scholarpedia.org/w/images/thumb/4/48/Table1.jpg/700px-Table1.jpg)](http://www.scholarpedia.org/article/File:Table1.jpg)


The actual Belousov-Zhabotinskii reaction is complex, involving many individual steps, and involves the oscillation between the concentration of $HBrO_2$ and $Br^{-}$. This kinetic model was "reduced" (simplified while retaining major behavior) to the Oregonator model:

$$\begin{align} k_1 &: A + Y \quad \rightarrow X + P \\ k_2 &: X + Y \quad \rightarrow 2P \\ k_3 &: A + X \quad \rightarrow 2X + 2Z \\ k_4 &: 2X \quad \quad \rightarrow A + P \\ k_5 &: B + Z \quad \rightarrow \frac{1}{2} fY \end{align}$$

Where, $X = HBrO_2, \ Y = Br^{-}, \ Z = Ce(IV), \ A = BrO_3^{-}, \ B = CH_2(COOH)_2$, and $ P=HOBr$ or $BrCH(COOH)_2$. $P$ represents the product species.

## Oregonator
In addition to color changes, selective electrodes can be used to measure ion concentrations. Note the "induction period" before the oscillations start, due partially to bromination of malonic acid. The oscillations eventually die out as the system approaches equilibrium. Field, Koros and Noyes at the University of Oregon in the 1970's developed kinetic models of the raction that were able to explain much of the experimental behavior. This kinetic model is known as the _Oregonator_. The Oregonator Mass-Action dynamics in a well-stirred, homogeneous system is given by Eqs.(1)-(3).

### Dynamics Equations
The Oregonator Mass-Action dynamics in a well-stirred, homogenenous systems is given by Eqs. (1)-(3).

$$\begin{align} \frac{d[X]}{dt} &= k_1 [A][Y] - k_2 [X][Y] + k_3 [A][X] - 2k_4 [X]^2 \tag{1} \\ \frac{d[Y]}{dt} &= -k_1 [A][Y] - k_2 [X][Y] + \frac{1}{2} fk_5 [B][Z] \tag{2} \\ \frac{d[Z]}{dt} &= 2k_3 [A][X] - k_5[B][Z] \tag{3} \end{align}, $$

where the adjustable parameter, $f$, takes values in the range 0-3. ALtough we could go ahead and integrate these equations numerically, it is helpful to scale them dimensionless and reduce the number of constants:

$$\begin{align} \alpha \frac{dx}{d \tau} &= \gamma y - xy + x(1-x) \tag{4} \\ \beta \frac{dy}{d \tau} &= - \gamma y - xy + fz \tag{5} \\ \frac{dz}{d \tau} &= x -z \tag{6} \end{align}$$

The scaling relationships and parameters in Eqs. (4)-(6) are

$$\begin{align} x =\frac{2k_4[X]}{k_3[A]}, \ y =\frac{k_2 [Y]}{k_3 [A]}, \ z = \frac{k_4 k_5 [B][Z]}{(k_3 [A])^2} \end{align}$$

$$\begin{align} \alpha =\frac{k_5 [B]}{k_3 [A]}, \ \beta = \frac{2k_4 k_5 [B]}{k_2 k_3 [A]}, \ \gamma =\frac{2k_1 k_4}{k_2 k_3}\end{align}$$

as derived at the end of this chapter.

## Preliminaries
Scipy's `solve_ivp` function can be used to integrate the differential equations of the Oregonator model, given a set of initial conditions, which here we take to be $x=(0) \ y=(0) \ z =(0) \ = 1$.

## Exercise
The rate constant, $k_i$, used in the above model relate to the rates of paticular reaction steps in the full mechanism and depend on the solution pH through:

$$\begin{align} k_1 &=(2.1 \ M^{-3} \ s^{-1}) [H^{+}]^{2} \\ k_2 &= (3 \times 10^{6} \ M^{-2} \ s^{-1}) [H^{+}] \\ k_3 &= (42 \ M^{-2} \ s^{-1}) [H^{+}] \\ k_4 &= (3000 \ M^{-2} \ s^{-1}) [H^{+}] \end{align}$$ 

The values of $k_1 - k_4$ are calculated from the values of $k_{R2}, \ k_{R3}, \ K_{R4}$ and $k_{R5}$ in Table 1 with $[H^+] = 0.8 \ M$. 

The reactant concentration (which we assume to be constant over the few cycles of the raction studied here) are taken to be [A] = 0.006 M and [B] = 0.02 M.

The following code performs numerical integration of Field-Noyex equations (4-6) using `scipy.integrate.solve_ivp` with initial condition are $x_0 = y_0 \ = z_0 \ = 1$.

```Python
# set environment
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
```

```Python
# Calculate oregonator
def deriv(tau, X, alpha, beta, gamma, f):
    """ Return the derivatives dx/dtau, dy/dtau, and dz/dtau"""

    x, y, z = X
    dxdtau = (gamma*y - x*y + x*(1-x)) /alpha
    dydtau = (-gamma*y - x*y + f*z) /beta
    dzdtau = x - z
    return dxdtau, dydtau, dzdtau
```

```Python
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
```

```Python
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
```

![Figure. Scaled Concentrations of $HBrO_2$, $Br^-$, and $Ce^{4+}$ as a function of the scaled time coordinate, $\tau$, for stoichiomteric parameter, $f=1$](/quarto-workflows/images/oregonator.svg)

The figure above shows the three ODEs and integration from specified parameters [A] = 0.06 M and [B] = 0.02 M and initial conditions $x_0 = y_0 \ = z_0 \ = 1$.

## Conclusion
- The mechanism for the Oregonator model was obtained as a result of "reducing" the 10-step Field, Koros, Noyes (FKN) mecahnism to a 5-step mechanism. It is essential for undertanding how complex (chaos), non linear systems chemical reactions.
- The reduction was done by methods of chemical kinetics, steady state approximation and partial equilibrium approximation.

## Reference
[1] [R.J.Field, E.Koros, R.M. Noyes, _J.AM.Chem.Soc_. __94__, 8649 (1972)](https://doi.org/10.1021/ja00780a001)

[2] [R.J. Field, "Oregonator", Scholarpedia, __2__(5): 1386 (2007)](http://www.scholarpedia.org/article/Oregonator)

