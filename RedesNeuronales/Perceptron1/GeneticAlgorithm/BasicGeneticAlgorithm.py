import random
import math
import matplotlib.pyplot as plt

class BasicBitGeneticAlgorithm:
    def __init__(self, mutationRate = 0.01, fixSeed = False):
        self.population = []
        self.measuredPopulation = []
        self.fittestIndividuals = []
        self.generationBest = None
        self.generationFitnessAverage = 0
        self.generationFitnessBest = -1
        self.mutationRate = mutationRate
        self.numberOfGenes = 0
        if fixSeed:
            random.seed(1337)

    def getGene(self):
        return random.randint(0, 1)

    def newRandomPopulation(self, populationSize):
        self.population = []
        for i in range(populationSize):
            individual = []
            for n in range(self.numberOfGenes):
                individual.append(self.getGene())
            self.population.append(individual)

    def calcFitness(self, individual, correctAnswer):
        assert (len(individual) == len(correctAnswer))
        fitness = 0
        for i in range(len(correctAnswer)):
            if (individual[i] == correctAnswer[i]):
                fitness += 1
        return fitness

    def tournamentFitness(self, numOfParticipants):
        random.shuffle(self.measuredPopulation)
        tournamentBest = self.measuredPopulation[0][0]
        tournamentBestFitness = self.measuredPopulation[0][1]
        for measuredIndividual in self.measuredPopulation[1:numOfParticipants]:
            fit = measuredIndividual[1]
            if fit > tournamentBestFitness:
                tournamentBestFitness = fit
                tournamentBest = measuredIndividual[0]
        self.fittestIndividuals.append(tournamentBest)

    def measureGenerationFitness(self, correctAnswer, populationSize):
        self.measuredPopulation = []
        self.generationFitnessBest = -1
        self.generationFitnessAverage = 0.0
        for individual in self.population:
            fitness = self.calcFitness(individual, correctAnswer)
            self.measuredPopulation.append([individual, fitness])
            self.generationFitnessAverage += fitness
            if fitness > self.generationFitnessBest:
                self.generationFitnessBest = fitness
                self.generationBest = individual
        self.generationFitnessAverage = self.generationFitnessAverage/populationSize

    def generatePopulationOffspring(self):
        self.population = []
        numberOfGenes = len(self.fittestIndividuals[0])
        for n in range(int(len(self.fittestIndividuals)/2)):
            parent1 = self.fittestIndividuals[2*n]
            parent2 = self.fittestIndividuals[(2*n)+1]
            randIndex = random.randint(0, numberOfGenes)
            offspring = []
            offspring[0:randIndex] = parent1[0:randIndex]
            offspring[randIndex:numberOfGenes] = parent2[randIndex:numberOfGenes]
            for i in range(len(offspring)):
                chance = random.random()
                if chance < self.mutationRate:
                    offspring[i] = self.getGene()
            self.population.append(offspring)
        self.fittestIndividuals = []

    def startGeneticAlgorithm(self, populationSize = 10, nonImprovementLimit = 100, correctAnswer = [1, 1, 1, 1, 1, 1, 1, 1, 1]):
        print("Initiating Algorithm")
        if not correctAnswer == []:
            self.numberOfGenes = len(correctAnswer)
        self.newRandomPopulation(populationSize)
        currentGeneration = 0
        allTimeBestFitness = 0
        generationsWithoutImprovement = 0
        plotXaxis = []
        plotYaxisBest = []
        plotYaxisAverage = []
        while(generationsWithoutImprovement < nonImprovementLimit and allTimeBestFitness < self.numberOfGenes):
            self.measureGenerationFitness(correctAnswer, populationSize)
            if self.generationFitnessBest > allTimeBestFitness:
                allTimeBestFitness = self.generationFitnessBest
            else:
                generationsWithoutImprovement += 1
            print("Current Generation: {0}".format(currentGeneration))
            print("Generation's top Fitness score: {0}".format(self.generationFitnessBest))
            print("Generation's average Fitness: {0}".format(self.generationFitnessAverage))
            print("")
            for i in range(populationSize*2):
                self.tournamentFitness(math.floor(populationSize*3/4))
            print("Generation's top:")
            print(self.generationBest)
            print("")
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

#gen = BasicBitGeneticAlgorithm()
#gen.startGeneticAlgorithm()
