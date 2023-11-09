import itertools
import time


def init():
    available_numbers = list(range(1, 10))
    a_numbers = []
    b_numbers = []
    return available_numbers, a_numbers, b_numbers


def is_winner(numbers):
    if len(numbers) < 3:
        return False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 15:
                    return True
    return False


def final_state(available_numbers, a_numbers, b_numbers):
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
        choice = minmax(available_numbers, a_numbers, b_numbers, 'B')[1]
        print(f"Robot chose {choice}\n")
    return move(turn, available_numbers, a_numbers, b_numbers, choice)


def min_value(available_numbers, a_numbers, b_numbers):
    if final_state(available_numbers, a_numbers, b_numbers)[0]:
        if is_winner(b_numbers):
            return float('inf')
        elif is_winner(a_numbers):
            return float('-inf')
        else:
            return 0
    min_score = float('inf')
    for number in available_numbers:
        _, new_available_numbers, new_a_numbers, new_b_numbers = move(0, available_numbers[:], a_numbers[:], b_numbers[:], number)
        score = max_value(new_available_numbers, new_a_numbers, new_b_numbers)
        min_score = min(min_score, score)
    return min_score


def max_value(available_numbers, a_numbers, b_numbers):
    if final_state(available_numbers, a_numbers, b_numbers)[0]:
        if is_winner(b_numbers):
            return float('inf')
        elif is_winner(a_numbers):
            return float('-inf')
        else:
            return 0
    max_score = float('-inf')
    for number in available_numbers:
        _, new_available_numbers, new_a_numbers, new_b_numbers = move(1, available_numbers[:], a_numbers[:], b_numbers[:], number)
        score = min_value(new_available_numbers, new_a_numbers, new_b_numbers)
        max_score = max(max_score, score)
    return max_score

def heuristic(available_numbers, a_numbers, b_numbers, player):
    opponent = 'B' if player == 'A' else 'A'
    player_potential_wins = 0
    opponent_potential_wins = 0

    # calculate the possible moves taking into account the moves that have already been played
    player_possible_moves = [x for x in list(range(1, 10)) if x not in a_numbers]
    opponent_possible_moves = [x for x in list(range(1, 10)) if x not in b_numbers]

    for combination in itertools.combinations(player_possible_moves, 3):
        if sum(combination) == 15:
            player_potential_wins += 1
    for combination in itertools.combinations(opponent_possible_moves, 3):
        if sum(combination) == 15:
            opponent_potential_wins += 1
    return player_potential_wins - opponent_potential_wins

def minmax(available_numbers, a_numbers, b_numbers, player, depth=3):

    final, winner = final_state(available_numbers, a_numbers, b_numbers)
    if final:
        if winner == "D":
            return 0, None
        else:
            return float('inf') if winner == 'B' else float('-inf'), None
    if depth == 0:
        return heuristic(available_numbers, a_numbers, b_numbers, player), None
    best_score = float('-inf') if player == 'B' else float('inf')
    best_action = None
    for number in available_numbers:
        turn = 0 if player == 'A' else 1
        _, new_available_numbers, new_a_numbers, new_b_numbers = move(turn, available_numbers[:], a_numbers[:], b_numbers[:], number)
        score, _ = minmax(new_available_numbers, new_a_numbers, new_b_numbers, 'B' if player == 'A' else 'A', depth - 1)
        if player == 'B' and score > best_score or player == 'A' and score < best_score:
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
