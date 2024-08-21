import unittest
from packages.math.LeibnizRule import LeibnizRule

class TheLeibnizRule(unittest.TestCase):
    def test_leibniz_rule(self):
        test1 = LeibnizRule([3, -2, 5, 1]) # for f(x) = 3x^3 - 2x^2 + 5x + 1
        test2 = LeibnizRule([4, 0, 2]) # for f(x) =  4x^2 + 2 
        test3 = LeibnizRule([7]) # for f(x) = 7

        self.assertEqual(test1.compute_derivative(), [9, -4, 5])
        self.assertEqual(test2.compute_derivative(), [8, 0])
        self.assertEqual(test3.compute_derivative(),[])