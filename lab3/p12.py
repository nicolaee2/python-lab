def group_by_rhyme(words):
    rhyme_dict = {}

    for word in words:
        key = word[-2:]

        if key not in rhyme_dict:
            rhyme_dict[key] = []

        rhyme_dict[key].append(word)

    return list(rhyme_dict.values())


words = ['ana', 'banana', 'carte', 'arme', 'parte']
print(group_by_rhyme(words))
