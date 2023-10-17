def loop(dict):
    key = "start"
    visited_keys = [key]
    sol = []

    while dict[key] not in visited_keys:
        key = dict[key]
        sol.append(key)
        visited_keys.append(key)

    return sol

print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
print(
    loop(
        {
            'start': 'a',
            'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'start'
        }
    )
)