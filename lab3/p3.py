def list_operations(a, b):
    a = set(a)
    b = set(b)

    intersection = a.intersection(b)
    union = a.union(b)
    a_minus_b = a.difference(b)
    b_minus_a = b.difference(a)

    return intersection, union, a_minus_b, b_minus_a


# Example:
a = [1, 2, 3]
b = [3, 4, 5]
intersection, union, a_minus_b, b_minus_a = list_operations(a, b)
print("Intersection:", intersection)
print("Union:", union)
print("a - b:", a_minus_b)
print("b - a:", b_minus_a)
