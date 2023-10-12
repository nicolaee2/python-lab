# example {a, b, c}
# {1, 2, 3}
sequence = input("Enter sequence: ")
sequence = sequence[1:-1]
sequence = sequence.split(",")
sequence = list(map(lambda x: x.strip(), sequence))
print(sequence)

l2 = " ".join(hex(n)[2:] for n in range(ord(sequence[0]), ord(sequence[0]) + len(sequence)))
print(l2)
