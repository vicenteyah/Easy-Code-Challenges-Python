import unittest
from packages.arrays.FindFirstPalindrome import FindFirstPalindrome

class FindFirstPalindromeTest(unittest.TestCase):
    
    def test_first_palindrome(self):

        instance1 = FindFirstPalindrome(['abc', 'car', 'ada', 'racecar', 'cool'])
        instance2 = FindFirstPalindrome(['notapalindrome', 'racecar'])
        instance3 = FindFirstPalindrome(['def', 'ghi'])

        test1 = instance1.firstPalindrome()
        test2 = instance2.firstPalindrome()
        test3 = instance3.firstPalindrome()

        self.assertEqual(test1,'ada')
        self.assertEqual(test2,'racecar')
        self.assertEqual(test3,'')


if __name__ == "__main__":
    unittest.main()