import unittest

# from MakingChange import ChangeMaker
import MakingChange

class MakingChangeTest(unittest.TestCase):
    def testMakeChangeIterative1(self):
        expected = 2
        changeToMake = 1.25
        changeMaker = MakingChange.ChangeMaker()
        actual = changeMaker.makeChange(changeToMake)

        self.assertEqual(expected, actual)

    def testMakeChangeIterative2(self):
        changeToMake = 1.37
        expected = 5
        changeMaker = MakingChange.ChangeMaker()
        actual = changeMaker.makeChange(changeToMake)

        self.assertEqual(expected, actual)

    def testMakeChangeRecursive1(self):
        changeToMake = 1.25
        expected = 2
        changeMaker = MakingChange.ChangeMakerRecursive()
        changeMaker.makeChange(changeToMake)
        actual = changeMaker.count

        self.assertEqual(expected, actual)

    def testMakeChangeRecursive2(self):
        changeToMake = 1.37
        expected = 5
        changeMaker = MakingChange.ChangeMakerRecursive()
        changeMaker.makeChange(changeToMake)
        actual = changeMaker.count

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
