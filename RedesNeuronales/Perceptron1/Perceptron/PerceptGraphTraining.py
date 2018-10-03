import matplotlib.pyplot as plt
from Perceptron.PerceptronClass import perceptron
from random import *


class GraphTraining:
    # point1 & point2 -> [x, y]
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.percept = null

    def GraphTrain(self, iterations):
        self.percept = perceptron([uniform(-4,4), uniform(-4,4)], uniform(-4,4))

