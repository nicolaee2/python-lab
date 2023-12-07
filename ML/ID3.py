import sys
import math


class Column:
    def __init__(self, name, values):
        self.name = name
        self.unique_values_count = len(set(values))
        self.values = values
        self.values_set = set(values)


class Node:
    def __init__(self, column=None):
        self.column = column
        self.children = {}
        self.label = None


def read_data(file_name, has_labels=True, mapping_dicts=None):
    try:
        with open(file_name, 'r') as file:
            all_data = [line.strip().split(' ') for line in file]

            # check for optional attribute names
            attribute_names = []
            if all_data[0][0].startswith('%'):
                attribute_names = all_data[0][1:]
                all_data = all_data[1:]

            if mapping_dicts is None:
                mapping_dicts = [{} for _ in range(len(all_data[0]))]

            # convert string labels to numbers
            numerical_data = []
            for line in all_data:
                numerical_line = []
                for i, item in enumerate(line):
                    try:
                        numerical_line.append(int(item))
                    except ValueError:
                        # if conversion fails, check if item exists in the mapping, if not, add it
                        if item not in mapping_dicts[i]:
                            mapping_dicts[i][item] = len(mapping_dicts[i])
                        numerical_line.append(mapping_dicts[i][item])
                numerical_data.append(numerical_line)

            transposed_data = list(zip(*numerical_data))

            # use custom attribute names if available, else use default names
            if attribute_names:
                local_columns = [Column(name=name, values=col_data) for name, col_data in
                                 zip(attribute_names, transposed_data[:-1 if has_labels else None])]
            else:
                local_columns = [Column(name=f"A{i + 1}", values=col_data) for i, col_data in
                                 enumerate(transposed_data[:-1 if has_labels else None])]

            # if file.txt has labels, return them as a column. Otherwise, return instances.
            if has_labels:
                local_label_column = Column(name="Label", values=transposed_data[-1])
                inverse_label_mapping = {v: k for k, v in mapping_dicts[-1].items()}
                return local_columns, local_label_column, mapping_dicts, inverse_label_mapping
            else:
                instances = []
                for data in numerical_data:
                    if attribute_names:
                        instance = {name: val for name, val in zip(attribute_names, data)}
                    else:
                        instance = {f"A{i + 1}": val for i, val in enumerate(data)}
                    instances.append(instance)
                return local_columns, instances, mapping_dicts

    except FileNotFoundError:
        print(f"No such file: '{file_name}'")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)


def get_distribution(column, label_column):
    distribution = {value: {label: 0 for label in label_column.values_set} for value in column.values_set}
    attribute_distribution = {label: 0 for label in label_column.values_set}

    for col_val, label_val in zip(column.values, label_column.values):
        distribution[col_val][label_val] += 1
        attribute_distribution[label_val] += 1

    return distribution, attribute_distribution


def get_entropy(distribution):
    total = sum(distribution.values())
    return -sum((val / total) * math.log2(val / total) for val in distribution.values() if val != 0)


def get_conditional_entropy(distribution, attribute_distribution):
    total = sum(attribute_distribution.values())
    return sum((sum(dist.values()) / total) * get_entropy(dist) for dist in distribution.values())


def filter_data(columns, label_column, best_column, unique_value):
    filtered_values = [
        [col_val for col_val, best_col_val in zip(col.values, best_column.values) if best_col_val == unique_value]
        for col in columns
    ]

    filtered_label_values = [
        label_val for label_val, best_col_val in zip(label_column.values, best_column.values)
        if best_col_val == unique_value
    ]

    filtered_columns = [
        Column(name=col.name, values=col_values) for col, col_values in zip(columns, filtered_values)
        if col.name != best_column.name
    ]

    filtered_label_column = Column(name=label_column.name, values=filtered_label_values)
    return filtered_columns, filtered_label_column


def train(columns, label_column, depth=0):

    # check for stopping criteria: entropy is 0
    if len(label_column.values_set) == 1:
        leaf_node = Node()
        leaf_node.label = label_column.values_set.pop()
        return leaf_node

    # find the best column to split on
    best_column = None
    min_entropy = float("+inf")

    for column in columns:
        distribution, attribute_distribution = get_distribution(column, label_column)
        print(distribution, attribute_distribution)
        conditional_entropy = get_conditional_entropy(distribution, attribute_distribution)
        print(f"Depth: {depth}, Column: {column.name}, Conditional Entropy: {conditional_entropy}")

        if conditional_entropy < min_entropy:
            min_entropy = conditional_entropy
            best_column = column

    print(f"Depth: {depth}, Best Column: {best_column.name}, Min Conditional Entropy: {min_entropy}")

    # if no improvement is possible, return a leaf node with the most common label
    if best_column is None:
        leaf_node = Node()
        leaf_node.label = max(label_column.values_set, key=label_column.values.count)
        return leaf_node

    # create a new internal node
    new_node = Node(column=best_column)

    # recursively generate children nodes
    for unique_value in best_column.values_set:
        # filter columns and labels where best column equals unique value
        filtered_columns_values, filtered_label_values = filter_data(columns, label_column, best_column, unique_value)

        # create a new node for each value of the best column and recurse
        new_node.children[unique_value] = train(filtered_columns_values, filtered_label_values, depth + 1)

    return new_node


def print_tree(node, indent="", subtree=True):
    if node.label is not None:
        print(indent + "[Leaf node] Label:", node.label)
        return

    print(indent + f"[Decision node] Best Column: {node.column.name}")
    for value, child in node.children.items():
        print(indent + f"  If {node.column.name} == {value}:")
        print_tree(child, indent + "    ")


def predict(instance, node):
    if node.label is not None:
        return node.label

    column_value = instance.get(node.column.name)
    child_node = node.children.get(column_value)

    if child_node is not None:
        return predict(instance, child_node)
    else:
        return None

def test_decision_tree(test_instances, root_node):
    predictions = []
    for instance in test_instances:
        predictions.append(predict(instance, root_node))
    return predictions


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ID3.test.py <training_data_file> <testing_data_file>")
    else:
        train_file_name = sys.argv[1]
        test_file_name = sys.argv[2]

        columns, label_column, mapping_dicts, inverse_mapping_dicts = read_data(train_file_name)
        _, test_instances, _ = read_data(test_file_name, has_labels=False, mapping_dicts=mapping_dicts)

        # train the decision tree
        root_node = train(columns, label_column)

        # print the decision tree
        print_tree(root_node)

        # test the decision tree on test data
        predictions = test_decision_tree(test_instances, root_node)

        # print the predictions
        print("Predictions:")
        if len(inverse_mapping_dicts) > 1:
            predictions = [inverse_mapping_dicts[prediction] for prediction in predictions]
        print(predictions)



