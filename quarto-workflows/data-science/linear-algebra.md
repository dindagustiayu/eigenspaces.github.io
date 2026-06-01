---
date: "2026-2-1"
---

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/dindagustiayu/-Linear-Algebra-in-Balancing-a-Chemical-Reaction-/tree/main)

# Balancing a Chemical Reaction and Permutation Group

## Linear Algebra
Linear Algebra is the branch of mathematics that focuses on the study of vectors, vector spaces, matrices, and linear tranformations. It deals with linear equations, linear functions, and their representations through matrices and determinants. It has a wide range of appliation in Physics and Mathematics, It is the basic concept for machine learning and data science.

## Foundations of Linear 
Linear Algebra is trikingly similar to the algebra we learned in hihg school, except that in the place of ordinary single numbers, it deals with vectors. Elementary linear algebra introduces the foundational concepts that form the building blocks of the subject. It covers basic operations on matrices, solving system of equations, and understanding vectors.
1. Scalar
2. Vector
3. Vector Spaces
4. Matrices
5. Matrix Operations

## 1. Scalar
A scalar is a number. Examples of scalars are temperature, distances, speed, or mass, all quantities that have a magnitude but no "direction" other than perhaps positive or negative.

## 2. Vectors
In mathematics, vectors are fundamental objects that represent quantities with both magnitude and direction. A vector is _a list of numbers_. There are (at least) two ways to intrepret what this list of numbers mean: One way to think of the vector as being _a point in a space_. Another way to think of a vector is _a magnitude and a direction_.

## 3. Vector spaces
A basis set is  a linearly independent set of vectors that, when used in linear combinations, can combination represent every vector in agiven vector space. All vectors live within a _vector space_. A vector space is exactly what it sounds like the space in which vectors live. The vector space is intuitively spatial since all available directions of motion can be plotted directly onto a spacial map of the room.

## 4. Matrices
A matrix, like a vector, is also a collection of numbers. The difference is that a matrix is a set of numbers rather than a list. Many of the same rules we juct outlined for vectors above apply equally well to matrices. Matrices are rectangular arrays of numbers, symbols, or characters where all of these elements are arranged in each row and column. 
- A matrix is identified by its order, which is given in the form of rows x and columns and the location of each element is given by the row and column it belongs to.
- A matrix is represented as ($[P]_{m \times n}$), where P is the matrix, m is the number of rows and n is the number of columns.


## 5. Matrix operations
Matrix operations mainly involve three algebraic operations, which are the addition of matrices, subtraction of matrices, and multipication of matrices. To add or substract matrices, these must be of identical order, and for multipication, the number of columns in the first matrix equals the number of rows in the second matrix. Examples of matrix operations:
- transpose, sum and difference, scalar multiplication.
- matrix multiplication, matrix-vector product.
- matrix inverse.

# Linear Algebra in Chemistry
Linear Algebra is the study of vectors in vector spaces, and linear transformation in that vector spaces. The study of vector spaces and linear transformations in said spaces is called Linear Algebra. In this work, we will solving a set of linear equation for balancing reaction a chemical reaction.

## P18.1 Exercise: Balancing a redox reaction
Balance the equation ofr the reaction of permanganate and iodide ions in basic solution:
<p align='center'>
    $$MnO_{4}^{-} (aq) + I^{-} (aq) \longrightarrow MnO_{2} (s) + I_{2} (aq)$$
</p>

__Hint__: You will need to add $OH^{-}$ ions $H_{2}O$ molecules to the reaction in stoichiometric amounts to be determined.

In this redox reaction, the hydroxide ions and water molecules added before it can be balanced:
<p align='center'>
    $$aMnO_{4}^{-} (aq) + bI^{-} (aq) + cH_{2}O (l) \longrightarrow dMnO_{2} (s) + eI_{2} (aq) + fOH^{-} (aq)$$
</p>
We must also conserve the charge, which leads to the following four equations:
<p align='center'>
    
    Mn: a + d = 0
    O:  4a + c + 2d + f = 0
    I:  b + 2e = 0
    H:  2c + f = 0
    charge: a + b + f = 0
</p>

The problem is undertermined but we can set the constraint a = 1 since we know we can scale all the coefficients by the same amount and keep the reaction balanced. Therefore, in matrix form:
<p align='center'>
    $$\begin{pmatrix} 1 & 0 & 0 & 1 & 0 & 0\\4 & 0 & 1 & 2 & 0 & 1\\0 & 1 & 0 & 0 & 2 & 0\\0 & 0 & 2 & 0 & 0 & 1\\1 & 1 & 0 & 0 & 0 & 1\\1 & 0 & 0 & 0 & 0 & 0 \end{pmatrix}  \begin{pmatrix} a\\b\\c\\d\\e\\f  \end{pmatrix} = \begin{pmatrix} 0\\0\\0\\0\\0\\1 \end{pmatrix}$$
</p>

```python
import numpy as np
A = np.array([[1, 0, 0, 1, 0, 0], # Mn
              [4, 0, 1, 2, 0, 1], # O
              [0, 1, 0, 0, 2, 0], # I
              [0, 0, 2, 0, 0, 1], # H
              [1, 1, 0, 0, 0, 1], # charge
              [1, 0, 0, 0, 0, 0]]) # constraint a = 1
x = np.array([0, 0, 0, 0, 0, 1])
coeffs = np.linalg.solve(A, x)
print('a, b, c, d, e, f =', coeffs)
```
a, b, c, d, e, f = [ 1.   3.   2.  -1.  -1.5 -4. ]

The balanced reaction is therefore:
<p align='center'>
    $$2\;MnO_{4}^{-} (aq) + 6\;I^{-} (aq) + 4\;H_{2}O (l) \longrightarrow 2\;MnO_{2} (s) + 3\;I_{2} (aq) + 8\;OH^{-} (aq)$$
</p>

## P18.2 Exercise: Balancing a complex reaction
Balance the following equation [R. J. Stout, _J.Chem.Educ.__72__, 1125 (1995)]: 
<p align='center'>
    $$aCr_{7}N_{66}H_{96}C_{42}O_{24} + MnO_{4}^{-} + H^{+} \longrightarrow Cr_{2}O_{7}^{2-} + Mn^{2+} + CO_{2} + NO_{3}^{-} + H_{2}O$$
</p>
The stoichiometric constraints can be written as a sequence of three equations, one for each of the atoms Cr, N, H, C, O, and Mn.
<p align='center'>

        Cr: 7a + 2d = 0
        N : 66a + g = 0
        H : 96a + c + 2h = 0
        C : 42a + f = 0
        O : 24a + 4b + 7d + 2f + 3g + h = 0
        Mn: b + e = 0
    Charge: b + c + d + e + g = 0
</p>
Again, The problem is undertermined but we can set the constraint a = 1 since we know we can scale all the coefficients by the same amount and keep the reaction balanced. Therefore, in matrix form:
<p align='center'>
    $$\begin{pmatrix} 7 & 0 & 0 & 2 & 0 & 0 & 0 & 0\\ 66 & 0 & 0 & 0 & 0 & 0 & 1 & 0\\ 96 & 0 & 1 & 0 & 0 & 0 & 0 & 2\\ 42 & 0 & 0 & 0 & 0 & 1 & 0 & 0\\ 24 & 4 & 0 & 7 & 0 & 2 & 3 & 1\\ 0 & 1 & 0 & 0 & 1 & 0 & 0 & 0\\ 0 & -1 & 1 & -2 & 2 & 0 & -1 & 0\\ 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} a\\b\\c\\d\\e\\f\\g\\h \end{pmatrix} = \begin{pmatrix} 0\\0\\0\\0\\0\\0\\0\\1 \end{pmatrix}$$
</p>

```python
import numpy as np
A = np.array([[7, 0, 0, 2, 0, 0, 0, 0], 
              [66, 0, 0, 0, 0,0, 1, 0], 
              [96, 0, 1, 0, 0, 0, 0, 2], 
              [42, 0, 0, 0, 0, 1, 0, 0], 
              [24, 4, 0, 7, 0, 2, 3, 1], 
              [0, 1, 0, 0, 1, 0, 0, 0], 
              [0, -1, 1, -2, 2, 0, -1, 0], 
              [1, 0, 0, 0, 0, 0, 0, 0]])

x = np.array([0, 0, 0, 0, 0, 0, 0, 1])
coeffs = np.linalg.solve(A, x)
print('a, b, c, d, e, f, g, h=', coeffs)
```
a, b, c, d, e, f, g, h= [   1.   117.6  279.8   -3.5 -117.6  -42.   -66.  -187.9]

The balanced reaction is therefore:
<p align='center'>
    $$10\;Cr_{7}N_{66}H_{96}C_{42}O_{24} + 1176\;MnO_{4}^{-} + 2798\;H^{+} \longrightarrow 35\;Cr_{2}O_{7}^{2-} + 11760\;Mn^{2+} + 420\;CO_{2} + 660\;NO_{3}^{-} + 1879\;H_{2}O$$
</p>

## P18.3 Exercise: The reaction between copper and nitric acid
Copper metal may be thought of as reacting with nitric acid according to the followeing reaction:
<p align='center'>
    $$aCu\;(s) + bHNO_{3}\;(aq) \longrightarrow cCu(NO_{3})_{2}\;(aq) + dNO\;(g) + eNO_{2}\;(g) + fH_{2}O\;(l)$$
</p>
Show that this reaction is carried put with concentrated nitric acid the favored gaseous product is nitrogen dioxide instead of nitric oxide (d = 0); conversely, in dilute nitric acid nitric oxide is produced of $NO_{2}$ (e = 0). Write balanced equations for these two cases.


With concentrate $HNO_{3}$, we can eliminate the column corresponding to NO since $NO_{2}$ is observed to be the product.
<p align='center'>
    $$aCu\;(s) + bHNO_{3}\;(aq) \longrightarrow cCu(NO_{3})_{2}\;(aq) + dNO_{2}\;(g) + eH_{2}O\;(l)$$
</p>

The equations giverning the balance of the reaction can be written as,
<p align='center'>

    Cu: a + c = 0
    H:  b + 2e = 0
    N:  b + 2c + d = 0
    O: 3b + 6c + 2d + e = 0
</p>
Again, The problem is undertermined but we can set the constraint a = 1 since we know we can scale all the coefficients by the same amount and keep the reaction balanced. Therefore, in matrix form:
<p align='center'>
    $$\begin{pmatrix} 1 & 0 & 1 & 0 & 0\\ 0 & 1 & 0 & 0 & 2\\ 0 & 1 & 2 & 1 & 0\\ 0 & 3 & 6 & 2 & 1\\1 & 0 & 0 & 0 & 0\end{pmatrix} \begin{pmatrix} a\\b\\c\\d\\e \end{pmatrix} = \begin{pmatrix} 0\\0\\0\\0\\1 \end{pmatrix}$$
</p>

```python
import numpy as np
A = np.array([[1, 0, 1, 0, 0],
              [0, 1, 0, 0, 2],
              [0, 1, 2, 1, 0],
              [0, 3, 6, 2, 1],
              [1, 0, 0, 0, 0]])

x = np.array([0, 0, 0, 0, 1])
coeffs = np.linalg.solve(A, x)
print('a, b, c, d, e=', coeffs)
```
a, b, c, d, e= [ 1.  4. -1. -2. -2.]

The balanced reaction in this case is therefore:
<p lign='center'>
    $$Cu\;(s) + 4\;HNO_{3}\;(aq) \longrightarrow Cu(NO_{3})_{2}\;(aq) + 2\;NO_{2}\;(g) + 2\;H_{2}O\;(l)$$
</p>

In dilute nitric acid, we can eliminate the column corresponding to $NO_{2}$ instead:
<p align='center'>
    $$aCu\;(s) + bHNO_{3}\;(aq) \longrightarrow cCu(NO_{3})_{2}\;(aq) + dNO\;(g) + eH_{2}O\;(l)$$
</p>

The equations giverning the balance of the reaction can be written as,
<p align='center'>

    Cu: a + c = 0
    H:  b + 2e = 0
    N:  b + 2c + d = 0
    O: 3b + 6c + d + e = 0
</p>
Again, The problem is undertermined but we can set the constraint a = 1 since we know we can scale all the coefficients by the same amount and keep the reaction balanced. Therefore, in matrix form:
<p align='center'>
    $$\begin{pmatrix} 1 & 0 & 1 & 0 & 0\\ 0 & 1 & 0 & 0 & 2\\ 0 & 1 & 2 & 1 & 0\\ 0 & 3 & 6 & 1 & 1\\1 & 0 & 0 & 0 & 0\end{pmatrix} \begin{pmatrix} a\\b\\c\\d\\e \end{pmatrix} = \begin{pmatrix} 0\\0\\0\\0\\1 \end{pmatrix}$$
</p>

```python
import numpy as np
A = np.array([[1, 0, 1, 0, 0],
              [0, 1, 0, 0, 2],
              [0, 1, 2, 1, 0],
              [0, 3, 6, 1, 1],
              [1, 0, 0, 0, 0]])

x = np.array([0, 0, 0, 0, 1])
coeffs = np.linalg.solve(A, x)
print('a, b, c, d, e=', coeffs)
coeffs * 3 # To get integer coefficients, multiply by 3
```
<p align='left'>
  
    a, b, c, d, e= [ 1. 2.66666667 -1. -0.66666667 -1.33333333]
    array([ 3.,  8., -3., -2., -4.])
</p>

The balanced reaction in this case is
<p lign='center'>
    $$3Cu\;(s) + 8\;HNO_{3}\;(aq) \longrightarrow 3Cu(NO_{3})_{2}\;(aq) + 2\;NO\;(g) + 4\;H_{2}O\;(l)$$
</p>

## P18.4 Construction the Cayley Table for a Permutation Group
What is the most effective way to shuffle a pack of cards?. To answer this question we need to return to the ideas about permutations. We will see that permutations provide an example of a mathematical structure called a _groups._ Groups plan an important role in many areas of mathematics.

Caycle's theorem states that every group G is isomorphic to a subgroup of the symmetric group acting on G. In this context, it means that if we have a vector of permutations tha comprise a group, then we can nicely represent its stucture using a table. 

The distinct rearrangements of three objects, [1, 2, 3], can be described by six distinct permutations, written in cycle notation as 
<p align='center'>
    e, (12), (13), (23), (123), (132).
</p>

Here, e represent the identity permutation (which leaves the objects undisturbed) and, for example, (12) swaps objects 1 and 2; (123) is the cyclic permutation ($1\rightarrow 2, 2\rightarrow 3, 3\rightarrow 1$).

- (a) Demonstrate that the inverse of each $3\times3$ permuation matrix is its transpose (i.e., the permutation matrices are _orthogonal_)
- (b) Show that there is some power of each permutation matrix that is the identity matrix.
- (c) The _parity_ of a permutation is -1 or +1 according to whether the number of distinct pairwise swaps it can be broken down into is odd or even, repectively. Show that the parity of each permutation is equal to the determinant of its corresponding permutation matrix.

## Mathematical meaning
This code is finding the order of each element in the group $S_{3}$:
- The order of an element g in a group is the smallest positive integer n such that $g^{n}=e$.
- If true, it prints that the matrix is __orthogonal__ (since orthogonal matrices satisfy $m^{-1}=m^{T}$).
- In $S_{3}$:
  - The identity e has order 1
  - Transpositions like (12), (13), (23)have order 2.
  - 3-cycles like (123), (132) have order 3.

## The key arguments:
- `np.eye(3, dtype=int)`: creates the 3 x 3 identity matrix (the permutation 'e').
- `np.array([...], dtype=int)`: the nested list `[[...], [...], [...]]` species the matrix.
- `np.allclose(minv, m.T)`: compares two matrices element-wise to check if they are approximately equal.
- `minv`: the inverse of the matrix.
- `m.T`: the transpose of the matrix.
- `enumerate`: `s` (list of matrices), iterates through the list `s`, returning both index `i` and matrix `m`.
- `np.linalg.matrix_power(m, n)`: `m` (matrix), `n` (integer).

(a) Demonstrate that the inverse of each 3 x 3 permutation matrix is its transpose (i.e., the permutation matrices are _orthogonal_)
```python
import numpy as np
s = [None] * 6
names = ['e', '(12)', '(13)', '(23)', '(123)', '(132)']
s[0] = np.eye(3, dtype=int)
s[1] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=int)
s[2] = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=int)
s[3] = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=int)
s[4] = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=int)
s[5] = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=int)

for i, m in enumerate(s):
    minv = np.linalg.inv(m)
    if np.allclose(minv, m.T):
        print(f's[{i}] is orthogonal')
```
<p align='left'>
  
    s[0] is orthogonal
    s[1] is orthogonal
    s[2] is orthogonal
    s[3] is orthogonal
    s[4] is orthogonal
    s[5] is orthogonal
</p>



(b) Show that there is some power of each permutation matrix that is the identity matrix.
```python
for i, m in enumerate(s):
    n = 1
    while not np.allclose(np.linalg.matrix_power(m, n), s[0]):
        n += 1
        print(f's[{i}]^{n} = e')
```
<p align='left'>
  
    s[1]^2 = e
    s[2]^2 = e
    s[3]^2 = e
    s[4]^2 = e
    s[4]^3 = e
    s[5]^2 = e
    s[5]^3 = e
</p>


(c) The _parity_ of a permutation is -1 or +1 according to whether the number of distinct pairwise swaps it can be broken down into is odd or even, repectively.
```python
parities = [1, -1, -1, -1, 1, 1]
for name, parity in zip(names, parities):
    print(f'{name:>5s}: {parity:2d}')
```
<p align='left'>
     
        e:  1
     (12): -1
     (13): -1
     (23): -1
    (123):  1
    (132):  1
</p>
 
