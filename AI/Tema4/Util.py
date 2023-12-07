import random
import numpy as np
import math


class Util:

    @staticmethod
    def get_number_of_attributes(filename):
        """
        Gets the number of attributes from a file.txt

        :param filename: The file.txt to read from
        :return: The number of attributes
        """

        # read the data from the file.txt
        with open(filename, 'r') as file:
            line = file.readline()

        # delete double tabs
        line = line.replace('\t\t', '\t')

        # split the line in multiple parts, one for each attribute
        parts = line.strip().split('\t')

        return len(parts) - 1

    @staticmethod
    def read_dataset(filename):
        """
        Reads a dataset from a file.txt

        :param filename: File to read from
        :return: dataset_x, dataset_y, num_attributes, num_classes
        """
        num_attributes = Util.get_number_of_attributes(filename)

        # read the data from the file.txt
        with open(filename, 'r') as file:
            data = file.readlines()

        # initialize the dataset
        dataset_x = []
        dataset_y = []

        # for each line in the file.txt
        for line in data:

            # delete double tabs
            line = line.replace('\t\t', '\t')

            # split the line in multiple parts, one for each attribute
            parts = line.strip().split('\t')

            # check if the line is valid
            if len(parts) == num_attributes + 1:

                # add the attributes and class label to the dataset
                dataset_x.append([float(part) for part in parts[:-1]])
                dataset_y.append(int(parts[-1]))
            else:
                print('Invalid line: ', line)

        return dataset_x, dataset_y, num_attributes, len(set(dataset_y))

    @staticmethod
    def split_dataset(dataset_x, dataset_y, training_split_ratio):
        """
        Splits a dataset into training and testing sets

        :param dataset_x: The dataset containing the attributes
        :param dataset_y: The dataset containing the class labels
        :param training_split_ratio: The ratio of the training set
        :return: A tuple containing the training and testing sets
        """
        dataset = list(zip(dataset_x, dataset_y))
        dataset_length = len(dataset)

        # shuffle the dataset
        random.shuffle(dataset)

        # compute separation index
        separation_index = int(dataset_length * training_split_ratio)

        # split the dataset
        training_set = dataset[:separation_index]
        testing_set = dataset[separation_index:]

        train_x, train_y = zip(*training_set)
        test_x, test_y = zip(*testing_set)

        return train_x, train_y, test_x, test_y

    @staticmethod
    def activation_function_sigmoid(vector):
        """
        Applies the activation function to the input

        :param x: The input
        :return: The output of the activation function
        """

        return [
            1 / (1 + math.exp(-x)) for x in vector
        ]

    @staticmethod
    def activation_function_hyperbolic_tangent(vector):
        return [
            (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)) for x in vector
        ]

    @staticmethod
    def activation_function_derivative(vector):
        """
        Applies the derivative of the activation function to the input

        :param vector: The input
        :return: The output of the derivative of the activation function
        """
        output = Util.activation_function_sigmoid(vector)
        return [
            o * (1 - o) for o in output
        ]

    @staticmethod
    def error_function_mse(predictions, targets):
        return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)
