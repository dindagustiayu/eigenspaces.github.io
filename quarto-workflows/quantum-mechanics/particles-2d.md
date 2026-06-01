---
date: "2026-1-20"
---



[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Particle-in-2D-Box/tree/main)

# Particles in Multidimensions
In this work, we will discuss some particularly straightforward examples, such as the particle in a two-dimensional box. The novel feature, which occurs in multidimensional quantum problems, is called "degeneracy" where different wave functions with different PDF's (probability density function / $\Psi^{2}$) can have exactly the same energy. 

The wavefunction in one-dimensional (1D):
<p align='center'>
    $\Psi n_{x},n_{y}=\Psi n_{x}(x)\Psi n_{y}(y)$
</p>
    
Ultimately, the source of degeneracy is symmetry in the potential. With energy symmetry, there is a conserved quantity which can be used to "label" the states. For rotationally symmetric potentials, the conserved quantities, which serve to label the quantum states are angular momenta. 

The most generate case is the square, $L_{x} = L{y}$, for which clearly $E_{m, n} = E_{n, m}$. Note if the box were rectangular rather than square, then instead of having a length of $L$ on both sides, there would be two different lengths $L_{x}$ and $L_{y}$. The formulas for the energies and wavefunctions become only slightly more complicated:
<p align="center">
    $\Psi n_{x},n_{y}(x, y) = \frac{2}{\sqrt{L_{x}L_{y}}} sin(\frac{n_{x}\pi x}{L_{x}})sin(\frac{n_{y}\pi y}{L_{y}})$
</p>

This Python script visualized the particle in two-dimensional (contour and surface plots). Where the state is defined by $L_{x}$ and $L_{y}$ = 1 and the quantum number $n_{x}$= 1, 2,... and $n_{y}=$1, 2,the countour maps for the time-dependent solution, with being the highest point. 

## The key arguments:

- `Lx` and `Ly`: to set the boundaries of the particle-in-a-box problem. The wavefunction is defined only within $0\leq x\leq L_{x}$ and $0\leq y \leq L_{y}$.
- `npts = 101`: number of points used in the grid for plotting.
- `x` and `y`: are 1D arrays of evenly spaced points between 0 and box length.
- `X, Y`: are 2D arrays created by `np.meshgrid`, representing all coordinate pairs.
- `nx, ny`: Quantum numbers in x and y directions.
- `ax.contourf`: to make a filled contour plot.

```python
import numpy as np
import matplotlib.pyplot as plt

# Choose to use a square well and define a meshgrid of coordinate points
Lx = Ly = 1
npts = 101
x = np.linspace(0, Lx, npts)
y = np.linspace(0, Ly, npts)
X, Y = np.meshgrid(x, y)

def psi_nxny(x, y, nx, ny):
    """
    The two-dimensional particle-in-a-box wavefunction for state nx, ny.
    X, Y can be single point or compatible arrays of such points.
    """
    N = 2 / np.sqrt(Lx * Ly)
    return N * np.sin(nx * np.pi * x /Lx) * np.sin(ny * np.pi * y /Ly)

def contour_plot(ax, nx, ny):
    """
    Make a contour plot of the wavefunction defined by (nx, ny) on the provided Axes object, ax.
    """
    ax.contourf(X, Y, psi_nxny(X, Y, nx, ny), cmap='hot')

    # ratio: i.e squares appear square.
    ax.axis('square')
    
    # add labels and title
    ax.set_xlabel('$\\mathit{x}$ [a.u]')
    ax.set_ylabel('$\\mathit{y}$ [a.u.]')
    ax.set_title(f"Particle in 2D Box $\\Psi$({nx}, {ny})")

# A 2 x 2 grid of Axes
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6))

# Ensure that the x- and y-axes appear with the same aspect
contour_plot(axes[0, 0], 1, 1)
contour_plot(axes[1, 0], 2, 1)
contour_plot(axes[0, 1], 1, 2)
contour_plot(axes[1, 1], 2, 2)

# necessary to call tight-layout() to add some padding around
plt.savefig('Contour particle 2D.svg', bbox_inches='tight')
plt.tight_layout()
plt.show()
```
![Figure 1. Contour plots of the first four states of the particle in a two-dimensional square box](/quarto-workflows/images/particles2d/Contour particle 2D.svg)

```python
import numpy as np
import matplotlib.pyplot as plt

# Choose to use a square well and define a meshgrid of coordinate points
Lx = Ly = 1
npts = 101
x = np.linspace(0, Lx, npts)
y = np.linspace(0, Ly, npts)
X, Y = np.meshgrid(x, y)

def surface_plot(ax, nx, ny):
    """
    Make a surface plot of the wavefunction defined by (nx, ny) on the provided Axes object, ax. 
    Axes 3D must have been imported from mpl.toolkits.mplot3d for this work!.
    """

# plot the wavefunction in "3D", coloring the surface
    ax.plot_surface(X, Y, psi_nxny(X, Y, nx, ny), cmap='hot')

# create a 3D figure, and plot the wavefunction as a surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
   
# add labels and title
ax.set_xlabel('$\\mathit{x}$ [a.u]')
ax.set_ylabel('$\\mathit{y}$ [a.u.]')
ax.set_title(r'Particle Surface plot in 2D Box $n_{x}$=2, $n_{y}$=4')

# plot the chosen state
nx, ny = 2, 4
surface_plot(ax, nx, ny)

plt.savefig('Particle surface plot in 2D.svg', bbox_inches='tight')
plt.tight_layout()
plt.show()
```
![Figure 2. Surface plot of the $n_{x}$=2, $n_{y}=4$ state of the particle in a two-dimensional square box](/quarto-workflows/images/particles2d/Particle surface plot in 2D.svg)
