[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Quantum-Harmonic-Oscillator/blob/main/Integral%20QHO.py)

# Quantum Harmonic Oscillator (QHO)
In Quantum Mechanics, the harmonic oscillator is an important pradigm because it provides a model for a variety of systems, such as the modes of the __electrodynamic field (photons)__ and __the vibrations of molecules and solids (phonons)__.

The Quantum Harmonic Oscillator (QHO) is a fundamental model in quantum mechanics, describing systems where a particle is subjected to a potential proportional to the square of its displacement from equilibrium. Examples include molecular vibrations and oscillations of atoms in a solid.

# Prior knowledge
- Classical Mechanics
- Quantum Fundamentals
- Mathematical Integration

# Preliminaries
- `scipy.integrate`: definite integrals.
- `dblquad`: double integrals.
- `tplquad`: triple integrals.
- `numpy.polynomial`: representing the cubic equation in n.

## Classical harmonic oscillator
The classical harmonic oscillator describes a particle subject to a restoring force $F=-m \omega^2 x$ proportional to the distance from an equilibrium position $x=0$. Newton's equation $m\ddot{x} = F$ results in an oscillatory motion $x(t)=x_0 \ cos \omega t + (v_0/ \omega) \ sin \omega t$, where $\omega = \frac{2 \pi}{T}$ and $T$ is the oscillation period. In this solution, $x_0 = x(0)$ is the initial position and $v_0 = \dot{x} (0)$ is the initial velocity of the particle. According to $F = -V^{'}$, the force $F = -m \omega^2 x$ corresponds to a parabolic potential energy.

The simple quantum harmonic oscillator is:
<p align= 'center'>
    $$ V(x) = \frac{1}{2} \times m \times \omega \times x^{2}$$
</p>

where,
- _m_ is the mass of the particle
- $\omega$ is the angular frequency of the oscillator
- _x_ is the displacement from equilibrium

## $Schr\ddot{o}dinger$ equation of the quantum harmonic oscillator

In order to solve this problem quantum mechanically, we follow our standard steps. The $schr\ddot{o}dinger$ equation of the harmonic oscillator is given by

<p align='center'>
    $$E \psi (x) = - \frac{\hbar}{2m} \psi^{"}(x) + \frac{1}{2} m \omega^2 x^2 \psi(x)$$
</p>

where,
- $\hbar$ is the reduced Planck's constant
- $\psi$ is the wavefunction
- $E$ is the energy of the state

This equation is again a linear differential equation of second order, but now one coefficient is position dependent. From our general considerations we already can anticipate the following:

- The solution $\psi(x)$ are continous.
- The deribatives $\psi'(x)$ of the solutions are also continious.
- As $V(x) \rightarrow \infty$ for $|x| \rightarrow \infty$, the particle cannot excape to infinity at finite energy $E$. This only permits bound states, which decay $\psi(x) \rightarrow 0$ as $|x| \rightarrow \infty$.
- The energies of the bound states are discrete (i.e., only at certain energies we can find valid solutions of the $schr\ddot{o}inger$ equation).
- The ground state energy $E_{0}$ will be larger than the classical minimal energy: $E_0 > 0$.

## Ground state and first excited state

The first two solutions correspond to the ground state and the first excited state of the harmonic oscillator:
 
__Ground state__: $n=0, \ f=1$, which gives to $f' = f^{"} = 0$. This is a solution when $\varepsilon \neq 2n + 1$ if $\epsilon =1 $, which corresponds to an energy $E_{0} = \frac{1}{2} \hbar \omega$. The wavefunction is given by:

<p align='center'>
    $$\psi_{0} (x)= c_{0} exp \left (-x^{2} \frac{m \omega}{2 \hbar} \right)$$
</p>

where $c_{0}$ can be determined from the normalisation condition,

<p align='center'>
    $$\int_{- \infty}^{\infty} |\psi (x)^{2}| \ dx = 1 $$
</p>

This gives $c_{0} = \left (\frac{m \omega}{\pi \hbar} \right)^{1/4}$.

## Normalisation of the ground state wavefunction

The ground state wave function of the harmonic oscillator provides us with a good occasion to practice once more the normalisation of the wavefunction. Since we want to interpret $| \psi_{0} (x)^{2} | = P (x)$ as the probability density for position, we require,

<p align='center'>
    $$\int_{- \infty}^{\infty} |\psi_{0} (x)^{2} | \ dx = 1$$
</p>

With $\psi_{0} (x) = c_{0} exp \left (-x^{2} \frac{m \omega}{2 \hbar} \right)$ this integral reads,

<p align='center'>
    $$ \int_{- \infty}^{\infty} c_{0}^{2} exp \left (-x^{2} \frac{m \omega}{\hbar} \right) \ dx$$
</p>

We use the standard integral $\int_{- \infty}^{\infty} exp(-ax^{2}) \ dx = \sqrt{\pi / a}$, where we set $a = \frac{m \omega}{\hbar}$:

<p align='center'>
    $$ \int_{- \infty}^{\infty} c_0^{2} exp \left(-x^{2} \frac{m \omega}{\hbar} \right) \ dx = c_0^{2} \sqrt{\frac{\pi \hbar}{m \omega}} = 1$$
</p>

The equations to 1 if $c_0 = \left(\frac{m \omega}{\pi \hbar} \right)^{1/4}$, in agreement with the value given in the previous section. 

This Python script illustrates the one-dimensional harmonic oscillator ground state wavefunction with the following parameters:

```Python
import numpy as np
from scipy.integrate import quad, dblquad, tplquad

def func(x):
    return np.exp(-x**2)

I, err = quad(func, -np.inf, np.inf)
c0 = 1 / np.sqrt(I)
print('I:', I)
print('c0:', c0)
```
```
I: 1.7724538509055159
c0: 0.7511255444649425
```

The probability density of the oscillator's position is given by $P_{0} (x) = | \psi_{0} (x)|^{2}$ and is non zero outside the classical turning points, $\neq \alpha^{- 1/2}$, a phenomenon known as tunneling. We will calculate the probability f tunneling for an oscillator in the state $\psi_{0}$. 

The wavefunction is symmetric about $x=0$, so the probability of tunneling is

<p align='center'>
    $$ \begin{align} P(x < -\alpha) + P(x > \alpha) &= 2P(x > \alpha) = 2 \sqrt{\frac{\alpha}{\pi}} \int_{\alpha^{-1/2}}^{\infty} exp(-\alpha x^{2}) \ dx \\ &= \frac{2}{\sqrt{\pi}} \int_{1}^{\infty} e^{-y^{2}} \ dy \end{align}$$
</p>

```Python
I, err = quad(func, 1, np.inf)
ptun = 2 / np.sqrt(np.pi) * I
print('I:', I)
print('Ptunneling:', ptun)
```
```
I: 0.13940279264033098
Ptunneling: 0.1572992070502851
```

## The Particle in a Box
The particle in a box is the simplest problem in element quantum mechanics, and as such is useful in more places than one can easily enumerate. For instance, the molecular orbital theory is explained easily in terms os particle in a box wavefunctions, easier tha using standard atomic orbitals.

Extending the (time-independent) $Schr\ddot{o}inger$ equation for a one-dimensional system,
<p align='center'>
    $$- \frac{\hbar^2}{2m} \ \frac{d^2 \psi (x)}{dx^2} + V(x)\psi (x) = E \psi (x)$$
</p>

to a two dimensional system is:
<p align='center'>
    $$-\frac{\hbar^2}{2m} \left(\frac{\partial^2 \psi(x,\ y)}{\partial x^2} + \frac{\partial^2 \psi (x, \ y)}{\partial y^2} \right) + V(x, \ y) \psi(x, \ y) = E \psi(x, \ y)$$
</p>

It can be simplified for the particle in a 2D box since we jnow that $V(x, \ y)=0$ within the box and $V(x, \ y)=\infty$ outside the box,

<p align='center'>
    $$  V(x, \ y) = \left \{ \begin{array} \\ 0  &  0 \leq x \leq a \ and \ 0 \leq y \leq b \\ \infty &  x < 0 \ and \ x > a \\ \infty & y<0 \ and \ y>b   \end{array} \right \}$$
</p>

So the wavefunctions becomes:
<p align='center'>
    $$ -\frac{\hbar^2}{2m} \left(\frac{\partial^2 \psi (x, \ y)}{\partial x^2} + \frac{\partial^2 \psi (x, \ y)}{\partial y^2} \right) = E\psi (x, \ y)$$
</p>

When we talk about rectangular and square boxes in two dimensional particle in a box problems, we are getting set up to discuss degeneracy. The wave equation itself offers no hint of the complexity that is coming, but the boundary conditions, which are inestricably bound to the solutions of the $schr\ddot{o}inger$ Equation, are the key here.

Assuming we are working in the x-y space (2 dimensions), so $\psi(x, \ y)$ is what is being sought, we have,
<p align='center'>
    $$\frac{\hbar^2}{2\mu} \left(\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2} \right) = E \psi$$
</p>

where x and y are the standard Cartesian coordinates. The solution to this variable separable differential equation is discussed in all texts, and has the form,
<p align='center'>
    $$X(x)Y(y) = N_{\ell_x, \ell_y} sin \frac{n_x \pi x}{\ell_x} sin \frac{n_y \pi y}{\ell_y}$$
</p>

where $n_x$ and $n_y$ are integer quantum numbers, ranging from 1 to $\infty$. The box is rectangular if $\ell_x \neq \ell_y$. $N_{\ell_x, \ell_y}$ is the normalization factor, which has the form

<p align='center'>
    $$N_{\ell_x, \ell_y} = \sqrt{\frac{2}{\ell_x}} \sqrt{\frac{2}{\ell_y}}$$
</p>

The two-dimensional particle in a rectangular box of has wavefuntions become:
<p align='center'>
    $$\psi_{n_x, n_y}(x, \ y) = N \ sin \left(\frac{n_x \pi x}{L_x} \right) \ sin \ \left(\frac{n_y \pi y}{L_y} \right)$$
</p>

The constant $N$ is now determined by the normalization condition
<p align='center'>
    $$\begin{align} \int_0^{L_y} \int_0^{L_x} |\psi_{n_x, n_y}(x, \ y)|^2 \ dx \ dy \ &= 1 \\ N^2 \int_0^{L_x} sin^2 \left (\frac{n_x \pi x}{L_x} \right) \ dx \ \int_0^{L_y} sin^2 \left(\frac{n_y \pi y}{L_y} \right) \ dy \ &=1 \\ N^2 \frac{L_x}{2} . \frac{L_y}{2} &= 1 \\ N &= \frac{2}{\sqrt{L_{(x, \ y)}}} \end{align}$$
</p>

so that the complete normalized 2D wavefunction is
<p align='center'>
    $$\psi_{n_x, n_y}(x, \ y) = \frac{2}{\sqrt{L_{(x, \ y)}}} sin \left(\frac{n_x \pi x}{L_x} \right) sin \left(\frac{n_y \pi y}{L_y} \right)$$
</p>

Reference: [Particle in 2D Box](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/05.5%3A_Particle_in_Boxes/Particle_in_a_2-Dimensional_Box#:~:text=Let%20us%20now%20consider%20the,BY-NC;%20%C3%9Cmit%20Kaya)

## Example: Probability
For a particle in a two-dimensional rectangular box, if the particle is in the $\psi_{2, \ 1}(x, \ y)$ state, what is the probability that a esurement of the particle's position will yield $x \in [0, \ 1.5]$ and $y \in [0, \ 2.5]$ ?.

This Python script to illustrate the two-dimensional particle in a rectangular box with following parameters: Box dimensions (length units) and quantum numbers.
- $L_x, \ L_y =$ 1.5, 2.5
- $n_x, \ n_y = $ 2, 1

## Solution
Substituting the limits of integration into formula, we have
<p align='center'>
    $$\begin{align} P(x \in [0, \ 1.5] \mbox{~and~} \ y \in [0, \ 2.5] &= \left [\int_0^{1.5} \psi_2^2(x) \ dx \right] \left[\int_0^{2.5} \psi_1^2(y) \ dy \right] \\ &= \left [\frac{2}{L_x} \int_0^{1.5} sin^2 \left(\frac{ 2 \pi x}{L_x} \right) \ dx \right] \left[\frac{2}{L_y} \int_0^{2.5} sin^2 \left(\frac{\pi y}{L_y} \right) \ dy \right] \\ &= \left[\frac{2}{1.5} \left( 0.75 \frac{1.5}{8 \pi} sin \left(\frac{6 \pi}{1.5} \right) \right) \right] \  \left[\frac{2}{2.5} \left( 1.25 \frac{2.5}{4 \pi} sin \left(\frac{5 \pi}{2.5} \right) \right) \right]\end{align}$$
</p>

```Python
import numpy as np
from scipy.integrate import quad, dblquad, tplquad

# Example parameters
Lx, Ly = 1.5, 2.5
nx, ny = 2, 1

def func(x, y, nx, ny, Lx, Ly):
    return(np.sin(nx * np.pi * x / Lx)**2 * np.sin(ny * np.pi * y / Ly)**2)

# Evaluate the integral of the square of the unormalized wavefunction
I, err = dblquad(func, 0, Ly, lambda y: 0, lambda y: Lx, args=(nx, ny, Lx, Ly)) # Lambda y:0, lambda y:Lx, these are the limits for the inner integral (over x)

# Calculate the Normalization
N = 1 / np.sqrt(I)

print('I:', I)
print('N:', N)
```
```
I: 0.9375000000000001
N: 1.0327955589886444
```
We can also use $N=\frac{2}{\sqrt{L_{(x, \ y}}}$
```Python
N = 2 / np.sqrt(Lx * Ly)
print('N:', N)
```
```
N: 1.0327955589886444
```


## Case study: Integral in van der Waals equation

P21.1 Calculate the work required, per kg, to compress $H_2$ at 298 K to 200 bar. What proportion of the combustion enthalpy does this correspond to? Take $m(H_2)$= 2 $g \ mol^-1$ and treat hydrogen as an van der Walls gas with parameters $a = 0.2476 \ L^2 \ bar \ mol^{-2}$ and $b = 0.02661 \ L \ mol^{-1}$. The molar entalphy of combustion is $\Delta_c H_m^{\ominus} (H_2) = -286 \ kJ \ mol^{-1}$. 

Repeat the exercise for methane, using the values $m(CH_4) = 16 g \ mol^{-1}$, $a=2.300 \ L^2 bar \ mol^{-2}, $b = 0.04301 \ L  \ mol^{-1}, $\Delta_c H_m^{\ominus} (CH_4) = -891 \ kJ \ mol^{-1}$. Comment on the difference between the two gases.

To compare value for $w$ obtained by analytical integration and by with numerical integration using `scipy.integrate.quad`.  

## Solution
If the process is isothermal then the temperature, $T = 298 \ K$ is constant. Let the initial pressure be $p_1= 101325$ and the $V_1$ (to be determined). The final pressure and volume are $p_2= 2 \times 10^7 \ Pa$.  

```Python
# 1. Parameters in the van der Waals
import numpy as np
from numpy.polynomial import Polynomial
from scipy.integrate import quad

# Define some quantities
R = 8.314 # Gas constant in J.K-1.mol-1.

M_H2 , M_CH4 = 2, 16 # Molar masses of H2 and CH4, g.mol-1
n_H2, n_CH4 = 1000 /M_H2, 1000/ M_CH4 # Number of moles of H2 and CH4 in kg of each gas.

DcHm_H2, DcHm_CH4 = -286e3, -891e3 # Molar combustion entalpies in J.mol-1.
DcHs_H2, DcHs_CH4 = DcHm_H2 * n_H2, DcHm_CH4 * n_CH4 # Specific combustion enthalpies in J.kg-1.

T = 298  # Temperature in K
p1, p2 = 1e5 , 2e7 # Initial and final pressure in Pa.

# In SI units, the van der Waals parameters in m6.Pa.mol-2 and m3.mol-1.
a_H2, b_H2 = 2.476e-2, 2.661e-5
a_CH4, b_CH4 = 0.2300, 4.301e-5
```

We need to know $V$, the number of moles of gas compressed, and the van der Waals equation can be arranged into the following cubic equation in $V$, which can be solve for its real root if $p_2, \ n,$ and $T$ are known. Rearranging the van der Waals equation gives:
<p align='center'>
    $$ \begin{align} PV^2(V-nb)=nRTV^2 - n^2 a (V-nb) \\ \Rightarrow pV^3 - n(Pb + RT) V^2 + n^2 aV - n^3 ab = 0 \end{align}$$
</p>


The work integral can be evaluated analytically for a van der Waals gas, 

<p align='center'>
    $$ \begin{align} -\int_{V_1}^{V_2} p \ dV &= -\int_{V_1}^{V_2} \frac{nRT}{V-nb} - \frac{n^2 a}{V^2} dV \\ &=-nRT \ ln(\frac{V_2 - nb}{V_1 - nb}) - n^2 a (\frac{1}{V_2} - \frac{1}{V_1}) \end{align}$$
</p>

```Python
# Invert the van der Waals equation to return V from n, p, T
def get_V(n, p, T, a, b):
    poly= Polynomial([-n**3 * a * b, n**2 * a, -n*(p * b + R * T), p])
    roots = poly.roots()
    return roots[np.isreal(roots)][0].real

# Return the work required to compress the gas to p2
def get_w_per_kg(n, p2, T, a, b):
    V1 = n * R * T / p1 # Ideal gas for the initial volume

    V2 = get_V(n, p2, T, a, b) # The final, compressed, volume from the van der Waals

    # Van der Waals equation of state
    def p(V, n, R, T, a, b):
        return n * R * T / (V-n * b) - n**2 * a / V**2

    # Numerical integration of p with respect to V 
    wp, err = quad(p, V1, V2, args=(n, R, T, a, b))
    return -wp

# Calculate workrequired for H2 and CH4
wH2 = get_w_per_kg(n_H2, p2, T, a_H2, b_H2)
print(f'1. Work required for compression of H2 to 200 bar:{wH2 / 1e6:.1f} MJ/Kg')
print(f'({wH2 / -DcHs_H2 * 100:.1f} of entalpy released on combustion)')

wCH4 = get_w_per_kg(n_CH4, p2, T, a_CH4, b_CH4)
print(f'2. Work required for compression of CH4 to 200 bar:{wCH4 / 1e6:.1f} MJ/Kg')
print(f'({wCH4 /-DcHs_CH4 * 100:.1f} of entalpy released on combustion)')
```
```
1. Work required for compression of H2 to 200 bar:6.5 MJ/Kg
(4.6 of entalpy released on combustion)
2. Work required for compression of CH4 to 200 bar:0.8 MJ/Kg
(1.4 of entalpy released on combustion)
```

