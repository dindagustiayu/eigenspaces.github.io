---
title: "Brusselator"
date: "2026-6-20" 
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](/pyfile/brusselator.py/)


# Mathematical Modelling of the Brusselator

The Brusselator is a model for predicting oscillations in chemcial reations under some conditions. As we progress, various models have been used to represent natural phenomenon. In classical thermodynamics, we model phenomena through simple linear equations. However, in the recent past, it is common to represent nature by non-linear equations. There are four laws that dominate traditional tehrmodynamics, which still hold true today [1]:

- Zeroth Law: If two thermodynamics systems are each in thermal equilibrium with a third, then they are in thermal equlibrium with each other.
  
- First Law: When a system undergoes a transformation of state, the algrebraic sum of the different energy changes, heat exchanged, work done, is independent of the manner of the transformation. It depends only on the initial and final states of the transformation.

- Second Law: The total entropy of any isolated thermodynamics system tends to increase over time, approaching a maxium value.

- Third Law: As temperature approaches absolute zero, the entropy of a system approaches a constant minimum.

With a basic grounding in these four laws, one can begin to delve deeper into thermodynamics. The fundamentals of thermodynamics came about in very unique methods, trials, thought, experiments, and physical experiments. However, now there is another method to describe natural phenomenon - Brusselator.

## Why Brusselator is important?

It is well known that reaction and diffusion of chemical or biochemical species can produce a variety of spatial patterns. This class of reaction diffusion systems includes some significant pattern formation equations arising from the modelling of kinetics of chemical or biochemical reactions and from the biological pattern formation theory. For this reason, the Brusselator is typicaly important and serves as mathematical model in physical chemistry and in biology. Nonlinear reaction-diffusion equations and systems play an important role in the modelling and study of many phenomena [2].

Brusselator model is a famous model of chemical reactions with oscillations and a theoritical model for a type of auto-catalytic reaction. In particular the Brusselator model consists of four reactions involving six-components A, B, D, E, X, Y where the chemical reactions follow the scheme (Table 1.)

Table 1. Mechanism of Brusselator

| Brusselator Model | Description|
| --- | --- |
| $A \rightarrow X \quad (1)$ | Species A makes species X |
| $B + X \rightarrow Y + D \quad (2)$ | Species X makes species Y. (Actication)|
| $2X + Y \rightarrow 3X \quad (3) $| Species Y makes species X. (Activation) |
| $X \rightarrow E \quad (4)$| Species X makes species E. (Inactivatio)|


Adding these reactions one obtains
$$ A +B + 4X + Y \rightarrow 4X + Y + D + E \tag{5}$$

and hence $A +B \rightarrow D +E$, $X$ and $Y$ are catalysis (in particular, X is auto-catalytic and provides the nonlinearity). 

The concentrations $[X]$ and $[Y]$ come from an infinite supply in this reaction scheme. The variable $k_i$ is reresented in units of $\left(\frac{mole}{l \ s} \right)^{-1}$. The equations for the evolution of $[X]$ and [Y]$ are as follows:

$$\begin{align} \frac{d[X]}{dt} &= k_1[A] - k_2[B][X] + k_3[X]^{2}[Y] -k_4[X] \tag{6} \\ \frac{d[Y]}{dt} &= k_2[B][X] -k_3[X]^2[Y] \tag{7} \\ [X](0) &= 0 \tag{8} \\ [Y](0) &=0 \end{align}$$

There are severl known examples of auto-catalysis which can be modeled by the Brusselator equations, such as ferrocyanide-iodate-sulphite reaction, chlorite-iodite-malonic acid reaction, arsenite-iodate reaction, some enzyme catalytic reactions and fungal mycelia growth.

## Preliminaries
Scipy's `solve_ivp` function can be used to integrate the differential equations of the Oregonator model, given a set of initial conditions, which here we take to be $x=(0) \ y=(0) \ z =(0) \ = 1$.

## Exercise
Obtain expression for the constants $p, \ q \ \mbox{and} \ r$ that scale the time variable and intermediate concentrations into the non-dimensional form: $x=p[X], \ y=q[Y]$ and $\tau = r t$. By solving the pair of differential equations, plot $x$ and $y$ as a function of $\tau$ using the initial conditions $(x_0, \ y_0) = (0, \ 0)$ for reactant concentrations(a) $(a, \ b) = (1, \ 0.7)$, (b) $(a, \ b) = (1, \ 1.8)$, and (c) $(a, \ b) = (1, \ 2.05)$. For each solution, also plot the phase space plot (the curve of $y$ againts $x$).

## Solution

1. We must solve for $[X]$ and $[Y]$ in the equation (5-6). Replacing the $x =p[X]$, $y=q[Y]$, and $\tau = r t$.

$$\begin{align} \frac{r}{p} \frac{dx}{d\tau} &= k_1 [A] + \frac{k_2}{p^2 q} x^2 y - \frac{k_3 [B]}{p} x - \frac{k_4}{p} x \tag{9} \\ \frac{r}{q} \frac{dy}{d \tau} &= -\frac{k_2}{p^2 q} x^2 y + \frac{k_3 [B]}{p} x \tag{10} \end{align}$$

Rearranging,

$$\begin{align} \frac{dx}{d \tau} &= \frac{pk_1 [A]}{r} + \frac{k_2}{pqr} x^2 y - \frac{1}{r} (k_3[B] + k_4) x \tag{11} \\ \frac{dy}{d \tau} &= - \frac{k_2}{p^2 r} x^2 y + \frac{k_3 [B]q}{pr} x \tag{12} \end{align}$$

2. Choosing $k_4/r = 1$ and $pk_1[A]/r=1$ fixes $r=k_4$ and $p=k_4/(k_1[A])$. It would be nice if the factors involving $[B]$ were the same. We can define

$$b=\frac{k_3 [B]}{r} = \frac{k_3[B]q}{pr} \Rightarrow \ q =p=\frac{k_4}{k_1[A]} \tag{13}$$

which leaves

$$a =\frac{k_2}{p^2 r} = \frac{k_2}{pqr} = \frac{k_1^{2} k_2[A]^{2}}{k_4^3} \tag{14}$$

Therefore,
$$\begin{align} \frac{dx}{d \tau} &= 1 + ax^2 y - (b+1)x \tag{15} \\ \frac{dy}{d \tau} &= -ax^2y + bx \tag{16} \end{align}$$

```Python
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
```

3. The system has a single _fixed point_: the pair of values ($x_{*}, \ y_{*}$) that remain unchanged in time under these differential equations, show that $x_{*} = 1$ and $y_{*}=b/a$. Then it must be the case that:

$$\begin{align} \frac{dx}{d \tau} &= 0 = 1 + a_*^{2} y_{*} - (b +1)x_* \\ \frac{dy}{d \tau} &= 0 = -ax_*^{2} y_* + bx_{*} \end{align}$$

This pair of equations are readily solved to yield $x_*=1$, $y_*=b/a$.

```Python
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
```

For each solution, also plot the phase space plot (the curve of $y$ againts $x$).

```Python
fig, axes = plt.subplots(nrows =3, ncols = 2, figsize=(6, 8))
# Plot the Brusselator solutions for different reactant concentrations, a and b.

plot_brusselator(1, 0.7, 0, axes)
plot_brusselator(1, 1.8, 1, axes)
plot_brusselator(1, 2.05, 2, axes)

fig.tight_layout()
plt.savefig("brusselator.svg")
plt.show()
```
![Figure. The Brusselator model for different reactant concentrations (a, b). Left column: time evolutiion of the scaled intermediate consentration $x(\tau)$ and $y(\tau)$. Right column: phase potraits ($y \ vs \ x$)](/quarto-workflows/images/brusselator.svg)

- When b is small, the system settles down to a stable steady state (no oscillation).
- when b is large, the system oscillates forever in a repeating cycle (limit cycle).
- The phase portrait show whether the system spirals inward (stable) or goes in a closed loop (oscillating).


## Conclusion

As it turns out, for ($a,\ b) = (1, \ 0.7$) and ($1, \ 1.8$), the Brusselator is stable and the intermediate concentrations converge on the fixed point ($x_*, \ y_*) = (1, \ b/a$). For ($a, \ b) = (1, \ 2.05$), the intermediate concentrations enter a _limit cycle_.


## Reference

[[1] Mathematical Modelling of the Brusselator by Matthew P.McDowell 2008](https://academicweb.nd.edu/~powers/mcdowell.pdf)

[ [2] Influence of Diffusion on the Stability of a Full Brusselator model 2018](https://ems.press/content/serial-article-files/39950)