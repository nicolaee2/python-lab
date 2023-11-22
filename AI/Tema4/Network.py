from Layer import Layer
from Util import Util
import matplotlib.pyplot as plt


class Network:
    def __init__(self, input_layer_size, hidden_layer_sizes, output_layer_size, learning_rate=0.05, epochs=100):
        # Initialize the network with specified layer sizes and parameters for learning
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
        # Pass the inputs through each layer of the network to get the output
        outputs = inputs
        for layer in self.layers:
            outputs = layer.compute_output(outputs)
        return outputs

    def train(self, train_x, train_y):
        train_errors = []

        for epoch in range(self.epochs):
            # start with no error at the beginning of each epoch
            total_error = 0

            for x, y in zip(train_x, train_y):
                # get the network's current output for this example
                self.evaluate(x)

                # create a list that says what the correct output should have been
                target = [0 for _ in range(self.output_layer_size)]
                target[y - 1] = 1

                # figure out how different the actual output is from the correct output
                output_errors = [target[i] - self.layers[-1].output[i] for i in range(self.output_layer_size)]

                # adjust the difference by how much the output can change (gradient)
                output_deltas = [output_errors[i] * Util.activation_function_derivative(self.layers[-1].output)[i] for i
                                 in range(self.output_layer_size)]

                # start from the end and move backwards
                for i in reversed(range(len(self.layers))):
                    layer = self.layers[i]  # Look at each layer.
                    inputs = x if i == 0 else self.layers[i - 1].output

                    # prepare to calculate new adjustments
                    new_deltas = [0.0 for _ in range(len(inputs))]

                    # for every neuron in the layer, update its weights
                    for j, neuron in enumerate(layer.neurons):
                        for k in range(len(neuron.weights)):

                            neuron.weights[k] += self.learning_rate * output_deltas[j] * inputs[k]
                            # if not the first layer, calculate how much this neuron's error affects the previous layer
                            if i != 0:
                                new_deltas[k] += output_deltas[j] * neuron.weights[k]

                    # if not the first layer, the error adjustments we just calculated become the errors for the previous layer
                    if i != 0:
                        output_deltas = [
                            new_deltas[k] * Util.activation_function_derivative(self.layers[i - 1].output)[k] for k in
                            range(len(new_deltas))]

                # add up all the errors for each example to get the total error for this epoch.
                total_error += Util.error_function_mse(self.layers[-1].output, target)

            train_errors.append(total_error / len(train_x))

            print(f"Epoch {epoch + 1}/{self.epochs}, Error: {total_error / len(train_x)}")

        plt.plot(train_errors)
        plt.xlabel('Epoch')
        plt.ylabel('Error')
        plt.show()

    def predict(self, test_x, test_y):
        correct = 0
        class_counts = {i: {'TP': 0, 'FP': 0, 'FN': 0} for i in range(1, self.output_layer_size + 1)}

        for x, y in zip(test_x, test_y):
            output = self.evaluate(x)
            prediction = output.index(max(output)) + 1

            # check if the prediction is correct.
            if prediction == y:
                correct += 1
                class_counts[y]['TP'] += 1
            else:
                class_counts[y]['FN'] += 1
                class_counts[prediction]['FP'] += 1

        # calculate precision and recall for each class.
        for class_id, counts in class_counts.items():
            precision = counts['TP'] / (counts['TP'] + counts['FP']) if (counts['TP'] + counts['FP']) > 0 else 0
            recall = counts['TP'] / (counts['TP'] + counts['FN']) if (counts['TP'] + counts['FN']) > 0 else 0
            print(f"Class {class_id} Precision: {precision}")
            print(f"Class {class_id} Recall: {recall}")

        # overall accuracy
        accuracy = correct / len(test_x)
        print(f"Overall Accuracy: {accuracy}")

    def __str__(self):
        layers = ""
        for layer in self.layers:
            layers += str(layer) + "\n"
        return "Network: layers = " + layers
