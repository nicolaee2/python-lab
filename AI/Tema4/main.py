import math

from Util import Util
from Network import Network



def activation_function(x):
    """
    Applies the activation function to the input

    :param x: The input
    :return: The output of the activation function
    """

    return 1 / (1 + math.exp(-x))


def activation_function_derivative(x):
    """
    Applies the derivative of the activation function to the input

    :param x: The input
    :return: The output of the derivative of the activation function
    """

    return activation_function(x) * (1 - activation_function(x))


def mean_squared_error(predictions, targets):
    """
    Computes the mean squared error

    :param predictions: The predictions
    :param targets: The targets
    :return: The mean squared error
    """

    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)


dataset_x, dataset_y, num_attributes, num_classes = Util.read_dataset('seeds_dataset.txt')
train_x, train_y, test_x, test_y = Util.split_dataset(dataset_x, dataset_y, 0.8)

network = Network(num_attributes, [3, 5], num_classes)
network.evaluate_and_train(train_x, train_y, 0.1, 30)

# weights_input_to_hidden, weights_hidden_to_output, epochs = parameter_initialization(num_attributes, 3, 5)