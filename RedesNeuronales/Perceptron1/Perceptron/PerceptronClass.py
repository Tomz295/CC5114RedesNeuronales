class perceptron:
    def __init__(self, weights, biass):
        self.weight = weights
        self.bias = biass

    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        suma = 0
        for a in range(len(inputs)):
            suma += inputs[a] * self.weight[a]
        suma += self.bias
        return suma > 0


class AND(perceptron):
    def __init__(self):
        super().__init__([2, 2], -3)


class OR(perceptron):
    def __init__(self):
        super().__init__([1, 1], 0)


class NAND(perceptron):
    def __init__(self):
        super().__init__([-2, -2], 3)


class SUMADOR:
    def __init__(self):
        self.nand = NAND()

    def sumar2bits(self, bit1, bit2):
        nand1 = self.nand.feed([bit1, bit2])
        nand2 = self.nand.feed([bit1, nand1])
        nand3 = self.nand.feed([bit2, nand1])
        suma = self.nand.feed([nand2, nand3])
        carry = self.nand.feed([nand1, nand1])
        return int(suma), int(carry)

