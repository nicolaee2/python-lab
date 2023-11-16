import numpy as np
from Neuron import Neuron
from Util import Util


class Layer:
    def __init__(self, input_count, neuron_count):
        self.neurons = []
        for i in range(neuron_count):
            self.neurons.append(Neuron(np.random.uniform(-1, 1, input_count)))

    def compute_output(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.compute(inputs))
        return Util.activation_function_sigmoid(outputs)

    def __str__(self):
        neurons = ""
        for neuron in self.neurons:
            neurons += str(neuron) + "\n"
        return "Layer: neurons = " + neurons
