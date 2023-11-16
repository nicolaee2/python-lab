from Util import Util
from Network import Network


dataset_x, dataset_y, num_attributes, num_classes = Util.read_dataset('seeds_dataset.txt')
train_x, train_y, test_x, test_y = Util.split_dataset(dataset_x, dataset_y, 0.8)

network = Network(num_attributes, [3, 5], num_classes)
network.evaluate_and_train(train_x, train_y)
