

class NullLayer:
    def __init__(self):
        pass

    def isNull(self):
        return True

    def feedLayer(self, inputs):
        return inputs

    def backPropagation(self):
        pass

    def backPropagationOutLayer(self, error):
        assert False

    def updateWeights(self):
        pass

    def getNeuronList(self):
        return []