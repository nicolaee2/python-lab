def word_char_occurrences(word):
    dict = {}
    for letter in word:
        if dict.get(letter) is None:
            dict[letter] = 1
        else:
            dict[letter] += 1
    return dict


print(word_char_occurrences("cecilia are cipici"))
print(word_char_occurrences("Ana has apples"))