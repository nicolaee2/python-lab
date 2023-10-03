def main():
    matrix = []
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))
    for i in range(n):
        row = []
        for j in range(m):
            row.append(input(f"Enter character for row {i} column {j}: "))
        matrix.append(row)

    result = []
    while matrix:
        result += matrix.pop(0)

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        if matrix:
            result += matrix.pop()[::-1]

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))

    print(''.join(result))


main()