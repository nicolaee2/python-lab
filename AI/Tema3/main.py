import itertools


def init():
    available_numbers = list(range(1, 10))
    a_numbers = []
    b_numbers = []
    return available_numbers, a_numbers, b_numbers


def is_winner(numbers):
    """
    Checks if the given numbers form a winning combination.

    :param numbers:
    :return:
    """
    if len(numbers) < 3:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 15:
                    return True
    return False


def final_state(available_numbers, a_numbers, b_numbers):
    """
    Check final state

    :param available_numbers: available numbers
    :param a_numbers: the numbers chosen by A
    :param b_numbers: the numbers chosen by B
    :return: True, if it is a final state, false otherwise
    """
    if is_winner(a_numbers):
        return True, 'A'
    elif is_winner(b_numbers):
        return True, 'B'
    if not len(available_numbers):
        return True, 'D'
    else:
        return False, None


def move(turn, available_numbers, a_numbers, b_numbers, choice):
    if choice not in available_numbers:
        return False, available_numbers, a_numbers, b_numbers
    available_numbers.remove(choice)
    if turn == 0:
        a_numbers.append(choice)
    else:
        b_numbers.append(choice)
    return True, available_numbers, a_numbers, b_numbers


def play(turn, available_numbers, a_numbers, b_numbers):
    if turn == 0:
        print("Player's turn")
        choice = int(input("Choose a number: "))
        while choice not in available_numbers:
            choice = int(input("Choose a number: "))
        print(f"Player chose {choice}\n")
    else:
        print("Robot is thinking...")
        choice = minmax(available_numbers, a_numbers, b_numbers)[1]
        print(f"Robot chose {choice}\n")
    return move(turn, available_numbers, a_numbers, b_numbers, choice)


def min_value(available_numbers, a_numbers, b_numbers):
    if final_state(available_numbers, a_numbers, b_numbers)[0]:
        if is_winner(b_numbers):
            return float('1000')
        elif is_winner(a_numbers):
            return float('-1000')
        else:
            return 0
    min_score = float('1000')
    for number in available_numbers:
        _, new_available_numbers, new_a_numbers, new_b_numbers = move(0, available_numbers[:], a_numbers[:], b_numbers[:], number)
        score = max_value(new_available_numbers, new_a_numbers, new_b_numbers)
        min_score = min(min_score, score)
    return min_score


def max_value(available_numbers, a_numbers, b_numbers):
    if final_state(available_numbers, a_numbers, b_numbers)[0]:
        if is_winner(b_numbers):
            return float('1000')
        elif is_winner(a_numbers):
            return float('-1000')
        else:
            return 0
    max_score = float('-1000')
    for number in available_numbers:
        _, new_available_numbers, new_a_numbers, new_b_numbers = move(1, available_numbers[:], a_numbers[:], b_numbers[:], number)
        score = min_value(new_available_numbers, new_a_numbers, new_b_numbers)
        max_score = max(max_score, score)
    return max_score


def heuristic(available_numbers, a_numbers, b_numbers):
    """
    Returns a value for a state

    :param available_numbers: the available numbers
    :param a_numbers: the chosen numbers of player A.
    :param b_numbers: the chosen numbers of player B
    :return: a value for the state
    """

    # initialize the number of wins for each player
    a_potential_wins = 0
    b_potential_wins = 0

    # initialize the possible moves for each player
    a_possible_moves = a_numbers + available_numbers
    b_possible_moves = b_numbers + available_numbers

    # check the possible combinations for player A
    for comb in itertools.combinations(a_possible_moves, 3):
        if sum(comb) == 15:
            a_potential_wins += 1

    # check the possible combinations for player B
    for comb in itertools.combinations(b_possible_moves, 3):
        if sum(comb) == 15:
            b_potential_wins += 1

    return b_potential_wins - a_potential_wins


def minmax(available_numbers, a_numbers, b_numbers, depth=4, is_maximizing_player=True):
    """
    Returns the best score and the best action for the current state, considering the next best moves for the opponent

    :param available_numbers: the available numbers
    :param a_numbers: the chosen numbers of player A.
    :param b_numbers: the chosen numbers of player B
    :param depth: the depth of the tree
    :param is_maximizing_player: True if the current player is the maximizing player, False otherwise
    :return: the best score and the best action for the current state
    """

    # check final state
    final, winner = final_state(available_numbers, a_numbers, b_numbers)
    if final:

        # if the state is final, return the score and None
        if winner == "D":
            return 0, None
        elif winner == "A":
            return float('-1000'), None
        else:
            return float('1000'), None

    # check final depth, return the heuristic value and None
    if depth == 0:
        return heuristic(available_numbers, a_numbers, b_numbers), None

    # initialize the best score and the best action
    if is_maximizing_player:
        best_score = float('-1000')
    else:
        best_score = float('1000')

    best_action = None

    for number in available_numbers:

        if is_maximizing_player:
            _, new_available_numbers, new_a_numbers, new_b_numbers = (
                move(1, available_numbers[:], a_numbers[:], b_numbers[:], number)
            )
        else:
            _, new_available_numbers, new_a_numbers, new_b_numbers = (
                move(0, available_numbers[:], a_numbers[:], b_numbers[:], number)
            )

        score, _ = minmax(new_available_numbers, new_a_numbers, new_b_numbers, depth - 1, not is_maximizing_player)

        if is_maximizing_player:
            if score >= best_score:
                best_score = score
                best_action = number
        else:
            if score <= best_score:
                best_score = score
                best_action = number

    return best_score, best_action


def main():
    available_numbers, a_numbers, b_numbers = init()
    turn = 0
    while True:
        print(f"Available numbers: {available_numbers}")
        is_valid, available_numbers, a_numbers, b_numbers = play(turn, available_numbers, a_numbers, b_numbers)
        if is_valid:
            is_final, winner = final_state(available_numbers, a_numbers, b_numbers)
            if is_final:
                if winner == 'A':
                    print("Player won!")
                elif winner == 'B':
                    print("Robot won!")
                else:
                    print("Draw game!")
                break
            else:
                turn = 1 - turn
        else:
            print("Invalid move!")
            continue

main()
