import unittest
from packages.arrays.NumberOfGoodPairs import NumberOfGoodsPairs

class NumberOfGoodPairs(unittest.TestCase):
    def test_num_identical_pairs(self):
        self.assertEqual(NumberOfGoodsPairs.num_identical_pairs([1,2,3,1,1,3]), 4)
        self.assertEqual(NumberOfGoodsPairs.num_identical_pairs([1,1,1,1]), 6)
        self.assertEqual(NumberOfGoodsPairs.num_identical_pairs([1,2,3]), 0)


if __name__ == "__main__":
    unittest.main()