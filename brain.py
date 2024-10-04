import random

class Brain:
    def __init__(self):
        self.weights = None
        self.random_weights()

    def perseptron(self, matrix):
        sum = 0 # вхід персептрона
        rety = None # зенайдений вихід персептрона
        test = None # напрямок корегування ваг

        for i in range(20):
            for j in range(20):
                sum+=matrix[i][j]*self.weights[i][j]

    def random_weights(self):
        for i in range(20):
            row = []
            for j in range(20):
                row.append((-3 + random.randint(0, 5)) / 10.0)
            self.weights.append(row)


