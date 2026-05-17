[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/-String-list-and-loops-and-Flow-Control-in-Python-for-Chemistry-Exercises/tree/main)

# Strings, List and Loops, and Comparison and Flow Control in Python for Chemistry Exercises.

## Key Equation
- Density Computations
  - $\rho=\frac{m}{v}=\frac{nA}{V_{C}N_{A}}$
- Avogadro's number
  - 6.022 x $10^{23}$, 1 amu/atom (or molecule) = 1 g/mol

# 1. Strings
## P3.1
Produce a nicely formatted list of the values of the physical constants, _h_, _c_, $k_{B}$, _R_, and _$N_{A}$_, to four significant figures, with their units.
```python
h, h_units = 6.62607015e-34, 'J.s'
c, c_units = 299792458, 'm.s-1'
kB, kB_units = 1.380649e-23, 'J.K-1'
R, R_units = 8.314462618, 'J.K.mol-1'
N_A, N_A_units = 6.02214076e+23, 'mol-1'

s1 = (f'h = {h:9.3e} {h_units}\t'
     f'c = {c:9.3e} {c_units}\t' 
      f'kB = {kB:9.3e} {kB_units}\t'
       f'R = {R:9.3e} {R_units}\t'
        f'N_A = {N_A:9.3e} {N_A_units}\t')

s2 = (f'h   = {h:9.3e}{h_units}\n'
      f'c   = {c:9.3e}{c_units}\n' 
      f'kB  = {kB:9.3e}{kB_units}\n'
      f'R   = {R:9.3e}{R_units}\n'
      f'N_A = {N_A:9.3e}{N_A_units}\n')
print(s1)

print(s2)
```
```
h = 6.626e-34 J.s	c = 2.998e+08 m.s-1	kB = 1.381e-23 J.K-1	R = 8.314e+00 J.K.mol-1	N_A = 6.022e+23 mol-1	
h   = 6.626e-34J.s
c   = 2.998e+08m.s-1
kB  = 1.381e-23J.K-1
R   = 8.314e+00J.K.mol-1
N_A = 6.022e+23mol-1
```

## P3.2
The following variables define some thermodynamic properties of $CO_{2}$ and $H_{2}O$.
```python
# Triple point of CO2 (K, Pa)
T3_CO2, p3_CO2 = 216.58, 5.185e5
# Entalphy of fusion of CO2 (kJ.mol-1).
DfusH_CO2 = 9.019
# Entrophy of fusion os CO2 (J.K-1.mol-1).
DfusS_CO2 = 40
# Entalphy of vaporization of CO2 (kJ.mol-1).
DvapH_CO2 = 15.326
# Entrophy of vaporization of CO2 (J.K-1.mol-1).
DvapS_CO2 = 70.8

# Triple point of H2O (K, Pa)
T3_H2O, p3_H2O = 273.16, 611.73
# Entalphy of fusion of H2O (kJ.mol-1).
DfusH_H2O = 6.01
# Entrophy of fusion of H2O (J.K-1.mol-1).
DfusS_H2O = 22.0
# Entalphy of vaporization of H2O (kJ.mol-1).
DvapH_H2O = 40.68
# Entrophy of vaporization of H2O (J.K-1.mol-1).
DvapS_H2O = 118.89

print(' '*22 + 'CO2' + ' '*9 + 'H20')
print('_'*40)
print('p3     /pa         ', f'{p3_CO2:5.0f}      {p3_H2O:5.2f}')
print('T3     /K          ', f'{T3_CO2:5.2f}      {T3_H2O:5.2f}')
print('DfusH  /kJ.mol-1   ', f'{DfusH_CO2:5.3f}       {DfusH_H2O:5.3f}')
print('DfusS  /J.K-1.mol-1', f'{DfusS_CO2:4.1f}      {DfusS_H2O:6.1f}')
print('DvapH  /kJ.mol-1   ', f'{DvapH_CO2:5.3f}    {DvapH_H2O:8.3f}')
print('DvapS  /j.k-1.mol-1', f'{DvapS_CO2:5.1f}       {DvapS_H2O:5.1f}')

```
```
                      CO2         H20
________________________________________
p3     /pa          518500      611.73
T3     /K           216.58      273.16
DfusH  /kJ.mol-1    9.019       6.010
DfusS  /J.K-1.mol-1 40.0        22.0
DvapH  /kJ.mol-1    15.326      40.680
DvapS  /j.k-1.mol-1  70.8       118.9
```

## P3.3
Nuclear binding energy and the mass defect. A neutron has a slightly larger mass than the proton. These are often given in terms of an atomic mass unit, where one atomic mass unit (u) is defined as 1/12th the mass of a carbon-12 atom.

```python
# Mass Particle constant, in kg.
atomic_kg = 1.660540 * 10 ** -27
neutron_kg = 1.674929 * 10 ** -27
proton_kg = 1.672623 * 10 ** -27 
electron_kg = 9.109390 * 10 ** -31

# Mass particle, in u.
atomic_u = 1.000 
neutron_u = neutron_kg / atomic_kg 
proton_u = proton_kg / atomic_kg
electron_u = electron_kg / atomic_kg

# Mass particle, in MeV/c2
atomic_ev = 931.5
neutron_ev = neutron_u * atomic_ev
proton_ev = proton_u * atomic_ev
electron_ev = electron_u * atomic_ev


title = '|' + ' '*19 + '{:43}'.format('Binding Nuclear Energy') + '|'
line = '+' + '-'*16 + '+' + ('-'*14 + '+')*3
row = '|{:<15} |' + ' {:12} |'*3
header = '| {:^14} |'.format('Particle') + (' {:^12} |'*3). format('Mass (kg)', 'Mass (u)', 'Mass (Mev/c2)')

print('+' + '-'*(len(title)-2) + '+',
      title,
      line,
      header,
      line,
      row.format('atomic mass', atomic_kg, f'{atomic_u:8.3f}', f'{atomic_ev:6}'),
      row.format('neutron', neutron_kg, f'{neutron_u:8.7f}', f'{neutron_ev:8.2f}'),
      row.format('proton', proton_kg, f'{proton_u:8.7f}', f'{proton_ev:8.2f}'), 
      row.format('electron', electron_kg, f'{electron_u:8.7f}', f'{electron_ev:8.3f}'),
      line,
      sep='\n')
                                                                   
```
```
+--------------------------------------------------------------+
|                   Binding Nuclear Energy                     |
+----------------+--------------+--------------+--------------+
|    Particle    |  Mass (kg)   |   Mass (u)   | Mass (Mev/c2) |
+----------------+--------------+--------------+--------------+
|atomic mass     |  1.66054e-27 |    1.000     |  931.5       |
|neutron         | 1.674929e-27 | 1.0086653    |   939.57     |
|proton          | 1.672623e-27 | 1.0072765    |   938.28     |
|electron        |  9.10939e-31 | 0.0005486    |    0.511     |
+----------------+--------------+--------------+--------------+
```

## 2. List and Loops
## P3.4
Straight-chain alkanes are hydrocarbons with the general stoichiometric formula $C_{n}H_{2n+2}$, in which the carbon atoms form a simple shain: for example, butane, $C_{4}H_{10}$ has the structural formula that may be depicted $H_{3}CC_{2}CH_{2}CH_{3}$. Write a progra, to output the structural formula of such an alkane, given its stoichiometry (assume $n\geq1$).

```python
# Assume n = 5
stoich = 'C5H12'
fragments = stoich.split('H')
nC = int(fragments[0][1:])
nH = int(fragments[1])
if nH != 2*nC + 2:
    print('{} is not alkane!'.format(atoich))
else:
    print('H\u2083C', end='')
    for i in range(nC-2):
        print('-CH\u2082', end='')
    print('-CH\u2083')
```
```
H₃C-CH₂-CH₂-CH₂-CH₃
```

## P3.5
Produce a table if the FCC element symbols abd their corresponding atomic radius (nm) and atomic weight (g/mol).
```python
symbols = ['Al', 'Cu', 'Au', 'Pb', 'Ni', 'Pt', 'Ag']
Atomic_radiuss = [0.1431, 0.1278, 0.1442, 0.1750, 0.1246, 0.1387, 0.1445]
Atomic_weigth = [26.981, 63.546, 196.966, 206.14, 58.693, 195.084, 107.868]
line = '-'*52
print(line)
print('Elements | Atomic Radii (nm) | Atomic weight (g/mol)')
print(line)
for i in range(len(symbols)):
    print(' '*2, symbols[i], ' '*5, Atomic_radiuss[i], ' '*13, Atomic_weigth[i])
    print(line)
```
```
----------------------------------------------------
Elements | Atomic Radii (nm) | Atomic weight (g/mol)
----------------------------------------------------
   Al       0.1431               26.981
----------------------------------------------------
   Cu       0.1278               63.546
----------------------------------------------------
   Au       0.1442               196.966
----------------------------------------------------
   Pb       0.175               206.14
----------------------------------------------------
   Ni       0.1246               58.693
----------------------------------------------------
   Pt       0.1387               195.084
----------------------------------------------------
   Ag       0.1445               107.868
----------------------------------------------------
```

## P3.6
reference: 
- [Atomic radii of the elements](https://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page))

Alumunium, copper and lead has an atomic radius of 121, 132, and 146 nm, respectively, an FCC crystal structure, and atomic weight of 26.98, 63.55, and 207.20 g/mol. Compute their theoretical density and compare the answer with their measured density.

in the FCC unit cell illustrated, the atoms touch one another across a face-diagonal, the length of which is _4R_. Because the unit cell is a cube, its volume is $a^{3}$, where _a_ is the cell edge length. From the right triangle on the face.

<p align='center'>
  $$a^{2} + a^{2} = (4R)^{2}$$
</p>

Solving for a,
<p align='center'>
  $$a=2R\sqrt{2}$$
</p>

The FCC unit cell volume $V_{C}$ may be computed from
<p align='center'>
  $$V_{C}=a^{3}=(2\sqrt{2})^{3}=16R^{3}\sqrt{2}$$
</p>

```python
import numpy as np
# Avogadro's number , in atoms/mol.
NA = 6.022 * 10 **23

# The number of atoms per unit cell in FCC
n = 4

# The atomic weight, and Radii of atoms (use floats/ints instead of strings)
Atomics = ['Al', 'Cu', 'Pb'] # use string ' '
A_weight = [26.98, 63.55, 207.20] # atomic weights in g/mol use float
Radii = [143 * 10 **-10, 128 * 10 **-10, 180 * 10 **-10] # radii in cm (converted from pm) use float/integers

# Computational density
for atom, weight, radius in zip(Atomics, A_weight, Radii):
    V_cell = 16 * (radius**3) * np.sqrt(2)
    m_cell = 4 * weight
    rho = m_cell / (V_cell *NA)
    print(f" {atom}: V_cell={V_cell:.3e} cm^3, m_cell={m_cell:.3e} g, rho={rho:.3f} g/cm^3")
```
```
 Al: V_cell=6.617e-23 cm^3, m_cell=1.079e+02 g, rho=2.708 g/cm^3
 Cu: V_cell=4.745e-23 cm^3, m_cell=2.542e+02 g, rho=8.895 g/cm^3
 Pb: V_cell=1.320e-22 cm^3, m_cell=8.288e+02 g, rho=10.429 g/cm^3
```

# 3. Comparison and Flow Control
    Table. Python comparison operators
| Symbols |         meaning              | 
|:--------|-----------------------------:|
| ==      |            Equal to          |
| !=      |         Not equal to         |
| >       |         Greater than         |
| <       |          Less than           |
| >=      |   Greater than or equal to   |
| <=      |    Less than or equal to     |

## P3.7
Determine whether each of the following electron configurations is an inert gas, a halogen, an alkali metal, an alkaline earth metal, or a transition metal. Justify your choices.

    (a) 1s2.2s2.2p6.3s2.3p5
    (b) 1s2.2s2.2p6.3s2.3p6.3d7.4s2
    (c) 1s2.2s2.2p6.3s2.3p6.3d7.4s2.4P6
    (d) 1s2.2s2.2p6.3s2.3p6.4s1
    (e) 1s2.2s2.2p6.3s2.3p6.3d7.4s2.4p6.4d10.5s2
    (f) 1s2.2s2.2p6.3s2

```python
# Electron configuration
configs = {
    '(a)': '1s2.2s2.2p6.3s2.3p5',
    '(b)': '1s2.2s2.2p6.3s2.3p6.3d7.4s2',
    '(c)': '1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6',
    '(d)': '1s2.2s2.2p6.3s2.3p6.4s1',
    '(e)': '1s2.2s2.2p6.3s2.3p6.3d7.4s2.4p6.4d5.5s2',
    '(f)': '1s2.2s2.2p6.3s2'}

def classify_configuration(cfg: str):
    subshells = cfg.split(".")
    parsed = []

    # Parse subshells into (n, orbital, electrons)
    for s in subshells:
        try:
            n = int(s[0])          # principal quantum number
            orbital = s[1]         # orbital type (s, p, d, f)
            electrons = int(s[2:]) # electron count
            parsed.append((n, orbital, electrons))
        except:
            continue

    if not parsed:
        return "Unknown"

    #Classify configuration electron by the last and the second-last subshells
    last_orbital, last_e = parsed[-1][1], parsed[-1][2]
    second_orbital, second_e = parsed[-2][1], parsed[-2][2] if len(parsed) >= 2 else (None, None)

    # Rules
    if last_orbital == "p" and last_e == 6:
        return "Inert gas (Noble gas)"
    elif last_orbital == "p" and last_e == 5:
        return "Halogen"
    elif last_orbital == "s" and last_e == 1:
        return "Alkali metal"
    elif last_orbital == "s" and last_e ==2:
        if second_orbital == "p" and second_e == 6:
            return "Akaline Earth metal"
        elif second_orbital =="d" and second_e <10:
            return "Transition metal"
 
# print results
for label, cfg in configs.items():
    print(f"{label} {cfg} => {classify_configuration(cfg)}")
```
```
(a) 1s2.2s2.2p6.3s2.3p5 => Halogen
(b) 1s2.2s2.2p6.3s2.3p6.3d7.4s2 => Transition metal
(c) 1s2.2s2.2p6.3s2.3p6.3d10.4s2.4p6 => Inert gas (Noble gas)
(d) 1s2.2s2.2p6.3s2.3p6.4s1 => Alkali metal
(e) 1s2.2s2.2p6.3s2.3p6.3d7.4s2.4p6.4d5.5s2 => Transition metal
(f) 1s2.2s2.2p6.3s2 => Akaline Earth metal
```
