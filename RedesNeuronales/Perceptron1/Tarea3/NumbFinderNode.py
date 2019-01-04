from Tarea3.EquationNode import ENode
import random

class NumNode(ENode):
    def __init__(self, numbers = (1,3,10,26)):
        super().__init__(1, 1, -1)
        self.nums = numbers

    def numberValue(self):
        self.value = str(random.choice(self.nums))

    def newNode(self):
        return NumNode(self.nums)