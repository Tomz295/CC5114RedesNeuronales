from Perceptron.PerceptronClass import perceptron
import math


class sigmoid(perceptron):

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        weightedInputs = 0
        for a in range(len(inputs)):
            weightedInputs += inputs[a] * self.weight[a]
        output = 1.0 / (1+ math.exp(- weightedInputs - self.bias))
        return output

