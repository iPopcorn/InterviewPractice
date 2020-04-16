class SpiralArrayBuilder:
    RIGHT = 'right'
    DOWN = 'down'
    LEFT = 'left'
    UP = 'up'

    def __init__(self, **kwargs):
        self.rows = kwargs.pop('rows', 0)
        self.cols = kwargs.pop('cols', 0)

        if self.rows == 0 or self.cols == 0:
            raise ValueError('Rows or Columns not initialized')

        self.array = [[0 for col in range(self.cols)] for row in range(self.rows)]

    def moveBack(self, curDirection, index):
        if curDirection == self.RIGHT:
            return self.moveLeft(index)
        elif curDirection == self.DOWN:
            return self.moveUp(index)
        elif curDirection == self.LEFT:
            return self.moveRight(index)
        else:
            return self.moveDown(index)

    def changeDirection(self, previousDirection):

        if previousDirection == self.RIGHT:
            return self.DOWN
        elif previousDirection == self.DOWN:
            return self.LEFT
        elif previousDirection == self.LEFT:
            return self.UP
        else:
            return self.RIGHT

    def move(self, direction, index):
        if direction == self.RIGHT:
            return self.moveRight(index)

        elif direction == self.DOWN:
            return self.moveDown(index)

        elif direction == self.LEFT:
            return self.moveLeft(index)

        else:
            return self.moveUp(index)

    def moveRight(self, index):
        newIndex = (index[0], index[1] + 1)

        return newIndex

    def moveUp(self, index):
        newIndex = (index[0] - 1, index[1])

        return newIndex

    def moveDown(self, index):
        newIndex = (index[0] + 1, index[1])

        return newIndex

    def moveLeft(self, index):
        newIndex = (index[0], index[1] - 1)

        return newIndex

    def setValue(self, index, value):
        self.array[index[0]][index[1]] = value

    def getValue(self, index):
        value = -1
        try:
            value = self.array[index[0]][index[1]]

        except IndexError:
            pass

        return value

    def createSpiralArray(self):
        index = (0, 0)
        count = 1
        curDirection = self.RIGHT
        value = 0
        stopCount = 0

        while value == 0:
            self.setValue(index, count)
            index = self.move(curDirection, index)
            count += 1
            value = self.getValue(index)

            while value != 0 and stopCount <= 5:
                index = self.moveBack(curDirection, index)
                curDirection = self.changeDirection(curDirection)
                index = self.move(curDirection, index)
                value = self.getValue(index)
                stopCount += 1

            stopCount = 0

        return self.array
