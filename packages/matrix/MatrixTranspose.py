from typing import List
"""
    #Check if a Matrix is the Transpose of Another

    Problem Description:
    Given two matrices mat1 and mat2 of dimensions m x n and n x m, respectively, write a function to determine if mat2 is the transpose of mat1.

    The transpose of a matrix is obtained by swapping its rows and columns. In other words, the entry (i, j) in the original matrix becomes the entry (j, i) in the transposed matrix.

    Return true if mat2 is the transpose of mat1, and false otherwise.

    Example 1:
        Input: mat1 = [[1, 2, 3], [4, 5, 6]], mat2 = [[1, 4], [2, 5], [3, 6]]
        Output: true
        Explanation: mat2 is the transpose of mat1.
    
    Example 2:
        Input: mat1 = [[1, 2], [3, 4]], mat2 = [[1, 3], [4, 2]]
        Output: false
        Explanation: mat2 is not the transpose of mat1, because the element at position (2, 2) should be 4 in mat2 to be the transpose of mat1.
    
    Example 3:
        Input: mat1 = [[1]], mat2 = [[1]]
        Output: true
        Explanation: mat2 is the transpose of mat1.
"""

class MatrixTranspose :
    def __init__(self, mat1: List[List[int]], mat2: List[List[int]]):
        self.mat1 = mat1
        self.mat2 = mat2
    
    def is_transpose(self) -> bool:
        return False