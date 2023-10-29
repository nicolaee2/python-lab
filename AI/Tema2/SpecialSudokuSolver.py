from Board import Board
import copy


class SpecialSudokuSolver:
    def __init__(self, board, special_cells):
        self.__board_state = Board(len(board))
        self.__init_board(board, special_cells)

    def __init_board(self, board, special_cells):
        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        even_domain = [2, 4, 6, 8]

        for i in range(self.__board_state.get_size()):
            for j in range(self.__board_state.get_size()):
                if board[i][j] != 0:
                    self.__board_state.get_cell(i, j).set_domain(copy.deepcopy([board[i][j]]))
                else:
                    if (i, j) not in special_cells:
                        self.__board_state.get_cell(i, j).set_domain(copy.deepcopy(domain))
                    else:
                        self.__board_state.get_cell(i, j).set_domain(copy.deepcopy(even_domain))

        for i in range(self.__board_state.get_size()):
            for j in range(self.__board_state.get_size()):
                if board[i][j] != 0:
                    self.__filter_domains(i, j, board[i][j])
                    pass

    def __filter_domains(self, row, col, num):
        indices_of_domains_modified = []

        for cell in self.__board_state.get_row(row):
            if cell.get_y() != col and num in cell.get_domain():
                cell.get_domain().remove(num)
                indices_of_domains_modified.append((cell.get_x(), cell.get_y()))

        for cell in self.__board_state.get_column(col):
            if cell.get_x() != row and num in cell.get_domain():
                cell.get_domain().remove(num)
                indices_of_domains_modified.append((cell.get_x(), cell.get_y()))

        for cell in self.__board_state.get_square(row - row % 3, col - col % 3, 3):
            if cell.get_x() != row and cell.get_y() != col and num in cell.get_domain():
                cell.get_domain().remove(num)
                indices_of_domains_modified.append((cell.get_x(), cell.get_y()))

        return indices_of_domains_modified

    def __restore_domains(self, indices_of_domains_modified, num):
        for x, y in indices_of_domains_modified:
            self.__board_state.get_cell(x, y).get_domain().append(num)

    def __find_next_cell(self):
        mrv_cells = []
        for i in range(self.__board_state.get_size()):
            for j in range(self.__board_state.get_size()):
                if self.__board_state.get_cell(i, j).get_value() == 0:
                    mrv_cells.append((i, j, len(self.__board_state.get_cell(i, j).get_domain())))

        if len(mrv_cells) == 0:
            return None

        mrv_cells.sort(key=lambda x: x[2])
        return mrv_cells[0][0], mrv_cells[0][1]

    def __is_valid_move(self, row, col, num):
        if self.__board_state.get_cell(row, col).get_value() != 0:
            return False
        if num in self.__board_state.get_row_as_values(row):
            return False
        if num in self.__board_state.get_column_as_values(col):
            return False
        if num in self.__board_state.get_square_as_values(row - row % 3, col - col % 3, 3):
            return False

        return True

    def find_solution(self):
        empty_cell = self.__find_next_cell()
        if not empty_cell:
            return self.__board_state, True

        row, col = empty_cell

        for num in self.__board_state.get_cell(row, col).get_domain():
            if self.__is_valid_move(row, col, num):
                self.__board_state.get_cell(row, col).set_value(num)

                # filter domains in row, column and square
                indices_of_domains_modified = self.__filter_domains(row, col, num)

                next_state, solution_found = self.find_solution()
                if solution_found:
                    return next_state, True

                self.__board_state.get_cell(row, col).set_value(0)

                # restore domains in row, column and square
                self.__restore_domains(indices_of_domains_modified, num)

        return self.__board_state, False
