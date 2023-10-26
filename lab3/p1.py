def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_num = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_num)
        return fib_sequence

n = 10
print(fibonacci(n))