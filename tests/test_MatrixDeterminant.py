import unittest
from packages.matrix.MatrixDeterminant import MatrixDeterminant

class MatrixDeterminantDefinition (unittest.TestCase):
    def test_matrix_determinant(self):
        test1 = MatrixDeterminant([[1, 2], [3, 4]])
        test2 = MatrixDeterminant([[2, 5, 3], [1, -2, -1], [1, 3, 4]])
        test3 = MatrixDeterminant([[1]])

        self.assertEqual(test1.calculate_determinant(),-2)
        self.assertEqual(test2.calculate_determinant(), 49)
        self.assertEqual(test3.calculate_determinant(), 1)

if __name__ == "__main__":
    unittest.main()