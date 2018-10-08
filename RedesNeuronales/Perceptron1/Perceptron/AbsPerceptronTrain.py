import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from random import *
from abc import ABC


# Clase generica que entrena un perceptron, usada solo para ser heredada
# Se debe hacer override a los metodos trueValue y randomInputs
class GenericPerceptronTraining(ABC):
    def __init__(self):
        self.neuron = ""
        self.newRadomNeuron()

    def newRadomNeuron(self):
        self.neuron = perceptron([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    def randomInputs(self):
        pass

    # Valor que debiera obtenerse a partir de los inputs entregados.
    # Se debe hacer override con el valor correspondiente
    def trueValue(self, inputs):
        pass

    def trainNeuron(self, iterations):
        for a in range(iterations):
            randCoords = self.randomInputs()
            expectedOutput = self.trueValue(randCoords)
            self.neuron.train(randCoords, expectedOutput)

    def learningCurve(self, TrainsPerPoint = 100, XPoints = 20):
        self.newRadomNeuron()
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
                perceptOutput = self.neuron.feed(randCoords[n])
                Yvalue += int(perceptOutput == expectedOutput[n])
            Yaxis.append(Yvalue/500.0)
            Xaxis.append(TrainsPerPoint * i)
            self.trainNeuron(TrainsPerPoint)
        plt.plot(Xaxis, Yaxis)