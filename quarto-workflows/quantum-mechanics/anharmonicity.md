[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/The-Morse-Oscillator/blob/main/Vibrational%20levels.html)

# Vibrational Anharmonicity

## Beyond The Harmonic Oscillator
Let's now consider two ways in which the vibrational structure of "real molecules" is more complicated than what we've seen for the harmonic oscillator. 

## Anharmonicity
First, real vibrational motions involve "anharmonicity", e.g., Their potential deviates from a perfect harmonic oscillator quadratic potential energy surfaces. We've already touched on this by looking at the Morse Potential.
<p align='center'>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Morse-potential.svg/960px-Morse-potential.svg.png" alt="figure" width="400"/>
</p>

<p align='center'>
    $$\mbox{Figure.The Morse Potential (blue) and harmonic oscillator potential (green)}$$
</p>

The harmonic oscillator is a reasonable approximation of this potential near the equilibrium geometry, but deviates substantially for $x$ far from the center of the well. Correspondingly, the vibrational levels of the Morse potential will deviate from those of the HO model. Note that the Morse potential levels grow closer together as energy increases.

## Limitations of the Harmonic Oscillator Model for Molecular Vibrations
The harmonic oscillation is a great approximation of a molecular vibration, but has key limitations:
- Due to equal spacing of energy, all transitions occur at the _same_ frequency (i.e., single line spectrum). However, experimentally, many lines are often observed (called overtones).
- The harmonic oscillator does not predict bond dissociation, you cannot break it, no matter how much energy is introduced.

# Morse Oscillator Breakdown
The Morse oscillator, named after physicist [Philip M. Morse](https://www.nae.edu/28848/Dr-Philip-M-Morse) is a better approximation for the vibrational structure of the molecule than the harmonic oscillator because it explicitly includes

The Morse oscillator is a model for a particle in a one-dimensional anharmonic potential energy surface with a dissociative limit at infinite displacement. It is commonly used for describing the spectroscopy of diatomic molecules and anharmonic vibrational dynamics, and most of its properties can be expressed through analytically expressions. The Morse potential is

<p align='center'>
    $$V(x) = D_e[1-e^{-\alpha x}]^2 \quad (1)$$
</p>

where $x = (r - r_0)$, $D_e$ sets the depth of the energy minimu at $r=r_0$ relative to the dissociation limit as $r \rightarrow \infty$, and $\alpha$ sets the curvature of the potential. If we expand $V$ in powers of $x$ about $x=0$, the parameter $\alpha = \sqrt{k_e /2D_e}$ and $k_e = \left(\frac{d^2 V}{dx^2} \right)_e$ is the bond force constant at the bottom of the potential well.

The Morse oscillator Hamiltonian for a diatomic molecule of reduced mass _mR_ bound by the potential is

<p align='center'>
    $$H = \frac{p^2}{2m_R} + V(x)$$
</p>

and has the eigenvalues
<p align='center'>
    $$E_n = \hbar \omega_0 \left[\left(n + \frac{1}{2} \right) - x_e \left(n + \frac{1}{2} \right)^2 \right] \quad n =0, \ 1, 2, \ 3, \ldots \quad (2)$$
</p>

where
- $v$ is vibrational quantum number.
- $\omega_0 = \sqrt{2 D_e \alpha^2 / m_R}$ is the fundamental frequency.
- $x_e = \frac{\hbar \omega_0}{4 D_e}$ is the harmonic constant.
- The frequency $\omega_0$ is equivalent to equating the harmonic for constant $\mathcal{K} = (\partial^2 V/ \partial x^2)_{x=0}$ with $m_R \omega_0^2$.

The harmonic oscillator approximation is convenient to use for diatomic molecules with quantized vibrational energy levels given by the following equation:
<p align='center'>
    $$E_n=v = \left ( v + \frac{1}{2} \right) \omega_e$$
</p>

The new energy levels of this _anharmonic_ potential can be found using _perturbation theory_. We will just write down the result here that we find higher-order corrections to the energy according to:

<p align ='center'>
    $$G(v) = \omega_e \left(v + \frac{1}{2} \right) - \omega_e x_e \left( v + \frac{1}{2} \right)^2 + \omega_e y_e \left(v + \frac{1}{2} \right)^3 + \ldots \quad (3)$$
</p>

where $\omega_e$ is the anharmonic oscillator frequency, and $x_e$ is the _anharmonic constant_, which is typically much smaller than $\omega_e$.

While it may seem that the harmonic oscillator and the anharmonic oscillator are closely related, this is in fact not the case. The difference in the wavefunctions leads to a breakdown of selection rules, specifically, $\Delta n = \pm 1$ selection rule can not be applied, and higher order terms must be accounted in the energy calculations. 

On the other note is that anharmonicity also changes the selection rules for IR transitions. For absorption of IR light, we can now have:
<p align='center'>
    $$\Delta v = +1, \ +2, \ +3, + \ldots$$
</p>

where $\Delta n = +1$ are _fundamental transition_ and $\Delta n = +2, \ +3, + \ldots$ are called _overtones_, and can occur but are much weaker in intensity than the _fundamental_. Overtone transitions are not always observed, especially in larger molecules, because the transitions become weaker with increasing $Delta n$.

## Overtones
Based on the harmonic oscillator approximation, the energy of the overtone transition would be $n$ times larger than the energy of the fundamental transition frequency, but the _anharmonic oscillator_ calculations show that the overtones are less than a multiple of the fundamental frequency. This is demonstrated with the vibration of the diatomic in the gas phase:

<p align='center'>
    $\mbox{Table 1. HCl vibrational spectrum}$
</p>

<div align='center'>
  
|Transition | Term | $v_{obs} \ [cm^{-1}]$ | $v_{Harmonic} \ [cm^{-1}]$| $v_{Anharmonic} \ [cm^{-1}]$ |
|:-----------:|:------:|:---------------------:|:-------------------------:|:----------------------------:|
| $0 \rightarrow 1$ | fundamental | 2,885.9 | 2,885.9 | 2,885.3 |
| $0 \rightarrow 2$ | first overtone | 5,668.0 | 5,771.8 | 5,665.0 |
| $0 \rightarrow 3$ | second overtone | 8,347.0 | 8,657.7 | 8,339.0|
| $0 \rightarrow 4$ | third overtone | 10,923.1 | 11,543.6 | 10,907. 4|
| $0 \rightarrow 4$| fourth overtone | 13,396.5 | 14,429.5 | 13,370|

</div>

We can see from Table 1, that the anharmonic frequencies correspond much better with the observed frequencies, especially as the vibrational levels increase.

## The Morse oscillator $Schr\ddot{o} dinger$ equation

Solving the $Schr\ddot{o}dinger$ with the Morse oscillator is not trivial, but can be done analytically in terms of associated __Laguerre polynomials__.

<p align='center'>
    $$\psi (n) = N_n z^{\lambda - n - \frac{1}{2}} e^{-z / 2} L_n^{2 \lambda - 2n - 1} (z) \quad [in \ cm^{-1}] \quad (4)$$
</p>

where 
- $N_n = \sqrt{\frac{n!(2\lambda - 2n - 1)a}{\Gamma (2 \lambda - n)}}, \quad \lambda = \frac{\sqrt{2mD_e}}{a\hbar}$ is normalization constant.
- $\mathcal{L}_n^(\alpha) = \frac{z^{- \alpha} e^z}{v !} \ \frac{d^n}{dz^n} (z^{n + \alpha} e^{-z}), \quad z= 2\lambda e^{-x}$ is a _generalized Laguerre Polynomial_.
- $n = 0, \ 1, \ 2, \ 3, \ldots, \left[ \lambda - \frac{1}{2} \right]$

## Preliminaries
`scipy.constants`: is the package provides the internationally agreed standard values and uncertainties for physical constants include a large number of algorithms for calculating functions that appear in science.

<p align='center'>
    $$\mbox{Table 1. Physical constants} \ \mathtt{scipy.constant}$$
</p>

<div align='center'>

|Constant string | Variable | Value | Units |
|--------------|:--------:|-----|-----|
|Planck constant| h | 6.62606957e-34 | J s |
|Speed of light in vacuum | c | 299792458.0 | m s-1 |
|Avogadro constant | N_A | 6.02214129E+23 | mol-1|
|Atomic mass | u | 1.6605390666e-27 | kg |
    
</div>


The code below defines the class Morse representing a Morse oscillator, which can be used to generate depictions of the wavefunctions and energy levels as given in the example for $HCl$.

## E24.1 Inferring Morse Parameters from a vibrational spectrum
The vibrational spectrum of the $HCl$ molecule shows a fundamental band at $2,885.9 \ cm^{-1}$ and the first overtone band at $5,668.0$. This information can be used to estimate the Morse parameters, $D_e$ and $\alpha$, and hence the good strength and maximum vibrational level.

__Solution__:
1. Observe bands to estimate the parameters $\omega_e$ and $\omega_e x_e$. The fundamental vibrational band, corresponding to the transition $v = 0 \rightarrow 1$, occurs at a wavenumber given by
   
<p align='center'>
    $$v_{0 \rightarrow 1} = G(1) - G(0) = \omega_e - 2\omega_e x_e$$
</p>

_Overtone bands_, for which $\Delta > 1$ are predicted to be observed at wavenumber 

<p align='center'>
    $$v_{0 \rightarrow v} = G(v) - G(0) = \omega_e v - \omega_e x_e v(v+1)$$
</p>

The observed bands of HCl,

<p align='center'>
    $$\begin{align} v_{0 \rightarrow 1} &= \omega_e - 2 \omega_e x_e = 2885 \ cm^{-1}, \\ v_{0 \rightarrow 2} &= 2\omega_e - 6\omega_e x_e = 5668 \ cm^{-1} \end{align}$$
</p>

Therefore
<p align='center'>
    $$\begin{align} \omega_e x_e &= \frac{1}{2} (2 v_{0 \rightarrow 1} - v_{0 \rightarrow 2}), \\ \omega_e &= v_{0 \rightarrow 1} + 2 \omega_e x_e \end{align}$$
</p>

2. Compute the Morse oscillator model

<p align='center'>
    $$\begin{align} D_e &=\frac{\omega^2}{4 \omega_e x_e} \ \mbox{and} \\ \alpha &=2 \pi c \omega_e \sqrt{\frac{\mu}{2 D_e}} \end{align}$$
</p>

where $\mu$ is the reduced mass of the molecule.

4. Calculate the bond strength from the ground state.
From eq.1 the ground state (or zero-point) energy is

<p align='center'>
    $$ E_0 = \frac{1}{2} \hbar \omega_0 (1 - \frac{1}{2} x_e)$$
</p>

So the dissociation energy for the Morse potential is given by $D_0 = D_e - E_0$. The transition energies are
<p align='center'>
    $$E_n - E_m = \hbar \omega_0 (n - m) \left[1 - x_e \left(n + m + \frac{1}{2} \right) \right]$$
</p>

The proper harmonic expressions are obtained from the above for the Morse oscillator by setting $D_e \rightarrow \infty$ or $x_e \rightarrow 0$.

5. Calculate the highest energy level ($v_{max}$)

The vibrational energy levels converge with increasing quantum number, $v$, the highest energy level, $v_max$ is given by the condition
<p align='center'>
    $$\begin{align} \frac{d G(v)}{dv} & = 0 \\ \omega_e - 2 \omega_e x_e(v_{max} + \frac{1}{2}) & =0 \\ v_{max} &=\frac{\omega_e}{2 \omega_e x_e} - \frac{1}{2} \end{align}$$
</p>

6. Plotting the Morse oscillator potential.

```Python
# 1. The parameter we and wexe
nu_0_1, nu_0_2 = 2885, 5668
wexe = (2 * nu_0_1 - nu_0_2) / 2
we = nu_0_1 + 2 * wexe

print(f'we = {we} cm-1, wexe = {wexe} cm^-1')
```
```
we = 2987.0 cm-1, wexe = 51.0 cm^-1
```

```Python
# 2. Compute the Morse oscillator model
import numpy as np
from scipy.constants import h, c, N_A, u
import matplotlib.pyplot as plt

# Dissociation energy measured from the potential minimum, cm-1
De = we**2 / 4 / wexe

# Reduced mass of (1H) (35.5Cl)
mu = 1 * 35.5 / (1 + 35.5) * u

# Compute everything to SI units in calculating a: De / J = hc.De / cm-1
a = 2 * np.pi * (c * 100) * we * np.sqrt(mu / 2 / (De * h * (c * 100)))

# Convert a from m-1 to A-1
a *= 1.e-10

print(f'De = {De:.0f} cm-1, a = {a:.1f} A-1')
```
```
De = 43736 cm-1, a = 1.7 A-1
```

The Morse parameter, $D_e$, is the dissociation energy measured from the potential minimum. The bond strength is the energy required to dissociate the molecule from its ground state ($v =0$, with energy $G(0) = \frac{1}{2} \omega_e - \frac{1}{4} \omega_e x_e)$.

```Python
E0 = we / 2 - wexe / 4
D0 = De - E0

# Convert dissociation energy, D0, to kj.mol-1
bond_strength = D0 * h * (c * 100) * N_A / 1000
print(f' CO bond strength = {bond_strength:.0f} kj.mol-1')
```
```
CO bond strength = 505 kj.mol-1
```

```Python
# Calculate the highest energy level ($v_{max}$)

vmax = int(we / 2 / wexe - 0.5)
print(f'vmax = {vmax}')
```
```
vmax = 28
```

To plot the potential energy curve and energy levels, create an array of bind displacement, $x= r - r_e$ and use the Morse oscillator formula $V(x)$:

```Python
# 6.  Plotting the Morse oscillator potential.

# Grid of bond displacement values, x = r - re, in Angstrom.
x = np.linspace(-2, 6, 3000)

# Morse Oscillator potential
V = De * (1 - np.exp(-a*x))**2

# Plot the Morse Oscillator
plt.plot(x, V)
plt.xlabel(r'$(r - r_e) \ \mathrm{\AA}$')
plt.ylabel(r'$D_e  \ cm^{-1}$')
plt.ylim(0, De)
plt.title("Morse Oscillator Potential with Vibrational Levels of HCl")

# Arrays of vibrational quantum number nd corresponding energy.
v = np.arange(0, vmax+1, 1, dtype=int)
Ev = np.array([we * (v+0.5) - wexe * (v + 0.5)**2])

# Classical turning points
xm = - np.log(1 + np.sqrt(Ev / De)) / a
xp = - np.log(1 - np.sqrt(Ev/ De)) / a

# Plot the energy level as horizontal lines between xm and xp at Ev
plt.savefig('Morse Oscillator Potential with Vibrational Levels.svg', bbox_inches='tight')
plt.hlines(Ev, xm, xp)
```
<div align='center'>
    <img src="https://github.com/dindagustiayu/The-Morse-Oscillator/blob/main/Morse%20Oscillator%20Potential%20with%20Vibrational%20Levels%20of%20HCl.svg">
</div>

# Conclusion
- The Morse oscillator is a bridge of the gap between idealized theory and real molecular behavior.
- Understanding vibrational spectroscopy, chemical bonding, and molecular dissociation is very important.
