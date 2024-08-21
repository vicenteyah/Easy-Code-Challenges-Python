# Determine if a Matrix is Idempotent

Problem Description:

Given a square matrix mat of size n x n, write a function to determine if the matrix is idempotent. A matrix is considered idempotent if, when multiplied by itself, it yields the same matrix.

In other words, a matrix A is idempotent if:

$$  A \times A = A $$

Return true if the matrix is idempotent, and false otherwise.

#### Example 1:
```bash
Input: mat = [[2, -2], [-2, 2]]
Output: false
Explanation: 
A^2 = [[2, -2], [-2, 2]] × [[2, -2], [-2, 2]] = [[8, -8], [-8, 8]] 
Since A^2 ≠ A, the matrix is not idempotent.
```

#### Example 2:
```bash
Input: mat = [[1, 0], [0, 0]]
Output: true
Explanation: 
A^2 = [[1, 0], [0, 0]] × [[1, 0], [0, 0]] = [[1, 0], [0, 0]] 
Since A^2 = A, the matrix is idempotent.
```

#### Example 3:
```bash
Input: mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: true
Explanation: 
A^2 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] × [[0, 0, 0], [0, 1, 0], [0, 0, 0]] = [[0, 0, 0], [0, 1, 0], [0, 0, 0]] 
Since A^2 = A, the matrix is idempotent.
```
### Constraints
+ mat is a square matrix of size n x n, where 1 <= n <= 100.
+ The elements of mat are integers within the range -10^9 to 10^9
+ The matrix multiplication operation is defined as the standard matrix product.