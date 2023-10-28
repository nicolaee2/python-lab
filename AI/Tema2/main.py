from Board import Board


def special_sudoku_board_initialization(board_state, board, special_cells):
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_domain = [2, 4, 6, 8]

    for i in range(len(special_cells)):
        x, y = special_cells[i]
        board_state.get_cell(x, y).set_domain(even_domain)

    for i in range(board_state.get_size()):
        for j in range(board_state.get_size()):
            if board[i][j] != 0:
                board_state.get_cell(i, j).set_domain([board[i][j]])
            else:
                board_state.get_cell(i, j).set_domain(domain)

    return board_state


def find_next_cell(board_state):
    for i in range(board_state.get_size()):
        for j in range(board_state.get_size()):
            if not board_state.get_cell(i, j).get_value() != 0:
                return i, j
    return None


def is_valid_move(board_state, row, col, num):
    if board_state.get_cell(row, col).get_value() != 0:
        return False
    if num in board_state.get_row(row):
        return False
    if num in board_state.get_column(col):
        return False
    if num in board_state.get_square(row - row % 3, col - col % 3, 3):
        return False
    return True


def find_solution(board_state):
    empty = find_next_cell(board_state)
    if not empty:
        return board_state, True

    row, col = empty

    for num in board_state.get_cell(row, col).get_domain():
        if is_valid_move(board_state, row, col, num):
            board_state.get_cell(row, col).set_value(num)

            next_state, solution_found = find_solution(board_state)
            if solution_found:
                return next_state, True

            board_state.get_cell(row, col).set_value(0)

    return board_state, False


def main():
    # board = [
    #     [8, 4, 0, 0, 5, 0, 0, 0, 0],
    #     [3, 0, 0, 6, 0, 8, 0, 4, 0],
    #     [0, 0, 0, 4, 0, 9, 0, 0, 0],
    #     [0, 2, 3, 0, 0, 0, 9, 8, 0],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 4],
    #     [0, 9, 8, 0, 0, 0, 1, 6, 0],
    #     [0, 0, 0, 5, 0, 3, 0, 0, 0],
    #     [0, 3, 0, 1, 0, 6, 0, 0, 7],
    #     [0, 0, 0, 0, 2, 0, 0, 1, 3]
    # ]
    board = [
        [8, 4, 9, 2, 0, 7, 6, 3, 1],
        [3, 5, 0, 0, 1, 8, 2, 4, 9],
        [6, 1, 2, 4, 3, 9, 7, 5, 8],
        [4, 2, 3, 7, 6, 1, 9, 0, 0],
        [1, 6, 5, 8, 9, 2, 3, 0, 0],
        [0, 0, 0, 3, 4, 5, 0, 6, 2],
        [2, 8, 1, 5, 7, 3, 4, 9, 6],
        [9, 3, 4, 1, 8, 6, 5, 2, 7],
        [5, 7, 6, 9, 2, 4, 8, 1, 3]
    ]

    special_cells = [(0, 6), (2, 2), (2, 8), (3, 4), (4, 3), (4, 5), (5, 4), (6, 0), (6, 6), (8, 2)]
    board_state = Board(len(board))
    board = special_sudoku_board_initialization(board_state, board, special_cells)

    solution_board, solution_found = find_solution(board)

    if solution_found:
        print(solution_board)
    else:
        print("No solution found!")

main()