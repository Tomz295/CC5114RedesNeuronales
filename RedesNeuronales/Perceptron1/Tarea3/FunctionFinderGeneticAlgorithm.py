from Tarea3.EquationNode import ENode
from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm
import random
import math
import matplotlib.pyplot as plt
from copy import copy
import statistics


class FuncFindAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, lowestValue = 0, highestValue = 10, chanceOfX = 0.8,
                 mutationRate = 0.1, testFromValue = -20, testToValue = 20, treeSize = 3, fixSeed = False):
        super().__init__(mutationRate, fixSeed)
        self.low = lowestValue
        self.high = highestValue
        self.xchance = chanceOfX
        self.testrange = list(range(testFromValue, testToValue + 1, int((testToValue-testFromValue)/20)))
        self.size = treeSize

    def newRandomPopulation(self, populationSize):
        self.population = []
        for i in range(populationSize):
            individual = ENode(self.low, self.high, self.xchance)
            individual.buildTree(self.size)
            self.population.append(individual)

    def calcFitness(self, individual, correctAnswer):
        fitness = 0
        anslist = []
        for i in range(len(correctAnswer)):
            value = individual.calcValue(self.testrange[i])
            correct = correctAnswer[i]
            absolute = abs(correct - value)
            fitness -= absolute
        return fitness

    def generatePopulationOffspring(self):
        self.population = []
        for n in range(int(len(self.fittestIndividuals))):
            parent1 = copy(self.fittestIndividuals[n])
            #parent1 = copy(self.fittestIndividuals[2*n])
            #parent2 = copy(self.fittestIndividuals[(2*n)+1])
            offspring = parent1
            #splicedepth = random.randint(0, self.size-1)
            #node = parent2.getRandomDepthNode(splicedepth)
            #offspring.getRandomDepthNode(splicedepth).cloneNode(node)
            offspring.mutate(self.mutationRate)
            self.population.append(offspring)
        self.fittestIndividuals = []

    def startGeneticAlgorithm(self, functionToFindInString, fitnessThreshold = 0, populationSize = 100, nonImprovementLimit = 100):
        AnswerValues = []
        for val in self.testrange:
            x = val
            result = eval(functionToFindInString)
            AnswerValues.append(result)
        print("Initiating Algorithm")
        self.newRandomPopulation(populationSize)
        currentGeneration = 0
        allTimeBestFitness = -float('inf')
        generationsWithoutImprovement = 0
        plotXaxis = []
        plotYaxisBest = []
        plotYaxisAverage = []
        while(generationsWithoutImprovement < nonImprovementLimit and allTimeBestFitness < -fitnessThreshold):
            self.measureGenerationFitness(AnswerValues, populationSize)
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

            if allTimeBestFitness < -fitnessThreshold:
                self.generatePopulationOffspring()

            plotXaxis.append(currentGeneration)
            plotYaxisBest.append(self.generationFitnessBest)
            plotYaxisAverage.append(self.generationFitnessAverage)

            currentGeneration += 1
        if generationsWithoutImprovement >= nonImprovementLimit:
            print("Limit of generations without improvement reached. The answer was not found")
        else:
            print("The answer has been reached by Generation {0}".format(currentGeneration-1))
        plt.subplot(3, 1, 1)
        plt.subplots_adjust(None, None, None, None, None, 0.5)
        plt.grid(True)
        plt.plot(plotXaxis, plotYaxisBest, 'b')
        plt.ylabel('Fitness')
        plt.xlabel('Generación')
        plt.title('Mejor Fitness por generación')
        plt.subplot(3, 1, 2)
        plt.grid(True)
        plt.plot(plotXaxis, plotYaxisAverage, 'r')
        plt.ylabel('Eitness Promedio')
        plt.xlabel('Generación')
        plt.title('Fitness promedio por generación')
        plt.subplot(3, 1, 3)
        bestValues = []
        for val in self.testrange:
            result = self.generationBest.calcValue(val)
            bestValues.append(result)
        plt.grid(True)
        plt.plot(self.testrange, AnswerValues, 'b*')
        plt.plot(self.testrange, bestValues, 'r')
        plt.ylabel('f(x)')
        plt.xlabel('x')
        plt.title('Aproximacion vs funcion real')
        plt.show()

#e = FuncFindAlgorithm()
#e.startGeneticAlgorithm('19+x*3')