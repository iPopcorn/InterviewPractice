"""
making change: Given an input x, write a function to determine the minimum number of coins required to make that exact
amount of change
"""


class ChangeMakerRecursive:
    def __init__(self):
        self.count = 0

    def makeChange(self, changeToMake):
        if changeToMake - 1.0 >= 0:
            changeToMake -= 1.0
            self.count += 1
            self.makeChange(changeToMake)
        elif changeToMake - 0.5 >= 0:
            changeToMake -= 0.5
            self.count += 1
            self.makeChange(changeToMake)
        elif changeToMake - 0.25 >= 0:
            changeToMake -= 0.25
            self.count += 1
            self.makeChange(changeToMake)
        elif changeToMake - 0.10 >= 0:
            changeToMake -= 0.10
            self.count += 1
            self.makeChange(changeToMake)
        elif changeToMake - 0.05 >= 0:
            changeToMake -= 0.05
            self.count += 1
            self.makeChange(changeToMake)
        elif changeToMake - 0.01 >= 0:
            changeToMake -= 0.01
            self.count += 1
            self.makeChange(changeToMake)
        else:
            return


class ChangeMaker:
    def __init__(self):
        self.coins = {
            'dollar': {
                'value': 1.0,
                'count': 0
            },
            'halfDollar': {
                'value': 0.5,
                'count': 0
            },
            'quarter': {
                'value': 0.25,
                'count': 0
            },
            'dime': {
                'value': 0.1,
                'count': 0
            },
            'nickel': {
                'value': 0.05,
                'count': 0
            },
            'penny': {
                'value': 0.01,
                'count': 0
            }
        }

        # self.changeMade = 0

    def coinFits(self, coin, changeToMake):
        # print('ChangeMaker.coinFits()\nchangeToMake = ' + str(changeToMake))
        if changeToMake - self.coins[coin]['value'] >= 0:
            return True

        return False

    def addCoin(self, coin, changeToMake):
        # self.changeMade += self.coins[coin]['value']
        self.coins[coin]['count'] += 1
        changeToMake -= self.coins[coin]['value']

        return changeToMake

    def getTotalCoins(self):
        total = 0

        for coin in self.coins.keys():
            total += self.coins[coin]['count']

        return total

    def makeChange(self, changeToMake):
        while changeToMake > 0.001:
            if self.coinFits('dollar', changeToMake):
                changeToMake = self.addCoin('dollar', changeToMake)

            elif self.coinFits('halfDollar', changeToMake):
                changeToMake = self.addCoin('halfDollar', changeToMake)

            elif self.coinFits('quarter', changeToMake):
                changeToMake = self.addCoin('quarter', changeToMake)

            elif self.coinFits('dime', changeToMake):
                changeToMake = self.addCoin('dime', changeToMake)

            elif self.coinFits('nickel', changeToMake):
                changeToMake = self.addCoin('nickel', changeToMake)

            elif self.coinFits('penny', changeToMake):
                changeToMake = self.addCoin('penny', changeToMake)

            else:
                break

        return self.getTotalCoins()


if __name__ == '__main__':
    print('Hello, world!')
