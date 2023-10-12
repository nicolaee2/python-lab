# brute force the solution
n = float(input("Enter a number: "))
r = int(input("Enter a root: "))
d = int(input("Enter number of digits: "))


def find_digit(current, n, r, power):
    candidate = 0

    if power == 1:
        stop = int(n / 2)
    else:
        stop = 10

    for digit in range(stop):
        number = current + digit / power
        if pow(number, r) <= n:
            candidate = digit
    return candidate


power = 1
current = 0
for i in range(d):
    digit = find_digit(current, n, r, power)
    print(current, digit, power)
    current = current + digit / power
    power *= 10
print(current)