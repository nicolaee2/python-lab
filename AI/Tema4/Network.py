from Layer import Layer
from Util import Util
import matplotlib.pyplot as plt


class Network:

    def __init__(self, input_layer_size, hidden_layer_sizes, output_layer_size, learning_rate=0.05, epochs=200):
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
        # initialize list to keep track of training errors
        train_errors = []

        # loop over each epoch
        for epoch in range(self.epochs):
            # sum total error for each epoch
            total_error = 0
            # iterate over each training example
            for x, y in zip(train_x, train_y):

                # perform forward pass to get network output
                self.evaluate(x)

                # create target output vector with correct class set to 1
                target = [0 for _ in range(self.output_layer_size)]
                target[y - 1] = 1
                # calculate error between network output and target
                output_errors = [target[i] - self.layers[-1].output[i] for i in range(self.output_layer_size)]

                # compute change signals based on derivative of activation function
                output_deltas = [output_errors[i] * Util.activation_function_derivative(self.layers[-1].output)[i] for i
                                 in range(self.output_layer_size)]

                # backpropagate the error through the network
                for i in reversed(range(len(self.layers))):
                    layer = self.layers[i]
                    # use inputs from previous layer or input data if first layer
                    inputs = x if i == 0 else self.layers[i - 1].output
                    new_deltas = [0.0 for _ in range(len(inputs))]
                    for j, neuron in enumerate(layer.neurons):
                        # update weights based on deltas and learning rate
                        for k in range(len(neuron.weights)):
                            neuron.weights[k] += self.learning_rate * output_deltas[j] * inputs[k]
                            # calculate new deltas for next layer
                            if i != 0:
                                new_deltas[k] += output_deltas[j] * neuron.weights[k]
                    # prepare deltas for next iteration
                    if i != 0:
                        output_deltas = [
                            new_deltas[k] * Util.activation_function_derivative(self.layers[i - 1].output)[k] for k in
                            range(len(new_deltas))]

                # accumulate the error from each example
                total_error += Util.error_function_mse(self.layers[-1].output, target)

            # add average error of epoch to list
            train_errors.append(total_error / len(train_x))

            # output the error at the end of each epoch
            print(f"Epoch {epoch + 1}/{self.epochs}, Error: {total_error / len(train_x)}")

        # plot the error as a function of the epochs for the training set
        plt.plot(train_errors)
        plt.xlabel('Epoch')
        plt.ylabel('Error')
        plt.title('Error as a function of the epochs for the training set')
        plt.show()

    def predict(self, test_x, test_y):
        true_positives = 0
        true_negatives = 0
        false_positives = 0
        false_negatives = 0

        correct_classified = {'x': [], 'y': []}
        incorrect_classified = {'x': [], 'y': []}

        for x, y in zip(test_x, test_y):
            outputs = self.evaluate(x)
            prediction = outputs.index(max(outputs)) + 1

            if prediction == y:
                correct_classified['x'].append(x[0])
                correct_classified['y'].append(x[1])
            else:
                incorrect_classified['x'].append(x[0])
                incorrect_classified['y'].append(x[1])

            if prediction == y:
                if prediction == 1:
                    true_positives += 1
                else:
                    true_negatives += 1
            else:
                if prediction == 1:
                    false_positives += 1
                else:
                    false_negatives += 1

        accuracy = (true_positives + true_negatives) / len(test_x) if len(test_x) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

        print(f"Accuracy: {accuracy}")
        print(f"Recall: {recall}")

        plt.scatter(correct_classified['x'], correct_classified['y'], color='green', label='Correct')
        plt.scatter(incorrect_classified['x'], incorrect_classified['y'], color='red', label='Incorrect')
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.title('Classification on Test Set')
        plt.legend()
        plt.show()

    def __str__(self):
        layers = ""
        for layer in self.layers:
            layers += str(layer) + "\n"
        return "Network: layers = " + layers