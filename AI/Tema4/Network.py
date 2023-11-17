from Layer import Layer
from Util import Util


class Network:

    def __init__(self, input_layer_size, hidden_layer_sizes, output_layer_size, learning_rate=0.1, epochs=2):
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

    def evaluate_and_train(self, train_x, train_y):
        for epoch in range(self.epochs):
            error = 0
            for x, y in zip(train_x, train_y):
                output = self.evaluate(x)
                target = [0 for _ in range(self.output_layer_size)]
                target[y - 1] = 1
                error += Util.error_function_mse(output, target)
                print(output)
                print(y)
                print()
            print("Epoch " + str(epoch) + " error: " + str(error / len(train_x)))

    def __str__(self):
        layers = ""
        for layer in self.layers:
            layers += str(layer) + "\n"
        return "Network: layers = " + layers


