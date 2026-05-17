[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/Functions-Data-structures-and-File-Input-or-Output-data-by-pandas-for-Physics-Problems/blob/main/Functions%2C%20Data%20Structures%2C%20and%20File%20Input%20or%20Output.py)

# Data structures and Pandas
This work aims to applying the concept of _Functions, Data Structures, and File Input/Output_ for solving physics problems by Python 3 and Jupyter Notebook. There are some solutions for tasks in this Python code.


# Key Equation
- The Solar mass
  -  $M_{Sun}=\frac{4\pi^{2}(1 AU)^{3}}{G (1 yr)^{2}}$
- The velocity of an atom
  - $v(x)=\sqrt{v_{0}^{2}+\frac{2F_{0}}{m}(cos\frac{x}{n}-1)}$
  

## 1. Function
### P4.1 - The solar mass
Calculate the solar mass. The solar mass can be calculated by using the relation:
<p align='center'>
  $$M_{Sun}=\frac{4\pi^{2}(1 AU)^{3}}{G (1 yr)^{2}}$$
</p>

In this task, we will use approximate values for AU and G. The unit AU is an astronomical unit of length. Its value is defined to be the average distance between the Sun and Earth:

1 AU = 1.496 x $10^{11}$ m
            
where 1 lightyear = 9.5 x $10^{12}$ km. The constant G is called the gravitational constant and has the following value:

G = 6.674 X $10^{-11}m^{3}kg^{-1}s^{-1}$

```python
# The Astronomical unit of length, in meters
AU = 1.496e11

# The orbital period o Earth in seconds, for one year
yr = 365.256 * 24 * 3600

# The Gravitational constant, in m3.kg-1,s-2
G = 6.674e-11

# Calculate the solar mass, in kg
import math
def Solar_mass():
    M_Sun = (4 * math.pi ** 2 * AU**3) / (G * yr**2)
    return M_Sun
print(Solar_mass())
```
```
1.9885939441528014e+30
```

### P4.2 - The velocity of an atom
The atoms within a material are structured such that they create a lattice. We will look at an atom which moves along the surface of a material. Since the atoms are aligned as a lattice, we could use a periodic model to find the velocity of the atom moving across the surface:
<p align='center'>
  $$v(x)=\sqrt{v_{0}^{2}+\frac{2F_{0}}{m}(cos\frac{x}{n}-1)}$$
</p>

where m is the mass of the atom, x is the position, v0 is its initial velocity, and n is a scaled distance between the atoms within the material. We set the force F0 = 1N. Find the velocity of the atom when x = 1, v0 = 2, n = 4 and m = 3.

- Repeat the calculation for Zn, Cu, and Ni for F0 = 1 x $10^{-25}$ N

```python
v0 = 2 # the velocity of atom
x =1 # the position of atom
m = 3 # the mass of atom
n = 4 # scaled distanced between atom within the material
F0 = 1 # The force in N

# Calculate the velocity of atom
import numpy as np
def velocity_atom():
    v_a = np.sqrt(v0**2 + (2 *F0 / m) * (np.cos(x/n)-1))
    return v_a
print(velocity_atom())
```
```
1.9948120081368812
```
```python
v0 = 2 # the velocity of atom
x =1 # the position of atom
n = 4 # scaled distanced between atom within the material
F0 = 1e-25 # The force in N

# Calculate for atom Zn, Cu, and Ni
A_units = 1.6605e-27 # Atomic per units in kg

# Calculate mass of Zn, Cu, and Ni
masses = {
    "Zn": 65.38 * 1.6605e-27,
    "Cu": 63.55 * 1.6605e-27,
    "Ni": 58.69 * 1.6605e-27
}

import numpy as np
def velocity_atom(atom):
    m = masses[atom]
    velocity = v0 **2 + (2 *F0 / m) * (np.cos(x/n)-1)
    return np.sqrt(velocity) if velocity >= 0 else None

for atom in masses:
    print(f"{atom}: {velocity_atom(atom)}")
```
```
Zn: 1.9856306859195652
Cu: 1.985215363307596
Ni: 1.9839861380776256
```



## 2. Data Structures

### P4.3 - The crystall lattice structures
The crystal lattice structures of the first row transition metal elements are given below. Some elements have different crystal structures under different conditions of temperatures and pressure. Use python sets to group them and determine which metal,

(a) only exist face-centered cubic (fcc), body-centered cubic (bcc), hexagonal-centered cubic (hcp)
(b) exist  in two of these structures
(c) do not form an hcp structure.

| Lattice |      Elements           |
|:--------|------------------------:|
|FCC      | Cu, Co, Fe, Mn, Ni, Sc  |
|BCC      | Cr, Fe, Mn, Ti, V       |
|HCP      | Co, Ni, Sc, Ti, Zn      |

```python
# set the elements in fcc, bcc, and hcp by lattice type
fcc = set(['Cu', 'Co', 'Fe', 'Mn', 'Ni', 'Sc'])
bcc = set(['Cr', 'Fe', 'Mn', 'Ti', 'V'])
hcp = set(['Co', 'Ni', 'Sc', 'Ti', 'Zn'])

# (a) print only exist fcc, bcc, and hcp
print('(a) only_fcc:', fcc - bcc - hcp)
print('(a) only_bcc:', bcc - fcc - hcp)
print('(a) only_hcp:', hcp - fcc - bcc)

# (b) exist in two structures
print('(b) fcc and bcc:', fcc & bcc - hcp)
print('(b) fcc and hcp:', fcc & hcp - bcc)
print('(b) bcc and hcp:', bcc & hcp - fcc)

# (c) print do not form hcp
all_metals = fcc | bcc | hcp

print('(c) no_hcp:', all_metals - hcp)

# (d) print the metals exist in fcc, bcc, and hcp
print('(d) fcc and bcc and hcp:', fcc & bcc & hcp)
```
```
(a) only_fcc: {'Cu'}
(a) only_bcc: {'V', 'Cr'}
(a) only_hcp: {'Zn'}
(b) fcc and bcc: {'Mn', 'Fe'}
(b) fcc and hcp: {'Co', 'Ni', 'Sc'}
(b) bcc and hcp: {'Ti'}
(c) no_hcp: {'V', 'Cu', 'Cr', 'Fe', 'Mn'}
(d) fcc and bcc and hcp: set()
```


### P4.4 - Magnetic classification
The magnetic properties are related to metals. Some elements have different properties under different conditions of temperatures and pressure. Use python sets to group them and determine which category, 
- (a) only exist as diamagnetic, paramagnetic, and non-magnetic.
- (b) exist  in two of these magnetic.
- (c) exist  in three of these magnetic.

| category    |      Elements         |
|:------------|----------------------:|
|Diamagnetic  | Zn, Cu, Sc, Ti        |
|Paramagnetic | Cr, Mn, V, Fe, Cu, Ti |
|Non-magnetic | Al, Zn, Sc            |


### P4.5 - Magnetic classification
The magnetic properties are related to metals. Some elements have different properties under different conditions of temperatures and pressure. Use python sets to group them and determine which category, 
- (a) only exist as diamagnetic, paramagnetic, and non-magnetic.
- (b) exist  in two of these magnetic.
- (c) exist  in three of these magnetic.

| category    |      Elements         |
|:------------|----------------------:|
|Diamagnetic  | Zn, Cu, Sc, Ti        |
|Paramagnetic | Cr, Mn, V, Fe, Cu, Ti |
|Non-magnetic | Al, Zn, Sc            |

```python
# set the elements in diamagnetic, paramagnetic and non-magnetic
Diamagnetic = set(['Zn', 'Cu', 'Sc', 'Ti'])
Paramagnetic = set(['Cr', 'Mn', 'V', 'Fe', 'Cu', 'Ti'])
Non_magnetic = set(['Al', 'Zn', 'Sc'])

# print only exist diamagnetic, paramagnetic or non-magnetic
print('(a) only_Diamagnetic:', Diamagnetic - Paramagnetic - Non_magnetic)
print('(a) only_Paramagnetic:', Paramagnetic - Diamagnetic - Non_magnetic)
print('(a) only_Nonmagnetoc:', Non_magnetic - Diamagnetic - Paramagnetic)

# Exist in two properties
print('(b) Diamagnetic and Paramagnetic:', Diamagnetic & Paramagnetic - Non_magnetic)
print('(b) Diamagnetic and Non_magnetic:', Diamagnetic & Non_magnetic - Paramagnetic)
print('(b) Paramagnetic and Non_magnetic:', Paramagnetic & Non_magnetic - Diamagnetic)

# Exist in three properties
all_category = Diamagnetic | Paramagnetic | Non_magnetic

print('(c) Diamagnetic and Paramagnetic and Non_magnetic:', Diamagnetic & Paramagnetic & Non_magnetic)
```
```
(a) only_Diamagnetic: set()
(a) only_Paramagnetic: {'V', 'Cr', 'Mn', 'Fe'}
(a) only_Nonmagnetoc: {'Al'}
(b) Diamagnetic and Paramagnetic: {'Ti', 'Cu'}
(b) Diamagnetic and Non_magnetic: {'Zn', 'Sc'}
(b) Paramagnetic and Non_magnetic: set()
(c) Diamagnetic and Paramagnetic and Non_magnetic: set()
```

## 3. File Input/Output

Table. Python file open modes
<div style="width:60%; margin:auto;">
    
| **Character**  |         **Description**                                  | 
|:----------:|:-----------------------------------------------------:|
| 'r'        | open for reading (the default)                       |
| 'w'        | open for writing, over writing the file if it exist  |
| 'x'        | open for writing, failing if the file exist already  |
| 'a'        | open for writing, appending if the file exist        |
| 't'        | read/write text data (the dafault)                   |
| 'b'        | read/write binary data                               |
| '+'        | open for updating (reading and writing)              |
</div>

### P4.5 - The computational density
The text file [atomic-data.txt](http://localhost:8888/lab/tree/atomic-data.txt), which can download directly, contains data for the elements, molar cell, and volume cell for Al, Cu, Pb. Read in data and calculate computational density for each subtances.

```python
import pandas as pd

# Read the txt file (comma-separated)
df = pd.read_csv("atomic-data.txt")

print(df.head())   # show first 5 rows

for row in data:
    element, molar_cell, volume_cell = row
    molar_cell = float(molar_cell)
    volume_cell = float(volume_cell)
    density = molar_cell / volume_cell
    print(f"{element}: Density = {density:.2f} g/cm³")
```
```
  elements      \tm-cell  \tvolume-cell (cm^3)
0       Al  1.792000e-22          6.620000e-23
1       Cu  4.221000e-22          6.750000e-23
2       Pb  1.376000e-21          1.320000e-22
Al: Density = 2.71 g/cm³
Cu: Density = 6.25 g/cm³
Pb: Density = 10.42 g/cm³
```
