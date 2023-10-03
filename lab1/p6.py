def main():
    number = int(input("Enter a number: "))

    temp_number = number
    reverse_number = 0

    while number:
        print(number)
        reverse_number = reverse_number * 10 + number % 10
        number //= 10

    if temp_number == reverse_number:
        print(f"{temp_number} is palindrome")
    else:
        print(f"{temp_number} is not palindrome")


main()
