from Tarea3.EquationNode import ENode
from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm

class FuncFindAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, lowestValue = 1, highestValue = 10, chanceOfX = 0.4, mutationRate = 0.1, fixSeed = False):
        super().__init__(mutationRate, fixSeed)
        self.low = lowestValue
        self.high = highestValue
        self.xchance = chanceOfX

        #WIP
