from NeuralNetworkPack.NeuralLayer import NeuralLayer
from NeuralNetworkPack.NeuralNetwork import NeuralNet
from Sigmoid.SigmoidClass import sigmoid
import unittest


class NetworkTests(unittest.TestCase):

    def setUp(self):
        self.net = NeuralNet()
        self.layer1 = NeuralLayer()
        self.layer2 = NeuralLayer()
        self.neuron1 = sigmoid([0.4, 0.3], 0.5, 0.5)
        self.neuron2 = sigmoid([0.3], 0.4, 0.5)

    def testLayer(self):
        self.assertEqual(len(self.layer1.neuronList), 0)
        self.layer1.setXNeuronsWithYInputs(5, 2)
        self.assertEqual(len(self.layer1.neuronList), 5)

    def testAppendLayer(self):
        self.assertEqual(len(self.net.layerList), 0)
        self.net.appendLayer(self.layer1)
        self.assertEqual(self.net.firstLayer, self.layer1)
        self.assertEqual(self.net.outputLayer, self.layer1)
        self.assertEqual(len(self.net.layerList), 1)

        self.net.appendLayer(self.layer2)
        self.assertEqual(self.net.firstLayer, self.layer1)
        self.assertEqual(self.net.outputLayer, self.layer2)
        self.assertEqual(len(self.net.layerList), 2)

# testcase entregado en ucursos
    def testCase1(self):
        self.layer1.setNeurons([self.neuron1])
        self.layer2.setNeurons([self.neuron2])
        self.net.appendLayer(self.layer1)
        self.net.appendLayer(self.layer2)
        self.net.trainNetwork([1, 1], [1])

        self.assertEqual(round(self.neuron1.weight[0], 15), 0.402101508999489)
        self.assertEqual(round(self.neuron1.weight[1], 15), 0.302101508999489)
        self.assertEqual(round(self.neuron2.weight[0], 15), 0.330262548639919)


if __name__ == '__main__':
    unittest.main()
