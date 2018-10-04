import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from random import *

# Clase que entrena un perceptron para dibujar puntos en un grafo cuyo color
# depende de si se está bajo la linea o no. Linea se puede definir en el constructor
# Grafo se dibuja entre valores de -100 y 100
# True -> Bajo la linea
# False -> Sobre la linea
class GraphTraining:
    def __init__(self, pendiente = 2, interseccionY = 30):
        self.m = pendiente
        self.n = interseccionY
        self.percept = perceptron([uniform(-4, 4), uniform(-4, 4)], uniform(-4, 4))

    def newRadomPerceptron(self):
        self.percept = perceptron([uniform(-4, 4), uniform(-4, 4)], uniform(-4, 4))

    # Retorna una lista de un par de coordenadas al azar entre -100 y 100
    def randomCoords(self):
        return [uniform(-100, 100), uniform(-100, 100)]

    def GraphTrain(self, iterations):
        for a in range(iterations):
            randCoords = self.randomCoords()
            expectedOutput = randCoords[1] < (randCoords[0] * self.m + self.n)
            self.percept.train(randCoords, expectedOutput)

    # Dibuja un grafo con {quantity} numero de puntos
    def drawPoints(self, quantity):
        plt.plot([-100, 100], [(-100 * self.m + self.n), (100 * self.m + self.n)], 'r')
        for a in range(quantity):
            randCoords = self.randomCoords()
            isBelow = self.percept.feed(randCoords)
            if isBelow:
                plt.plot(randCoords[0], randCoords[1], 'bo')
            else:
                plt.plot(randCoords[0], randCoords[1], 'ro')
