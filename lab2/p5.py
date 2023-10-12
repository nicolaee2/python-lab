matrix = [
    [1, 1, 1, 1, 10],
    [1, 1, 0, 0, 5],
    [0, 0, 1, 1, 5],
    [1, 0, 1, 0, 5]
]

min_val, max_val = 0, 50

sol = []

for x1 in range(min_val, max_val + 1):
    for x2 in range(min_val, max_val + 1):
        for x3 in range(min_val, max_val + 1):
            for x4 in range(min_val, max_val + 1):
                if all(round(sum(r[j] * x for j, x in enumerate([x1, x2, x3, x4]))) == r[-1] for r in matrix):
                    sol.append((x1, x2, x3, x4))

if sol:
    for solution in sol:
        print("A solution is: ", solution)
else:
    print("No solution found.")
