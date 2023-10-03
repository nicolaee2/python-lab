def main():
    vowels = "aeiouAEIOU"
    input_string = input("Enter a string: ")

    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    print(vowel_count)

main()