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


def next_state(current_state, action, wind_strength):
    """
    Calculate the next state given the current state, action, and wind strength.
    """
    row, old_col = current_state
    col = old_col

    # Apply action
    if action == actions['up']:
        row = max(row - 1, 0)
    elif action == actions['down']:
        row = min(row + 1, rows - 1)
    elif action == actions['left']:
        col = max(old_col - 1, 0)
    elif action == actions['right']:
        col = min(old_col + 1, cols - 1)

    # Apply wind effect
    row = max(row - wind_strength[old_col], 0)

    return row, col


def q_learning(Q_table, episodes, alpha, gamma, epsilon, wind_strength, goal_state):
    """
    Q-learning algorithm implementation.
    """
    for episode in range(episodes):
        state = initial_state
        done = False

        while not done:
            # Epsilon-greedy strategy for action selection
            if random.uniform(0, 1) < epsilon:
                action = random.choice(list(actions.values()))  # Explore action
            else:
                action = np.argmax(Q_table[state])  # Exploit learned values

            # Calculate the next state and reward
            next_state_ = next_state(state, action, wind_strength)
            reward = -1  # Reward is -1 for all transitions

            # Q-learning update
            Q_table[state + (action,)] += alpha * (reward + gamma * np.max(Q_table[next_state_]) - Q_table[state + (action,)])

            # Update state
            state = next_state_

            # Check if goal is reached
            if state == goal_state:
                done = True

    return Q_table


episodes = 1000
goal_state = (3, 7)  # Goal state

# Run Q-learning algorithm
Q_table_trained = q_learning(Q_table, episodes, alpha, gamma, epsilon, wind_strength, goal_state)

def extract_policy(Q_table):
    """
    Extract the policy from the Q-table by choosing the action with the highest Q-value for each state.
    """
    policy = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            policy[i, j] = np.argmax(Q_table[i, j])
    return policy

# Extract the policy
policy = extract_policy(Q_table_trained)

# Convert policy actions to directions for better readability
directions = {0: '↑', 1: '↓', 2: '←', 3: '→'}
policy_readable = np.vectorize(directions.get)(policy)

print(policy_readable)

