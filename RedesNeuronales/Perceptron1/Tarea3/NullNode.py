

class NullNode:
    def __init__(self):
        pass

    def isNull(self):
        return True

    def calcValue(self, x):
        return ''

    def toString(self):
        return ''

    def mutate(self, chanceOfMutation):
        pass