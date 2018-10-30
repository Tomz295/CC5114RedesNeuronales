import csv
import matplotlib.pyplot as plt
from NeuralNetworkPack.NeuralNetwork import NeuralNet


# El dataset utilizado indica si un color se puede considerar "color de piel" basado en los
# valores RGB (ordenado BGR en el dataset) del color. El output consiste en 1 si el color
# se puede considerar color de piel (no necesariamente piel clara) y 0 si no
class SkinDataset:
    def __init__(self):
        self.network = NeuralNet()
        self.network.newNetworkWithRandomWeights([4, 1], 3)

    def newNetwork(self, neronsPerLayerList, outputs, learningRate):
        self.network.newNetworkWithRandomWeights(neronsPerLayerList, outputs, learningRate)

    def trainSingleEpoch(self):
        with open('IsSkinColorData.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                inputs = [int(line['R'])/255, int(line['G'])/255, int(line['B'])/255]
                outputs = [int(line['O'])]
                self.network.trainNetwork(inputs, outputs)

    def trainNEpochs(self, num):
        for n in range(num):
            self.trainSingleEpoch()

    def learningCurve(self, threshold = 0.25, EpochsPerPoint = 1, XPoints = 10):
        plt.grid(True)
        Yaxis = []
        Xaxis = []
        for i in range(XPoints):
            Yvalue = 0
            with open('IsSkinColorData.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for line in reader:
                    inputs = [int(line['R']) / 255, int(line['G']) / 255, int(line['B']) / 255]
                    expectedOutput = [int(line['O'])]
                    networkOutput = self.network.feedNetwork(inputs)
                    diff = expectedOutput[0] - networkOutput[0]
                    Yvalue += int(abs(diff) <= threshold)
            Yaxis.append(Yvalue/245057.0)
            Xaxis.append(EpochsPerPoint * i)
            self.trainNEpochs(EpochsPerPoint)
            print(i)
        plt.plot(Xaxis, Yaxis)

skin = SkinDataset()
skin.learningCurve()