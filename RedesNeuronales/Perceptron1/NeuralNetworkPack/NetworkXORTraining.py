import matplotlib.pyplot as plt
from NeuralNetworkPack.NeuralNetwork import NeuralNet
from random  import *

class NetworkXORTraining:
    def __init__(self):
        self.network = NeuralNet()

    def newNetwork(self, neuronsPerLayerList):
        self.network.newNetworkWithRandomWeights(neuronsPerLayerList, 2)
        assert(neuronsPerLayerList[-1] == 1)

    def randomInputs(self):
        return [randint(0,1),randint(0,1)]

    def expectedOutputs(self, inputs):
        return [inputs[0] and inputs[1]]

    def trainNetwork(self, numberOfTrainings):
        for n in range(numberOfTrainings):
            Inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
            expectedOut = [[0], [0], [0], [1]]
            for i in range(4):
                self.network.trainNetwork(Inputs[i], expectedOut[i])

    def feed(self, inputs):
        return self.network.feedNetwork(inputs)

    def learningCurve(self, threshold = 0.3, TrainsPerPoint = 100, XPoints = 50):
        self.newNetwork([1])
        plt.grid(True)
        Yaxis = []
        Xaxis = []
        randCoords = []
        expectedOutput = []
        for x in range(500):
            rand = self.randomInputs()
            randCoords.append(rand)
            expectedOutput.append(self.expectedOutputs(rand))
        for i in range(XPoints):
            Yvalue = 0
            for n in range(500):
                networkOutput = self.network.feedNetwork(randCoords[n])
                diff = expectedOutput[n][0] - networkOutput[0]
                Yvalue += int(abs(diff) <= threshold)
            Yaxis.append(Yvalue/500.0)
            Xaxis.append(TrainsPerPoint * i)
            self.trainNetwork(TrainsPerPoint)
        plt.plot(Xaxis, Yaxis)


net = NetworkXORTraining()
net.learningCurve()
