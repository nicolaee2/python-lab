shortest_word = ""
longest_word = ""
first_word_with_second_letter_b = ""
last_word_with_last_letter_a = ""
unique_words = set()

shortest_word_length = float("inf")
longest_word_length = 0

try:
    f = open("file.txt", "r")
    for line in f:
        words = line.split()
        for word in words:
            if len(word) < shortest_word_length:
                shortest_word = word
                shortest_word_length = len(word)
            if len(word) > longest_word_length:
                longest_word = word
                longest_word_length = len(word)
            if word[1] == 'b' and first_word_with_second_letter_b == "":
                first_word_with_second_letter_b = word
            if word[-1] == 'a':
                last_word_with_last_letter_a = word
            unique_words.add(word)
    f.close()
except:
    print("Unable to read file.txt")

print("Shortest word: " + shortest_word)
print("Longest word: " + longest_word)
print("First word with second letter b: " + first_word_with_second_letter_b)
print("Last word with last letter a: " + last_word_with_last_letter_a)
print("Unique words: " + str(unique_words))

unique_words = sorted(unique_words, key=lambda word: (word[0], len(word)))
print("Unique words sorted: " + str(unique_words))

try:
    f = open("sol.txt", "w")
    # write as key: value
    f.write("shortest_word: " + shortest_word + "\n")
    f.write("longest_word: " + longest_word + "\n")
    f.write("first_word_with_second_letter_b: " + first_word_with_second_letter_b + "\n")
    f.write("last_word_with_last_letter_a: " + last_word_with_last_letter_a + "\n")
    f.write("unique_words: " + str(unique_words) + "\n")
    f.close()
except:
    print("Unable to write to sol.txt")

