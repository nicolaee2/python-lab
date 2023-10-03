def main():
    n = int(input("Enter a number: "))
    sol = 0
    while n > 0:
        if n & 1 == 1:
            sol += 1
        n >>= 1
    print(sol)


main()
