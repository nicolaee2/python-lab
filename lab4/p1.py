def set_results(a, b):
    a_set = set(a)
    b_set = set(b)
    return [
        a_set.intersection(b_set),
        a_set.union(b_set),
        a_set.difference(b_set),
        b_set.difference(a_set),
    ]


print(
    set_results(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 4, 6, 8, 10, 12, 14, 16, 18]
    )
)