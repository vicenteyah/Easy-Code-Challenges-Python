import unittest
from packages.arrays.FindWordsContainingCharacter import FindWordsContainingCharacter

class FindWordsContainingCharacterTest(unittest.TestCase):
    def test_find_word_containing(self):
        test1 = FindWordsContainingCharacter(['leet','code'],'e')
        test2 = FindWordsContainingCharacter(['abc','bcd','aaa','cbc'],'a')
        test3 = FindWordsContainingCharacter(['abc','bcd','aaa','cbc'],'z')
        self.assertEqual(test1.find_word_containing(),[0,1])
        self.assertEqual(test2.find_word_containing(),[0,2])
        self.assertEqual(test3.find_word_containing(),[])

if __name__=="__main__":
    unittest.main()