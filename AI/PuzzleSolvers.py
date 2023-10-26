from PuzzleStateUtil import *
import heapq
import time


class PuzzleSolvers:
    @staticmethod
    def dls(current_state, previous_state, max_depth, step_counter, path):
        """
        Depth Limited Search

        :param path: The solution path
        :param step_counter: The number of steps
        :param previous_state: The previous state
        :param current_state: The current state
        :param max_depth: The maximum depth
        :return: The solution
        """
        step_counter += 1

        # stop recurring if the final state was reached
        if is_final_state(current_state):
            return current_state, step_counter, path

        # stop recurring if the max depth was reached
        if max_depth <= 0:
            return False, step_counter, path

        # for all adjacent states, call recursive dls
        for move in get_all_moves(current_state):
            is_valid, new_state = transition(current_state, previous_state, move)

            if is_valid:
                result, steps_for_subtree, path = (
                    PuzzleSolvers.dls(new_state, current_state, max_depth - 1, 0, path)
                )

                # add the steps for the visited subtree
                step_counter += steps_for_subtree

                # when we find the solution, add the current move
                if result:
                    path.append(move)
                    return result, step_counter, path

        # if no solution was found
        return False, step_counter, path

    @staticmethod
    def iddfs(current_state):
        """
        Iterative Deepening Depth First Search

        :param current_state: The current state
        :return: The solution, if it exists
        """
        depth = 0
        total_steps = 0
        path = []

        # check if the initial state is a final state
        if is_final_state(current_state):
            return current_state, total_steps, depth, path

        # check the non-solvable case
        if not is_solvable(current_state):
            return False

        while True:
            previous_state = []

            result, total_steps, path = PuzzleSolvers.dls(
                current_state,
                previous_state,
                depth,
                total_steps,
                path
            )

            if result:
                path.reverse()
                return result, total_steps, depth, path

            # go to next depth
            depth += 1

    @staticmethod
    def greedy_search(initial_state, heuristic):
        if not is_solvable(initial_state):
            return None, [], 0

        visited_states = set()
        stack = [(initial_state, [])]

        while stack:
            current_state, current_path = stack.pop()

            if tuple(current_state) in visited_states:
                continue

            visited_states.add(tuple(current_state))

            if is_final_state(current_state):
                return current_state, current_path, len(current_path)

            moves = get_all_moves(current_state)

            next_states = []
            for move in moves:
                valid_transition, next_state = transition(current_state, current_state, move)
                if valid_transition and tuple(next_state) not in visited_states:
                    next_states.append((next_state, move))

            if not next_states:
                continue

            # evaluate heuristic and sort
            state_costs = [(heuristic(state), state, move) for state, move in next_states]
            state_costs.sort(key=lambda x: x[0])

            optimal_cost = state_costs[0][0]

            # filter states with optimal cost
            state_costs = [x for x in state_costs if x[0] == optimal_cost]

            for cost, state, move in state_costs:
                stack.append((state, current_path + [move]))

        return None, [], 0

    # Example usage:
    # initial_state = init([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
    # final_state, path, path_length = greedy_search_stack(initial_state, manhattan_distance)

    @staticmethod
    def a_star_search(initial_state):
        if not is_solvable(initial_state):
            return None

        # queue containing (f, state, path, prev_state)
        queue = [(manhattan_distance(initial_state), initial_state, [], None)]
        explored = set()

        while queue:

            # get the current optimum
            f, state, path, prev_state = heapq.heappop(queue)

            # check final state case
            if is_final_state(state):
                return state, path, len(path)

            explored.add(tuple(state))

            for move in get_all_moves(state):
                valid_transition, new_state = transition(state, prev_state, move)

                if valid_transition and tuple(new_state) not in explored:
                    # compute f, g and h
                    g = len(path) + 1
                    h = manhattan_distance(new_state)
                    f = g + h

                    # add to queue
                    heapq.heappush(queue, (f, new_state, path + [move], state))

        # no solution found
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