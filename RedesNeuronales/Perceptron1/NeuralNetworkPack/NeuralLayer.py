from Sigmoid.SigmoidClass import sigmoid


class NeuralLayer:
    def __init__(self, neurons):
        self.neuronList = neurons
        self.nextLayer = None
        self.prevLayer = None

    def addNeuron(self, neuron):
        self.neuronList.append(neuron)

    def setNeurons(self, neurons):
        self.neuronList = neurons

    def getNext(self):
        return self.nextLayer

    def getPrev(self):
        return self.prevLayer

    def feedLayer(self, inputs):
        outputs = []
        for neuron in self.neuronList:
            outputs.append(neuron.feed(inputs))
        if self.getNext() == None:
            return outputs
        else
            return self.getNext().feedLayer(outputs)


