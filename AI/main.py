# from tests import run_tests
from PuzzleStateUtil import *
from PuzzleSolvers import PuzzleSolvers

if __name__ == '__main__':
    # run_tests()
    puzzle1 = init([[8, 6, 7], [2, 5, 4], [0, 3, 1]])
    puzzle2 = init([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
    puzzle3 = init([[2, 7, 5], [0, 8, 4], [3, 1, 6]])
    # PuzzleSolvers.print_iddfs_result(PuzzleSolvers.iddfs(puzzle1))
    # PuzzleSolvers.print_iddfs_result(PuzzleSolvers.iddfs(puzzle2))
    # PuzzleSolvers.print_iddfs_result(PuzzleSolvers.iddfs(puzzle3))
    # print(PuzzleSolvers.a_star_search(puzzle1))
    # print(PuzzleSolvers.greedy_search_stack(puzzle3, chebyshev_distance))

    PuzzleSolvers.run_all_and_print([puzzle1, puzzle2, puzzle3])