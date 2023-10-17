def zero_below_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j < i:
                matrix[i][j] = 0
    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(zero_below_diagonal(matrix))
