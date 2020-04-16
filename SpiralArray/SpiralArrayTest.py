import unittest
from SpiralArray import SpiralArrayBuilder


class SpiralArrayTest(unittest.TestCase):
    def testBuildSpiral1(self):
        expected = [[1, 2],
                    [4, 3]]

        builder = SpiralArrayBuilder(rows=2, cols=2)
        actual = builder.createSpiralArray()
        self.assertEqual(expected, actual)

    def testBuildSpiral2(self):
        expected = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]

        builder = SpiralArrayBuilder(rows=3, cols=3)
        actual = builder.createSpiralArray()
        self.assertEqual(expected, actual)

    def testBuildSpiral3(self):
        expected = [[1, 2, 3, 4],
                    [14, 15, 16, 5],
                    [13, 20, 17, 6],
                    [12, 19, 18, 7],
                    [11, 10, 9, 8]]

        builder = SpiralArrayBuilder(rows=5, cols=4)
        actual = builder.createSpiralArray()
        self.assertEqual(expected, actual)

    def testBuildSpiral4(self):
        expected = [[1, 2, 3, 4, 5],
                    [14, 15, 16, 17, 6],
                    [13, 20, 19, 18, 7],
                    [12, 11, 10, 9, 8]]

        builder = SpiralArrayBuilder(rows=4, cols=5)
        actual = builder.createSpiralArray()
        self.assertEqual(expected, actual)

    def testBuildSpiralInvalid(self):
        self.assertRaises(ValueError, SpiralArrayBuilder, rows=1, cols=0)

    def testBuildSpiralMinimum(self):
        expected = [[1]]

        builder = SpiralArrayBuilder(rows=1, cols=1)
        actual = builder.createSpiralArray()

        self.assertEqual(expected, actual)

    def testBuildSpiralMinimum2(self):
        expected = [[1, 2]]

        builder = SpiralArrayBuilder(rows=1, cols=2)
        actual = builder.createSpiralArray()

        self.assertEqual(expected, actual)

    def testBuildSpiralMinimum3(self):
        expected = [[1],
                    [2],
                    [3]]

        builder = SpiralArrayBuilder(rows=3, cols=1)
        actual = builder.createSpiralArray()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
