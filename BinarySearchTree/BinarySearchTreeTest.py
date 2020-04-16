import unittest
from BinarySearchTree.BST import BinarySearchTree, TreeHandler


class BinarySearchTreeTest(unittest.TestCase):
    def testTraverseAscendingIterative2(self):
        expected = [1, 2, 3, 4, 5, 6]

        myTree = BinarySearchTree(3)
        myTree.add(1)
        myTree.add(6)
        myTree.add(2)
        myTree.add(4)
        myTree.add(5)

        handler = TreeHandler(myTree)
        handler.traverseAscending(handler.root)

        actual = handler.values

        self.assertEqual(expected, actual)

    def testTraverseAscendingIterative1(self):
        expected = [1, 2, 3]

        myTree = BinarySearchTree(2)
        myTree.add(1)
        myTree.add(3)

        handler = TreeHandler(myTree)
        handler.traverseAscendingIterative()

        actual = handler.values

        self.assertEqual(expected, actual)

    def testTraverseDescending1(self):
        expected = [3, 2, 1]

        myTree = BinarySearchTree(2)
        myTree.add(1)
        myTree.add(3)

        handler = TreeHandler(myTree)
        handler.traverseDescending(handler.root)

        actual = handler.values

        self.assertEqual(expected, actual)

    def testTraverseDescending2(self):
        expected = [6, 5, 4, 3, 2, 1]

        myTree = BinarySearchTree(3)
        myTree.add(1)
        myTree.add(6)
        myTree.add(2)
        myTree.add(4)
        myTree.add(5)

        handler = TreeHandler(myTree)
        handler.traverseDescending(handler.root)

        actual = handler.values

        self.assertEqual(expected, actual)

    def testTraverseAscending1(self):
        expected = [1, 2, 3]

        myTree = BinarySearchTree(2)
        myTree.add(1)
        myTree.add(3)

        handler = TreeHandler(myTree)
        handler.traverseAscending(handler.root)

        actual = handler.values

        self.assertEqual(expected, actual)

    def testTraverseAscending2(self):
        expected = [1, 2, 3, 4, 5, 6]

        myTree = BinarySearchTree(3)
        myTree.add(1)
        myTree.add(6)
        myTree.add(2)
        myTree.add(4)
        myTree.add(5)

        handler = TreeHandler(myTree)
        handler.traverseAscending(handler.root)

        actual = handler.values

        self.assertEqual(expected, actual)

    def testAddLeft1Layer(self):
        expected = BinarySearchTree(4)

        myTree = BinarySearchTree(5)
        actual = myTree.add(4)

        self.assertEqual(expected, actual)

    def testAddRight1Layer(self):
        expected = BinarySearchTree(6)

        myTree = BinarySearchTree(5)
        actual = myTree.add(6)

        self.assertEqual(expected, actual)

    def testAddLeft2Layer(self):
        expected = BinarySearchTree(3)

        myTree = BinarySearchTree(5)
        myTree.add(4)
        actual = myTree.add(3)

        self.assertEqual(expected, actual)

    def testAddRight2Layer(self):
        expected = BinarySearchTree(7)

        myTree = BinarySearchTree(5)
        myTree.add(6)
        actual = myTree.add(7)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
