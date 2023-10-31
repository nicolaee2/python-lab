class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(0)
            self.data.append(row)

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        raise IndexError("Row or column index out of bounds.")

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value
        else:
            raise IndexError("Row or column index out of bounds.")

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must equal number of rows in second matrix.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.get(i, k) * other.get(k, j)
                result.set(i, j, total)
        return result

    def apply_transformation(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, func(self.get(i, j)))

    def __str__(self):
        string = ""
        for row in self.data:
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        return string


m = Matrix(2, 2)
m.set(0, 0, 1)
m.set(0, 1, 2)
m.set(1, 0, 3)
m.set(1, 1, 4)
print(m)

m_transposed = m.transpose()
print(m_transposed)

m.apply_transformation(lambda x: x + 1)
print(m.get(0, 0))
