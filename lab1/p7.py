
def main():
    str = input("Enter string: ")
    found = False
    start = -1
    sol = 0

    for index in range(len(str)):
        chr = str[index]
        if chr.isnumeric():
            found = True
            start = index
            break
    else:
        print("No number in string")
        return

    while index < len(str) and str[index].isnumeric():
        sol = sol * 10 + int(str[index])
        index += 1
    else:
        print(sol)


main()
