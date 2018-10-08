import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from Perceptron.AbsPerceptronTrain import GenericPerceptronTraining
from random import *


# Clase que entrena un perceptron para dibujar puntos en un grafo cuyo color
# depende de si se está bajo la linea o no. Linea se puede definir en el constructor
# Grafo se dibuja entre valores de -100 y 100
# True -> Bajo la linea
# False -> Sobre la linea
class GraphTraining(GenericPerceptronTraining):
    def __init__(self, pendiente = 3, interseccionY = 5):
        self.m = pendiente
        self.n = interseccionY
        super().__init__()

    # Retorna una lista de un par de coordenadas al azar entre -100 y 100
    def randomInputs(self):
        return [uniform(-20, 20), uniform(-20, 20)]

    def trueValue(self, inputs):
        return inputs[1] < (inputs[0] * self.m + self.n)


    # Dibuja un grafo con {quantity} numero de puntos
    def drawPoints(self, quantity):
        plt.plot([-20, 20], [(-20 * self.m + self.n), (20 * self.m + self.n)], 'r')
        for a in range(quantity):
            randCoords = self.randomInputs()
            isBelow = self.neuron.feed(randCoords)
            if isBelow:
                plt.plot(randCoords[0], randCoords[1], 'bo')
            else:
                plt.plot(randCoords[0], randCoords[1], 'ro')


g = GraphTraining()
g.learningCurve()
