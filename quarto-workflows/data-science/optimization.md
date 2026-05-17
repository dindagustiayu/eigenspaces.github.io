[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Mathematical-Optimization/blob/main/Mathematical%20Optimization%20use%20SciPy.html)

# Mathematical Optimization
Optimization comes from the same root as optimal, which means _best_. When you optimize something, you are __making it best__. But _best_ can vary. 

_People optimize_. If you are a football player, you might want to maximiza your running yards, and also minimize your fumbles. Both maximizing and minimizing are types of optimization problems. 

_Nature optimize_. Physical systems tend to a state of minimum energy. The molecules in an isolated chemical system react with each other until the total potential energy of their electrons is minimized. Rays of light follow paths that minimize their travel time.

Optimization is an important tool in decision science and in the analysis of physical systems. The process is:
1. We must first identify some _objective_, a quantitative measure of the performance of the system under study (time, potential energy, or any values).
2. The objective depends on certain characteristics of the systems, called _variables_ or _unknowns_.
3. Often the variables are restricted, or _constrained_, in some way. For instance, such as electron density in a molecule and the interest rate on a loan, cannot be negative.
4. The process of identifying objective, variables and constraints for a given problem is known as _modelling_.
5. Once the model has been formulated, an optimization algorithm can be used to find its solution.
6. After optimization, we must be able to recognize whether it has succeeded in its task of finding a solution. In many cases, there are ellegant mathematical expression known as _optimally conditions_ for checking that the current set of variables is indeed the solution of the problem.

## Prerequisites
- Linear Algebra
- Calculus I (Derivatives)
- Computer programming skills

## Preliminaries

- `scipy.optimize`: provides a range of algorithms for the minimization of multidimensional functions (with or without constraints).
- `scipy.optimize.minimize`: minimize routine which implements several different algorithms for minimization.
- `scipy.optimize.minimize_scalar`: provide a way to minimize a function of a single variable.

## Constrained and Unconstrained Optimization
Problems can be classified according to the nature of the objective function and constraints (linear, nonlinear, convex). 
- _Unconstrained optimization_ problems arise directly in many practical applications. If there are natural constraints on the variables, it is sometimes safe to disregard them and to assume that they have no effect on the optimal solution.
- _Constrained optimization_ problems arise from models that include explicit constraints on the variables. These constraints may be simple bounds such as $0 \leq x_1 \leq 100$, more general linear constraints such as $\sum_i x_i \leq 1$, or nonlinear inequalities that represent complex relationships among the variables.

When both the objective function and all the constraints are linear functions of $x$, the problem is a _linear programming_ problem. Management sciences and operations research make extensive use of linear models.

## Optimization Algorithms
Optimization algorithms are iterative. They begin with an initial guess of the optimal values of the variables and generate a sequence of improved estimates until they reach a solution. The strategy used the values of the objective function $f$, the constraints $c$, and possibly the first and second derivatives of these functions.

## Mathematical Formula
In mathematics, optimization is the minimization or maximization of a function subject to constraints on its variables. We use the following notation:

- $x$ is the vector of _variables_, also called _unknowns_ or _parameters_.
  Variables, $x_1 \ x_2 \ x_3$ and so on, which are the __inputs__ things we can control. They abbreviated $x_n$ to refer to individuals or $x$ to refer to them as a group.
  
- $f$ is the _objective function_, a function of x that we want to maximize or minimize. The objective function, $f(x)$, which is the __output__ we are trying to maximize or minimize.

- $c$ is the vector of _constraints_ that the unknowns must satisfy. This is a vector function of the variables $x$. The number of components in $c$ is the number of individual restrictions that we place on the variables. _Constraints_, which are equations that place limits on how big or small some variables can get.

    - Equality constraints are noted $h_n (x)$
    - Inequality constraints are noted $g_n (x)$


The optimization problem can then be written as 
<p align='center'>
    $$ \begin{align} \min_{x \ \in \ R^n} \ f(x) \quad \mbox{subject \ to} \ \left \{\begin{array} \\ c_i (x) = 0, \quad i \ \in \ \varepsilon \\ c_i(x) \geq 0, \quad i \ \in \ \imath \end{array} \right \} \end{align}$$
</p>

## Derivatives
Most algorithms for nonlinear optimization and nonlinear equations require kbowledge of derivatives. Sometimes the derivatives are easy to calculate by hand, and it is reasonable to expect the user to prive code to comoute them. In other cases, the functions are too complicated, so we look for ways to calculate or approximate the derivatives automatically. 

### The Jacobian matrix
The first derivative in minimization known as the _Jacobian_. Let $f: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a function such that each of its first-order partial derivatives exists on $\mathbb{R}^n$. This function takes a vector $x = (x_1, \ldots, \ x_n) \in \mathbb{R}^n$ as input and produces the vector $f(x) = (f_1(x), \ldots, \ f_m(x)) \in \mathbb{R}^m$ as output. Then the Jacobian matrix of $f$, denoted $J_f$, is the $m \times n$ matrix whose (i, j) entry is $\frac{\partial f_i}{\partial x_j}$; explixity;

<p align='center'>
    $$J_f = \left[\frac{\partial f}{\partial x_1} \ \cdots  \ \frac{\partial f}{\partial x_n} \right] =\left [\begin{array} \bigtriangledown^T f_1 \\ \vdots \\ \bigtriangledown^T f_m \end{array} \right] = \left [\begin{array} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{array} \right]$$
</p>

where $\bigtriangledown^T f_i$ is the transpose (row vector) of the gradient of the $i$-th component.

Furthermore, some sophisticated optimization algorithms require information about the second derivatives of the function, a symmetric matrix of values called the _Hessian_. 

### The Hessian matrix
In mathematics, the Hessian matrix is a square matrix of second-order partial derivatives of a scalar-valued function, or scalar-field. Suppose $f: \mathbb{R}^n \rightarrow \mathbb{R}$ is a function taking as input a vector $x \in \mathbb{R}^n$ and outputting a scalar $f(x) \in \mathbb{R}$. If all second-order partial derivatives of $f$ exist, then the Hessian matrix $\mathbf{H}$ of $f$ is a square $n \times n$ matrix, usually defined and arranged as,

<p align='center'>
    $$\mathbf{H_f} = \left [\begin{array} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \ \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \ \partial x_n} \\ \frac{\partial^2 f}{\partial x_2 \ \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \ \partial x_n} \\ \vdots & \vdots & \ddots & \vdots \\ \frac{\partial^2 f}{\partial x_n \ \partial x_1} & \frac{\partial^2 f}{\partial x_n \ \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{array} \right]$$
</p>

That is, the entry of the $i$-th row and the $j$-th column is
<p align='center'>
    $$(\mathbf{H_f})_{i, \ j} = \frac{\partial^2 f}{\partial x_i \ \partial x_j}$$
</p>

Reference:
- [Jacobian Matrix](https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant#:~:text=The%20Jacobian%20matrix%20represents%20the,differential%20of%20f%20at%20x.)
- [Hessian Matrix](https://en.wikipedia.org/wiki/Hessian_matrix)

## Example Multivariate scalar functions
The general algorithm for the mInimization of a multivariate scalar function is `scipy.optimize.minimize`, which takes two mandatory arguments:

```
minimize(func, x0, ...)
```
- `fun`: a function object, this function should take an array of values, `x`, defining the point at which it is to be evaluated $(x_1, \ x_2, \ldots, \ x_n)$

- `x0`: is an array of values representing the initial guess for the minimization algorithms to start at.

### Example 1
Here $f$ and each $c_i$ are scalar-valued functions of the variables $x$, and $\mathcal{I}, \ \mathcal{I}$ are sets of indices. As a simple example, consider the problem
<p align='center'>
    $$\begin{align} \mbox{min} \ (x_1 - 2)^2 + (x_2 - 1)^2 \quad \mbox{subject \ to} \ \left \{\begin{array} \\ x_1^2 - x_2 \quad \leq \ 0 \\ x_1 + x_2 \quad \leq \ 2 \end{array} \right \} \end{align}$$ 
</p>

### Solution
- The objective function $f(x)$
<p align='center'>
    $$f(x_1, \ x_2) = (x_1 -2)^2 + (x_2 -1)^2$$
</p>
    Often, it is more natural or convenient to label the unknowns with two or three subscripts, or to use different variables by completely different names, so that relabeling is necessary to achieve the standard form.
    
- Calculate the constraints $c(x)$ with $\mathcal{E} = 0$ and $\mathcal{I} = [1, \ 2]$, these consraints are __inequality__ so $c_i (x) \geq 0$. We can write this problem by defining the constraints,

    Another common difference is that we are required to _maximize_ rather than _minimize_ $f$, but we can accommodate this change easily by _minimizing_ $-f$ in this formulation.

    - constraint 1: $-x_1^2 + x_2 \geq 0$
    - constraint 2: $-x_1 - x_2 + 2 \geq 0$


<p align='center'>
    $$\begin{align} f(x) &= (x_1 - 2)^2 + (x_2 -1)^2, \quad x =\left  [\begin{array} \ x_1 \\ x_2 \end{array} \right] \\ c(x) &= \left [\begin{array} \ c_1 (x) \\ c_2 (x) \end{array} \right] = \left [\begin{array} \ -x_1^2 + x_2 \\ -x_1 - x_2 + 2 \end{array} \right], \quad \imath= \{ 1, \ 2 \}, \quad \varepsilon = 0  \end{align}$$
</p>

This Python script to illustrate the multivariate optimization with initial variables:
<p align='center'>
    $$x= \left[\begin{array} \ 1 \\ 1  \end{array} \right]$$
</p>

```Python
from scipy.optimize import minimize

def f(vars):
    x1, x2 = vars # tuple
    return (x1 -2)**2 + (x2 -1)**2

x0 = [1, 1] # Initial guesses for x1, and x2
minimize(f, x0)
```
```
 message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 1.1102337951918135e-16
        x: [ 2.000e+00  1.000e+00]
      nit: 2
      jac: [-4.325e-13  2.879e-13]
 hess_inv: [[ 5.000e-01  3.725e-09]
            [ 3.725e-09  1.000e+00]]
     nfev: 9
     njev: 3
```

### Example 2
This Python script to demonstrate the use of `minimize` with _Himmelblau's function_. _Himmelblau's function_ is
<p align='center'>
    $$f(x, \ y) = (x^2 + y - 11)^2 + (x + y -7)^2$$
</p>

The region is $-5 \leq x \leq 5$, $-5 \leq y \leq 5$. 

```Python
from scipy.optimize import minimize

def f(X):
    x, y = X # tuple
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

x0 = [0, 0] # Initial guesses for x, and y
minimize(f, x0)
```
```
message: Optimization terminated successfully.
  success: True
   status: 0
      fun: 1.3782249516558895e-13
        x: [ 3.000e+00  2.000e+00]
      nit: 10
      jac: [-3.950e-06 -1.191e-06]
 hess_inv: [[ 1.578e-02 -9.481e-03]
            [-9.481e-03  3.495e-02]]
     nfev: 48
     njev: 16
```

### Example 3
This Python script to demonstrate the use of `minimize` with the two-dimensional function,
<p align='center'>
    $$f(x, \ y) = x^2 - ax -xy + by + 4y^2 $$
</p>

where $a$ and $b$ are constants. For example, to use $a = 4$, and $b = 10$.

```Python
from scipy.optimize import minimize

def f(X, a, b):
    x, y = X # tuple
    return x**2 - a*x - x*y + b*y + 4 * y**2

x0 = [0, 0] # Initial guesses for x, and y
minimize(f, x0, args=(4, 10)) # use constants a=4 and b=10
```
```
 message: Optimization terminated successfully.
  success: True
   status: 0
      fun: -8.266666666662827
        x: [ 1.467e+00 -1.067e+00]
      nit: 6
      jac: [ 3.576e-06  1.431e-06]
 hess_inv: [[ 5.419e-01  6.855e-02]
            [ 6.855e-02  1.337e-01]]
     nfev: 21
     njev: 7
```

## Example Univariate scalar functions
If the function to be minimized is _univariate_ (i.e., takes only one variable, a scalar), a faster algorithm is provided by `scipy.optimize.minimize_scalar`. To simply return a minimum, this function can be called with `method = brent`, which implements Brent's method for locating a minimum.

However, if it is possible to _bracket_ the required minimum by providing values for $x, \ (a, \ b, \ c)$ such that $f(a) > f(b)$ and $f(c) > f(b)$. 

For example, the function,
<p align='center'>
    $$f(x)=\left (\frac{x}{10} \right)^2 + sin \ x$$
</p>

where a, b, and c are -4, 0, and 1, respectively.

```Python
from scipy.optimize import minimize_scalar
import numpy as np

def f(x):
    return (x / 10)**2 + np.sin(x)

minimize_scalar(f, bracket=(-4, 0, 1))
```
```
message: 
          Optimization terminated successfully.
          The returned value satisfies the termination criteria
          (using xtol = 1.48e-08 )
 success: True
     fun: -0.9758098306412542
       x: -1.5399916226762196
     nit: 9
    nfev: 12
```

## Summary

The returned object summarizes how the algorithm proceeded. The most important information in this object is as follows:

| Key | Description |
|-----|-------------|
|`fun`| the value of the function at the minimum identified as x |
|`success`| `True` and `massage`: `Optimization terminated successfully` - the optimization was successful |
|`x`| this is the optimization, the values of $(x_1, \ x_2, \ldots, \ x_n)$ |
|`nit`| 2 (example) - the algorithm took two iterations|
|`jac`| Jacobian - the first derivative of the function |
|`hess_inv`| Inverse Hessian - the second derivatives use the quasi-Newton  method |
|`nfev`| the number of evaluations of the function|
|`njev`| the number of times the optimizer computed or approximated the gradient| 
