from Perceptron.PerceptronClass import perceptron
import math


class sigmoid(perceptron):

    def __init__(self, weights, biass, learnRate = 0.1):
        super().__init__(weights, biass, learnRate)
        self.lastOutput = 0
        self.delta = 0

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        weightedInputs = 0
        for a in range(len(inputs)):
            weightedInputs += inputs[a] * self.weight[a]
        output = 1.0 / (1 + math.exp(- weightedInputs - self.bias))
        self.lastOutput = output
        return output

