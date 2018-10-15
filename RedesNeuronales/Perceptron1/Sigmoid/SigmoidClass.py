from Perceptron.PerceptronClass import perceptron
import math


class sigmoid(perceptron):

    def __init__(self, weights, biass, learnRate = 0.1):
        super().__init__(weights, biass, learnRate)
        self.lastInputs = 0
        self.lastOutput = 0
        self.delta = 0

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        weightedInputs = 0
        for a in range(len(inputs)):
            weightedInputs += inputs[a] * self.weight[a]
        output = 1.0 / (1 + math.exp(- weightedInputs - self.bias))
        self.lastInputs = inputs
        self.lastOutput = output
        return output

    def getWeights(self):
        return self.weight

    def getDelta(self):
        return self.delta

    def adjustDelta(self, error):
        self.delta = error * self.lastOutput * (1 - self.lastOutput)

    def updateNeuron(self):
        for n in range(len(self.weight)):
            self.weight[n] = self.weight[n] + (self.lr * self.delta * self.lastInputs[n])
        self.bias = self.bias + (self.lr * self.delta)

