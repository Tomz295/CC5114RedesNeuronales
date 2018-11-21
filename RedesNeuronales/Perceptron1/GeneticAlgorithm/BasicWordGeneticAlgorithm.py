from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm
import string
import random

class BasicWordAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, mutationRate = 0.1, fixSeed = False):
        super().__init__(mutationRate, fixSeed)

    def getGene(self):
        return random.choice(string.ascii_lowercase)

    def startGeneticAlgorithm(self, populationSize = 10, nonImprovementLimit = 100, correctAnswer = ['a','b','c','d','e']):
        super().startGeneticAlgorithm(populationSize, nonImprovementLimit, correctAnswer)

gen = BasicWordAlgorithm()
gen.startGeneticAlgorithm()