def gcd(a, b):
    if b == 0:
        return a
    while b:
        r = a % b
        a = b
        b = r
    return a


def main():
    n = int(input("Enter n: "))

    a = int(input("Enter n1: "))
    sol = a
    for i in range(2, n+1):
        b = int(input(f"Enter n{i}: "))
        sol = gcd(a, b)
        a = b

    print(f"gcd of the {n} numbers is: {sol}")


main()
