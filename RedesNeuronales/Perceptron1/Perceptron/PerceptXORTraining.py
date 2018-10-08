import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from random import *

# Clase que entrena un perceptron para dibujar puntos en un grafo cuyo color
# depende de si se está bajo la linea o no. Linea se puede definir en el constructor
# Grafo se dibuja entre valores de -100 y 100
# True -> Bajo la linea
# False -> Sobre la linea
class XORTraining:
    def __init__(self):
        self.percept = perceptron([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    def newRadomPerceptron(self):
        self.percept = perceptron([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    # Retorna una lista de un par de coordenadas al azar entre -100 y 100
    def randomBits(self):
        return [getrandbits(1), getrandbits(1)]

    def GraphTrain(self, iterations):
        for a in range(iterations):
            randBits = self.randomBits()
            expectedOutput = (randBits[0] ^ randBits[1])
            self.percept.train(randBits, expectedOutput)

    def LearningCurve(self, TrainsPerPoint = 100, XPoints = 20):
        self.newRadomPerceptron()
        plt.grid(True)
        Yaxis = []
        Xaxis = []
        randBits = []
        expectedOutput = []
        for x in range(500):
            rand = self.randomBits()
            randBits.append(rand)
            expectedOutput.append(rand[1] ^ rand[0])
        for i in range(XPoints):
            Yvalue = 0
            for n in range(500):
                perceptOutput = self.percept.feed(randBits[n])
                Yvalue += int(perceptOutput == expectedOutput[n])
            Yaxis.append(Yvalue/500.0)
            Xaxis.append(TrainsPerPoint * i)
            self.GraphTrain(TrainsPerPoint)
        plt.plot(Xaxis, Yaxis)

xor = XORTraining()
xor.LearningCurve()
