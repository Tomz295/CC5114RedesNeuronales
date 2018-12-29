import random
from Tarea3.NullNode import NullNode

class ENode:
    def __init__(self, lowestInt = 1, highestInt = 10, chanceOfXDecimal = 0.3):
        self.value = '0'
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

    def buildTree(self, numberChanceDecimal, size):
        self.assignValue(numberChanceDecimal, size == 1)
        if self.isLeaf: # Node is leaf -> End tree
            self.left = NullNode()
            self.right = NullNode()
        else: # Node is parent
            self.left = ENode()
            self.left.buildTree(numberChanceDecimal, size-1)
            self.right = ENode()
            self.right.buildTree(numberChanceDecimal, size-1)

    def assignValue(self, numberChanceDecimal, forceLeaf = False, forceParent = False):
        if (numberChanceDecimal > random.random() or forceLeaf) and (not forceParent):
            #value is number -> node is leaf
            self.value = 'x' if self.xchance > random.random() else str(random.randint(self.low, self.high))
            self.isLeaf = True
        else:
            # value is operation -> node is parent
            self.isLeaf = False
            options = ['+', '-', '*']
            self.value = options[random.randint(0, 2)]

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

    def toString(self):
        return self.left.toString() + ' ' + self.value + ' ' + self.right.toString()

    def mutate(self, chanceOfMutation):
        if random.random() < chanceOfMutation:
            self.assignValue(numberChanceDecimal, self.isLeaf, not self.isLeaf)
        self.left.mutate(chanceOfMutation)
        self.right.mutate(chanceOfMutation)