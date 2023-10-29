from Cell import Cell


class Board:
    def __init__(self, size):
        self.cells = []
        self.size = size
        self.__init_cells()

    def __init_cells(self):
        for i in range(self.size):
            row = []
            for j in range(self.size):
                cell = Cell(i, j)
                row.append(cell)
            self.cells.append(row)

    def get_size(self):
        return self.size

    def get_cell(self, x, y):
        return self.cells[x][y]

    def get_row(self, x):
        return self.cells[x]

    def get_column(self, y):
        return [row[y] for row in self.cells]

    def get_square(self, x, y, size):
        square = []

        if (x + size) > len(self.cells) or (y + size) > len(self.cells):
            return None

        for i in range(x, x + size):
            for j in range(y, y + size):
                square.append(self.cells[i][j])
        return square

    def get_row_as_values(self, x):
        return [cell.get_value() for cell in self.cells[x]]

    def get_column_as_values(self, y):
        return [row[y].get_value() for row in self.cells]

    def get_square_as_values(self, x, y, size):
        square = []

        if (x + size) > len(self.cells) or (y + size) > len(self.cells):
            return None

        for i in range(x, x + size):
            for j in range(y, y + size):
                square.append(self.cells[i][j].get_value())
        return square

    def __str__(self):
        string = ""
        for row in self.cells:
            for cell in row:
                string += str(cell) + " "
            string += "\n"
        return string
