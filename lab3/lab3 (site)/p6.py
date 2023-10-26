def unique_and_duplicates(lst):
    a = 0
    b = 0
    elements = set(lst)
    appeared = set()
    duplicates = set()
    for item in lst:
        if item in elements:
            appeared.add(item)
            a += 1
            elements.remove(item)
        elif item in appeared:
            b += 1
            a -= 1
            duplicates.add(item)
            appeared.remove(item)
    return (a, b)

print(
    unique_and_duplicates(
        [1, 2, 2, 2, 3, 3, 4]
    )
)

print(
    unique_and_duplicates(
        [1, 4, 2, 3, 4, 4, 5]
    )
)