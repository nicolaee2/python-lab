from PuzzleStateUtil import *


def run_tests():
    # Test 1: Check solvable instances
    print(is_solvable([1, 2, 3, 4, 5, 6, 7, 8, 0]) is True)
    print(is_solvable([8, 6, 7, 2, 5, 4, 0, 3, 1]) is True)
    print(is_solvable([2, 5, 3, 1, 0, 6, 4, 7, 8]) is True)
    print(is_solvable([2, 7, 5, 0, 8, 4, 3, 1, 6]) is True)

    # Test 2: Check unsolvable instances
    print(is_solvable([1, 2, 3, 4, 5, 6, 8, 7, 0]) is False)

    # Test 3: Check matrix initialization
    initial_state = init([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    print(initial_state == [1, 2, 3, 4, 5, 6, 7, 8, 0])

    # Test 4: Ensure only 3x3 matrices are accepted
    try:
        init([[1, 2], [3, 4], [5, 6], [7, 8, 0]])
    except ValueError as e:
        print(str(e) == "Matrix must have 3 rows")

    try:
        init([[1, 2, 3], [4, 5, 6, 7], [8, 0]])
    except ValueError as e:
        print(str(e) == "Each row must have 3 columns")

    # Test 5: The matrix instance must have only numbers from 0 to 8:
    try:
        init([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    except ValueError as e:
        print((str(e) == "State must contain numbers 0 to 8"))

    # Test 5: Validate final state detection
    print(is_final_state([1, 2, 3, 4, 0, 5, 6, 7, 8]) is True)
    print(is_final_state([0, 1, 2, 3, 4, 5, 6, 7, 8]) is True)
    print(is_final_state([1, 2, 3, 4, 5, 6, 7, 8, 0]) is True)

    # Test 6: Check valid moves generation
    print(get_all_moves([1, 2, 0, 4, 5, 6, 7, 8, 3]) == ['R', 'U'])

    # Test 7: Check state modification
    print(modify_state([1, 2, 0, 4, 5, 6, 7, 8, 3], 'U') == [1, 2, 6, 4, 5, 0, 7, 8, 3])

    # Test 8: Check transition logic
    is_valid, new_state = transition([1, 2, 0, 4, 5, 6, 7, 8, 3], [1, 2, 0, 4, 5, 6, 7, 8, 3], 'R')
    print(is_valid is True)
    print(new_state == [1, 0, 2, 4, 5, 6, 7, 8, 3])

    # Test 9: Check incorrect transition
    is_valid, new_state = transition([1, 2, 3, 4, 5, 6, 7, 8, 0], [1, 2, 3, 4, 5, 6, 7, 8, 0], 'U')
    print(is_valid is False)
    print(new_state == [1, 2, 3, 4, 5, 6, 7, 8, 0])

    # Test 10: Check not previous state
    is_valid, new_state = transition([1, 2, 0, 3, 4, 5, 6, 7, 8], [1, 0, 2, 3, 4, 5, 6, 7, 8], 'R')
    print(is_valid is False)
    print(new_state == [1, 2, 0, 3, 4, 5, 6, 7, 8])
