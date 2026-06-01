---
title: "Adiabatic process and Carnot Cycle"
date: "2026-1-23"
---



# Maxwell-Boltzmann Distribution

Write a function to the plot the Maxwell-Boltzmann Distribution of molecular speed for a gas of particles of a given mass at a given temperature, indicating the modal speed ($v_{*}$), mean ($\langle v \rangle$), and root mean square (rms, $\langle v^{2} \rangle^{1/2}$) speeds with vertical lines.

Call this function for the atomic gasses Helium (m = 4u), and Argon (m = 40u) at 300 K.

__Hints__: The modal speed is the maximum of the probability distribution and can be found $df/dv$. The mean and rms speeds can be obtained, respectively, from the integrals.

$\langle v\rangle = \int_{0}^{\infty} vf(v)$ and $\langle v^{2} \rangle = \int_{0}^{\infty} v^{2}f(v) dv$.

The following expression for the different types of average speed can be derived:

- $v_{*} = \sqrt{\frac{2k_{B}T}{m}}$ (mode)
- $\langle v \rangle = \sqrt{\frac{8k_{B}T}{\pi m}}$ (mean)
- $\langle v^{2} \rangle^{1/2} = \sqrt{\frac{3k_{B}T}{m}}$ (rms speed).

```python
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import ipywidgets as widgets
from ipywidgets import interact

# Boltzman constant, J.K-1, atomis mass unit (kg)
kB = 1.381e-23
u = 1.661e-27

# Gas particle masses, in kg
m_He = 4 * u
m_Ar = 40 * u

# Temperature in K
T = 300

# The value of the Maxwell-Boltzmann distribution
def fMB(v, T, m): # mass in kg, at temperature in K, at the speed v (in m.s-1)
    fac = m /2 /kB/T
    return (fac / np.pi)**1/5 * 4 * np.pi * v**2 * np.exp(-fac * v **2)

# Speed range
v= np.linspace(0, 3000, 3000)

# Temerature to include in dropdown menu
temperatures = [100, 200, 300, 400, 500, 800, 1000]

fig = go.Figure()

# Add traces for each temperature
for T in temperatures:
    fig.add_trace(go.Scatter(
    x=v, y=fMB(v, T, m_He),
    visible=(T==300),
    mode='lines',
    name=f"He, T={T}K",
    line=dict(color='orange', dash='solid')   # solid orange line
    ))

    fig.add_trace(go.Scatter(
    x=v, y=fMB(v, T, m_Ar),
    visible=(T==300),
    mode='lines',
    name=f"Ar, T={T}K",
    line=dict(color='blue', dash='dash')      # dashed blue line
    ))            

# Create dropdown menu
buttons = []
for i, T in enumerate(temperatures):
    visible = [False] * (2*len(temperatures))
    visible[2*i] = True   # He trace
    visible[2*i+1] = True # Ar trace
    buttons.append(dict(label=f"T={T}K",
                        method="update",
                        args=[{"visible": visible},
                              {"title": f"Maxwell-Boltzmann Distribution at T={T}K"}]))

fig.update_layout(
    title="Maxwell-Boltzmann Distribution at T=300K", 
    updatemenus=[dict(
        type="dropdown",
        buttons=buttons,
        x=1.05, y=1.0,
        xanchor="right", yanchor="top"
    )],
    margin=dict(l=80, r=170, t=80, b=60),
    xaxis_title="Speed (v) / m.s-1",
    yaxis_title="Density f(v) / s.m-1",
    template="plotly_white"
)

fig.show()
# Save as standalone HTML
fig.write_html("index.html", auto_open=True)
```
