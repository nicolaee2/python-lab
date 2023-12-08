import numpy as np
import random

rows, cols = 7, 10
n_actions = 4
actions = {'up': 0, 'down': 1, 'left': 2, 'right': 3}
Q_table = np.zeros((rows, cols, n_actions))
alpha = 0.5
gamma = 0.9
epsilon = 0.1
initial_state = (3, 0)
wind_strength = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
episodes = 1000
goal_state = (3, 7)


def next_state(current_state, action, wind_strength):
    """
    Calculate the next state given the current state, action, and wind strength
    """
    row, old_col = current_state
    col = old_col

    if action == actions['up']:
        row = max(row - 1, 0)
    elif action == actions['down']:
        row = min(row + 1, rows - 1)
    elif action == actions['left']:
        col = max(old_col - 1, 0)
    elif action == actions['right']:
        col = min(old_col + 1, cols - 1)

    # apply wind strength
    row = max(row - wind_strength[old_col], 0)

    return row, col


def q_learning(Q_table, episodes, alpha, gamma, epsilon, wind_strength, goal_state):
    for episode in range(episodes):
        state = initial_state
        done = False
        Nsa = np.zeros((rows, cols, n_actions), dtype=int)

        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(list(actions.values()))
            else:
                action = np.argmax(Q_table[state])

            next_state_ = next_state(state, action, wind_strength)
            reward = -1 if next_state_ != goal_state else 0

            # increment Nsa for the current state-action pair
            sa = tuple(list(state) + [action])
            Nsa[sa] += 1

            # Q-learning update with dynamic alpha
            Q_table[sa] += alpha / Nsa[sa] * (reward + gamma * np.max(Q_table[next_state_]) - Q_table[sa])

            state = next_state_
            if state == goal_state:
                done = True

    return Q_table


def extract_policy(Q_table):
    """
    Extract the policy from the Q-table by choosing the action with the highest Q-value for each state
    """
    policy = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            policy[i, j] = np.argmax(Q_table[i, j])
    return policy


def extract_policy_readable(policy, directions):
    policy_readable = []
    for row in policy:
        row_readable = []
        for action in row:
            row_readable.append(directions[action])
        policy_readable.append(row_readable)
    return policy_readable


Q_table_trained = q_learning(Q_table, episodes, alpha, gamma, epsilon, wind_strength, goal_state)
policy = extract_policy(Q_table_trained)
directions = {0: '↑', 1: '↓', 2: '←', 3: '→'}
policy_readable = extract_policy_readable(policy, directions)

for row in policy_readable:
    print(' '.join(row))


