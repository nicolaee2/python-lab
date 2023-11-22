import numpy as np


class Neuron:
    def __init__(self, weights):
        self.weights = weights

    def compute(self, inputs):
        return np.dot(inputs, self.weights)

    def __str__(self):
        return "Neuron: weights = " + str(self.weights)