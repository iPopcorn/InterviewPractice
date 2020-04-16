import unittest
from LongestPalindrome import LongestPalindrome
# import LongestPalindrome


class LongestPalindromeTest(unittest.TestCase):

    def testIsPalindromeNegative2(self):
        testString = 'cat'
        stringTester = LongestPalindrome()

        self.assertFalse(stringTester.isPalindrome(testString))

    def testIsPalindromeNegative1(self):
        testString = 'ab'
        stringTester = LongestPalindrome()

        self.assertFalse(stringTester.isPalindrome(testString))

    def testIsPalindromePositive3(self):
        testString = 'daccad'
        stringTester = LongestPalindrome()

        self.assertTrue(stringTester.isPalindrome(testString))

    def testIsPalindromePositive2(self):
        testString = 'dad'
        stringTester = LongestPalindrome()

        self.assertTrue(stringTester.isPalindrome(testString))

    def testIsPalindromePositive1(self):
        testString = 'aa'
        stringTester = LongestPalindrome()

        self.assertTrue(stringTester.isPalindrome(testString))

    def testIsPalindromeSingleChar(self):
        testString = 'a'

        stringTester = LongestPalindrome()

        self.assertTrue(stringTester.isPalindrome(testString))

    def testIsPalindromeEmptyString(self):
        testString = ''
        expected = True

        stringTester = LongestPalindrome()
        actual = stringTester.isPalindrome(testString)

        self.assertEqual(expected, actual)

    def testLongestPalindrome1(self):
        testString = "ababbabbaaa"
        expected = 'abbabba'

        stringTester = LongestPalindrome()
        actual = stringTester.findLongestPalindrome(testString)

        self.assertEqual(expected, actual)

    def testLongestPalindrome2(self):
        testString = "Where is my racecar?"
        expected = 'racecar'

        stringTester = LongestPalindrome()
        actual = stringTester.findLongestPalindrome(testString)

        self.assertEqual(expected, actual)

    def testLongestPalindromeEmpty(self):
        testString = ""
        expected = ''

        stringTester = LongestPalindrome()
        actual = stringTester.findLongestPalindrome(testString)

        self.assertEqual(expected, actual)

    def testLongestPalindromeNegative(self):
        testString = "abcd"
        expected = 'a'

        stringTester = LongestPalindrome()
        actual = stringTester.findLongestPalindrome(testString)

        self.assertEqual(expected, actual)
