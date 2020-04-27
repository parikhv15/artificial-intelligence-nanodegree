import time
import random

from sample_players import DataPlayer

_HEURISTICS = {
    0: 'defensive_strategy',
    1: 'offensive_strategy',
    2: 'moves_to_board_strategy',
    3: 'offensive_to_defensive_strategy',
    4: 'defensive_to_offensive_strategy',
    5: 'blank_spaces_strategy',
    6: 'balanced_strategy'
}

class Heuristic():
    def score(self, game_state, player_id):
        raise NotImplementedError

class CustomHeuristic(Heuristic):
    def __init__(self):
        pass

    def __get_player_liberties(self, game_state, player_id):
        loc = game_state.locs[player_id]
        return game_state.liberties(loc)

    def __get_opponent_liberties(self, game_state, player_id):
        loc = game_state.locs[[1 - player_id]]
        return game_state.liberties(loc)

    def __weighted_strategy(self, game_state, player_id, weight_player, weight_opponent):
        player_moves = self.__get_player_liberties(game_state, player_id)
        opponent_moves = self.__get_player_liberties(game_state, player_id)

        return (weight_player * len(player_moves)) - (weight_opponent * len(opponent_moves))

    def balanced_strategy(self, game_state, player_id, factor=1):
        return self.__weighted_strategy(game_state, player_id, factor, factor)

    def defensive_strategy(self, game_state, player_id, factor=2):
        return self.__weighted_strategy(game_state, player_id, factor, 1)

    def offensive_strategy(self, game_state, player_id, factor=2):
        return self.__weighted_strategy(game_state, player_id, 1, factor)

    def moves_to_board_strategy(self, game_state, player_id, factor=2):
        player_moves = self.__get_player_liberties(game_state, player_id)
        opponent_moves = self.__get_player_liberties(game_state, player_id)
        round = game_state.ply_count
        board_size = game_state.size

        return self.__weighted_strategy(game_state, player_id, 2 * round / board_size, 1)

    def offensive_to_defensive_strategy(self, game_state, player_id, factor=2):
        round = game_state.ply_count
        board_size = game_state.size

        if round / board_size <= 0.5:
            return self.offensive_strategy(game_state, player_id, factor)
        else:
            return self.defensive_strategy(game_state, player_id, factor)

    def defensive_to_offensive_strategy(self, game_state, player_id, factor=2):
        round = game_state.ply_count
        board_size = game_state.size

        if round / board_size > 0.5:
            return self.offensive_strategy(game_state, player_id, factor)
        else:
            return self.defensive_strategy(game_state, player_id, factor)

    def blank_spaces_strategy(self, game_state, player_id, factor=-1.1):
        player_moves = self.__get_player_liberties(game_state, player_id)
        opponent_moves = self.__get_player_liberties(game_state, player_id)
        blank_spaces = game_state.get_blank_spaces()

        num_blank_spaces = len(blank_spaces) if blank_spaces else 0

        return len(player_moves) - (2 * len(opponent_moves)) - (factor**len(blank_spaces))

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
        self.context = {
            'depths': []
        }

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

    def average_depth(self):
        context = self.context if self.context else {}
        depths = context['depths'] if 'depths' in context else []

        if depths: return sum(depths) / len(depths)

        return 0

    def depths(self):
        return self.context['depths']

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

        if state.ply_count < 2:
            self.queue.put(random.choice(state.actions()))
        else:
            self._minimax_iterative_deepening(state)

    def _minimax_iterative_deepening(self, state):
        import random
        from isolation import StopSearch

        depth = 1
        action = random.choice(state.actions())
        self.context['depths'].append(depth)
        # self.queue.put(action)

        self.__time_start()
        while True:
            try:
                action = self._minimax_alpha_beta_prune(state, depth)

                if action == float('inf') or action == float('-inf'):
                    print("stopping..")
                    break

                depth = depth + 1

                if self.queue.qsize() > 10: self.qsize.get()
                self.context['depths'][-1] = depth
                self.queue.put(action)
            except SearchTimeout as e:
                break
        self.__time_stop()

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
