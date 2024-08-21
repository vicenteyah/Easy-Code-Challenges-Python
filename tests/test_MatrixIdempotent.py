import unittest
from packages.matrix.MatrixIdempotent import MatrixIdempotent

class MatrixIdempotentDefinition (unittest.TestCase):
    def test_matrix_determinant(self):
        test1 = MatrixIdempotent([[2, -2], [-2, 2]])
        test2 = MatrixIdempotent([[1, 0], [0, 0]])
        test3 = MatrixIdempotent([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

        self.assertEqual(test1.is_idempotent(), False)
        self.assertEqual(test2.is_idempotent(), True)
        self.assertEqual(test3.is_idempotent(), True)

if __name__ == "__main__":
    unittest.main()