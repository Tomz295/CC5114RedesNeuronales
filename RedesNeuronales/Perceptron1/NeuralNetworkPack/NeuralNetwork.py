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
            layer.setPrev(self.outputLayer)
        self.layerList.append(layer)
        self.outputLayer = layer

    # Creates a new network by accepting a list which indicates
    # the number of neurons on each layer.
    def newNetworkWithRandomWeights(self, neuronsPerLayer, numberOfInputs):
        nOfInputs = numberOfInputs
        for numberOfNeurons in neuronsPerLayer:
            newLayer = NeuralLayer()
            newLayer.setXNeuronsWithYInputs(numberOfNeurons,nOfInputs)
            self.appendLayer(newLayer)
            nOfInputs = numberOfNeurons


    def clearLayers(self):
        self.firstLayer = NullLayer()
        self.outputLayer = NullLayer()
        self.layerList = []

    def feedNetwork(self, inputs):
        return self.firstLayer.feedLayer(inputs)

    # Genera una sola iteracion de entrenamiento (entrena una vez)
    # Para entrenar varias veces se debe llamar este metodo dentro de algun loop
    def trainNetwork(self, inputList, expectedOutputs):
        actualOutputs = self.feedNetwork(inputList)
        error = []
        for n in range(len(actualOutputs)):
            error.append(expectedOutput[n] - actualOutputs[n])
        self.outputLayer.backPropagationOutLayer(error)
        self.firstLayer.updateWeights()


