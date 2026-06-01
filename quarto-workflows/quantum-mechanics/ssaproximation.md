---
date: "2025-12-14"
---



[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/The-Steady-State-Approximation-for-Solve-Physics-Problems-/blob/main/Steady-State%20Approximation.py)


# Steady State Approximation

1. In chemistry
The __steady-state pproximation__ is widely used in chemical kinetics to calculations and help determine the overal reactions rate without considering the detailed time-dependent changes in intermediates concentrations.

2. In Physics
The __steady-state approximation__ is used in physics problems, such as semiconductors and Quantum optics, used in rate equations for excited states.

__The Pyhton Function Basics:__

- `def`: defines a function
- `return`: sends a result back from the function
- `for` loop: repeats code for each item in a list
- `fig`: the whole figure
- `ax`: the plotting area
- `ax.set_x or y ticks(ticks)`: sets the position of ticks on the x-axis or y-axis)
- `assert`: used for debugging
- `except`: used in try/except blocks for error handling.

Reference:
- [Cornell Chemical Engineering Lecture 7](https://duncan.cbe.cornell.edu/cheme2200/KINETICSLECTURES/ChemE_2200_lecture_K7.pdf)


## P7.1 - Particle Accelerator
An electric filed of strength _E_ will apply a force $F=qE$ onto a particle with electric charge _q_. In one dimension, with an initial velocity $v_{0}$, the particle's velocity and position will be given as 
<p align='center'>
   $$x(t)=v_{0}t + 0.5 \frac{qE}{m} t^{2}$$, and
</p>
<p align='center'>
   $$v(t)=v_{0} + \frac{qE}{m}t$$
</p>

a) Consider an electron, which has a mass $m\approx 9.1 \times 10^{-31}$ kg and electric charge $q\approx -1.6 \times 10^{-19}$ C, caught in an electric field of strength $E = 0.02 N/C$.
Make a program that asks the user for values for $v_{0}$ and $t$, and prints the position and velocity pf the electron.
Test your program by checking the electrons position and velocity at _t = 15 s_ with $v_{0} = 220$ m/s.

b) Rewrite your program to take $v_{0}$ and _t_, as well as _q_ and _m_ from the command line. Use a try/except block to initialize the variables, in case the user provides too few, or they cannot be converted to floats. In that case, ask the user for the parameters as input, like in excercise b).

Protons have mass $m\approx 1.67 \times 10^{-27}$ kg and electric charge $q\approx 1.6 \times 10^{-19}$ C. Neutrons have virtually the same mass as protons, and no electric charge. Check the position and velocity of these two particles with the same parameters as in exercise.

```python
# a) electron in an electric field
#parameters
me = 9.1e-31 # mass e in kg
mp = 1.67e-27 # mass proton in kg
mn = 1.67e-27 # mass neutron in kg
E = 0.02 # N/C
q = 1.6e-19 # electric  charge in C
v0 = 220 # in m/s
t = 15 # in s

# Calculate the position and velocity particle
# electron
xe = v0 * t + 0.5 * (q * E / me) * t**2
ve = v0 + (q * E /me) * t

# proton
xp = v0 * t + 0.5 * (q * E /mp) * t**2
vp = v0 + (q * E /mp) * t

# neutron
xn = v0 * t + 0.5 * (0 * E / mn) * t**2
vn = v0 + (0 * E/ mn) * t

# Make a while loop, which two lists
cw = 30 # column width
print(f'{"The Particles":^{cw}} | {"The position particles":^{cw}} | {"The velocity of particles":^{cw}}')
print('-' * cw * 3)
print(f'{'electrons':^{cw}} | {xe:^{cw}.3e} | {ve:^{cw}.3e}')
print(f'{'protons':^{cw}} | {xp:^{cw}.3e} | {vp:^{cw}.3e}')
print(f'{'neutrons':^{cw}} | {xn:^{cw}.2e} | {vn:^{cw}}')
```
```
        The Particles          |     The position particles     |   The velocity of particles   
------------------------------------------------------------------------------------------
          electrons            |           3.956e+11            |           5.275e+10           
           protons             |           2.156e+08            |           2.874e+07           
           neutrons            |            3.30e+03            |             220.0
```
```python
# Create bar
import numpy as np
import matplotlib.pyplot as plt

# Data
particles = ['Electron', 'Proton', 'Neutron']
positions = [xe, xp, xn]
velocities= [ve, vp, vn]

x = np.arange(len(particles))
width = 0.35

fig, ax=plt.subplots(figsize=(6,5))
ax.bar(x - width/2, positions, width, label='position (m)', edgecolor='black', hatch='//', color='royalblue')
ax.bar(x + width/2, velocities, width, label='velocity (m/s)', edgecolor='black', hatch='\\', color='salmon')

ax.set_title('Particle Accelerator')
ax.set_xticks(x)
ax.set_xticklabels(particles)
ax.set_ylabel('Value (Position & Velocity)')
ax.set_yscale('log')
ax.legend()
ax.grid(True, color='grey', zorder=0, linestyle='--')
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('Particle Accelerator.svg', bbox_inches='tight')
plt.show()
```
![Figure 1. Particle Accelerator](/quarto-workflows/images/ssa/Particle Accelerator.svg)


## P7.2 -Capacitor discharge
__Physical introduction__: A caoacitor is simply two metals plates set up parallel to each other. We can charge up each plate with positive and negative electic charges by connection them to a battery. If we remove the battery and connect the two plates together, the charges will flow from the negative plate to the positive plate, and the capacitor will discahrge. To avoid the electrical current becoming infinite, we connect a resistor between the plates. We now have an RC-circuit.
The cahrge _Q_ of a capacitor that discharge in a RC-circuit, is given as.
<p align='center'>
   $$Q(t) = CVe^{-t/RC}$$
</p>

The following program calculates this discharge for _n_ = 1000 time-steps over an interval _t_ = 10 s. The capacitor has a capacitance of _C_ = 0.007 F, an initial coltage $V_{0}$= 50 V, and the resistor has a resistance $R=35 \Omega$. 

a) RC-circuit discharge program and vectorize with Python list and loop.

b) RC-circuit discharge program  and vectorize it with NumPy
```python
# a) Vectorize with Python list
import numpy as np
import matplotlib.pyplot as plt

def Q_func(t, R, C, V0):
    return C* V0* np.exp(-t / (R *C))

V0 = 50 # in V
R = 35 # in omega
C = 0.007 # in F

t = 10 # in s
n = 1000 # in time-steps
dt = float(t)/n

t_list = []
Q_list = []
for i in range(n):
    t = dt * i
    t_list.append(t)
    Q_list.append(Q_func(t, R, C, V0))

plt.plot(t_list, Q_list, label='Charge Q(t)')
plt.title("Capacitor Discharge (Loop version)")
plt.xlabel("Time (s)")
plt.ylabel("Charge Q(t) [C]")
plt.legend()
plt.grid(True, color='black', zorder=0, linestyle='--')
plt.savefig('Capacitor Discharge (loop).svg', bbox_inches='tight')
plt.show()
```
![Figure 2. Capacitor Discharge (loop)](/quarto-workflows/images/ssa/Capacitor Discharge (loop).svg)

```python
# b) Vectorize with NumPy
t_max = 10
# time factor
t = np.linspace(0, t_max, n)

# Charge vector
Q = C * V0 * np.exp(-t / (R * C))
plt.plot(t_list, Q_list, label='Charge Q(t)', color='red')
plt.title("Capacitor Discharge (NumPy version)")
plt.xlabel("Time (s)")
plt.ylabel("Charge Q(t) [C]")
plt.legend()
plt.grid(True, color='black', zorder=0.5, linestyle='--')
plt.savefig('Capacitor Discharger (NumPy).svg', bbox_inches='tight')
plt.show()
```
![Figure 3. Capacitor Discharger (NumPy)](/quarto-workflows/images/ssa/Capacitor Discharger (NumPy).svg)


## P7.3 - Kinetic Friction Wooden Block
In this exercise, you are supposed to create a program which finds out hoe far a wooden block with initial velocity $v_{0}$ m/s will slide across surfaces of different materials. The material of the surfaces will affect the frictional force acting on the wooden block.

The position of the block can be expressed as such:
<p align='center'>
   $$x(t)=v_{0}t - \frac{1}{2}\mu gt^{2}$$
</p>

where $\mu$ is a coefficient of friction and g = 9.81 $m/s^{2}$.

One can find  by some calculations at which time _T_ the block will stop moving. The time _T_ is found to be
<p align='center'>
   $$T=\frac{v_{0}}{\mu g}$$
</p>

Define a function which takes a list of different coefficients of friction as a parameter, calculates the position at time _T_, that is $x(T)$, and then stories the results in a list. The list of the calculated positions must then be returned by the function. Distance before stopping.
<p align='center'>
   $$x(T)=\frac{v_{0}^{2}}{2 \mu g}$$
</p>

Let $v_{0}=5$ m/s and the list of coefficients of friction be [0.62, 0.3, 0.45, 0.2]. Call the function and write out every position along with corresponding coefficient of friction.

```python
# Calculate the kinetic friction 
g = 9.81 # gravitation in m/s^2

def position(t, v0, miu, g=9.81):
    return v0 * t -0.5 * miu * g * t**2 # Position x(t) under kinetic friction

def stop_time(v0, miu, g=9.81):
    return v0 / 2 * miu * g # stopping time when v(t)=0

def stop_distance(v0, miu, g=9.81):
    return v0**2 / 2 * miu * g # total distance before stopping

def analyze(v0, miu_list, g=9.81):
    results = []
    for miu in miu_list:
        T= stop_time(v0, miu, g)
        xT= stop_distance(v0, miu, g)
        results.append({'miu':miu, 'T_s':T, 'x_T':xT})
    return results

# parameters
v0 = 5.0
miu_list= [0.62, 0.3, 0.45, 0.2]

results = analyze(v0, miu_list)

# Make a while loop which two lists
cw = 28 # column width
print(f'{"Friction coefficient":^{cw}} | {"Stopping time T (s)":^{cw}} | {"Distances x(T) (m)":^{cw}}')
print('-' * cw * 3)
for r in results:
    print(f'{r['miu']:^{cw}} | {r['T_s']:^{cw}.3f} | {r['x_T']:^{cw}.4f}')
```
```
    Friction coefficient     |     Stopping time T (s)      |      Distances x(T) (m)     
------------------------------------------------------------------------------------
            0.62             |            15.206            |           76.0275           
            0.3              |            7.357             |           36.7875           
            0.45             |            11.036            |           55.1813           
            0.2              |            4.905             |           24.5250
```
```python
# Create plot
T_list=[r['T_s'] for r in results]
xT_list=[r['x_T'] for r in results]

# print plot
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6,5))
ax.set_facecolor('lightgrey')
ax.plot(miu_list, T_list, marker='o', label='Stopping Time')
ax.plot(miu_list, xT_list, marker='o', label='Stopping Distances')
ax.set_xlabel('Friction coefficient')
ax.set_ylabel('values')
ax.set_title('Stopping Time and Distances vs Friction Coefficient)')
ax.legend()
ax.grid(True, color='black', zorder=0, linestyle='--')
plt.savefig('Kinetic Friction.svg', bbox_inches='tight')
plt.show()
```
![Figure 4. Kinetic Friction](/quarto-workflows/images/ssa/Kinetic Friction.svg)


## P7.4 - Heisenberg's uncertainty relation
Heisenberg proved in 1972 that we cannot exactly know the velocity of an article and its position _at the same time_. This means that if we know precisely the velocity of a particle, we will not be able to have a precise mesurement of the position of the particle, and vice versa.
This can be written mathematically as:
<p align='center'>
   $$\Delta x \Delta p \geq \frac{h}{4\pi}$$
</p>
where,
- $\Delta x$ is the uncertainty (a measurement of how precise a measurement is) of the position of the particle
- $\Delta p$ is the uncertainty of the momentum of the particle.

we will use that Vi bruker at $h \approx 6.626 \times 10^{-34}$

write the program and use the function `assert` to test the relation.
Test your program where,
<p align='center'>
   $$\Delta x_{1} = 3.10165 \times 10^{-9}$ m, \Delta p_{1} = 1.7 \times 10^{-26} kgm/s$$
</p>
<p align='center'>
   $$\Delta x_{2} = 5.2 \times 10^{-32} m, \Delta p_{2} = 1 \times 10^{-3} kgm/s$$.
</p>

The uncertainties $\Delta x_{1}$ and $\Delta p_{1}$ does not violate the principle. However, the uncertainties $\Delta x_{2}$ and $\Delta p_{2}$ will violate with the principle (and your program should therefore display an error message for this case).

reference: 
- [Heisenberg Equation](https://www.bing.com/videos/riverview/relatedvideo?q=Heisenberg+Quantum+Mechanics&mid=0C1F3C05C6A16C1995FF0C1F3C05C6A16C1995FF&FORM=VIRE)

```python
# parameters
h = 6.626e-34 # Planc's constant

import math
def check_uncertainty (delta_x, delta_p):
    '''
    Check Heisenbirg;s uncertainty relation:
    Delta_x * Delta_P >= h / 4* pi
    '''
    threshold = h / (4 * math.pi)
    product = delta_x * delta_p

    # use the function assert to test the relation
    assert product >= threshold, (f'Violation detected delta_x * delta_P = {product}', f' is smaller than threshold {threshold}')
    print(f'delta_x * delta_P = {product} >= {threshold}')

# TEST CASES
try:
    # case 1 satisfy the principle
    delta_x1 = 3.10165e-9 # in m
    delta_p1 = 1.7e-26 # in kg.m/s
    check_uncertainty(delta_x1, delta_p1)
    
    # case 2 violate the principle
    delta_x2 = 5.2e-32 # in m
    delta_P2 = 1e-3 # in kg.m/s
    check_uncertainty(delta_x2, delta_p2)

except AssertionError as e:
    print('Error:', e)
```
```
delta_x * delta_P = 5.272805e-35 >= 5.272803264634492e-35
Error: ('Violation detected delta_x * delta_P = 5.2e-35', ' is smaller than threshold 5.272803264634492e-35')
```

## P7.5 - Reflectivity
Crown glass has a refractive index of 1.51 in the visible spectral region. Calculate the reflectivity of the air-glass interface and the transmission of a typical glass window.

Solution:
The medium of glass is transparent, so that $\alpha=0$. 

1. The reflectivity
<p align='center'>
   $$R=\frac{(n-1)^{2} + k^{2}}{(n+1)^{2} + k^{2}}$$
</p>

2. Transmission
<p align='center'>
    $$T=\frac{1-R}{1+R}$$
</p>

```python
# The absorption coefficient of the medium transparent  = 0
k = 0
n = 1.51 # refractive index

# Calculate the reflecivity
R = ((n - 1) / (n + 1))**2

# Calculate the transmission
T = (1 - R)**2

print('Reflectivity per inter-face:', R)
print('Transmission through the glass:', T)
```
```
Reflectivity per interface: 0.04128505896731798
Transmission through the glass: 0.919134338159299
```

