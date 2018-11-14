import random
import math
import copy

class BasicGeneticAlgorithm1:
    def __init__(self):
        self.population = []
        self.populationSize = 0
        self.measuredPopulation = []
        self.fittestIndividuals = []
        self.generationFitnessAverage = 0
        self.generationFitnessBest = -1

    def newRandomBitPopulation(self, numOfGenes):
        self.population = []
        for i in range(self.populationSize):
            individual = []
            for n in range(numOfGenes):
                individual.append(random.randint(0, 1))
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

    def measureGenerationFitness(self, correctAnswer):
        self.measuredPopulation = []
        self.generationFitnessBest = -1
        self.generationFitnessAverage = 0.0
        for individual in self.population:
            fitness = self.calcFitness(individual, correctAnswer)
            self.measuredPopulation.append([individual, fitness])
            self.generationFitnessAverage += fitness
            if fitness > self.generationFitnessBest:
                self.generationFitnessBest = fitness
        self.generationFitnessAverage = self.generationFitnessAverage/self.populationSize

    def generateBitPopulationOffspring(self):
        self.population = []
        numberOfGenes = len(self.fittestIndividuals[0])
        randomIndexArray = list(range(numberOfGenes))
        genesToChange = math.floor(numberOfGenes*2/3)
        for i in range(self.populationSize):
            offspring = copy.copy(random.choice(self.fittestIndividuals))
            random.shuffle(randomIndexArray)
            for index in randomIndexArray[0:genesToChange]:
                offspring[index] = random.randint(0, 1)
            self.population.append(offspring)
        self.fittestIndividuals = []

    def startBitGeneticAlgorithm(self, populationSize = 50, correctAnswer = [0,0,1,0,1,1,0,1,1], nonImprovementLimit = 20):
        self.populationSize = populationSize
        print("Initiating Algorithm")
        numberOfGenes = len(correctAnswer)
        self.newRandomBitPopulation(numberOfGenes)
        currentGeneration = 1
        allTimeBestFitness = 0
        generationsWithoutImprovement = 0
        while(generationsWithoutImprovement < nonImprovementLimit and allTimeBestFitness < numberOfGenes):
            self.measureGenerationFitness(correctAnswer)
            if self.generationFitnessBest > allTimeBestFitness:
                allTimeBestFitness = self.generationFitnessBest
            else:
                generationsWithoutImprovement += 1
            print("Current Generation: {0}".format(currentGeneration))
            print("Generation's top Fitness score: {0}".format(self.generationFitnessBest))
            print("Generation's average Fitness: {0}".format(self.generationFitnessAverage))
            print("")
            for i in range(5):
                self.tournamentFitness(math.floor(populationSize/5))
            print("Generation's top:")
            for individual in self.fittestIndividuals:
                print(individual)
            print("")
            self.generateBitPopulationOffspring()
            currentGeneration += 1
        if generationsWithoutImprovement >= nonImprovementLimit:
            print("Limit of generations without improvement reached. The answer was not found")
        else:
            print("The answer has been reached by Generation {0}".format(currentGeneration-1))

gen = BasicGeneticAlgorithm1()
gen.startBitGeneticAlgorithm()