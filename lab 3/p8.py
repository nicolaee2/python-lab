def filter_strings(x=1, string_list=[], flag=True):
    result = []

    for s in string_list:
        if flag:
            filtered_chars = [char for char in s if ord(char) % x == 0]
        else:
            filtered_chars = [char for char in s if ord(char) % x != 0]

        result.append(filtered_chars)

    return result


x = 2
strings = ["test", "hello", "lab002"]
flag = False
print(filter_strings(x, strings, flag))
