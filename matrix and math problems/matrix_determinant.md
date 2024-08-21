
# Calculate the Determinant of an 𝑛 × 𝑛  Matrix Using Cramer's Method

Problem Description:

Given a square matrix mat of size n x n, write a function to calculate the determinant of the matrix using the method of Cramer’s rule.

The determinant of a matrix is a scalar value that is a function of the entries of the matrix. It provides important properties of the matrix, such as whether the matrix is invertible.

You are required to calculate the determinant using the recursive expansion by minors (Cramer’s rule). Specifically, for any 
𝑛
×
𝑛
matrix, the determinant can be calculated as:

**The Cramer's Method**
$$det(A) = \sum_{j=1}^n \left(-1\right)^{i+j} * a_{ij} * det(M_{ij})  $$

#### Where
$$a_{ij} \text{ is the element from the first row and the } j^{th} \text{ column. }$$
##
$$M_{ij} \text{ is the } (n - 1) \times (n - 1) \text{ submatrix obtained  by removing the } i^{th} \text{ row and } j^{th} \text{ column from } A.$$
##
$$\text{The base case for recursion is when the matrix is } 1 \times 1 \text{ where the determinant is simply the value of the single element. }$$

Return the determinant as an integer
#### Example 1:
```bash
Input: mat = [[1, 2], [3, 4]]
Output: -2
Explanation:
The determinant is calculated as:
det(A) = 1 * 4 - 2 * 3 = 4 - 6 = -2
```
#### Example 2:
```bash
Input: mat = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
Output: 49
Explanation:
The determinant is calculated as:
det(A) = 2 * det([[ -2, -1], [3, 4]]) - 5 * det([[1, -1], [1, 4]]) + 3 * det([[1, -2], [1, 3]]) 
= 2 * ((-2 * 4) - (-1 * 3)) - 5 * ((1 * 4) - (-1 * 1)) + 3 * ((1 * 3) - (-2 * 1)) 
= 2 * (-5) - 5 * (5) + 3 * (5) 
= -10 - 25 + 15 
= -20
```
#### Example 3:
```bash
Input: mat = [[1]]
Output: 1
Explanation:
The determinant of a 1x1 matrix is simply the single element.
```

### Constraints
+ mat is a square matrix of size n x n, where 1 <= n <= 10.
+ The elements of mat are integers within the range -10^9 to 10^9.
+ You must use Cramer's method (recursive expansion by minors) to calculate the determinant.
