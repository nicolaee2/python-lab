from PuzzleStateUtil import *
from PuzzleSolvers import PuzzleSolvers


if __name__ == '__main__':
    # run_tests()
    # puzzle1 = init([[8, 6, 7], [2, 5, 4], [0, 3, 1]])
    puzzle2 = init([[2, 5, 3], [1, 0, 6], [4, 7, 8]])
    puzzle3 = init([[2, 7, 5], [0, 8, 4], [3, 1, 6]])
    # print(PuzzleSolvers.iddfs(puzzle1))
    print(PuzzleSolvers.iddfs(puzzle2))
    print(PuzzleSolvers.iddfs(puzzle3))