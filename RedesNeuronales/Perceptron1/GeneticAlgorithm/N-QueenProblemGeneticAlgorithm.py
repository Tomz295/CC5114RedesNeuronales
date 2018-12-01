from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm
import random
import matplotlib.pyplot as plt


class NQueenAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, tableSize = 4, mutationRate = 0.1, fixSeed = False):
        super().__init__(mutationRate, fixSeed)
        self.numberOfGenes = tableSize

    def getGene(self):
        return random.randint(0, self.numberOfGenes-1)

    def calcFitness(self, individual, correctAnswer = None):
        # fitness = self.numberOfGenes
        # fitness -= self.numberOfGenes - len(set(individual))
        fitness = len(set(individual))
        for index in range(self.numberOfGenes-1):
            geneValue = individual[index]
            choqueMas = False
            choqueMenos = False
            for n in range(1, self.numberOfGenes-index):
                comparedGene = individual[index+n]
                if comparedGene + n == geneValue:
                    choqueMas = True
                elif comparedGene - n == geneValue:
                    choqueMenos = True
            if choqueMas:
                fitness -= 1
            if choqueMenos:
                fitness -= 1
        return fitness

    def startGeneticAlgorithm(self, populationSize = 8, nonImprovementLimit = 100):
        super().startGeneticAlgorithm(populationSize, nonImprovementLimit, [])


queen = NQueenAlgorithm()
queen.startGeneticAlgorithm()