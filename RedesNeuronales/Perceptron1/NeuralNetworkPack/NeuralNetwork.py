from NeuralNetworkPack.NeuralLayer import NeuralLayer
from NeuralNetworkPack.NeuralLayerNullObject import NullLayer


# NeuralNetwork class
class NeuralNet:
    def __init__(self):
        self.firstLayer = NullLayer()
        self.outputLayer = NullLayer()
        self.layerList = []

    def appendLayer(self, layer):
        if self.firstLayer.isNull():
            self.firstLayer = layer
        else:
            self.outputLayer.setNext(layer)
            layer.setPrev(self.outputLayer)
        self.layerList.append(layer)
        self.outputLayer = layer

    # Creates a new network by accepting a list which indicates
    # the number of neurons on each layer.
    # neuronsPerLayer = list[]
    # numberOfInputs = int
    def newNetworkWithRandomWeights(self, neuronsPerLayerList, numberOfInputs, learningRate = 0.5):
        self.clearLayers()
        nOfInputs = numberOfInputs
        for numberOfNeurons in neuronsPerLayerList:
            newLayer = NeuralLayer()
            newLayer.setXNeuronsWithYInputs(numberOfNeurons, nOfInputs, learningRate)
            self.appendLayer(newLayer)
            nOfInputs = numberOfNeurons


    def clearLayers(self):
        self.firstLayer = NullLayer()
        self.outputLayer = NullLayer()
        self.layerList = []

    # Entrega Inputs en forma de una lista a la red neuronal
    def feedNetwork(self, inputs):
        return self.firstLayer.feedLayer(inputs)

    # Genera una sola iteracion de entrenamiento (entrena una vez)
    # Para entrenar varias veces se debe llamar este metodo dentro de algun loop
    def trainNetwork(self, inputList, expectedOutputs):
        actualOutputs = self.feedNetwork(inputList)
        error = []
        for n in range(len(actualOutputs)):
            error.append(expectedOutputs[n] - actualOutputs[n])
            #print (error)
        self.outputLayer.backPropagationOutLayer(error)
        self.firstLayer.updateWeights()


