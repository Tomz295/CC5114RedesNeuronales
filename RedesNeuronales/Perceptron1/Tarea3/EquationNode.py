import random
from Tarea3.NullNode import NullNode

class ENode:
    def __init__(self, lowestInt = 1, highestInt = 10, chanceOfXDecimal = 0.4):
        self.value = 1
        self.isLeaf = True
        self.left = None
        self.right = None
        self.low = lowestInt
        self.high = highestInt
        self.xchance = chanceOfXDecimal

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

    def buildTree(self, numberChanceDecimal):
        self.assignValue(numberChanceDecimal)
        if not self.isLeaf: # Node is parent
            self.left = ENode()
            self.left.buildTree(numberChanceDecimal)
            self.right = ENode()
            self.right.buildTree(numberChanceDecimal)
        else: # Node is leaf -> End tree
            self.left = NullNode()
            self.right = NullNode()

    def assignValue(self, numberChanceDecimal):
        if numberChanceDecimal > random.random():
            #value is number -> node is leaf
            self.value = 'x' if self.xchance > random.random() else str(random.randint(self.low, self.high))
        else:
            # value is operation -> node is parent
            self.isLeaf = False
            options = ['+', '-', '*', '/']
            self.value = options[random.randint(0, 3)]

    # returns the value of the equation as a number
    def calcValue(self, Xvalue):
        x = Xvalue
        left = str(self.left.calcValue(Xvalue))
        right = str(self.right.calcValue(Xvalue))
        equation = left + self.value + right
        try:
            return eval(equation)
        except ZeroDivisionError:
            return float('inf')


