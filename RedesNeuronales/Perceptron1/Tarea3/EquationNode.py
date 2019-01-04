import random
from Tarea3.NullNode import NullNode

class ENode:
    def __init__(self, lowestInt = 1, highestInt = 10, chanceOfXDecimal = 0.3):
        self.value = '0'
        self.left = NullNode()
        self.right = NullNode()
        self.low = lowestInt
        self.high = highestInt
        self.xchance = chanceOfXDecimal

    def isNull(self):
        return False

    def isLeaf(self):
        return (self.left.isNull() and self.right.isNull())

    def cloneNode(self, node):
        self.value = node.value
        self.left = node.left
        self.right = node.right
        self.low = node.low
        self.high = node.high
        self.xchance = node.xchance

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

    def newNode(self):
        return ENode(self.low, self.high, self.xchance)

    def buildTree(self, size):
        if size <= 1:  # Node is leaf -> End tree
            self.numberValue()
            self.left = NullNode()
            self.right = NullNode()
        else:  # Node is parent
            options = ['+', '-', '*']
            self.value = options[random.randint(0, 2)]
            self.left = self.newNode()
            self.left.buildTree(size - 1)
            self.right = self.newNode()
            self.right.buildTree(size - 1)

#    def buildTree(self, numberChanceDecimal, size):
#        leaf = self.assignValue(numberChanceDecimal, size == 1)
#        if leaf: # Node is leaf -> End tree
#            self.left = NullNode()
#            self.right = NullNode()
#        else: # Node is parent
#            self.left = ENode()
#            self.left.buildTree(numberChanceDecimal, size-1)
#            self.right = ENode()
#            self.right.buildTree(numberChanceDecimal, size-1)

#    def assignValue(self, numberChanceDecimal, forceLeaf = False, forceParent = False):
#        if (numberChanceDecimal > random.random() or forceLeaf) and (not forceParent):
#            #value is number -> node is leaf
#            self.value = 'x' if self.xchance > random.random() else str(random.randint(self.low, self.high))
#            return True
#        else:
#            # value is operation -> node is parent
#            options = ['+', '-', '*']
#            self.value = options[random.randint(0, 2)]
#            return False

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

    def numberValue(self):
        self.value = 'x' if self.xchance > random.random() else str(random.randint(self.low, self.high))

    def mutate(self, chanceOfMutation):
        if random.random() < chanceOfMutation:
            if self.isLeaf():
                #self.value = 'x' if self.xchance > random.random() else str(self.numberValue())
                self.numberValue()
            else:
                options = ['+', '-', '*']
                self.value = options[random.randint(0, 2)]
        self.left.mutate(chanceOfMutation)
        self.right.mutate(chanceOfMutation)

    def getRandomDepthNode(self, depth):
        if depth <= 0 or self.isLeaf():
            return self
        else:
            if bool(random.randint(0,1)) and not self.left.isNull():
                return self.left.getRandomDepthNode(depth - 1)
            elif not self.right.isNull():
                return self.right.getRandomDepthNode(depth - 1)
            else:
                return self

    #def replaceRandomDepthNode(self,depth, node):
    #    if depth <= 0 or self.isLeaf():
    #        self.clone(node)
    #    else:
    #        if bool(random.randint(0,1)):
    #            self.left.replaceRandomDepthNode(depth - 1)
    #        else:
    #            self.right.replaceRandomDepthNode(depth - 1)


