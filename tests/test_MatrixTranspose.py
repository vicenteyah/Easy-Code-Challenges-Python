import unittest
from packages.matrix.MatrixTranspose import MatrixTranspose

class MatrixTransposeDefinition (unittest.TestCase):
    def test_matrix_transpose(self):
        test1 = MatrixTranspose([[1, 2, 3], [4, 5, 6]] , [[1, 4], [2, 5], [3, 6]] )
        test2 = MatrixTranspose([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        test3 = MatrixTranspose([[1]], [[1]])

        self.assertEqual(test1.is_transpose(),True)
        self.assertEqual(test2.is_transpose(), False)
        self.assertEqual(test3.is_transpose(), True)

if __name__ == "__main__":
    unittest.main()