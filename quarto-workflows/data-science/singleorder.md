[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Equations-of-Motion-of-Harmonic-Oscillator/blob/main/Second%20ODE%20in%20Quantum%20Oscillator.html)


## Second Order Differential Equations

In this unit, we move from first-order differential equations to __second-order differential equations__, that is, differential equations involving a second (but no higher) derivative. Examples of such equations are

<p align='center'>
    $$\frac{d^y}{dx^2} - 3\frac{dy}{dx} + 2y = 4e^x \ \mbox{and} \ 3\frac{d^2y}{dx^2} + y = x \ sin \ x$$
</p>

Second-order differential equations play a central role in the physical sciences. They are found, for example, in laws describing,
- mechanical system
- wave motion
- electric currents
- quantum phenomena.

To take a simple case, consider a particle of mass $m$ that moves in one dimension along the $x$-axis. At any given time $t$, the particle's position is $x(t)$, and its velocity and acceleration are given by the derivatives $dx/dt$ and $d^2x/dt$. There are no general laws for the positions or velocity of the particle, but there is a very important law for its acceleration: $\mbox{Newton's second law}$ tells us that

<p align='center'>
    $$ \mbox{mass} \times \mbox{acceleration} = \mbox{force}$$
</p>

which implies that
<p align='center'>
    $$m \frac{d^2x}{dt^2} = F \quad (1)$$
</p>

where $F$ is the force acting on the particle. The force need not be constant, and may vary with the position $x$ or the velocity $dx/dt$ of the particle. So, depending on the precise details, we get a second-order differential equation for $x$ as a function of $t$, and the solution of this equation tells us how the particle can move.

The system known as a _simple harmonic oscillator_ provides a good example. We consider the case where the force is proportional to the displacement from equilibrium, and take

<p align='center'>
    $$F = -kx$$
</p>

where $k$ is a positive constant. The negative sign in this equation ensures that the force always acts in a direction that tends to restore the particle to its equilibrium position. We get the differential equation
<p align='center'>
    $$m \frac{d^2 x}{dt^2} = -k x \quad (2)$$
</p>

Recalling that $k>0$ and $m<0$, we can also express this as 
<p align='center'>
    $$\frac{d^2 x}{dt^2} = -\omega^2 x \quad (3)$$
</p>

where $\omega = \sqrt{k/m}$ is a positive constant. Equation (3) is called the _equation of motion_ of a simple harmonic oscillator. It is a second-order differential equation whose solution tells us how the particle can move.

This equation may be decomposed into two first-order equations as follows:
<p align='center'>
    $$\begin{align} \frac{dx_1}{dt}= x_2, \\ \frac{dx_2}{dt}= \omega^2 x_1 \end{align}$$
</p>

where $x_1$ is identified with $x$ and $x_2$ with $dx/dt$.
This units develops systematic techniques to solve equations like this. For the moment, we will simply guess the solution and check that it works. We know that,

<p align='center'>
    $$\begin{align} \frac{d}{dt} (\sin \ t) &= \cos \ t \quad \mbox{and} \quad \frac{d}{dt} (\cos \ t) = - \sin \ t, \\ \frac{d^2}{dt^2} (\sin \ t) &= - \sin \ t \quad \mbox{and} \quad \frac{d^2}{dt^2} (\cos \ t) = - \cos \ t \end{align}$$ 
</p>

In other words, taking the second derivative of a sine or cosine function gives the same function back again.

## Preliminaries
`solve_ivp` function is a simplified interface to the more advanced `scipy.integrate` method which provides a range of different numerical integrators, including Runge-Kutta algorithms and support for complex-valued variables.

---
The following code performs solution of the harmonic oscillator equation of motion using `scipy.integrate.solve_ivp` and compares the result with the numerical approach.

```Python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Mass (kg), force constant (N.m-1)
m, k = 1, 2
omega = np.sqrt(k / m)

# Harmonic oscillator initial condition (position, m, and velocity, m.s-1)
x0 = 0.01, 0

# Initial and final time points for the integration (s)
t0, tf = 0, 10

# Return dx1/dt and dx2/dt = dx1^2/dt^2 time (t)
def derivative(t, x, omega):
    x1, x2 = x
    dx1dt = x2
    dx2dt = -omega**2 * x1
    return dx1dt, dx2dt

# Integrate the differential equation (Numerical solution)
soln = solve_ivp(derivative, (t0, tf), x0, args=(omega,), dense_output=True)
print(soln.message)

t = np.linspace(t0, tf, 200)
x, v = soln.sol(t)

# Solution for exact analytical solution
x_exact = x0[0] * np.cos(omega * t)
v_exact = -x0[0] * omega * np.sin(omega * t)

# Plot and compare the numerical and exact solutions
plt.plot(t, x_exact, '-k', label=r'$\mathrm{x-exact}$')
plt.plot(t, v_exact, 'black', label= r'$\mathrm{v-exact}$')
plt.plot(t, x, 'o', markevery= 3, label=r'$x$')
plt.plot(t, v, 'D', markevery= 3, color='gray', label=r'$v$')
plt.xlabel(r'$t/s$')
plt.ylabel(r'$x \ / \ \mathrm{m}, \ v \ / \ \mathrm{m} \ s^{-1}$')
plt.legend()
plt.title('Numerical Integration vs Exact calculation of QHO')
plt.savefig('Numerical Integration vs Exact calculation of QHO.svg', bbox_inches='tight')
plt.show()
```
The solver successfully reached the end of the integration interval.
<div align='center'>
<img src="Numerical Integration vs Exact calculation of QHO.svg">
</div>

<p align='center'>
Figure 1. Numerical and exact solutions to the harmonic oscillator ODE for a mass, $m$ = 1 kg and force constant $k = 2 \ N \ m^{-1}$ with initial conditions $x(0)=1$ cm and $v(0)=0$.
</p>


## Conclusion
- Harmonic oscillators play a central role in physics and its applications. If a system performs small oscillations about an equilibrium point, then it is generally a good approximation to model it as a harmonic oscillator.
- It should come as no surprise that to-and-fro motion of a pendulum clock can be modelled by a harmonic oscillator. On a smaller scale, vibrating molecules and vibrating crystals are also modelled as harmonic oscillators.

