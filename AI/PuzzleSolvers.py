from PuzzleStateUtil import *
import heapq

class PuzzleSolvers:
    @staticmethod
    def dls(state, prev_state, depth, steps, solution_path):
        """
        Depth Limited Search

        :param solution_path: The solution path
        :param steps: The number of steps
        :param prev_state: The previous state
        :param state: The current state
        :param depth: The maximum depth
        :return: The solution (if found)
        """
        steps += 1

        # If reached the final state, stop recursing.
        if is_final_state(state):
            return state, steps, solution_path

        # If reached the maximum depth, stop recursing.
        if depth <= 0:
            return False, steps, solution_path

        # Recur for all the adjacent states
        for move in get_all_moves(state):
            is_move_valid, new_state = transition(state, prev_state, move)

            if is_move_valid:
                result, steps_for_subtree, solution_path = (
                    PuzzleSolvers.dls(new_state, state, depth - 1, 0, solution_path))

                steps += steps_for_subtree
                if result:
                    solution_path.append(move)
                    return result, steps, solution_path

        return False, steps, solution_path

    @staticmethod
    def iddfs(state):
        """
        Iterative Deepening Depth First Search

        :param state: The current state
        :return: The solution (if found)
        """
        depth = 0
        total_steps = 0
        solution_path = []

        if is_final_state(state):
            return state, total_steps, depth, solution_path

        if not is_solvable(state):
            return False

        while True:
            prev_state = []
            result, total_steps, solution_path = PuzzleSolvers.dls(state, prev_state, depth, total_steps, solution_path)
            if result:
                solution_path.reverse()
                return result, total_steps, depth, solution_path
            depth += 1

    @staticmethod
    def print_iddfs_result(result):
        """
        Print the result of IDDFS

        :param result: The result
        """
        state, total_steps, depth, solution_path = result
        print("Depth: {}".format(depth))
        print("Total steps: {}".format(total_steps))
        print("Solution: {}".format(state))
        print("Solution path: {}".format(solution_path))
        print("\n\n")

    @staticmethod
    def a_star_search(initial_state):
        if not is_solvable(initial_state):
            return None

        # queue containing (f, state, path)
        queue = [(manhattan_distance(initial_state), initial_state, [])]
        explored = set()

        while queue:
            f, state, path = heapq.heappop(queue)

            if is_final_state(state):
                return state, path, len(path)

            explored.add(tuple(state))

            for move in get_all_moves(state):
                new_state = modify_state(state, move)

                if tuple(new_state) not in explored:
                    g = len(path) + 1
                    h = manhattan_distance(new_state)
                    f = g + h
                    heapq.heappush(queue, (f, new_state, path + [move]))

        return None

