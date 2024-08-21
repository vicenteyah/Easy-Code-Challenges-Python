import unittest

from packages.binarySearch.KthMissingnumber import KthMissingNumber

class KthMissingNumberTest(unittest.TestCase):
    def test_find_kth_positive(self):
        test1 = KthMissingNumber.find_kth_positive([2,3,4,7,11], 5)
        test2 = KthMissingNumber.find_kth_positive([1,2,3,4],2)
        self.assertEqual(test1,9)
        self.assertEqual(test2,6)