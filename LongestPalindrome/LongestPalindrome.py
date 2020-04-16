"""
Given a string, find the longest palindrome that the string contains
"""


class LongestPalindrome:
    def isPalindrome(self, givenString):
        """
        Checks if a given string is a palindrome or not, returns True if so
        :param givenString: The string to test
        :return: boolean - true if the string is a palindrome
        """
        charArray = list(givenString)

        if len(charArray) <= 1:
            return True

        else:
            forwardPointer = 0
            reversePointer = len(charArray) - 1

            while reversePointer - forwardPointer >= 1:
                if charArray[forwardPointer] != charArray[reversePointer]:
                    return False

                forwardPointer += 1
                reversePointer -= 1

            return True

    def findLongestPalindrome(self, givenString):

        i = len(givenString)
        start = 0
        while i - start >= 0:
            end = i
            while end <= len(givenString):
                curSub = givenString[start:end]

                if self.isPalindrome(curSub):
                    return curSub

                start += 1
                end += 1

            start = 0
            i -= 1

