from Layer import Layer
from Util import Util


class Network:

    def __init__(self, input_layer_size, hidden_layer_sizes, output_layer_size, learning_rate=0.05, epochs=1000):
        self.layers = []
        self.layers.append(Layer(input_layer_size, hidden_layer_sizes[0]))
        for i in range(1, len(hidden_layer_sizes)):
            self.layers.append(Layer(hidden_layer_sizes[i - 1], hidden_layer_sizes[i]))
        self.layers.append(Layer(hidden_layer_sizes[-1], output_layer_size))

        self.input_layer_size = input_layer_size
        self.hidden_layer_sizes = hidden_layer_sizes
        self.output_layer_size = output_layer_size
        self.learning_rate = learning_rate
        self.epochs = epochs

    def evaluate(self, inputs):
        outputs = inputs
        for layer in self.layers:
            outputs = layer.compute_output(outputs)
        return outputs

    def train(self, train_x, train_y):
        for epoch in range(self.epochs):
            total_error = 0
            for x, y in zip(train_x, train_y):

                layer_inputs = x
                for layer in self.layers:
                    layer_inputs = layer.compute_output(layer_inputs)

                target = [0 for _ in range(self.output_layer_size)]
                target[y - 1] = 1
                output_errors = [target[i] - self.layers[-1].output[i] for i in range(self.output_layer_size)]

                output_deltas = [output_errors[i] * Util.activation_function_derivative(self.layers[-1].output)[i] for i
                                 in range(self.output_layer_size)]

                for i in reversed(range(len(self.layers))):
                    layer = self.layers[i]
                    inputs = x if i == 0 else self.layers[i - 1].output
                    new_deltas = [0.0 for _ in range(len(inputs))]
                    for j, neuron in enumerate(layer.neurons):
                        for k in range(len(neuron.weights)):
                            neuron.weights[k] += self.learning_rate * output_deltas[j] * inputs[k]
                            if i != 0:
                                new_deltas[k] += output_deltas[j] * neuron.weights[k]
                    if i != 0:
                        output_deltas = [
                            new_deltas[k] * Util.activation_function_derivative(self.layers[i - 1].output)[k] for k in
                            range(len(new_deltas))]

                total_error += Util.error_function_mse(self.layers[-1].output, target)

            # Output the error at the end of each epoch
            print(f"Epoch {epoch + 1}/{self.epochs}, Error: {total_error / len(train_x)}")

    def __str__(self):
        layers = ""
        for layer in self.layers:
            layers += str(layer) + "\n"
        return "Network: layers = " + layers


