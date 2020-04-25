import time
import random

from sample_players import DataPlayer
from heuristics import CustomHeuristic

_HEURISTICS = {
    0: 'defensive_strategy',
    1: 'offensive_strategy',
    2: 'moves_to_board_strategy',
    3: 'offensive_to_defensive_strategy',
    4: 'defensive_to_offensive_strategy',
    5: 'blank_spaces_strategy',
    6: 'balanced_strategy'
}

class CustomPlayer(DataPlayer):
    """ Implement your own agent to play knight's Isolation

    The get_action() method is the only required method for this project.
    You can modify the interface for get_action by adding named parameters
    with default values, but the function MUST remain compatible with the
    default interface.

    **********************************************************************
    NOTES:
    - The test cases will NOT be run on a machine with GPU access, nor be
      suitable for using any other machine learning techniques.

    - You can pass state forward to your agent on the next turn by assigning
      any pickleable object to the self.context attribute.
    **********************************************************************
    """
    def __init__(self, player_id, heuristic=5):
        super().__init__(player_id)
        self.action_start_time = None

        heuristic_class = CustomHeuristic()
        heuristic_name = _HEURISTICS[heuristic]

        self.heuristic_function = getattr(heuristic_class, heuristic_name)

    def __time_left(self):
        # print("Checking time left.")
        if self.action_start_time:
            # print("Time Elapsed: {}".format(time.time()*1000 - self.action_start_time))
            return time.time() * 1000 < self.action_start_time + self.TIME_LIMIT

        return False

    def __time_elapsed(self):
        if self.action_start_time:
            return time.time() * 1000 - self.action_start_time

    def __time_start(self):
        self.action_start_time = time.time() * 1000

    def __time_stop(self):
        self.action_start_time = None

    def get_action(self, state):
        """ Employ an adversarial search technique to choose an action
        available in the current state calls self.queue.put(ACTION) at least

        This method must call self.queue.put(ACTION) at least once, and may
        call it as many times as you want; the caller will be responsible
        for cutting off the function after the search time limit has expired.

        See RandomPlayer and GreedyPlayer in sample_players for more examples.

        **********************************************************************
        NOTE:
        - The caller is responsible for cutting off search, so calling
          get_action() from your own code will create an infinite loop!
          Refer to (and use!) the Isolation.play() function to run games.
        **********************************************************************
        """
        # TODO: Replace the example implementation below with your own search
        #       method by combining techniques from lecture
        #
        # EXAMPLE: choose a random move without any search--this function MUST
        #          call self.queue.put(ACTION) at least once before time expires
        #          (the timer is automatically managed for you)
        import random

        action = None
        if state.ply_count < 2:
            action = random.choice(state.actions())
        else:
            action = self._minimax_iterative_deepening(state)

        self.queue.put(action)

    def _minimax_iterative_deepening(self, state):
        import random

        # print("[Iterative Deepening] Starting to fetch action for state: {}".format(state))
        self.__time_start()

        action = random.choice(state.actions())
        depth = 1
        while self.__time_left():
            # print("[Iterative Deepening] Running for depth {} and state: {}".format(depth, state))
            try:
                action = self._minimax_alpha_beta_prune(state, depth)
                depth = depth + 1
            except SearchTimeout as e:
                # print(e.message)
                break

        # self.__time_stop()
        # print("[Iterative Deepening] Returning action: {} for state: {}".format(action, state))
        return action

    def _minimax_alpha_beta_prune(self, state, depth):

        def min_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)

            if depth <= 0: return self.heuristic_function(state, self.player_id)

            if not self.__time_left():
                raise SearchTimeout("Timing out player {}'s turn after {} ms".format(state.player(), self.__time_elapsed()))

            value = float("inf")
            for action in state.actions():
                value = min(value, max_value(state.result(action), depth - 1, alpha, beta))
                if value <= alpha: return value
                beta = min(value, beta)

            return value

        def max_value(state, depth, alpha, beta):
            if state.terminal_test(): return state.utility(self.player_id)

            if depth <= 0: return self.heuristic_function(state, self.player_id)

            if not self.__time_left():
                raise SearchTimeout("Timing out player {}'s turn after {} ms".format(state.player(), self.__time_elapsed()))

            value = float("-inf")
            for action in state.actions():
                value = max(value, min_value(state.result(action), depth - 1, alpha, beta))
                if value >= beta: return value
                alpha = max(value, alpha)

            return value

        return max(state.actions(), key=lambda x: min_value(state.result(x), depth - 1, float("-inf"), float("inf")))

class SearchTimeout(Exception):
    def __init__(self, message):
        self.message = message
