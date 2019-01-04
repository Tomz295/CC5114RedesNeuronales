from Tarea3.FunctionFinderGeneticAlgorithm import FuncFindAlgorithm
from Tarea3.NumbFinderNode import NumNode
import matplotlib.pyplot as plt
import math

class NumFindAlgorithm(FuncFindAlgorithm):
    def __init__(self, numbers = (2,5,10,23), mutationRate = 0.1, treeSize = 3, fixSeed = False):
        super().__init__(0, 10, -1, mutationRate, -10, 10, treeSize, fixSeed)
        self.nums = numbers

    def newRandomPopulation(self, populationSize):
        self.population = []
        for i in range(populationSize):
            individual = NumNode(self.nums)
            individual.buildTree(self.size)
            self.population.append(individual)

    def calcFitness(self, individual, correctAnswer):
        return -abs(correctAnswer - individual.calcValue(1))

    def startGeneticAlgorithm(self, numberToFind, populationSize = 100, nonImprovementLimit = 100):
        print("Initiating Algorithm")
        self.newRandomPopulation(populationSize)
        currentGeneration = 0
        allTimeBestFitness = -float('inf')
        generationsWithoutImprovement = 0
        plotXaxis = []
        plotYaxisBest = []
        plotYaxisAverage = []
        while(generationsWithoutImprovement < nonImprovementLimit and allTimeBestFitness < 0):
            self.measureGenerationFitness(numberToFind, populationSize)
            if self.generationFitnessBest > allTimeBestFitness:
                allTimeBestFitness = self.generationFitnessBest
            else:
                generationsWithoutImprovement += 1
            print("Current Generation: {0}".format(currentGeneration))
            print("Generation's top Fitness score: {0}".format(self.generationFitnessBest))
            print("Generation's average Fitness: {0}".format(self.generationFitnessAverage))
            print("")
            for i in range(populationSize*1):
                self.tournamentFitness(math.floor(populationSize*3/4))
            print("Generation's top:")
            print(self.generationBest.toString())
            print("")

            if allTimeBestFitness < 0:
                self.generatePopulationOffspring()

            plotXaxis.append(currentGeneration)
            plotYaxisBest.append(self.generationFitnessBest)
            plotYaxisAverage.append(self.generationFitnessAverage)

            currentGeneration += 1
        if generationsWithoutImprovement >= nonImprovementLimit:
            print("Limit of generations without improvement reached. The answer was not found")
        else:
            print("The answer has been reached by Generation {0}".format(currentGeneration-1))
        plt.subplot(2, 1, 1)
        plt.subplots_adjust(None, None, None, None, None, 0.5)
        plt.grid(True)
        plt.plot(plotXaxis, plotYaxisBest, 'b')
        plt.ylabel('Fitness')
        plt.xlabel('Generación')
        plt.title('Mejor Fitness por generación')
        plt.subplot(2, 1, 2)
        plt.grid(True)
        plt.plot(plotXaxis, plotYaxisAverage, 'r')
        plt.ylabel('Eitness Promedio')
        plt.xlabel('Generación')
        plt.title('Fitness promedio por generación')
        plt.show()

e = NumFindAlgorithm()
e.startGeneticAlgorithm(2)