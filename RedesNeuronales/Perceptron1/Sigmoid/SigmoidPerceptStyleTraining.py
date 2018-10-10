from Sigmoid.SigmoidClass import sigmoid
from Perceptron.AbsPerceptronTrain import GenericPerceptronTraining
from random import *


class SigmoidBasicTraining(GenericPerceptronTraining):

    def __init__(self):
        super().__init__()

    def newRadomNeuron(self):
        self.neuron = sigmoid([uniform(-40, 40), uniform(-40, 40)], uniform(-40, 40))

    def trueValue(self, inputs):
        return True

    def randomInputs(self):
        return [getrandbits(1), getrandbits(1)]


class SigmoidORTraining(SigmoidBasicTraining):
    def __init__(self):
        super().__init__()

    def trueValue(self, inputs):
        return inputs[0] or inputs[1]


class SigmoidANDTraining(SigmoidBasicTraining):
    def __init__(self):
        super().__init__()

    def trueValue(self, inputs):
        return inputs[0] and inputs[1]


class SigmoidNANDTraining(SigmoidBasicTraining):
    def __init__(self):
        super().__init__()

    def trueValue(self, inputs):
        return not (inputs[0] and inputs[1])

sand = SigmoidNANDTraining()
sand.learningCurve(0.5)