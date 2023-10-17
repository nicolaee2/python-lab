def is_solvable(state):
    """
    Check if a state of the problem is solvable

    :param state: The state
    :return: True if the state is solvable, else False
    """

    # remove the empty tile from the state
    state_no_zero = [x for x in state if x != 0]

    inversion_count = 0

    # compare each tile with every tile after it
    for i in range(len(state_no_zero)):
        for j in range(i + 1, len(state_no_zero)):
            if state_no_zero[i] > state_no_zero[j]:
                inversion_count += 1

    # if the inversion count is even, the state is solvable
    return inversion_count % 2 == 0


def init(matrix):
    """
    Initialize a state from a matrix

    :param matrix: A configuration of the board
    :return: The state represented as a 1D list
    :raise ValueError: If the matrix is not 3x3 or if it doesn't contain numbers 0-8
    """

    # check that matrix row count is 3
    if len(matrix) != 3:
        raise ValueError("Matrix must have 3 rows")

    # check that each row of the matrix has 3 columns
    for row in matrix:
        if len(row) != 3:
            raise ValueError("Each row must have 3 columns")

    # flatten the matrix and return the initial state
    state_initial = [elem for sublist in matrix for elem in sublist]

    # check that the state contains all numbers from 0 to 8
    if sorted(state_initial) != list(range(9)):
        raise ValueError("State must contain numbers 0 to 8")

    return state_initial


def is_final_state(state):
    """
    Check if a state is the goal state

    :param state: A 1D list representing the current configuration of the tiles in the puzzle
    :return: True if the state is the goal state, otherwise False
    """
    state_without_zero = [x for x in state if x != 0]
    return state_without_zero == sorted(state_without_zero)


def get_all_moves(state):
    """
    Get all valid moves for a given state

    :param state: The state
    :return: List of possible moves
    """
    # get position of the empty cell
    zero_pos = state.index(0)

    moves = []
    if zero_pos % 3 > 0:
        # if the empty cell is not in left column
        moves.append("R")
    if zero_pos % 3 < 2:
        # if the empty cell is not in right column
        moves.append("L")
    if zero_pos // 3 > 0:
        # if the empty cell is not in first row
        moves.append("D")
    if zero_pos // 3 < 2:
        # if the empty cell is not in third row
        moves.append("U")

    return moves


def modify_state(state, move):
    """
    Modify a given state based on a given move
    The move is considered valid

    :param state: The state
    :param move: The move ("U", "D", "L", "R")
    :return: The new state after the move
    """

    zero_pos = state.index(0)
    new_state = state.copy()

    if move == "U":
        new_state[zero_pos], new_state[zero_pos + 3] = new_state[zero_pos + 3], new_state[zero_pos]
    elif move == "D" and zero_pos // 3 > 0:
        new_state[zero_pos], new_state[zero_pos - 3] = new_state[zero_pos - 3], new_state[zero_pos]
    elif move == "L" and zero_pos % 3 < 2:
        new_state[zero_pos], new_state[zero_pos + 1] = new_state[zero_pos + 1], new_state[zero_pos]
    elif move == "R" and zero_pos % 3 > 0:
        new_state[zero_pos], new_state[zero_pos - 1] = new_state[zero_pos - 1], new_state[zero_pos]

    return new_state


def transition(state, state_prev, move):
    """
    Make a transition from current state, to new state, given a move

    :param state: The state
    :param state_prev: The previous state
    :param move: The move ("U", "D", "L", "R")
    :return: True if the transition is valid, otherwise False.
             The new state, or the current state, if transition is invalid
    """
    moves = get_all_moves(state)
    if move not in moves:
        return False, state

    state_new = modify_state(state, move)
    if state_new != state_prev:
        return True, state_new

    return False, state