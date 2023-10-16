from PuzzleStateUtil import *


class PuzzleSolvers:
    @staticmethod
    def dls(state, prev_state, depth, steps):
        """
        Depth Limited Search

        :param steps: The number of steps
        :param prev_state: The previous state
        :param state: The current state
        :param depth: The maximum depth
        :return: The solution (if found)
        """
        steps += 1

        # If reached the final state, stop recursing.
        if is_final_state(state):
            return state, steps

        # If reached the maximum depth, stop recursing.
        if depth <= 0:
            return False, steps

        # Recur for all the adjacent states
        for move in get_all_moves(state):
            is_move_valid, new_state = transition(state, prev_state, move)

            if is_move_valid:
                result, steps_for_subtree = PuzzleSolvers.dls(new_state, state, depth - 1, 0)
                steps += steps_for_subtree
                if result:
                    return result, steps

        return False, steps

    @staticmethod
    def iddfs(state):
        """
        Iterative Deepening Depth First Search

        :param state: The current state
        :return: The solution (if found)
        """
        depth = 0
        total_steps = 0

        if is_final_state(state):
            return state, total_steps, depth

        if not is_solvable(state):
            return False

        while True:
            prev_state = []
            result, total_steps = PuzzleSolvers.dls(state, prev_state, depth, total_steps)
            if result:
                return result, total_steps, depth
            depth += 1