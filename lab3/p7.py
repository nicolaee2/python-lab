def is_palindrome(num):
    return str(num) == str(num)[::-1]


def palindrome_statistics(numbers):
    count = 0
    greatest_palindrome = float('-inf')

    for num in numbers:
        if is_palindrome(num):
            count += 1
            if num > greatest_palindrome:
                greatest_palindrome = num

    if greatest_palindrome == float('-inf'):
        greatest_palindrome = None

    return count, greatest_palindrome

numbers = [1231, 232, 343, 454, 565]
print(palindrome_statistics(numbers))
