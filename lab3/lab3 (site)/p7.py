def operations_dict(*sets):
    dict = {}
    for first_set in sets:
        # to not repeat the same operations, all operators are symmetric
        is_right = False
        for second_set in sets:
            if first_set != second_set and is_right is True:
                dict[f"{first_set} | {second_set}"] = first_set.union(second_set)
                dict[f"{first_set} & {second_set}"] = first_set.intersection(second_set)
                dict[f"{first_set} - {second_set}"] = first_set.difference(second_set)
                dict[f"{second_set} - {first_set}"] = second_set.difference(first_set)
            elif first_set == second_set:
                is_right = True
    return dict


print(
    operations_dict(
        {1, 2},
        {2, 3},
        {2, 3, 4}
    )
)