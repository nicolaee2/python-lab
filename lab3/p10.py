def tuple_lists(*args):
    max_length = max(len(lst) for lst in args)
    padded_lists = [lst + [None] * (max_length - len(lst)) for lst in args]
    return [tuple(items) for items in zip(*padded_lists)]


lists = ([1, 2, 3], [5, 6], ["a"])
print(tuple_lists(*lists))
