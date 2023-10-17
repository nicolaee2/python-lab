def compare_dicts(d1, d2):
    if set(d1.keys()) != set(d2.keys()):
        return False

    for key in d1:
        if isinstance(d1[key], dict) and isinstance(d2[key], dict):
            if not compare_dicts(d1[key], d2[key]):
                return False
        elif isinstance(d1[key], list) and isinstance(d2[key], list):
            if len(d1[key]) != len(d2[key]):
                return False
            for item1, item2 in zip(d1[key], d2[key]):
                if isinstance(item1, (dict, list, set)) or isinstance(item2, (dict, list, set)):
                    if not compare_dicts({"item": item1}, {"item": item2}):
                        return False
                elif item1 != item2:
                    return False
        elif isinstance(d1[key], set) and isinstance(d2[key], set):
            if d1[key] != d2[key]:
                return False
        else:
            if d1[key] != d2[key]:
                return False

    return True

print(
    compare_dicts(
        {
            "a": 1,
            "b": 2,
            "c": [1, 2, 3],
            "d": set([1, 2, 3]),
            "e": {
                "a": 1,
                "b": 2,
            },
        },
        {
            "a": 1,
            "b": 2,
            "c": [1, 2, 3],
            "d": set([1, 2, 3]),
            "e": {
                "a": 1,
                "b": 2,
            },
        }
))

print(
    compare_dicts(
        {
            "a": 1,
            "b": 2,
            "c": [1, 2, 3],
            "d": set([1, 2, 3]),
            "e": {
                "a": 2,
                "b": 2,
            },
        },
        {
            "a": 1,
            "b": 2,
            "c": [1, 2, 3],
            "d": set([1, 2, 3]),
            "e": {
                "a": 1,
                "b": 2,
            }
        }
    ))