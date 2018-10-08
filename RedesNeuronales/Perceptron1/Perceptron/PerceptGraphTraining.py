import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from random import *

# Clase que entrena un perceptron para dibujar puntos en un grafo cuyo color
# depende de si se está bajo la linea o no. Linea se puede definir en el constructor
# Grafo se dibuja entre valores de -100 y 100
# True -> Bajo la linea
# False -> Sobre la linea
class GraphTraining:
    def __init__(self, pendiente = 3, interseccionY = 5):
        self.m = pendiente
        self.n = interseccionY
        self.percept = perceptron([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    def newRadomPerceptron(self):
        self.percept = perceptron([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    # Retorna una lista de un par de coordenadas al azar entre -100 y 100
    def randomInputs(self):
        return [uniform(-20, 20), uniform(-20, 20)]

    def trueValue(self, inputs):
        return inputs[1] < (inputs[0] * self.m + self.n)

    def GraphTrain(self, iterations):
        for a in range(iterations):
            randCoords = self.randomInputs()
            expectedOutput = self.trueValue(randCoords)
            self.percept.train(randCoords, expectedOutput)

    # Dibuja un grafo con {quantity} numero de puntos
    def drawPoints(self, quantity):
        plt.plot([-20, 20], [(-20 * self.m + self.n), (20 * self.m + self.n)], 'r')
        for a in range(quantity):
            randCoords = self.randomInputs()
            isBelow = self.percept.feed(randCoords)
            if isBelow:
                plt.plot(randCoords[0], randCoords[1], 'bo')
            else:
                plt.plot(randCoords[0], randCoords[1], 'ro')

    def LearningCurve(self, TrainsPerPoint = 100, XPoints = 20):
        self.newRadomPerceptron()
        plt.grid(True)
        Yaxis = []
        Xaxis = []
        randCoords = []
        expectedOutput = []
        for x in range(500):
            rand = self.randomInputs()
            randCoords.append(rand)
            expectedOutput.append(self.trueValue(rand))
        for i in range(XPoints):
            Yvalue = 0
            for n in range(500):
                perceptOutput = self.percept.feed(randCoords[n])
                Yvalue += int(perceptOutput == expectedOutput[n])
            Yaxis.append(Yvalue/500.0)
            Xaxis.append(TrainsPerPoint * i)
            self.GraphTrain(TrainsPerPoint)
        plt.plot(Xaxis, Yaxis)

g = GraphTraining()
g.LearningCurve()