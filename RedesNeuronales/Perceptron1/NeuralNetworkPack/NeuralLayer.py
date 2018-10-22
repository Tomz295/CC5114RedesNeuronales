from Sigmoid.SigmoidClass import sigmoid
from NeuralNetworkPack.NeuralLayerNullObject import NullLayer
from random import *


class NeuralLayer:
    def __init__(self):
        self.neuronList = []
        self.nextLayer = NullLayer()
        self.prevLayer = NullLayer()

    def isNull(self):
        return False

    # Cambia la lista de neuronas para que tenga X neuronas con 5 entradas cada una
    def setXNeuronsWithYInputs(self, X, Y):
        neurons = []
        for x in range(X):
            weights = []
            for y in range(Y):
                weights.append(uniform(-2, 2))
            neurons.append(sigmoid(weights,uniform(-2, 2)))
        self.neuronList = neurons

    def setNeurons(self, neurons):
        self.neuronList = neurons

    def getNeuronList(self):
        return self.neuronList

    def getNext(self):
        return self.nextLayer

    def setNext(self, layer):
        self.nextLayer = layer

    def getPrev(self):
        return self.prevLayer

    def setPrev(self, layer):
        self.prevLayer = layer

    def feedLayer(self, inputs):
        outputs = []
        for neuron in self.neuronList:
            outputs.append(neuron.feed(inputs))
        return self.getNext().feedLayer(outputs)

    def backPropagationOutLayer(self, error):
        for n in range(len(self.neuronList)):
            self.neuronList[n].adjustDelta(error[n])
        self.prevLayer.backPropagation()

    def backPropagation(self):
        for n in range(len(self.neuronList)):
            trueError = 0
            for sigm in self.nextLayer.getNeuronList():
                trueError += sigm.getDelta() * sigm.getWeights()[n]
                #print([sigm.getDelta(), sigm.getWeights()[n], trueError])
            self.neuronList[n].adjustDelta(trueError)
        self.prevLayer.backPropagation()

    def updateWeights(self):
        for sigm in self.neuronList:
            sigm.updateNeuron()
        self.nextLayer.updateWeights()


