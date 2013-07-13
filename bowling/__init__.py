def score_game(throws):
    game = Game(throws)
    total = 0
    for index in _frame_indexes(game):
        total += game.pins_knocked_down(index) + game.pins_knocked_down(index + 1)
        if _is_strike(game, index):
            total += game.pins_knocked_down(index + 2)
        elif _is_spare(game, index):
            total += game.pins_knocked_down(index + 2)
        
    return total


def _frame_indexes(game):
    index = 0
    while index < len(game):
        yield index
        if _is_strike(game, index):
            index += 1
        else:
            index += 2


def _is_strike(game, index):
    return game.pins_knocked_down(index) == 10


def _is_spare(game, index):
    return game.pins_knocked_down(index) + game.pins_knocked_down(index + 1) == 10


class Game(object):
    def __init__(self, throws):
        self._throws = throws
        
    def pins_knocked_down(self, index):
        if index < len(self._throws):
            return self._throws[index]
        else:
            return 0
            
    def __len__(self):
        return len(self._throws)
