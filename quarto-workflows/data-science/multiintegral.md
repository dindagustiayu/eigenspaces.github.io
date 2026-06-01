---
date: "2026-3-07"
---


[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Multiple-Integrals/blob/main/Doble%20and%20Triple%20Integrals.html)

# Multiple Integrals
Most of the derivatives topics extended somewhat naturally from their __Calculus I__ counturparts and that will be the same here. However, because we are now involving functions of two or three variables there will be some differences as well. There will be new notation and some new issues that simply don't arise when dealing with function of a single variable. In mathematics (specifically multivariable calculus), a multiple integral is a definite integral of a function of several real variables, for instance, 
$f(x, y)$ or $f(x, y, z)$.

Integrals of a function of two variables over a region in $$\mathbb{R^2}$$ (the real-number plane) are called __double integrals__ or two dimensional planar regions and surfaces, and integrals of a function of three variables over region in $\mathbb{R^2}$ (real-number 3D space (volumes) are called __triple integrals__. When integrating over curves and surfaces, one can integral vector fields, where the one integrates either the tangential (for curves) or the normal (for surfaces) component of the vector field.

## Double integrals
A double integral is defined as the limit of sums. Why bother with sums and limits in the first place?. Two reasons. There has to be a definition and a computation to fall back on, when the single intagrals are difficult or impossible. And also, this we emphasize multiple integrals represent more than _area and volume_. The true applications are mostly to other things, but the central idea is always the same: _Add up small pieces and take limits_. We begin with the area of $R$ and the volume of $V$, by double integrals. 

__Question__: What is the volume above $R$ and below the graph of $z=f(x,y)$?. 

__Answer__: It is a double integral, __the integral of__ $f(x, y)$ over $R$.

For single integrals, the interval $[a,\; b]$ is divided into short pieces of length $\Delta x$. For double integrals, $R$ is divided into small rectangles of area $$\Delta A = (\Delta x)(\Delta y)$$. 

The simplest examples of such quantities are the __volumes__ that have the surface $f(x, y)$ as height. Suppose that $R =[a, b] \times [c, d]$ is a rectangle in the $xy$-plane, where $x$ runs from $a$ to $b$ and $y$ runs from $c$ to $d$. Let's figure out the volume of the solid over the rectangle $R$, between the $xy$-plane and the surface $z=f(x, y)$. We can divide the rectangle into a grid, $m$ subdivisions in one direction and $n$ in the other. 

With functions of one variable, we take the limit of the approximations of area under a curve $f$ and get an integral:
<p align='center'>
    $$A=\int_a^b f(x) dx = \lim_{m \rightarrow \infty} \sum_{i=1}^n f(x_i) \Delta x$$
</p>

Similarly, given our double sum approximation the volume, the limit of this sum is the defenition of a (double) integral. The double integral of $f$ over $R$ is:
<p align='center'>
    $$\lim_{m \rightarrow \infty} \lim_{n \rightarrow \infty} \sum_{i=1}^m \sum_{j=1}^n f(x_{ij},\; y_{ij}) \Delta A = \int \int_{R} f(x,\; y) dx \; dy = \int \int_{R} f(x, \; y) dA$$
</p>

(When we take the limit, it doesn't matter which sample point we take, so we take the upper-right corner of the rectangle $R_{ij}$). The __double integral__ of $f$ over the region $R$. The notation $dA$ indicates a small bit of area, without specifying any particular order for the variables $x$ and $y$. It is shorter and more 'generic' than writing $dx \; dy$.

## Triple Integrals
We can guess what triple integrals are like. Instead of a small interval or a small rectangle, there is a small box. Instead of length $dx$ or area $dx \; dy$, the box has volume $dV=dx dy dz$. The main problem will be to discover the correct limits on $x, y, z$. Then we add them all up and take the limit, to get an integral:
<p align='center'>
    $$\int_{x_0}^{x_1} \int_{y_0}^{y_1} \int_{z_0}^{z_1} dz \; dy \; dx$$
</p>

If the limits are constant, we are simply computing the volume of a rectangular box.

## Prior Knowledge
- Integration
- Limits
- Partial Derivatives
- Geometry
- Linear Algebra

## Preliminaries
- `scipy.integrate`: definite integrals.
- `dblquad`: double integrals.
- `tplquad`: triple integrals.


## Examples: Double Integrals
Shows the function $\int \int_R 1 + (x-1)^2 + 4y^2 \ dA$, where $R = [0, 3] \times [0, 2]$ in two ways.

  First,
<p align='center'>
    $$\begin{align} \int_0^2 \int_0^3 1 + (x-1)^2 + 4y^2 dx\; dy &= \int_0^2 \left [x + \frac{(x-1)^3}{3} + 4y^2 \; x \right]_0^3 \; dy \\ &=\int_0^2 3 + \frac{8}{3} + 12y^2 - (- \frac{1}{3}) \; dy  \\ &= \left [3y + \frac{8}{3} y + \frac{12}{3} y^3 + \frac{1}{3} y \right]_0^2 \\ &= 6 + \frac{16}{3} + 32 + \frac{2}{3} - 0 \\ &= 44 \end{align}$$
</p>


  Second,
<p align='center'>
    $$\begin{align} \int_0^3 \int_0^2 1 + (x-1)^2 + 4y^2 dy\; dx &= \int_0^3 \left [y + (x-1)^2 y + \frac{4}{3} y^3 \right]_0^2 \; dx \\ &= \int_0^3 2 + 2(x-1)^2 + \frac{32}{3}  dx \\ &= \left [2x + \frac{2}{3} (x-1)^3 + \frac{32}{3} x \right]_0^3 \\ &= 6 + \frac{16}{3} + 32 + \frac{2}{3} \\ & = 44 \end{align}$$
</p>

To calculate the integral, we can simply use `dlbquad`, the function must be defined with the innermost variable $(y)$ given as the first argument, and its limits themselves defined as functions the outermost variable $(x)$.
<p align='center'>
    $$\int_a^b \int_{c(x)}^{d(x)} f(x,\;y) \; dy\; dx$$
</p>

```Python
from scipy.integrate import dblquad

def func(y, x):
    return 1 + (x-1)**2 + 4*y**2

# Definite the limit
a, b = 0, 3 #Limits of the x integral
c, d = 0, 2 # limit of the y integral

result = dblquad(func, a, b, lambda x: 0, lambda x: 2)
print('result:', result)
```
```
result: (44.0, 4.884981308350689e-13)
```
## Exercises: Double Integrals
1. Compute $\int_0^1 \int_0^{x^2} x+2y^2 \ dy \ dx \Rightarrow$

   
<p align='center'>
    $$\begin{align} \int_0^1 \int_0^{x^2} x+2y^2 \; dy\; dx &= \int_0^1 \left [xy + \frac{2}{3} y^3 \right]_0^{x^2} dx \\ &= \int_0^1 x^3 + \frac{2}{3} x^6 \; dx \\ &=  \left [\frac{x^4}{4} + \frac{2}{21} x^7 \right]_0^1 \\ &= \frac{1}{4} + \frac{2}{21} \\ &= \frac{29}{84} \end{align}$$
</p>

```Python
from scipy.integrate import dblquad

def func(y, x):
    return x + 2*y**2

# Definite the limit
a, b = 0, 1 #Limits of the x integral

result = dblquad(func, a, b, lambda x: 0, lambda x: x**2)
print('result:', result)
```
```
result_1: (0.3452380952380953, 1.8335642853877514e-14)
```

2. Compute $\int_0^1 \int_{y^2 / 2}^{\sqrt{y}} \ dx \ dy \Rightarrow$

<p align='center'>
    $$\begin{align} \int_0^1 \int_{y^2 / 2}^{\sqrt{y}} \; dx \; dy &= \left [\sqrt{y} - \frac{y^2}{2} \right]_0^1 \\ &= \sqrt{1} - \frac{1}{2} - 0 \\ &= \frac{1}{2} \end{align}$$
</p>

```Python
from scipy.integrate import dblquad
import numpy as np

def func(x, y):
    return 1

# Definite the limit
a, b = 0, 1 #Limits of the x integral

result = dblquad(func, a, b, lambda y: y**2 / 2, lambda y:np.sqrt(y))
print('result:', result)
```
```
result: (0.5000000000000001, 6.6077499564637e-15)
```

3. Compute $\int_1^2 \int_1^x \frac{x^2}{y^2} \ dy \ dx \Rightarrow$

<p align='center'>
    $$\begin{align} \int_1^2 \int_1^x \frac{x^2}{y^2}\; dy\; dx  &= \int_1^2 \int_1^x x^2y^{-2}\; dy\;dx \\ &= \; \int_1^2 x^2 \left [-\frac{1}{y} \right]_1^x \; dx \\ &= \int_1^2 x^2 \left (-\frac{1}{x} + 1\right)\; dx \\ &= \int_1^2 x^2 - x \; dx \\ &= \left [\frac{x^3}{3} - \frac{x^2}{2} \right]_1^2 \\ &= \frac{8}{3} - \frac{4}{2} - \left (\frac{1}{3} - \frac{1}{2} \right) \\ & = \frac{5}{6} \end{align}$$ 
</p>

```Python
from scipy.integrate import dblquad

def func(y, x):
    return x**2 / y**2

# Definite the limit
a, b = 1, 2 #Limits of the x integral

result = dblquad(func, a, b, lambda x: 1, lambda x: x)
print('result:', result)
```
```
result: (0.8333333333333335, 2.213219007615129e-14)
```

4. Compute $\int_0^{\sqrt{\pi / 2}} \int_0^{x^2} x \ cos \ y \ dy \ dx \ \Rightarrow$
   
<p align='center'>
    $$ \begin{align} \int_0^{\sqrt{\pi / 2}} \int_0^{x^2} x\;cos\;y\;dy\;dx &= \int_0^{\sqrt{\pi / 2}} \left [x\; sin y \right]_0^{x^2} \; dx \\ &= \int_0^{\sqrt{\pi / 2}} x\;sin\; x^2 - sin\; 0 \; dx \end{align}$$
</p>

Use integration by substitution $(u)$:
<p align='center'>
    $$\begin{align} u &= x^2 \\ du &= 2x \; dx \\ x\; dx &= \frac{1}{2} \; du \end{align}$$
</p>

Change the limits:
<p align='center'>
    $$\begin{align} x &= 0 \Rightarrow u = 0^2 = 0 \\ x &= \sqrt{\pi / 2} \Rightarrow u = (\sqrt{\pi / 2})^2 = \pi / 2 \end{align}$$
</p>

Substitute the limits to integral:
<p align='center'>
    $$\begin{align} \int_0^{\pi / 2} \frac{1}{2} \; sin \; u \; du &= \frac{1}{2} \left [-cos \; u \right]_0^{\pi / 2} \\ &= \frac{1}{2} \;(-cos(\pi / 2) - (-cos(0)) \\ &= \frac{1}{2} \end{align}$$
</p>

```Python
from scipy.integrate import dblquad
import numpy as np

def func(y, x):
    return x* np.cos(y)

# Definite the limit
a = 0 
b = np.sqrt(np.pi / 2) #Limits of the x integral

result = dblquad(func, a, b, lambda x: 0, lambda x: x**2)
print('result:', result)
```
```
result: (0.4999999999999998, 1.3884045385060703e-14)
```
5. Compute $\int_0^{\sqrt{2} / 2} \int_{- \sqrt{1-2x^2}}^{\sqrt{1-2x^2}} x \ dy\ dx \Rightarrow$

<p align='center'>
    $$\begin{align} \int_0^{\sqrt{2} / 2} \int_{- \sqrt{1-2x^2}}^{\sqrt{1-2x^2}} x \; dy\; dx &= \int_0^{\sqrt{2} / 2} [xy]_{- \sqrt{1-2x^2}}^{\sqrt{1-2x^2}} \; dx \\ &= \int_0^{\sqrt{2} / 2} x(\sqrt{1-2x^2}) - x(-\sqrt{1-2x^2}) \; dx \\& = \int_0^{\sqrt{2} / 2} 2x(\sqrt{1-2x^2}) \; dx \end{align}$$
</p>

Use integration by substitution $(u)$:
<p align='center'>
    $$\begin{align} u &= 1-2x^2 \; dx \\ du &=  -4x \; dx \\ x \; dx &= -\frac{1}{4} \; du \end{align}$$
</p>

Change the limits:
<p align='center'>
    $$\begin{align} x &= 0 \Rightarrow u = 1 -2(0)^2 = 1 \\ x &= \frac{\sqrt{2}}{2} \Rightarrow u = 1 - 2 \left(\frac{\sqrt{2}}{2} \right)^2 = 0 \end{align}$$
</p>

Substitute the limits to integral:
<p align='center'>
    $$\begin{align} \int_1^0 2 \; -\frac{1}{4} \; \sqrt{u} \; du &= -\frac{1}{2} \int_1^0 u^{1/2} \; du \\ &= -\frac{1}{2} \left[\frac{2}{3}\; x^{3/2} \right]_1^0 \\& = \frac{1}{3} \end{align}$$
</p>

```Python
from scipy.integrate import dblquad
import numpy as np

def func(y, x):
    return x

# Definite the limit
a = 0 
b = np.sqrt(2) / 2 #Limits of the x integral

result = dblquad(func, a, b, lambda x: -np.sqrt(1-2*x**2), lambda x: np.sqrt(1-2*x**2))
print('result:', result)
```
```
result: (0.3333333333333327, 4.402013198401278e-10)
```

## Exercises: Triple Integrals

1. Evaluate $\int_0^1 \int_0^x \int_0^{x+y} 2x + y -1 \ dz \ dy \ dx \ \Rightarrow$

<p align='center'>
    $$\begin{align} \int_0^1 \int_0^x \int_0^{x+y} 2x + y -1 \; dz\;dy\;dx &= \int_0^1 \int_0^x \left [2xz+yz-z \right]_0^{x+y} \; dy\;dx \\ &= \int_0^1 \int_0^x 2x^2 + 3xy + y^2 - x - y \; dy\; dx \\&= \int_0^1 \left[2x^2 + \frac{3xy^2}{2} + \frac{y^3}{3} - xy - \frac{y^2}{2} \right]_0^x \; dx \\ &= \int_0^1 \frac{23}{6} x^3 - \frac{3}{2} x^2 \; dx \\ &= \left [\frac{23}{6} \times \frac{1}{4} x^4 - \frac{3}{2} \times \frac{1}{3} x^3 \right]_0^1 \\ &= \frac{11}{24} \end{align}$$
</p>

```Python
from scipy.integrate import tplquad

def func(z, y, x):
    return 2*x + y -1

# Definite the limit
a = 0 # x limits
b = 1 

result = tplquad(func, a, b, lambda x:0, lambda x:x, lambda x, y: 0, lambda x, y: x+y)
print('Result:', result)
```
```
Result: (0.4583333333333333, 4.407225152010278e-14)
```

2. Evaluate $\int_0^2 \int_{-1}^{x^2} \int_1^y xyz \ dz \ dy \ dx \Rightarrow$

<p align='center'>
    $$ \begin{align} \int_{-1}^{x^2} \int_1^y xyz \; dz\;dy\;dx &= \int_0^2 \int_{-1}^{x^2} \left [\frac{xyz^2}{2} \right]_1^y \; dy\; dx \\ &= \int_0^2 \int_{-1}^{x^2} \frac{xy^3}{2} - \frac{xy}{2} \; dy\; dx \\ &= \int_0^2 \left [\frac{1}{8} xy^4 - \frac{1}{4} xy^2 \right]_{-1}^{x^2} \; dx \\ &= \int_0^2 \frac{1}{8} x^9 - \frac{1}{4} x^5 + \frac{1}{8} x \; dx \\ &= \left [\frac{1}{80} x^{10} - \frac{1}{24} x^6 + \frac{1}{16} x^2 \right]_0^2 \\ &= \frac{1024}{80} - \frac{64}{24} + \frac{4}{16} \\ &= \frac{623}{60} \end{align}$$
</p>

```Python
from scipy.integrate import tplquad

def func(z, y, x):
    return x * y * z

# Definite the limit
a = 0 # x limits
b = 2 

result = tplquad(func, a, b, lambda x:-1, lambda x: x**2, lambda x, y: 1, lambda x, y: y)
print('Result:', result)
```
```
Result: (10.383333333333335, 6.501243052210528e-13)
```
3. Evaluate $\int_0^{\pi / 2} \int_0^{sin \ \theta} \int_0^{r\ cos \ \theta} r^2 \ dz \ dr \ d \theta \Rightarrow$

<p align='center'>
    $$\begin{align} \int_0^{\pi / 2} \int_0^{sin \; \theta} \int_0^{r\; cos \; \theta} r^2 \;dz\;dr\;d\theta &= \int_0^{\pi / 2} \int_0^{sin \; \theta} \left[r^2 z \right]_0^{r\; cos\; \theta} \; dr\; d\theta \\ &= \int_0^{\pi / 2} \int_0^{sin \; \theta} r^3\; cos \; \theta \; dr\; d\theta \\ &= \int_0^{\pi / 2} \left [\frac{1}{4} r^4 \; cos \theta \right]_0^{sin \; \theta} \\ & = \int_0^{\pi / 2} \frac{1}{4} \; (sin\; \theta)^4 \; cos \theta - 0 \; d\theta \end{align}$$
</p>

Change the limits:
<p align='center'>
    $$\begin{align} x &= 0 \Rightarrow u = sin \;(0) = 0 \\ x &= \pi / 2 \Rightarrow u = sin (\pi / 2) = 1 \end{align}$$
</p>

Substitute the limits to integral:

<p align='center'>
    $$\begin{align} \int_0^1 \frac{1}{4} (sin \; \theta)^4 \; d\theta &= \left [\frac{1}{4} \times \frac{1}{5} \; u^5 \right]_0^1 \\ &= \frac{1}{20} \end{align}$$
</p>

```Python
from scipy.integrate import tplquad
import numpy as np

def func(z, r, theta):
    return r**2

# Definite the limit
a = 0 # x limits
b = np.pi / 2 

result = tplquad(func, a, b, lambda theta:0, lambda theta: np.sin(theta), lambda r, theta: 0, lambda r, theta: r * np.cos(theta))
print('Result:', result)
```
```
Result: (0.19645573720394408, 9.392880388361082e-15)
```

4. Evaluate $\int_0^{2 \pi} \int_0^{\pi} \int_0^1 r^2 \ sin\ \theta \ dr \ d\theta \ d\phi $

<p align='center'>
    $$\begin{align} \int_0^{2 \pi} \int_0^{\pi} \int_0^1 r^2 \; sin\; \theta \; dr\; d\theta \; d\phi &=\int_0^{2 \pi} \int_0^{\pi} \left[\frac{1}{3} r^3 -cos\theta\right]_0^1 \; d\theta \; d\phi \\ &= \int_0^{2 \pi} \int_0^{\pi} \left[\frac{1}{3}-cos\theta + cos\theta \right] \; d\theta \; d\phi \\ &= \int_0^{2 \pi} \left [\frac{1}{3} sin \; \theta \right]_0^{\pi} \; d\theta \\ &= \int_0^{2 \pi} \frac{2}{3} \; d\phi \\ & = \left[\frac{2}{3} \; \phi \right]_0^{2 \pi} \\ &= \frac{4 \pi}{3} \end{align}$$
</p>

```Python
from scipy.integrate import tplquad
import numpy as np

def func(r, theta, phi):
    return r**2 * np.sin(theta)

# Definite the limit
a = 0 # x limits
b = 2 * np.pi

result = tplquad(func, a, b, lambda phi:0, lambda phi: np.pi, lambda theta, phi: 0, lambda theta, phi:1)
print('Result:', result)
```
```
Result: (4.18879020478639, 4.650491330678174e-14)
```

5. Evaluate $\int_1^2 \int_y^{y^2} \int_0^{ln(y + z)} e^x \ dx \ dz \ dy \Rightarrow$

<p align='center'>
    $$\begin{align} \int_1^2 \int_y^{y^2} \int_0^{ln(y + z)} e^x \; dx\; dz\; dy &=\int_1^2 \int_y^{y^2} \left[e^x \right]_0^{ln(y + z)} \; dz\; dy \\ & = \int_1^2 \int_y^{y^2} (y + z) - 1 \; dz\; dy \\ &= \int_1^2 \left [yz + \frac{1}{2} z^2 - z\right]_y^{y^2} \; dy \\ &= \int_1^2 y^3 + \frac{1}{2} y^4 - \frac{5}{2} y^2 + y \; dy \\ &= \left [\frac{1}{4} y^4 + \frac{1}{10} y^5 - \frac{5}{6} y^3 + \frac{1}{2} y^2 \right]_1^2 \\ &= \frac{151}{60} \end{align}$$
</p>

```Python
from scipy.integrate import tplquad
import numpy as np

def func(x, z, y):
    return np.exp(x)

# Definite the limit
a = 1 # x limits
b = 2 

result = tplquad(func, a, b, lambda y: y, lambda y: y**2, lambda y, z: 0, lambda y, z: np.log(y+z))
print('Result:', result)
```
```
Result: (2.5166666666666666, 8.83606086184683e-14)
```





