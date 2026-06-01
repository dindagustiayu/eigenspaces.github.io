---
date: "2026-4-13"
---



[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Hermite-Polynomials/blob/main/Hermite%20Polynomials%20in%20QHO.py)

# Hermite Polynomial in Quantum Harmornic Oscillator

## Vibrational Spectroscopy
__What is it?__: Vibrational spectroscopy detects transitions between the quantised vibrational energy levels associated with bond stretching and/or bond angle bending in molecules.

__How do we do it?__: Transitions are observed by measuring the amount of infrared radiation that is absorbed or emitted by vibrating molecules in solid, liquid, or gas phases.

__Why do we do it?__: A knowledge of the vibrational level spacings gives us the value of the stretching (or bending) force constants which characterise the stiffness of a bond, allows us to estimate the bond dissociation energy, and gives us a means of identifying characteristic functional groups of atoms within large molecules.

## Preliminaries

- `scipy.optimize`: provides a range of algorithms for minimization of multidimensional functions (with or without constraints).
- `scipy.optimize.minimize`: minimize routine which implements several different algorithms for minimization.
- `scipy.optimize.minimize_scalar`: provide a way to minimize a function of a single variable.
- `scipy.optimize.special`: is the function for the evaluation of different sirts of orthogonal polynomials, including the Legendre, Jacobi, Laguerre, Hermite and different flavors of Chebshev polynomials.
- `scipy.optimize.special import hermite`: (Physicists') Hermite polynomial, $H_n (x)$.

## Mathematical Prerequisites
- Differential equations, specifically the power series method.
- Orthogonal polynomials
- Gaussian functions

## Quantum Mechanical Prerequisites
- Time-Independent $Schr\ddot{o}dinger$
- Normalization of wavefunctions ($|\psi (x)|^2$)
- Quantum number ($n \in {0, \ 1, \ 2, \ldots}$ ) and energy level ($E_n$).

# Quantum approach
In quantum mechanics and in other branches of physics, it is common to approach physical problems algebraics and analytic methods. Examples include the use of differential equations for many interesting models, the use of quantum groups in quantum physics, and of differential geometry in relativity theory. In this work, we discuss the Hermite polynomials, some of their properties and a brief description of their applications to the Quantum Harmonic Oscillator.

The Harmonic Oscillator's Quantum Mechanical solution involves Hermite Polynomials, which are introduced here. The wavefunctions for the quantum harmonic oscillator contain the Gaussian form, which allows them to satisfy the necessary boundary conditions at infinity. In the wavefunction associated with a given value of the quantum number $n$, the Gaussian is multiplied by a polynomial of order $n$ (the Hermite polynomials above) and the constants necessary to normalize the wavefunctions.

# Hermite Polynomials
Hermite polynomials, named after the French mathematician [Charles Hermite](https://en.wikipedia.org/wiki/Charles_Hermite), are orthogonal polynomials, in a sense to be described below, of the form

<p align='center'>
    $$H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2} \tag{1}$$
</p>

for $n=0, \ 1, \ 2, \ 3, \ldots$
The first few Hermite polynomials are
- for $n=0$ we have $H_0 (x) = 1$
- for $n=1$ we have $H_1 (x) = 2x$
- for $n=2$ we have $H_2 (x) = 4x^2 - 2$
- for $n=3$ we have $H_3 (x) = 8x^3 - 12x$
- for $n=4$ we have $H_4 (x) = 16x^4 - 48x^2 + 12$
- for $n=5$ we have $H_5 (x) = 32x^5 - 160x^3 + 120x$
- for $n=6$ we have $H_6 (x) = 64x^6 - 480x^4 + 720x^2 -120$
- for $n=7$ we have $H_7 (x) = 128x^7 - 1344x^5 + 3360x^3 - 1680x$

For $n \in \mathbb{N}$, we define Hermite polynomials $H_n (x)$ by
<p align='center'>
    $$\sum_{n=0}^{\infty} \frac{H_n (x)}{n!} r^n = e^{2xr - r^2}, \quad for |r| < \infty \tag{2} $$
</p>

To find $H_n (x)$, expand the right-hand side of eq.(2) as a Maclaurin series in $r$ and equate coefficients. From eq.(2) we drive the closed expression
<p align='center'>
    $$H_n (x) = \sum_{k=0}^{[n/2]} \frac{(-1)^k n!}{k! (n-2k)!} (2x)^{n-2k} \tag{3} $$
</p>

where $[x]$ denotes the largest integer less than or equal to $x$. Checking with $n = 0, \ 1, \ 2, \ldots$ we find that eq.(3) yields the expected Hermite polynomials. To prove that eq.(3) holds in general.


# Connection with Harmonic Oscillator
In this final part, we will show the connection of Hermite Polynomials with the Quantum Harmonic Oscillator. First of all, the analogue of the classical Harmonic Oscillator in Quantum Mechanics is described by the $Schr\ddot{o}dinger$ equation

<p align='center'>
    $$ -\frac{\hbar^2}{2m} \frac{d^2 \psi}{dx^2} + \frac{1}{2} m \omega^2 x^2 \psi = E \psi \tag{4}$$
</p>

There are a bunch of constants sitting in eq.(4) and life is simpler if we can just get rid of them. To this end, define
<p align='center'>
    $$ y = \sqrt{\frac{m \omega}{\hbar} x} \quad \mbox{and} \quad \tilde{E} = \frac{2E}{\hbar \omega} \tag{5}$$
</p>

Then the $Schr\ddot{o}dinger$ equation takes the cleaner form
<p align='center'>
    $$\frac{d^2 \psi}{dy^2} - y^2 \psi = - \tilde{E} \psi \tag{6}$$
</p>

The derivatives are $\psi' = -y \psi$ and $\psi" = y^2\psi - \psi$, so we see that this obeys the $Schr\ddot{o}inger$ with (rescaled) energy $\tilde{E} = 1$.

Furthermore, it's simple to see that all normalisable solutions should fall off in the same exponential fashion, with $\psi \thicksim e^{-y^2 /2}$ as $y \rightarrow \pm \infty$. This follows from looking at the large $y$ behaviour of (eq.5), where the $\tilde{E} \psi$ term is necessarily neglible compared to the $y^2 \psi$. This motivated the general ansatz

<p align='center'>
    $$\psi (y) = h(y) e^{-y^2 /2} \tag{7}$$
</p>

In general, the functions $h(y)$ are known as _Hermite Polynomials_ and have a number of nice properties.

## The Wavefunctions
The wavefunctions for the quantum harmonic oscillator contain the Gaussian form, which allows them to satisfy the necessary boundary conditions at infinity. In the wavefunction associated with a given value of the quantum number $n$, the Gaussian is multiplied by a polynomial of order $n$ called a __Hermite polynomial__. The expressions are simplified by making the substitution,

<p align='center'>
    $$\psi (y) = e^{-y^2 / 2} \tag{8}$$
</p>

Because of the association of the wavefunction with a probability density, it is necessary for the wavefunction to include a normalization constant, $N_n$.

<p align= 'center'>
    $$N_n = \frac{1}{(2^n n! \sqrt{\pi})^{1/2}} \tag{9}$$
</p>

The final form of the harmonic oscillator wavefunction is this
<p align='center'>
    $$\psi_n (y) = N_n H_n (y) e^{-y^2 /2} \tag{10} $$
</p>

where $y = \sqrt{\alpha} x$ and $\alpha = \frac{m \omega}{\hbar}$.

The general formula for the normalized wavefunctions is 
<p align='center'>
    $$\psi_n (y) = \left(\frac{\alpha}{\pi} \right)^{1/4} \frac{1}{\sqrt{2^n n!}} H_n (y)e^{-y^2 /2} \tag{11}$$
</p>

where $H_n$ is the Hermite polynomial. First four harmonic oscillator normalized wavefunctions,
<p align='center'>
    $$\begin{align} \psi_0 &= \left(\frac{\alpha}{\pi} \right)^{1/4} e^{-y^2 /2} \\ \psi_1 &= \left(\frac{\alpha}{\pi} \right)^{1/4} \sqrt{2} y e^{-y^2 /2} \\ \psi_2 &= \left(\frac{\alpha}{\pi} \right)^{1/4} \frac{1}{\sqrt{2}} (2y^2 -1) e^{-y^2 /2} \\ \psi_3 &= \left(\frac{\alpha}{\pi} \right)^{1/4} \frac{1}{\sqrt{3}} (2y^3 - 3y) e^{-y^2 /2} \end{align}$$
</p>

All energies are proportional to $\hbar \omega$, with $\omega$ the frequency of the harmonic oscillator. The energies are

<p align='center'>
    $$E_n = \hbar \omega \left (\frac{1}{2} + n \right) \quad \mbox{with} \quad n = 0, \ 1, \ 2, \ldots \tag{12}$$
</p>

When the $Schr\ddot{o}dinger$ equation for the harmonic oscillator is solved by a series method, the solutions contain this set of polynomials, named the Hermite polynomials.

|n | $H_n (y)$ | $E_n$ |
|--|:----------:|:----:|
|0 | $1$         |$\frac{1}{2} \hbar \omega$ |
|1 | $2y$        |$\frac{3}{2} \hbar \omega$ |
|2 | $4y^2 -2$ |$\frac{5}{2} \hbar \omega$ |
|3| $8y^3 - 12y$ |$\frac{7}{2} \hbar \omega$ |
|4| $16y^4-48y^2 +12$ | $\frac{9}{2} \hbar \omega$ |
|5| $32y^5 - 160y^3 +120y$ | $\frac{11}{2} \hbar \omega$|

The wavefunctions for the quantum harmonic oscillator contain the Gaussian form, which allows them to satisfy the necessary boundary conditions at infinity. In the wavefunction associated with a given value of the quantum number $n$, the Gaussian is multiplied by a polynomial of order $n$ (the Hermite polynomials above) and the constants necessary to normalize the wavefunctions. 

# Example 
Visualizing the harmonic oscillator wavefunction for any vibrational quantum number $n$ use `scipy.special` package with normalized by integrating the corresponding probability distribution:

<p align='center'>
    $$\int_{-\infty}^{\infty} |\psi_n (y)|^2 \ dy = 1$$
</p>

__Solution__:
1. Calculate Normalization constant and Hermite polynomial for quantum number, $n =2$ and variable $x = 3$.

2. Calculate the one-dimensional harmonic oscillator wavefunction and energies is defined by eq.10 using Numpy:

<p align='center'>
    $$\psi_n (y) = N_n H_n (y) e^{-y^2 /2}$$
</p>

3. Plotted using Matplotlib
4. Verify that the wavefunctions are normalized using `scipy.integrate.quad`.

```Python
# 1. Normalization constant Calculate Hermite polynomial
from scipy.special import hermite
import numpy as np
import math

# Normalization constant for n =2
n = 2

N_n = 1 / (np.sqrt(np.pi) * 2**n * math.factorial(n))
print("N_n=", N_n)

# Hermite polynomial
H2 = hermite (2) # H_2(x) = 4x^2 - 2
print(f"H2(3)=", H2(3)) # 4*3**2 -2
```
```
N_n= 0.07052369794346953
H2(3)= 34.00000000000001
```

```Python
# 2. Calculate the QHO 
import numpy as np
import math
from scipy.special import hermite

def psi_n(y, n):
    "Return the harmonic oscillator function, psi_n at x"
    N_n = 1.0 / np.sqrt((2**n) * math.factorial(n) * np.sqrt(np.pi))
    H_n = hermite(n)
    return N_n * H_n(y) * np.exp(-y**2 /2)

# Example: print n=2 at y = 3
print("psi_2(3)=", psi_n(3, 2))
```
```
psi_2(3)= 0.10030470080286634
```
The Hermite polynomial for n = 2 and y = 3 is 0.1003.

```Python
# 3. Plotting use matplot for n = 2 and n=1
import matplotlib.pyplot as plt

def plot_psi(y, n):
    psi = psi_n(y, n)
    plt.plot(y, psi, label=f'$n={n}$')
    plt.xlabel(r'$y$')
    plt.ylabel(r'$\psi_n (y)$')

y = np.linspace(-4, 4, 500)
plot_psi(y, 0)
plot_psi(y, 1)
plot_psi(y, 3)
plt.legend()
plt.title("Quantum Harmonic Oscillator Wavefunctions (n= 0, 1, and 3)")
plt.grid(alpha=0.5)
plt.savefig('Quantum Harmonic Oscillator Wavefunctions (n= 0, 1, and 3).svg', bbox_inches='tight')
plt.show()
```
![Figure 1. Quantum Harmonic Oscillator Wavefunctions (n= 0, 1, and 3)](/quarto-workflows/images/hermite/Quantum Harmonic Oscillator Wavefunctions (n= 0, 1, and 3).svg)

```Python
# Verify the wavefucntions are normalized
from scipy.integrate import quad

def P_n(y, n):
    "Return the probability distribution function for psi_n"
    return psi_n(y, n)**2

n = 3
area, abserr = quad(P_n, -np.inf, np.inf, args=(n,))
print('area=', area)
```
```
area= 1.0000000000000004
```

# The Classical Probability Density (PDF)
In quantum mechanics, the behaviour of electrons and other small particles is not Newtonian. In fact, the behavior of quantum systems can almost appear random. Instead of having predictable trajectories that we expect of projectiles in Newtonian mechanics, individual quantum events are unpredictable. However, if we consider a large number of quantum events, a pattern emerges. This is known as a statistical distribution. We often use mathematical probabilities to describes the outcomes of quantum events. The probability of a single quantum events. The probability of a single quantum event is exactly proportional to the value of the statistical distribution.

The probability of a classical particle being found between $x$ and $x + \delta x$ is $p(x) \delta x$. For the harmonic oscillator,
<p align ='center'>
    $$\begin{align} x(t) &= x_0 \cos (\omega t) \quad (13) \\ t(x) &=\frac{1}{\omega} \arccos (x/x_0) \quad (14) \\ |v(x(t))| &= |\dot{x} (t) | = x_0 \omega | sin (\omega t) | \quad (15) \\ |v(x)| &= x_0 \omega | \sin (\arccos(x/x_0))| \quad (16)\end{align}$$
</p>

Now this can be simplified with
<p align='center'>
    $$ \begin{align} a &= \sin (\arccos (b)) \quad (17) \\ a^2 &= \sin^2 (\arccos (b)) = 1 - \cos^2 (\arccos (b)) = 1 - b^2 \quad (18) \\ |\sin (\arccos(b)) | &= \sqrt{1- b^2} \quad (19) \end{align}$$
</p>

So combining this we get
<p align='center'>
    $$P (x) = \frac{N}{\sqrt{1-(x/x_0)^2}} \tag{20} $$
</p>

for $|x| \leq x_0$ and $p(x) = 0$ otherwise. $N$ is normalisation constant.

where the normalization constant, $N$ (eq.9), must be chosen so that
<p align='center'>
    $$\int_{-A}^{A} P (x) \ dx = 1$$
</p>

The normalized classical probability density function is therefore
<p align='center'>
    $$ P (x) = \frac{1}{\pi} \ \frac{1}{\sqrt{A^2 - x^2}} \tag{21}$$
</p>

__Solution__:

1. Calculate and get the classical oscillator amplitude for $n$, y_(+) = A, \ y_(-) = -A.
2. Calculate normalized classical probability density function.
3. Plot the probability density distribution (classical vs quantum) and set the color lines.

```Python
# 1. Calculate the classical oscillator amplitude for state n
def get_A(n):
    "Return to the Classical oscillator amplitudo for state n"
    return np.sqrt(2*n + 1)
    A = get_A(n)

# 2. Calculate normalized classical probability density function.
def P_classical(y, A):
    return 1 / np.pi / np.sqrt(A**2 - y**2)

# 3. Plot the probability density distribution (classical vs quantum) and set the color lines
def plot_QM_and_Classical_Probabilities(y, n):
    P_qm_n = P_n(y, n)
    P_classical_n= P_classical(y, A)
    plt.plot(y, P_classical_n, label="Classical", c="black")
    plt.plot(y, P_qm_n, label="Quantum, $n={3}$", c="red")
    ymax = 1

    # As an alternative to pyplot.plot, pyplot.nlines([x1, x2, ...], y1, y2,...)
    # Plots vertical lines between y-coordinates y1 and y2 at x = x1, x2, ...
    plt.vlines([-A, A], ymin = 0, ymax=ymax, ls='--')
    plt.ylim(0, ymax=ymax)
    plt.xlabel('$y$')
    plt.ylabel('$P(y)$')
    plt.title(f"Quantum vs Classical Probabilities (n={n})")
    plt.legend()
    
y = np.linspace(-8, 8, 1000)
plot_QM_and_Classical_Probabilities(y, 3)
plt.savefig('Quantum vs Classical Probabilities (n=3).svg', bbox_inches='tight')
```
![Figure 2. Quantum vs Classical Probabilities (n=3)](/quarto-workflows/images/hermite/Quantum vs Classical Probabilities (n=3).svg)

# P23.1 Exercise 

By taking an average of $|\psi_n (x)|^2$ over a series of intervals of suitable constant with to smooth out its peaks, compare the classical and quantum mechanical probability density distribution for the $n = 20$ excited vibrational state of the harmonic oscillator.

__Solution__:
1. Use some preliminary syntax.
2. Plotting with its regions ($n = 20$).

```Python
import numpy as np
from scipy.special import hermite
from scipy.integrate import quad
import matplotlib.pyplot as plt

def psi_n(y, n):
    "Return the harmonic oscillator function, psi_n at x"
    N_n = 1.0 / np.sqrt((2**n) * math.factorial(n) * np.sqrt(np.pi))
    H_n = hermite(n)
    return N_n * H_n(y) * np.exp(-y**2 /2)

def P_n(y, n):
    "Return the probability distribution function for psi_n"
    return psi_n(y, n)**2

def get_A(n):
    "Return to the Classical oscillator amplitudo for state n"
    return np.sqrt(2*n + 1)
    A = get_A(n)

def P_classical(y, A):
    return 1 / np.pi / np.sqrt(A**2 - y**2)

n = 20
nregions = n // 2
A = get_A(n)
Dq = 2 * A /nregions
P_qm = np.zeros(nregions)
y = np.zeros(nregions)

# Looping over regions
for i in range(nregions):
    #Integrate the square of the wavefunction over the its region"
    # between -A + Dq.i and -A + Dq.(i + 1)
    a = -A + i * Dq

    # Quantum probability in each region
    P_qm[i] = quad(P_n, a, a + Dq, args=(n,))[0] /Dq
    y[i] = a + Dq / 2

# Classical probabilities for the regions
P_classical_n = P_classical(y, A)
plt.plot(y, P_qm, c='k', label=f"Quantum Mechanic $n={n}$")
plt.plot(y, P_classical_n, c = 'red', label='Classical')
plt.xlabel(r'$y$')
plt.ylabel(r'$P(y)$')
plt.legend()
plt.title(f"Quantum vs Classical Probabilities (n={n})")
plt.savefig('Quantum vs Classical Probabilities (n=20).svg', bbox_inches='tight')
```
![Figure 3. Quantum vs Classical Probabilities (n=20)](/quarto-workflows/images/hermite/Quantum vs Classical Probabilities (n=20).svg)

# Summary
1. Vibrational spectroscopy via Hermite Polynomials bridges quantum mechanics and classical physics.
2. At low quantum numbers, quantum mechanics predicts probability distributions that differ strongly from classical expectations, respectively for the opposite.
3. The quantum harmonic oscillator reproduces classical behaviour in the limit of large vibrational quantum numbers.
4. Hermite polynomials structure encodes the oscillations, while the classical distribution emerges as the envelope in the large $n$ limit.

