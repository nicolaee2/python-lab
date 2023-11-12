import random


class Network:

    def __init__(self, num_of_attributes, num_classes, hidden_layer_size):


    def parameter_initialization(self):
        """
        Initializes the parameters and weights for the neural network

        :param num_of_attributes: The number of attributes
        :param num_classes: The number of classes
        :param hidden_layer_size: The size of the hidden layer
        :return: A tuple containing the weights for the input to hidden layer and hidden to output layer
        """

        # initialize the weights for the input to hidden layer
        weights_input_to_hidden = [
            [random.uniform(-1, 1) for _ in range(hidden_layer_size)] for _ in range(num_of_attributes)
        ]

        # initialize the weights for the hidden to output layer
        weights_hidden_to_output = [
            [random.uniform(-1, 1) for _ in range(num_classes)] for _ in range(hidden_layer_size)
        ]

        epochs = 1000

        return weights_input_to_hidden, weights_hidden_to_output, epochs
