class perceptron:
    # Construnctor perceptron
    # weights -> list[] de pesos de cada entrada
    # biass -> bias del perceptron
    def __init__(self, weights, biass, learnRate = 0.1):
        self.weight = weights
        self.bias = biass
        self.lr = learnRate

    # Recibe una list[] de entradas y entrega la salida booleana correspondiente
    # return -> bool
    def feed(self, inputs):
        assert len(inputs) == len(self.weight)
        suma = 0
        for a in range(len(inputs)):
            suma += inputs[a] * self.weight[a]
        suma += self.bias
        return suma > 0

    # Entrena el perceptron a partir de una lista de inputs y el output booleano esperado
    # inputs -> list[] de inputs
    # expectedOutput -> bool del output esperado
    def train(self, inputs, expectedOutput):
        realOut = self.feed(inputs)
        difference = int(expectedOutput - realOut)
        for n in range(len(inputs)):
            oldweight = self.weight[n]
            self.weight[n] = oldweight + (self.lr * inputs[n] * difference)
        self.bias = self.bias + (self.lr * difference)


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

