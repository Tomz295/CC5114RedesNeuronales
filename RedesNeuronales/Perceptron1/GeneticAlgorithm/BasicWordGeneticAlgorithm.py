from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm
import string
import random

class BasicWordAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, mutationRate = 0.1):
        super().__init__(mutationRate)

    def getGene(self):
        return random.choice(string.ascii_lowercase)

    def startGeneticAlgorithm(self, populationSize = 10, correctAnswer = ['a','b','c','d','e'], nonImprovementLimit = 100):
        super().startGeneticAlgorithm(populationSize, correctAnswer, nonImprovementLimit)

gen = BasicWordAlgorithm()
gen.startGeneticAlgorithm()