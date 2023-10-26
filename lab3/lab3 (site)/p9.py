def my_function(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count


print(my_function(
    1, 2, 3, 4, x = 1, y = 2, z = 3, w = 5
))