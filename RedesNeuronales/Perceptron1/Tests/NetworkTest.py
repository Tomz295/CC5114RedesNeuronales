from NeuralNetworkPack.NeuralLayer import NeuralLayer
from NeuralNetworkPack.NeuralNetwork import NeuralNet
from Sigmoid.SigmoidClass import sigmoid

net = NeuralNet()
layer1 = NeuralLayer()
layer2 = NeuralLayer()

neuron1 = sigmoid([0.4, 0.3], 0.5, 0.5)
layer1.neuronList.append(neuron1)

neuron2 = sigmoid([0.3], 0.4, 0.5)
layer2.neuronList.append(neuron2)

net.appendLayer(layer1)
net.appendLayer(layer2)

net.trainNetwork([1, 1], [1])

print("neuron1: bias and weights")
print(neuron1.bias)
print(neuron1.getWeights())

print("neuron2: bias and weights")
print(neuron2.bias)
print(neuron2.getWeights())