word_occurrences = {}
import json


def is_valid(word):
    for letter in word:
        if not letter.isalpha():
            return False

    if word.islower() or (word[0].isupper() and word[1:].islower()):
        return True

    return False

try:
    f = open("file.txt", "r")
    for line in f:
        words = line.split()
        for word in words:
            lower_word = word.lower()
            if is_valid(word):
                if lower_word in word_occurrences:
                    word_occurrences[word] += 1
                else:
                    word_occurrences[word] = 1
    f.close()
except:
    print("Unable to read file.txt")

most_occurrences = sorted(word_occurrences.items(), key=lambda item: item[1], reverse=True)
most_occurrences = [word for word, occurrences in most_occurrences if occurrences == most_occurrences[0][1]]
least_occurrences = sorted(word_occurrences.items(), key=lambda item: item[1])
least_occurrences = [word for word, occurrences in least_occurrences if occurrences == least_occurrences[0][1]]

# write in a json file
try:
    f = open("sol.json", "w")
    f.write(json.dumps({
        "most_occurrences": most_occurrences,
        "least_occurrences": least_occurrences
    }))
    f.close()
except:
    print("Unable to write to sol.json")