from SpecialSudokuSolver import SpecialSudokuSolver


def main():
    board = [
        [8, 4, 0, 0, 5, 0, 0, 0, 0],
        [3, 0, 0, 6, 0, 8, 0, 4, 0],
        [0, 0, 0, 4, 0, 9, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 9, 8, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 9, 8, 0, 0, 0, 1, 6, 0],
        [0, 0, 0, 5, 0, 3, 0, 0, 0],
        [0, 3, 0, 1, 0, 6, 0, 0, 7],
        [0, 0, 0, 0, 2, 0, 0, 1, 3]
    ]

    special_cells = [(0, 6), (2, 2), (2, 8), (3, 4), (4, 3), (4, 5), (5, 4), (6, 0), (6, 6), (8, 2)]

    solver = SpecialSudokuSolver(board, special_cells)
    solution_board, solution_found = solver.find_solution()

    if solution_found:
        print(solution_board)
    else:
        print("No solution found!")


main()
