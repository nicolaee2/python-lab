import random


class Util:

    @staticmethod
    def get_number_of_attributes(filename):
        """
        Gets the number of attributes from a file

        :param filename: The file to read from
        :return: The number of attributes
        """

        # read the data from the file
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
        Reads a dataset from a file

        :param filename: File to read from
        :return: A list of tuples (<attributes values>, class label)
        """
        num_attributes = Util.get_number_of_attributes(filename)

        # read the data from the file
        with open(filename, 'r') as file:
            data = file.readlines()

        # initialize the dataset
        train_dataset = []

        # for each line in the file
        for line in data:

            # delete double tabs
            line = line.replace('\t\t', '\t')

            # split the line in multiple parts, one for each attribute
            parts = line.strip().split('\t')

            # check if the line is valid
            if len(parts) == num_attributes + 1:

                # extract the attributes and class label
                attributes = [float(part) for part in parts[:-1]]
                class_label = int(parts[-1])

                # append the tuple to the dataset
                train_dataset.append((attributes, class_label))
            else:
                print('Invalid line: ', line)

        return train_dataset

    @staticmethod
    def split_dataset(dataset, training_split_ratio):
        """
        Splits a dataset into training and testing sets

        :param dataset: The dataset to split
        :param training_split_ratio: The ratio of the training set
        :return: A tuple containing the training and testing sets
        """
        dataset_length = len(dataset)

        # shuffle the dataset
        random.shuffle(dataset)

        # split the dataset into classes
        dataset_class_1 = [data for data in dataset if data[1] == 1]
        dataset_class_2 = [data for data in dataset if data[1] == 2]
        dataset_class_3 = [data for data in dataset if data[1] == 3]

        # compute split index
        split_index = int((1 - training_split_ratio) * dataset_length / 3)

        # split the dataset into training set
        testing_set = dataset_class_1[:split_index]
        testing_set += dataset_class_2[:split_index]
        testing_set += dataset_class_3[:split_index]

        # split the dataset into testing set
        training_set = dataset_class_1[split_index:]
        training_set += dataset_class_2[split_index:]
        training_set += dataset_class_3[split_index:]

        # shuffle the training and testing sets
        random.shuffle(testing_set)
        random.shuffle(training_set)

        return training_set, testing_set
