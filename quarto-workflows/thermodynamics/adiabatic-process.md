---
title: "Adiabatic process and Carnot Cycle"
date: "2026-1-21"
---



[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Adiabatic-process/blob/main/Thermodynamics-Cycles.py)



## Introduction of Thermodynamics

Thermodynamics is the study of the relationship between heat (or energy) and work. In other words, thermodynamics looks at how we can put our energy into a system (whether it is a machine or molecule) and make it do work. Alternatively, we might be able to do some work on system and make it produce energy (like spinning the turbines in a power station to produce electricity).

In chemistry, we sometimes speak more broadly about "energetics" of reactions (rather than thermodynamics), because energy given off during a reaction may simply be lost to the surroundings without doing useful work. Nevertheless, the ideas are the same: energy can be added to a set of molecules in order to produce a reaction, or a reaction can occur between a set of molecules in order to release energy. 

Thermodynamics, on the other hand, is really concerned with the overall energy change from the beginning of a reaction to the end. It compares the energies of two sets of molecules to each other: the nergies of the reactants and the energies of the products. 


## Thermodynamics Cycles

A thermodynamic cycle consists of a linked sequence of thermodynamic processes that involve transfer of heat and work into and out of the system, while varying pressure, temperature, and other state variables within the system, and eventually return the system to its initial state.

Thermodynamics is concerned with the change in $U$ (and other functions) between states: 

<p align='center'>
    $\Delta U= U_{2}-U{1}$
</p>

since $U$ is a state function, the path between these states does not affect the value of $\Delta U$: We can choose the path that is easiest to calculate $\Delta U$ for, knowing that this quantity is the same for all paths.

## Internal Energy
The internal energy, $U$, of a thermodynamic system is the total energy, potential and kinetic, contained within it. For systems in equilibrium, the internal state can be thought of as entirely defined by the temperature, $T$, volume, $V$, pressure, $p$, and composition, $N_{i}$, of the system. 

## Adiabatic process
An adiabatic process is one in which no heat is gained or lost by the system. The first law of thermodynamics with Q=0 shows that all the change in internal energy is in the form of work done. 

An important alternative way the gas can expand is through an adiabatic process: if the cylinder is insulated so it is thermally isolated from its surroundings, $q=0$ and as it does expansion wirk its internal energy must decrease, $\Delta U = w < 0$ and its temperature drops. The reverse process, adiabatic compression, is familiar from inflating a bicycle tyre: As the air in the pump is compressed (rapidly enough that there is little time for heat flow to the surroundings) its temperature rises.

<p align='center'>
    $\frac{C_{v}}{nR} \frac{dT}{T} = -\frac{dV}{V}$
</p>

which can be integrated for a reversible expansion between the state ($V_{1}, T_{1})$) and ($V_{2}, T_{2})$) to give

<p align='center'>
    $\frac{C_V}{nR}ln \frac{dT}{T} = -ln\frac{V_{2}}{V_{1}}$
</p>

This expression is usually presented in the quivalent form $T_{1} V_{1}^{c}=T_{2} V_{2}^{c}$ where $c=\frac{C_{v}}{nR}$. The corresponding relation between pressure and volume is found from the fact that, for an ideal gas
<p align='center'>
    $\frac{T_{2}}{V_{2}} = \frac{p_{2}V_{2}}{p_{1}V_{1}}$
</p>
which leads to 
<p align='center'>
    $p_{1}V_{1}^{\gamma}=p_{2}V_{2}^{\gamma}$
</p>
for a (monoatomic) ideal gas. That is, $pV^{\gamma}$ is constant along an adiabat.


## Carnot Cycle

Another important thermodynamic cycle, the Carnot cycle, is based on a sequence of reversible isothermal and adiabatic processes between four states, A, B, C, and D.

   I. $A\rightarrow B$: _a reversible isothermal has expansion process_ from a state $(p_{A}, V_{A})$ to $(p_{B}, V_{B})$ at a high temperature, $T_{high}$. During this step, the system absorbs $q_{in}$, expands and does work surroundings.

II. $B\rightarrow C$: _a reversible adiabatic gas expansion process_ from state $(p_{B}, V_{B})$ to $(p_{C}, V_{C})$ at a lower temperature, $T_{low}$. This time the system is placed in thermal contact with a reservoir which receives heat.

III. $C\rightarrow D$: _a reversible isothermal gas compression process_ from state $(p_{C}, V_{C})$ to $(p_{D}, V_{D})$ at a contant temperature, $T_{low}$, and causes a loss of heat, $q_{out}$.

IV. $D\rightarrow A$: _a reversible adiabatic gas compression process_ from state $(p_{D}, V_{D})$ to $(p_{A}, V_{A})$. The system is insulated so no heat can flow and its temperature returns to $T_{high}$.


This Python script to illustrate the Carnot Cycle with labelled plot for states A, B, C, and D with following parameters:

- $V_{1}=0.2 m^{3}$
- $T_{high}$= 800 K$
- Isothermal compression ratio, $r_{i}=V_{B}/V_{A}=2$
- Adiabatic compression ratio,$r_{a}=V_{C}/V_{B}=2$


Demonstrate that the efficiency, defined as $\nu=w/q-hot$ where $w$ is the work done and $q-hot$ is the heat put into system in step $A\rightarrow B$, is given by,

<p align='center'>
    $\nu=1-\frac{T_{cold}}{T_{hot}}$
</p>


### Step 1: Set up and use function

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import R

# number of molecule gas
n = 1
```
```python
def get_p(V, T):
    """
    Return the pressure of 1 mol of an ideal gas at (V, T).
    """
    return n * R * T / V

def plot_isotherm(Vmin, Vmax, T, c='k'):
    """
    plot a single isoterm for temperature T between Vmin and Vmax.
    Returns the arrays of V, p values defining the isoterm.
    """
    V = np.linspace(Vmin, Vmax, 1000)
    p = get_p(V, T)
    plt.plot(V, p, c=c, label=f'{T:.1f} K', lw=1)
    return V, p

def plot_adiabatic(Vmin, Vmax, p0, V0, c='k', gamma=5/3):
    """
    plot a single adiabatic for between Vmin and Vmax.
    p0, V0, is a fixed point on the adiabatic, the function returns the arrays of V, p values defining the adiabatic.
    """
    V = np.linspace(Vmin, Vmax, 1000)
    p = p0 * (V/V0)**(-gamma)
    plt.plot(V, p, c=c, lw=1)
    return V, p

def carnot_cycle(V1, T_high, r_i, r_a):
    """
    Plot a p-V diagram for a Carnot Cycle for an ideal gas starting at a compressed state (V1, T_high) 
    defined by isothermal compression ratio 
    r_i = V2/V1 and adiabatic compression ratio, 
    r_a = V3/V2.
    """

    # Constant-volume heat capacity, "gamma" parameter (Cp/Cv)
    C_V, gamma = 3/2 * R, 5/3
```

### Step 2: Volumes at each state

```python
    # Calculate the state variables at each stage of the cycle.
    V2 = V1 * r_i
    V3 = V2 * r_a
    V4 = V3 * V1/V2
```


- $V_{1}$: initial compressed volume.
- $V_{2}$: after isothermal expansion (ratio, $r_{i}$).
- $V_{3}$: after adiabatic expansion (ratio $r_{a})$.
- $V_{4}$: after isothermal compression, derived so the cycle closes.


### Step 3: Pressures and Temperature

```python
    # State Pressure 
    p1, p2 = get_p(V1, T_high), get_p(V2, T_high)
    T_low = T_high * (V2/V3) ** (gamma - 1)
    p3, p4 = get_p(V3, T_low), get_p(V4, T_low)
```

- Compute pressures at each state using ideal gas law.
- $T_{low}$ is found from adiabatic relation, $TV^{\gamma-1}$


### Step 4: Plot the cycle

```python
# Plot the isotherms and adiabatic for the cycle.
    plot_isotherm(V1, V2, T_high, c='r')
    plot_adiabatic(V2, V3, p2, V2, c='g', gamma=gamma)
    plot_isotherm(V4, V3, T_low, c='b')
    plot_adiabatic(V1, V4, p1, V1, c='m', gamma=gamma)
```
- Red = isothermal expansion (high temperature).
- Green = adiabatic expansion.
- Blue = isothermal compression(low temperature).
- Magenta = adiabatic compression.


### Step 5: Work and Heat calculation

```python
# Step 1: isothermal expansion, V1 => v2 AT T_high
    w1 = - n * R * T_high * np.log(V2 / V1)
    q1 = -w1

    # Step 2: adiabatic expansion, (V2, T_high) => (V3, T_low)
    w2 = n * C_V * (T_low - T_high)
    q2 = 0

    # Step 3: Isothermal compression, V3 => V4, at T_low
    w3 = -n * R * T_low * np.log(V4 / V3)
    q3 = -w3

    # Step 4: adiabatic compression, (V4, T_low => V1, T_high).
    w4 = n * C_V * (T_high - T_low)
    q4 = 0
```


- Work and heat are calculated for each step.
- isothermal $w = -nRT(V_{final}-V_{initial})$.
- Adiabatic, $w = nC_{V}(T_{final}-T_{initial})$.
- Heat $q$ is zero for adiabatic steps.


### Step 6: Efficiency


```python
    # Total energy input through heating:
    q_in = q1

    # Total work done *on* the gas:
    w_total = w1 + w2 + w3 + w4

    # Efficiency
    eta = -w_total /q_in
    print('Efficiency = {:.1f} %'.format(eta * 100))
    
```


- Efficiency = work output/heat input
- Prints Carnot efficiency.



### Step 7: Plot Labels

```python
  # Label the states
    states = [(p1, V1), (p2, V2), (p3, V3), (p4, V4)]
    for i, (p, V) in enumerate(states):
        plt.text(V, p, "ABCD" [i])
```


### Step 8: Running the code

```python
# Run

plt.figure(figsize=(6, 5))
carnot_cycle(V1=0.01, T_high=800, r_i=2, r_a=2)
plt.savefig('Carnot Cycle p-V Diagram (Ideal Gas).svg', bbox_inches='tight')
plt.show()
```
- Creates a figure
- Runs the Carnot Cycle with chosen parameters.
- Saves the plot as an SVG.
- Displays the diagram.

```
Efficiency = 37.0%
```

![Figure 1. Carnot Cycle p-V Diagram (Ideal Gas)](/quarto-workflows/images/Carnot Cycle p-V Diagram (Ideal Gas).svg)

