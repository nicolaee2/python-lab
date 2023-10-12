#{0,1,2,3,4}
# sanitize input
sequence = input("Enter sequence: ")
sequence = sequence[1:-1]
sequence = sequence.split(",")
sequence = list(map(lambda x: int(x), sequence))

# loop through input and create binaries
sol = ""
cnt_0 = 0
cnt_1 = 0
binaries = []
for index, value in enumerate(sequence):
    binary = "{0:b}".format(value)
    if len(binary) < 8:
        toAdd = "0" * (8 - len(binary))
        sol += toAdd+binary
        binaries.append(toAdd+binary)
    elif len(binary) == 8:
        sol += binary
        binaries.append(binary)
    else:
        sol += binary[:8]
        binaries.append(binary[:8])
    sol += " "
sol = sol.rstrip()

for index, value in enumerate(binaries):
    for j in value:
        if j == "0":
            cnt_0 += 1
        else:
            cnt_1 += 1


print(f"'{sol}', {cnt_0}, {cnt_1}")

