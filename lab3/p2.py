def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_in_list(lst):
    return [num for num in lst if is_prime(num)]


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(primes_in_list(numbers))
