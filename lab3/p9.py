def obstructed_seats(stadium):
    rows = len(stadium)
    cols = len(stadium[0])

    obstructed = []

    for col in range(cols):
        for row in range(1, rows):
            if any(stadium[r][col] >= stadium[row][col] for r in range(row)):
                obstructed.append((row, col))

    return obstructed


stadium = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
print(obstructed_seats(stadium))
