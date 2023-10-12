alphabet = "abcdef"
p = 3

def generate(prefix, length, permutations):
    if length == 0:
        permutations.append(prefix)
    else:
        for letter in alphabet:
            generate(prefix + letter, length - 1, permutations)


permutations = []
generate("", p, permutations)

for perm in permutations:
    print(perm)
