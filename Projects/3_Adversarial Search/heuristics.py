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
