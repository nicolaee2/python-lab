def main():
    str = input("Enter a string: ")
    substr = input("Enter a substring: ")

    count = 0
    index = 0
    while True:
        index = str.find(substr, index)
        if index == -1:
            break

        count += 1
        index += len(substr)
    print(count)


main()
