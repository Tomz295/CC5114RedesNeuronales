from Tarea3.EquationNode import ENode
from GeneticAlgorithm.BasicGeneticAlgorithm import BasicBitGeneticAlgorithm

class FuncFindAlgorithm(BasicBitGeneticAlgorithm):
    def __init__(self, lowestValue = 1, highestValue = 10, chanceOfX = 0.4, chanceOfNumber = 0.4,
                 mutationRate = 0.1, testFromValue = -10, testToValue = 10, treeSize = 5, fixSeed = False):
        super().__init__(mutationRate, fixSeed)
        self.low = lowestValue
        self.high = highestValue
        self.xchance = chanceOfX
        self.numchance = chanceOfNumber
        self.testrange = list(range(testFromValue, testToValue + 1))
        self.size = treeSize

    def newRandomPopulation(self, populationSize):
        self.population = []
        for i in range(populationSize):
            individual = ENode(self.low, self.high, self.xchance)
            individual.buildTree(self.numchance, self.size)
            self.population.append(individual)

    def calcFitness(self, individual, correctAnswer):
        fitness = 0
        for i in range(len(correctAnswer)):
            fitness -= abs(correctAnswer[i] - individual.calcValue(self.testrange[i]))
        return fitness

    def generatePopulationOffspring(self):
        self.population = []
        for n in range(int(len(self.fittestIndividuals)/2)):
            parent1 = self.fittestIndividuals[2*n]
            parent2 = self.fittestIndividuals[(2*n)+1]
            #randIndex = random.randint(0, numberOfGenes)
            #offspring = []
            #offspring[0:randIndex] = parent1[0:randIndex]
            #offspring[randIndex:numberOfGenes] = parent2[randIndex:numberOfGenes]
            parent1.right = parent2.right
            parent1.mutate(self.mutationRate)
            self.population.append(parent1)
        self.fittestIndividuals = []

    def startGeneticAlgorithm(self, functionToFindInString, populationSize = 10, nonImprovementLimit = 100):
        AnswerValues = []
        for val in self.testrange:
            x = val
            result = eval(functionToFindInString)
            AnswerValues.append(result)
        print("Initiating Algorithm")
        self.newRandomPopulation(populationSize)
        currentGeneration = 0
        allTimeBestFitness = 0
        generationsWithoutImprovement = 0
        plotXaxis = []
        plotYaxisBest = []
        plotYaxisAverage = []
        while(generationsWithoutImprovement < nonImprovementLimit and allTimeBestFitness < self.numberOfGenes):
            self.measureGenerationFitness(AnswerValues, populationSize)
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