def items_appear_x_times(x, *lists):
    all_items = [item for sublist in lists for item in sublist]
    item_count = {}

    for item in all_items:
        item_count[item] = item_count.get(item, 0) + 1

    return [item for item, count in item_count.items() if count == x]


list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6, "test"]
list4 = [4, 1, "test"]
print(items_appear_x_times(2, list1, list2, list3, list4))