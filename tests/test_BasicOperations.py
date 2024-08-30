
import unittest
from packages.arrays.BasicOperations import BasicOperations

class BasicOperationsTest(unittest.TestCase):
    
    def test_basic_operations (self):
        test1 = BasicOperations([3,5,15,7,9])
        test2 = BasicOperations([6, 10, 30, 12, 25])
        
        self.assertEqual(test1.calculate_result(),12) # 12 - 5 + 5 = 12 
        self.assertEqual(test2.calculate_result(),-17) # 48 - 35 + 0 = 13 