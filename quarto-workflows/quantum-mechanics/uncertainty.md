---
title: "Uncertainty and The Gravitational Acceleration"
date: "2026-2-23"
---



[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Uncertainty-and-The-Gravitational-Acceleration/blob/main/Uncertainties.py)

# Propagation of Uncertainty
Propagation of Error (or Propagation of Uncertainty) is defined as the effect on a function by a variable's uncertainty. It is a calculus derived statistical calculation designed to combine uncertainties from multiple variables to provide an accurate measurement of uncertainty.

## Why we need to calculate error propagation
It's common for errors when combining many uncertain values or using calculations that amplify small differences (like multipication, division, or exponentation). Consequently, the final result can be much less precise than the original measurement error values suggest.

Understanding error propagation helps us avoid overconfidence in results and recognize when further precision in measurement is necessary.

## Formula for error propagation
If the uncertainties (random errors) in the measured quantities, $p,\;q,\;r,...$ can be assumed to be _uncorrelated_, a common approach is to propagate their uncertainties into an uncertainty in the function $y=y(p,\;q,\;r,...)$ with the formula:

<p align='center'>
    $$\sigma_y=\sqrt{\left (\frac{\partial y}{\partial p} \right)^2 \; \sigma_p^2 \;+\; \left (\frac{\partial y}{\partial q} \right)^2 \; \sigma_q^2 \;+\; \left (\frac{\partial y}{\partial r} \right)^2 \; \sigma_r^2 \;+\;...}$$ 
</p>
    
This is effectively the first non-zero term in a multivariate Taylor series expansion of the variances, $\sigma_{i}^2$, and is therefore only approximate: For highly non-linear functions $y$ it might be expected to give flawed results.

This approach assumes that:
- The input variables are independent of each other.
- The errors are random and normally distributed.
- The function $y$ is differentiable with respect to each quantities $(p,\; q,\; r,...)$

## Error propagation worked example
## P20.1 Case study: Random uncertainties
Use the equation above to show that the uncorrelated random uncertainties, $\sigma p$, $\sigma q$ and $\sigma x$ in the paramters $p,\; q$ and $x$ propagate into an uncertainty in the following functions of $y$ as follows (the quantities $a,\; b$ and $c$ may be assumed to be precisely known):

1. If you measure,
<p align="center">
  $$y=ap\pm bq  \Rightarrow  \sigma y = \sqrt{a^2 \sigma_p^2 + b^2 \sigma_q^2}$$
</p>

<p align="center">
  $$\begin{align} y& = ap \pm bq \\ \frac{\partial y}{\partial p} &= a \; \; \; \frac{\partial y}{\partial q}= \pm b \\ \sigma_y &=\sqrt{\left (\frac{\partial y}{\partial p} \right)^2 \; \sigma_p^2 \; + \; \left(\frac{\partial y}{\partial q} \right)^2 \; \sigma_q^2} \\ &= \sqrt{a^2 \sigma_p^2 + b^2 \sigma_q^2} \end{align} $$
</p>

2. If you measure,
<p align="center">
   $$y = cpq \; \Rightarrow \; \sigma_y = |y| \sqrt{\left (\frac{\sigma_p}{p} \right)^2 \; + \; \left (\frac{\sigma q}{q} \right)^2}$$
</p>

<p align='center'>
    $$\begin{align} y& = cpq \\ \frac{\partial y}{\partial p} &=cq \;\;\; \frac{\partial y}{\partial q} = cp \\ \sigma_y &= \sqrt{\left (\frac{\partial y}{\partial p} \right)^2 \; \sigma_p^2 \; + \; \left (\frac{\partial y}{\partial q} \right)^2 \; \sigma_q^2} \\&= \sqrt{(cq)^2\; \sigma_p^2 \;+\; (cp)^2\; \sigma_q^2} \\ &=\sqrt{c^2 q^2 \sigma_p^2\;+\; c^2 q^2 \sigma_q^2} \\ &=c\sqrt{p^2 q^2 \left (\frac{\sigma_p}{p} \right)^2\;+\; p^2 q^2 \left(\frac{\sigma_q}{q} \right)^2} \\ &=|cpq| \sqrt{\left(\frac{\sigma_p}{p} \right)^2\; +\; \left(\frac{\sigma_q}{q} \right)^2} \\ &=|y| \sqrt{\left(\frac{\sigma_p}{p} \right)^2\; +\; \left(\frac{\sigma_q}{q} \right)^2}\end{align}$$
</p>

3. If you measure,
<p align="center">
    $$y=ln(bx) \; \Rightarrow \; \sigma_y=\left |\frac{a}{x} \right|\sigma_x$$

<p align='center'>
    $$\begin{align} y&=ln(bx)\\ &=\frac{\partial_y}{\partial_x}= \frac{a}{x} \\ &=\sqrt{\left (\frac{\partial y}{\partial x} \right)^2 \; \sigma_x^2} \\ &= \sqrt{\left (\frac{a}{x} \right)^2} \\ &=\left |\frac{a}{x} \right| \; \sigma_x \end{align}$$
</p>

4. If you measure,
<p align='center'>
    $$y=ae^{bx} \; \Rightarrow \; \sigma_y= |by| \sigma_x$$
</p>

<p align='center'>
    $$\begin{align} y&=ae^{bx} \\ y&=abx^{bx} \\ &=\frac{\partial y}{\partial x}=by \\ \sigma_y&=\sqrt{\left (\frac{\partial y}{\partial x} \right)^2 \sigma_x^2} \\&=\sqrt{(by)^2 \sigma_x^2} \\&=|by|\sigma_x \end{align}$$
</p>

## P20.2 Case study: The gravitational acceleration
A novel way to measure the gravitational acceleration, $g$, involves an indirect measurement of the pressure inside a submerged, inverted test tube containing a small amount of water. The experimental set-up proposed by Quiroga et. al.

Let the ambient pressure be $p_0$, and the length and cross-sectional area of the test tube be $l_0$ and A, respectively, so that it has a volume $V_0=Al_0$. Treating the $n$ moles of air inside it as an ideal gas at temperature $T$, we have $p_0 V_0=nRT$.

When the tube is submerged to a distance $h$, water rises inside it, and the air it contains is compressed to a pressure $p_1$ and volume $V_1$, where $p_1 V_1=p_0 V_0$ if the temperature is constant. The new pressure is $p_1=p_0 + \rho g l_1$, where $\rho = 1 g\;cm^-1$ is the water density, $g$ is the gravitational acceleration (to be determined) and $l_1$ is the measured distance from the bulk water surface to the top of the water level in the test tube.

The $V_1=A[l_0 - (h-l_1)]$, and so
<p align='center'>
    $$p_1=\frac{l_0}{l_0 - (h - l_1)} p_0$$
</p>

therefore, 
<p align='center'>
    $$\left [\frac{l_0}{l_0 - (h-l_1)} - 1 \right] \; p_0 = \rho g l_1 $$
</p>

That is, if measurements of $l_1$ are made for different submersion depths, $h$, a plot of the left-hand side of this equation against $l_1$ should yield a straight line with gradient $\rho g$, from which $g$ can be deduced.

Assuming that $\sigma_h$ and $\sigma l_1$ (the uncertainties in the measurements of $h$ and $l_1$, respectively) dominate and that they are connected, show that the uncertainty in the quantity,
<p align='center'>
    $$y=p_1 - p_0 = \left [\frac{l_0}{l_0 - (h-l_1)} -1 \right] \; p_0=\rho g l_1$$
</p>

is
<p align='center'>
    $$\sigma_y=\frac{l_0 p_0}{[l_0 - (h - l_1]^2} \sqrt{\sigma_h^2 + \sigma_{l_1}^2}$$
</p>

Use the following data to estimate $g$ from a linear least squares fit and the uncertainty in this estimate. Take an average value for $\sigma_y$, calculated using the above formula.

These data were collected on a day with an ambient air pressure of $p_0=1037$ mbar and using a test tube of length 20 cm. Take $\sigma_h = \sigma_{l_0} = 1 mm$. These data are given in the file [h and L1.txt](/quarto-workflows)

```
    # Measured distance, h and L1, in cm
    h	     L1
    29.9	 29.3
    35	     34.3
    39.9	 39.2
    45.1	 44.5
    50	     49.1
    55	     54
    59.9	 58.7
    65	     64
    70.1	 68.9
    74.9	 73.5
    80.1	 78.6
    85.1	 83.7
    90.1	 88.6
    95	     93.4
    
```
### Step 1: Calculate the uncertainties in the measurements of h and l1
<p align='center'>
    $$\begin{align} y &= p_1 - p_0 = \left [\frac{l_0}{l_0 - (h -l_1)} \right] \; p_0 = \rho g l_1 \\ \frac{\partial y}{\partial h} &=\frac{l_0 p_0}{[l_0 - (h -l_1)]^2} \\ \frac{\partial y}{\partial l_1} &= - \frac{l_0 p_0}{[l_0 - (h-l_1)]^2} \\ \sigma_y&=\sqrt{\left (\frac{\partial y}{\partial h} \right)^2 \sigma_h^2\;+\; \left (\frac{\partial y}{\partial l_1} \right)^2 \sigma_{l_1^2}} \\ &= \sqrt{\frac{l_0^2 p_0^2}{[l_0 - (h-l_1)]^4} (\sigma_h^2 + \sigma_{l_1}^2) } \\ &=\frac{l_0 p_0}{[l_0 - (h-l_1)]^2} \sqrt{\sigma_h^2 + \sigma_{l_1}^2 } \end{align}$$
</p>

### Step 2: Measured distance h and l1 in cm
```Python
import numpy as np
import matplotlib.pyplot as plt

# Open file data
h, l1 = np.genfromtxt('h and L1.txt', unpack=True, skip_header=2)

n = len(h)

# convert from cm to m
h = h /100
l1 = l1 / 100

# Parameters
p0 = 1037 * 100 # mbar to pa
rho = 1 * 1000 # g. cm-1 to kg. m-3
l0 = 20 / 100 # length the test tube (cm to m)
sig_h = sig_l1 = 1 /1000 # uncertainties (mm to m)

# Calculate the uncertainties
x = l1
z = l0 -(h-l1)
y = p1_minus_p0 = (l0 /z - 1) * p0
sigma_y= l0 * p0 / (z)**2 * np.sqrt(sig_h**2 + sig_l1**2)

#Plotting error bar
def plot_data():
    plt.figure(figsize=(6, 4))
    plt.errorbar(l1, p1_minus_p0, yerr=sigma_y, xerr=sig_l1, marker='o', c='k', ls='', capsize=4)
    plt.xlabel(r'$l_1 \; /\; \mathrm{m}$')
    plt.ylabel(r'$p_1 - p_0 \; /\;\mathrm{Pa}$')
    plt.savefig('Uncertainty in The gravitational acceleration.svg', bbox_inches='tight')
plot_data()
```

![Figure 1. Uncertainty in The gravitational acceleration](/quarto-workflows/images/Uncertainty in The gravitational acceleration.svg)

### Step 3: Measure a straight line fit, $y = a \pm bx$
A straight line fit, $y = a \pm bx$ through these data provides an estimated value for g:
<p align='left'>
    $$\hat{\beta}=\begin{pmatrix} a\\b\end{pmatrix}\;where\;a=\frac{S_y S_{xx} - S_{xy} S_x}{nS_{xx} - S^2_x}\;and\;b=\frac{nS_{xy} S_y S_x}{nS_{xx} - S^2_x},$$
</p>
where
<p align='center'>
    $$S_x=\overset{n}{\underset{i=1}{\sum x_i}},\;S_y=\overset{n}{\underset{i=1}{\sum Y_i}},\;S_{xx}=\overset{n}{\underset{i=1}{\sum x_i^2}},\;S_{xy}=\overset{n}{\underset{i=1}{\sum x_iy_i}}.$$
</p>

The uncertainty in the fitted parameter b is,
<p align='center'>
    $$\sigma_b = \sigma_y \sqrt{\frac{n}{nS_{xx} - S_x^2}}$$
</p>
and we can estimate the uncertainty in g:

```python
# Fit data
Sx, Sy, Sxx, Sxy = np.sum(x), np.sum(y), np.sum(x*x), np.sum(x*y)
Delta = n * Sxx - Sx**2
a = (Sy*Sxx - Sxy * Sx) / Delta
b = (n * Sxy - Sy * Sx) / Delta
print('a, b =', a, b)
g_est = b /rho
print('g-estimated =', g_est)

# Estimate uncertainty in the fitted parameter b
sigma_b = np.mean(sigma_y) * np.sqrt(n / Delta) /rho
print('sigma-b=',sigma_b)
```
```
a, b = 113.64118138687233 9633.702167054678
g-estimated = 9.633702167054679
sigma-b= 1.1051296914381148
```
The result of this experiment is therefore $g = 9.6 \pm 1.1 m.s^{-2}$.

