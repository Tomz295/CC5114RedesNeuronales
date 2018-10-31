import csv
import matplotlib.pyplot as plt
import random
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
        with open('ShuffledSkinData - Train.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                inputs = [int(line['R'])/255, int(line['G'])/255, int(line['B'])/255]
                outputs = [int(line['O'])]
                self.network.trainNetwork(inputs, outputs)

    def trainNEpochs(self, num):
        for n in range(num):
            self.trainSingleEpoch()

    # retorna 1000 datos distintos, 500 de los cuales tienen output 1 y 500 output 0
    # esto reduce la carga al comparar datos en la curva de error y de aprendizaje
    def testData(self):
        with open('ShuffledSkinData - Test.csv', newline='') as testdatacsv:
            read = csv.DictReader(testdatacsv)
            return list(read)

    def learnAndErrorCurves(self, learnCurveThreshold = 0.1, EpochsPerPoint = 1, XPoints = 10):
        plt.grid(True)
        print("Generating Curves")
        print("Progress%:")
        learnYaxis = []
        errorYaxis = []
        Xaxis = []
        data = self.testData()
        for i in range(XPoints):
            learnYvalue = 0
            errorYvalue = 0
            totalValues = 0
            for singledata in data:
                inputs = [int(singledata['R']) / 255, int(singledata['G']) / 255, int(singledata['B']) / 255]
                expectedOutput = [int(singledata['O'])]
                networkOutput = self.network.feedNetwork(inputs)
                diff = expectedOutput[0] - networkOutput[0]
                learnYvalue += int(abs(diff) <= learnCurveThreshold)
                errorYvalue += (abs(diff))**2
                totalValues += 1
            learnYaxis.append(learnYvalue/totalValues)
            errorYaxis.append(errorYvalue)
            Xaxis.append(EpochsPerPoint * i)
            self.trainNEpochs(EpochsPerPoint)
            # print del porcentaje del progreso
            print(str(100.0*(i+1)/(EpochsPerPoint*XPoints))+"%")
        plt.subplot(2,1,1)
        plt.plot(Xaxis, learnYaxis, 'b')
        plt.title('Curva de aprendizaje')
        plt.subplot(2, 1, 2)
        plt.plot(Xaxis, errorYaxis, 'r')
        plt.title('Curva de error')


skin = SkinDataset()
skin.learnAndErrorCurves()
net = skin.network