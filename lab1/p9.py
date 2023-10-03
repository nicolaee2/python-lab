def main():
    appearance = []

    for i in range(26):
        appearance.append(0)

    maximum = 0
    solution = ''
    str = input("Enter a string: ")

    for letter in str:
        if not letter.isalpha():
            continue
        letter_lower = letter.lower()
        index = ord(letter_lower) - ord('a')
        appearance[index] += 1
        if appearance[index] > maximum:
            maximum = appearance[index]
            solution = letter_lower
    print(f"The character {solution} appears most times: {maximum}")


main()
