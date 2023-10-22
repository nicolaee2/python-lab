from PuzzleStateUtil import *
import heapq
import random
import time


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
    def greedy_search(initial_state, heuristic):
        if not is_solvable(initial_state):
            return None, [], 0

        visited_states = set()
        stack = [(initial_state, [])]  # Each item in the stack is a tuple (state, path_to_that_state)

        while stack:
            current_state, current_path = stack.pop()

            if tuple(current_state) in visited_states:
                continue

            visited_states.add(tuple(current_state))

            if is_final_state(current_state):
                return current_state, current_path, len(current_path)

            moves = get_all_moves(current_state)
            next_states = [
                (modify_state(current_state, move), move)
                for move in moves
                if tuple(modify_state(current_state, move)) not in visited_states
            ]

            if not next_states:
                continue

            # Evaluate heuristics and sort
            state_costs = [(heuristic(state), state, move) for state, move in next_states]
            state_costs.sort(key=lambda x: x[0])

            optimal_cost = state_costs[0][0]

            # filter states with optimal cost
            state_costs = [x for x in state_costs if x[0] == optimal_cost]

            for cost, state, move in state_costs:
                stack.append((state, current_path + [move]))

        return None, [], 0  # No solution found

    # Example usage:
    # initial_state = init([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    # final_state, path, path_length = greedy_search_stack(initial_state, manhattan_distance)

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

    @staticmethod
    def print_greedy_and_a_star_result(result):
        """
        Print the result of Greedy and A* search

        :param result: The result
        """
        state, solution_path, total_steps = result
        print("Total steps: {}".format(total_steps))
        print("Solution: {}".format(state))
        print("Solution path: {}".format(solution_path))

    @staticmethod
    def run_all_and_print(initial_states):
        heuristic_functions = [manhattan_distance, hamming_distance, chebyshev_distance]
        heuristic_functions_names = ["Manhattan", "Hamming", "Chebyshev"]

        for initial_state in initial_states:
            print("~" * 50)
            print("Initial state: {}".format(initial_state))
            print("Is solvable: {}".format(is_solvable(initial_state)))
            print("Is final state: {}".format(is_final_state(initial_state)))
            print("\n")

            print("IDDFS:")
            start_time = time.time()
            result = PuzzleSolvers.iddfs(initial_state)
            end_time = time.time()
            if result:
                PuzzleSolvers.print_iddfs_result(result)
                print("Execution time: {}".format(end_time - start_time))
            else:
                print("No solution found")
            print("")

            for heuristic_function, heuristic_function_name in zip(heuristic_functions, heuristic_functions_names):
                print("Greedy search with {} heuristic:".format(heuristic_function_name))
                start_time = time.time()
                result = PuzzleSolvers.greedy_search(initial_state, heuristic_function)
                end_time = time.time()
                if result:
                    PuzzleSolvers.print_greedy_and_a_star_result(result)
                    print("Execution time: {}".format(end_time - start_time))
                else:
                    print("No solution found")
                print("")

            print("A* search with Manhattan distance heuristic:")
            start_time = time.time()
            result = PuzzleSolvers.a_star_search(initial_state)
            end_time = time.time()
            if result:
                PuzzleSolvers.print_greedy_and_a_star_result(result)
                print("Execution time: {}".format(end_time - start_time))
            else:
                print("No solution found")
            print("\n\n")