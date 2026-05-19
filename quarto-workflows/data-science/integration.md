[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Integration-by-substitution/blob/main/Basic%20Integration.html)

# Integration
The second major component of the Calculus is called _integration_. This may be introduced as a means of finding areas using summation and limits. Integrals are a fundamental tool for a range of activities in fields such as mathematics, physics, and engineering.

## What is an integral?
A lot of problems in pysics are described by derivatives, the inverse of derivatives is namely integration. Derivatives is used to compute instantaneous rates of change of functions, integrals measure net change or total change of functions over interval.

## How is it used in real life?
In real-world experiment you would be standing on top of a large tower with a stop watch and you would drop an object, determining the acceleration $g$ from the time it takes the object to hit the ground and the known height $h$ of the tower. This clearly involves two integrations:
<p align='center'>
    $$\begin{align} v_f &= \int_0^t \; g\; dt\\ h&=\int_0^t \; gt \; dt \end{align}$$
</p>

## Prior Knowledge
- Definite and indefenite integrals.
- Integrals of power functions.
- Integrals of exponential and logarithmic functions.
- Integrals of trigonometric functions.
- Integration rules
  - The power rule
  - The sum, difference, and constant multiple rules
- Integration by substitution.

More information about integral, [__here__](https://articles.outlier.org/a-beginners-guide-to-integrals).

## Preliminaries

- `scipy.integrate`: sub package provides several integration techniques, including an ordinary differential equation integrator (with finite limits) and improper integral (those with one or more infinite limits).
- `quad`: the function provided to integrate a function of one variable between two points.
- `scipy.special`: definition of numerous special functions of mathematical physics. Available functions include airy, elliptic, bessel, gamma, beta, hypergeometric, parabolic cylinder, mathieu, spheroidal wave, struve, and kelvin.

## Hint
`quad` returns a `tuple` containing two values: the value of the _integral_ and _an estimate of the absolute error_. For a simple function, an anonymous (`lambda`) function is often used.


## Case study: Integral of a single variable
Integrals are used throughout physics, engineering, and maths to compute quantities such as area, volume, mass, physical work, and more. In this work, we will explore the basics python code of integrals. 

1. Suppose we want to find the integral:

$$ \int_0^2 \; 2x^2 \; dx$$

first, we use the power rule for integration,
<p align='center'>
    $$\begin{align} \int x^k \;dx &= \frac{1}{k+1} x^{k+1}+C \\ \int_0^2 \; 2x^2 \; dx &= 2 \frac{1}{2+1} x^{2+1} + C = \frac{2}{3} \; x^3 + C \end{align}$$
</p>

When $x=2$ and $x=0$, so we require,
<p align='center'>
    $$\begin{align} \int_0^2 \; 2x^2 \; dx&= \int_0^2 \frac{2}{3} \; x^3 + C \\ &= \left [\frac{2}{3} \; x^3 \right]_0^2 \\ &= \left [\frac{2}{3}(2)^3 - \frac{2}{3}(0)^3 \right] \\ &=\left[\frac{16}{3} - 0 \right] \\ &= \frac{16}{3} \end{align}$$
</p>

```Python
# using quad
import scipy.integrate as integrate
from scipy.integrate import quad

quad(lambda x:  2*x**2, 0, 2)
```
```
(5.333333333333334, 5.921189464667502e-14)
```

# Integration by Substitution
 There are occasions when it is possible to perform an apparently difficult piece of integration by first making a __substitution__. This has the effect of changing the variable and the integrand. When dealing with definite integrals, the limits of integration can also change. In this unit we will meet several examples of integrals where it is appropiate to make a substitution.

## Integration by substituting $u=ax+b$
We introduce the technique through some simple examples for which a linear substitution is appropriate.

## Case study: Integral $u=ax+b$
1. Suppose noe we wish to find the integral
   <p align='center'>
       $$\int cons(3x+4) \; dx$$
   </p>

Observe that if we make a substitution $u=3x+4$, the integral will then contain the much simpler form $cos \; u$, which we will be able to integrate.
As before, 
<p align='center'>
    $$du=\left(\frac{du}{dx} \; dx\right)$$
</p>

and so, with $u = 3x+4$ and $\frac{du}{dx} = 3$

It follows that 
<p align='center'>
    $$du=\left(\frac{du}{dx}\; dx \right)$$
</p>

So, substituting $u$ for $3x+4$, and with $dx=\frac{1}{3}\; du$
<p align='center'>
    $$\begin{align} \int cos(3x+4)\; dx&=1/3 \int cos\;u\;du \\ &=\frac{1}{3} sin\; u\;+\;C \end{align}$$
</p>

We can revert to an expression involving the original variable $x$ by recalling that $u=3x+4$, giving
<p align='center'>
    $$\int cos(3x+4) \; dx=\frac{1}{3} sin(3x+4)\;+\;C$$
</p>

We have completed the integration by substitution.

For example, we calculate the definite integral from 0 to 2. 
<p align='center'>
    $$\begin{align} \int_0^2 cos(3x+4) \; dx&=\frac{1}{3} [sin(3x+4)]_0^2 \\ &=\frac{1}{3} \left[ \;sin(3(2)+4) - \;sin(3(0)+4) \right] \\ &=\frac{1}{3} \left[sin(10)-sin(4) \right]\end{align}$$
</p>

```Python
from scipy.integrate import quad
import numpy as np

#For example, definite integral from 0 to 2

f = lambda x: np.cos(3*x + 4)
result = quad(f, 0, 2)
print('Integral result:', result)
```
```
Integral result: (0.07092712813951971, 1.3944582737777145e-14)
```

```Python
import matplotlib.pyplot as plt
import numpy as np


# 1. Create data area
x_fill = np.linspace(0, 2, 400)
y_fill = f(x_fill)

# 2. Plot the function
plt.plot(x_fill, y_fill, label='f(x)= cos(3x+4)', color='navy')

# 3. Plot area
plt.fill_between(x_fill, y_fill, alpha=0.2, color='skyblue', label='Area')

# 4. Add labels, legend, and dashed grid
plt.title("Visualization of $\\int_0^2  cos(3x+4) dx$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('cos(3x+4).svg', bbox_inches='tight')
plt.show()
```
![Figure 1. Visualization of cos(3x+4)](/quarto-workflows/images/integration/cos(3x+4).svg)

## Exercise 1:

1. In each case, use a substitution to find the integral:

<p align='center'>
    $$\begin{align} (a)\; \int_0^2 (x-2)^3 dx \;\;\; (b) \; \int_0^1 (x+5)^4 dx \;\;\; (c)\; \int_{0}^2 (2x-1)^7 dx \;\;\; (d)\; \int_{-1}^1 (1-x)^3 dx\end{align}$$
</p>

__Solution:__

(a) $\int (x-2)^3 dx$
<p align='center'>
    $$\begin{align} \int_0^2 (x-2)^3 dx &= \int_{-2}^0 u^3 du \\ &= \left [\frac{1}{4} \; u^4 \right]_{-2}^0 \\ &= \frac{1}{4} [(0)^4 - (-2)^4] \\ &= -4 \end{align}$$
</p>

(b) $\int_0^1 (x+5)^4 dx$
<p align='center'>
    $$\begin{align} \int_0^1 (x+5)^4 dx &= \int_5^6 u^4 du \\&= \left[\frac{1}{5} u^5 \right]_5^6 \\ &= \frac{1}{5}[(6)^5 - (5)^5] \\ &= \frac{1}{5} [7776 - 3125] \\ &= \frac{4651}{5} \end{align}$$
</p>

(c) $\int_{0}^2 (2x-1)^7 dx$
<p align='center'>
    $$\begin{align} \int_{0}^2 (2x-1)^7 dx&= \frac{1}{2} \int_{-1}^{3} \; u^7 \;du \\&= \frac{1}{2} \left[\frac{1}{8} u^8 \right]_{-1}^3 \\ &= \frac{1}{2} \times [\frac{1}{8} (3)^8 - \frac{1}{8}(-1)^8] \\ &= \frac{1}{2} \left[\frac{6561}{8} -\frac{1}{8} \right] \\ &= 410 \end{align}$$
</p>

(d) $\int_{-1}^1 (1-x)^3 dx$
<p align='center'>
    $$ \begin{align} \int_{-1}^1 (1-x)^3 dx &= - \int_2^0 u^3 du \\ &= - \frac{1}{4} [(0)^4 - (2)^4] \\ &= 4 \end{align}$$
</p>

```Python
from scipy.integrate import quad
import numpy as np

#For example definite integral from 0 to 2

f_1 = lambda x: (x - 2)**3
result_1 = quad(f_1, 0, 2)
print('Integral result:', result_1)

f_2 = lambda x: (x + 5)**4
result_2 = quad(f_2, 0, 1)
print('Integral result:', result_2)

f_3 = lambda x: (2*x - 1)**7
result_3 = quad(f_3, 0, 2)
print('Integral result:', result_3)

f_4 = lambda x: (1-x)**3
result_4 = quad(f_4, -1, 1)
print('Integral result:', result_4)
```
```
Integral result: (-4.0, 4.440892098500626e-14)
Integral result: (930.1999999999999, 1.0327294575063206e-11)
Integral result: (410.00000000000006, 4.553302178850362e-12)
Integral result: (4.0, 4.440892098500626e-14)
```

```Python
import matplotlib.pyplot as plt
import numpy as np

# Create figure 1
fig = plt.figure(figsize=(28, 6))
x_1 = np.linspace(0, 2, 400)
y_1= f_1(x_1)

ax1 = fig.add_subplot(1, 4, 1)
ax1.plot(x_1, y_1, label=r'$f(x)= (x-2)^3$', color='navy')
ax1.set_xlabel('x')
ax1.set_ylabel(r'f(x)')
ax1.set_title(r'Visualization $\int_0^2 (x-2)^3$')
ax1.legend()

# Create figure 2
x_2 = np.linspace(0, 2, 400)
y_2 = f_2(x_2)

ax2 = fig.add_subplot(1, 4, 2)
ax2.plot(x_2, y_2, label=r'$f(x)= (x+5)^4$', color='C2')
ax2.set_xlabel(r'x')
ax2.set_ylabel(r'f(x)')
ax2.set_title(r' Visualization $\int_0^1 (x+5)^4$')
ax2.legend()

# Create figure 3
x_3 = np.linspace(0, 2, 400)
y_3 = f_3(x_3)

ax3 = fig.add_subplot(1, 4, 3)
ax3.plot(x_3, y_3, label=r'$f(x)= (2x-1)^7$', color='C1')
ax3.set_xlabel(r'x')
ax3.set_ylabel(r'f(x)')
ax3.set_title(r'Visualization $\int_0^2 (x+5)^4$')
ax3.legend()

# Create figure 4
x_4 = np.linspace(0, 2, 400)
y_4 = f_4(x_4)

ax4 = fig.add_subplot(1, 4, 4)
ax4.plot(x_4, y_4, label=r'$f(x)= (1-x)^3$', color='C3')
ax4.set_xlabel(r'x')
ax4.set_ylabel(r'f(x)')
ax4.set_title(r'Visualization $\int_{-1}^1 (1-x)^3$')
ax4.legend()
plt.savefig('Integral substitution 1.svg', bbox_inches='tight')
plt.show()
```
![Figure 2. Visualization Integral substitution](/quarto-workflows/images/integration/Integral substitution 1.svg)


## Exercise 2:

2. In each case use a subtitution to find the integral:

<p align='center'>
    $$\begin {align} (a)\; \int_0^1 sin(7x-3)dx \;\; (b)\; \int_0^1 e^{3x-2}dx \;\; (c)\; \int_0^{\pi /2} cos (1-x)dx \;\; (d)\; \int_{-1}^1 \frac{1}{7x+5}dx \end{align}$$
</p>

(a) $\int_0^1 sin(7x-3) dx$
<p align='center'>
    $$\begin{align} \int_0^1 sin(7x-3) dx&= \frac{1}{7} \int_{-3}^4 sin (u) du \\&= \frac{1}{7} \left[-cos (u) \right]_{-3}^4 \\& = \frac{1}{7} [-cos (4) - (-cos(-3))] \end{align}$$
</p>

(b) $\int_0^1 e^{3x-2}dx$
<p align='center'>
    $$\begin{align} \int_0^1 e^{3x-2}dx &= \frac{1}{3} \int_{-2}^{1} e^u \;du \\&= \frac{1}{3} \left[e^u \right]_{-2}^{1} \\&= \frac{1}{3} [e^{-2} - e^1] \end{align}$$
</p>

(c) $\int_0^{\pi /2} cos (1-x)dx$
<p align='center'>
    $$\begin{align} \int_0^{\pi /2} cos (1-x)dx &= -\int_1^{\pi /2 -1} cos(u)du \\& = -\left[sin(u) \right]_1^{\pi / 2 -1} \\& = -[sin(\frac{\pi}{2} -1)- sin(1) ] \end{align}$$
</p>

(d) $\int_{-1}^1 \frac{1}{7x+5}dx$
<p align='center'>
    $$\begin{align} \int_{-1}^1 \frac{1}{7x+5}dx &= \frac{1}{7} \int_{-2}^2 \frac{1}{u} du \\ &= \frac{1}{7} \left[ln|u| \right]_{-2}^2 \\ &= \frac{1}{7} [ln(2) - ln (-2)] \end{align}$$
</p>


```Python
from scipy.integrate import quad
import numpy as np

f_a = lambda x: np.sin(7*x -3)
result_a = quad(f_a, 0, 1)
print('(a):', result_a)

f_b = lambda x: np.exp(3*x -2)
result_b = quad(f_b, 0, 1)
print('(b):', result_b)

f_c = lambda x: np.cos(1-x)
result_c = quad(f_c, 0, 3.14/2)
print('(c):', result_c)

f_d = lambda x: (1 / (7*x -5))
result_d = quad(f_d, 1, 2)
print('(d):', result_d)
```
```
(a): (-0.0480498393909762, 6.830516278251511e-15)
(b): (0.8609821817408109, 9.558822419606492e-15)
(c): (1.381103033541866, 1.5333323872178293e-14)
(d): (0.21486819953946773, 8.099013171248273e-11)
```

```Python
import matplotlib.pyplot as plt
import numpy as np

# Create figure 1
fig = plt.figure(figsize=(28, 6))
x_a = np.linspace(0, 2, 400)
y_a= f_a(x_a)

ax1 = fig.add_subplot(1, 4, 1)
ax1.plot(x_a, y_a, label=r'$f(x)= 7x-3', color='navy')
ax1.set_xlabel('x')
ax1.set_ylabel(r'f(x)')
ax1.set_title(r'Visualization $\int_0^1 7x-3$')
ax1.legend()

# Create figure 2
x_b = np.linspace(0, 2, 400)
y_b = f_b(x_b)

ax2 = fig.add_subplot(1, 4, 2)
ax2.plot(x_b, y_b, label=r'$f(x)= e^{3x-2}$', color='C2')
ax2.set_xlabel(r'x')
ax2.set_ylabel(r'f(x)')
ax2.set_title(r' Visualization $\int_0^1 e^{3x-2}$')
ax2.legend()

# Create figure 3
x_c = np.linspace(0, 2, 400)
y_c = f_c(x_c)

ax3 = fig.add_subplot(1, 4, 3)
ax3.plot(x_c, y_c, label=r'$f(x)= cos (1-x)$', color='C1')
ax3.set_xlabel(r'x')
ax3.set_ylabel(r'f(x)')
ax3.set_title(r'Visualization $\int_0^{\pi / 2} cos (1-x)$')
ax3.legend()

# Create figure 4
x_d = np.linspace(0, 2, 400)
y_d = f_d(x_d)

ax4 = fig.add_subplot(1, 4, 4)
ax4.plot(x_d, y_d, label=r'$f(x)=\frac{1}{7x-5}$', color='C3')
ax4.set_xlabel(r'x')
ax4.set_ylabel(r'f(x)')
ax4.set_title(r'Visualization $\int_{1}^2 \frac{1}{7x-5} $')
ax4.legend()

plt.savefig('Integration by substitution 2.svg', bbox_inches='tight')
plt.show()
```

![Figure 3. Visualization of Integration by substitution](/quarto-workflows/images/integration/Integration by substitution 2.svg)
