---
date: "2026-1-11"
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Gaussian-Distribution-Function/blob/main/Gaussian-function.py)

# Gaussian Distribution Functions
The Gaussian distribution is defined by two parameters: the mean ($\mu$) and the standard deviation ($\sigma$). These determine the centre and spread of the distribution, respectively. The probability density function (PDF) of the Gaussian distribution describes the likelihood of observing a value x given the distribution's parameters.

## Standard Normal Probability Density Function (PDF)
In one dimension, the standard normal probability density function $f(x)$ describes the probability density of observing a value $x$ from a standard normal distribution. It is defined as:

<p align='center'>
    $f(x\;|\;\mu,\;\sigma)=\frac{1}{\sigma\sqrt{2\pi}}exp[-\frac{x-\mu^{2}}{2\sigma^{2}}]$
</p>

where:
- x is the value at which to evaluate the probability density function.
- $\mu$ is the mean of the distribution.
- $\sigma$ is the standard deviation of the distribution.

## Function arguments

This script requires the following function arguments:

- `make_gauss`: Plot multiple Gaussian curves by defining a Gaussian function factory.
- `N` (amplitudo): Controls the overall height of the Gaussian.  
- `sig` (standard deviation, $\sigma$): Determines the spread of the Gaussian.
- `mu` (mean, $\mu$): Sets the center of the Gaussian.
- `return lambda`: creates a function of `x` that computes the Gaussian formula.

This Python script demonstrates the Gaussian distribution function, also known as the normal distribution. 

```python
import numpy as np
import matplotlib.pyplot as plt

def make_gauss(N, sig, mu):
    return lambda x: N/(sig * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2/(2 * sig**2))

def main():
    fig, ax = plt.subplots()
    x = np.arange (-5, 5, 0.01)

    variances = [0.2, 1, 5, 0.5]
    sigmas = np.sqrt(variances)
    mus = [0, 0, 0, -2]
    colors = ['b', 'r', 'y', 'g']

    for var, sig, mu, color in zip(variances, sigmas, mus, colors):
        gauss = make_gauss(1, sig, mu)(x)
        ax.plot(x, gauss, color, linewidth=2, label=f'$\\sigma^{2}={var}, \\mu={mu}$') 

    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 1)
    ax.set_ylabel(r'$\phi_{\mu,\sigma^{2}}(x)$', fontsize=14)
    ax.set_xlabel(r'$x$', fontsize=14)
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title("Gaussian Functions with Different Variable")
    plt.savefig('Gaussian Functions with Different Variable.svg', bbox_inches='tight')
    plt.show()

main()
```

![Figure 1. Gaussian function with different variables](/quarto-workflows/images/Gaussian/Gaussian Functions with Different Variable.svg)

    
    
## Two-dimensional Gaussian Function

In two dimensions, the circular Gaussian is the distribution function for uncorrelated variates $x$ and $y$ having a bivariate normal distribution and equal standard deviation $\sigma=\sigma_{x}=\sigma_{y}$.

<p align='center'>
    $(x,\;y)=exp(-x^{2}-y^{2})$
</p>
<p align='center'>
    $f(x,\;y)=A\;exp(-(\frac{(x-x_{0})^{2}}{2\sigma_{X}^{2}}\;+\;\frac{(y-y_{0})^{2}}{2\sigma_{Y}^{2}}))$
</p>

where:
- A is Amplitude
- $x_{0}$ and $y_{0}$ are the centre
- $\sigma_{x}$ and $\sigma_{y}$ are the X and Y spreads of the blob.

## Function arguments

This script requires the following function arguments:

- `X, Y`: are the meshgrid coordinates.
- `Z`: is the function value at `X, Y`.
- `fig.add_subplot(111)`: is to set up a 3D subplot with 1 row, 1 column, and the first subplot.
- `projection='3d'`: is matplotlib to make a 3D axis.

This Python script demonstrates the Gaussian distribution function, also known as the normal distribution. 

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Define grid
x = y = np.linspace(0, 1, 40)
X, Y = np.meshgrid(x, y)

# Gaussian parameters
x0 = y0 = 0.5
sig_X, sig_Y = 0.2, 0.4

# Gaussian function
f = np.exp(-(X-x0)**2/sig_X**2 - (Y-y0)**2/sig_Y**2)

# Create 3D plot
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot(111, projection='3d')

# Plot surface 
surf = ax.plot_surface(X, Y, f, cmap=cm.twilight, edgecolor = 'none')

# Add label
ax.set_xlabel('X position [a.u.]')
ax.set_ylabel('Y position [a.u.]')
ax.set_title('2D Gaussian Surface', fontsize=14)
ax.grid(True, alpha=0.6)

# Add color bar
cbar= fig.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_label('Amplitudo [a.u.]')
plt.savefig('2D Gaussian surface.svg', bbox_inches='tight')
plt.show()
```
![Figure 2. Two-dimensional Gaussian Surface](/quarto-workflows/images/Gaussian/2D Gaussian surface.svg)
