import NeuralNetworkPack.NeuralLayer


# NeuralNetwork class
class NeuralNet:
    def __init__(self):
        self.firstLayer = None
        self.outputLayer = None
        self.layerList = []

    def appendLayer(self, layer):

