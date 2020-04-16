class TreeHandler:
    def __init__(self, root):
        self.root = root
        self.values = []

    def traverseDescending(self, node):
        if node:
            self.traverseDescending(node.right)
            self.values.append(node.value)
            self.traverseDescending(node.left)

        return

    def traverseAscending(self, node):
        if node:
            self.traverseAscending(node.left)
            self.values.append(node.value)
            self.traverseAscending(node.right)

        return

    def traverseAscendingIterative(self):
        nodes = []
        visitedFlag = False
        curNode = self.root

        while curNode:
            if visitedFlag:
                self.values.append(curNode.value)

                if curNode.right:
                    curNode = curNode.right
                    visitedFlag = False

                else:
                    break
            else:
                if curNode.left:
                    nodes.append(curNode)
                    curNode = curNode.left
                else:
                    self.values.append(curNode.value)

                    if curNode.right:
                        # nodes.append(curNode)
                        curNode = curNode.right

                    else:
                        try:
                            curNode = nodes.pop()
                            visitedFlag = True
                        except IndexError:
                            break
        # nodes = []
        # # prevNode = None
        # curNode = self.root
        # visitedFlag = False
        # while curNode:
        #     # print('curNode: ' + str(walker['curNode']))
        #     index = len(nodes) - 1
        #     if index > -1:
        #         nodeDict = nodes[index]
        #         if nodeDict['count'] > 1:
        #             tempNode = nodes.pop(index)['node']
        #             if tempNode == curNode:  # move back up one
        #                 index = len(nodes) - 1
        #
        #                 if index < 0:
        #                     break
        #
        #                 nodeDict = nodes[index]
        #                 curNode = nodeDict['node']
        #                 # nodeDict['count'] += 1
        #
        #         elif nodeDict['node'] == curNode:
        #             self.values.append(curNode)
        #             nodeDict['count'] += 1
        #
        #             if curNode.right:
        #                 curNode = curNode.right
        #
        #             else:
        #                 continue
        #     if curNode.left:
        #         # prevNode = curNode
        #         nodes.append({
        #             'node': curNode,
        #             'count': 1
        #         })
        #         curNode = curNode.left
        #     else:
        #         self.values.append(curNode.value)
        #         if curNode.right:
        #             nodes.append({
        #                 'node': curNode,
        #                 'count': 1
        #             })
        #             curNode = curNode.right
        #         else:
        #             if len(nodes):
        #
        #                 nodeDict = nodes[index]
        #                 curNode = nodeDict['node']
        #                 nodeDict['count'] += 1
        #                 nodes[index] = nodeDict
        #             else:
        #                 break


class BinarySearchTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def add(self, value):
        if value <= self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
                return self.left
            else:
                return self.left.add(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
                return self.right
            else:
                return self.right.add(value)

    def __eq__(self, other):
        if not isinstance(other, BinarySearchTree):
            return False

        if self.left == other.left and self.value == other.value and self.right == other.right:
            return True

        return False

    def __repr__(self):
        return "Node: ( value: {} left: {} right: {} )".format(str(self.value), str(self.left), str(self.right))
