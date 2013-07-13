def score_game(throws):
    game = Game(throws)
    total = 0
    for frame in _frames(game):
        index = frame.index
        total += game.pins_knocked_down(index) + game.pins_knocked_down(index + 1)
        if _is_strike(game, index):
            total += game.pins_knocked_down(index + 2)
        elif _is_spare(game, index):
            total += game.pins_knocked_down(index + 2)
        
    return total


def _frames(game):
    index = 0
    while index < len(game):
        frame = _create_frame(game, index)
        yield frame
        index += frame.length


def _create_frame(game, index):
    return Frame(index, _frame_length(game, index))


def _frame_length(game, index):
    if _is_strike(game, index):
        return 1
    else:
        return 2


def _is_strike(game, index):
    return game.pins_knocked_down(index) == 10


def _is_spare(game, index):
    return game.pins_knocked_down(index) + game.pins_knocked_down(index + 1) == 10


class Frame(object):
    def __init__(self, index, length):
        self.index = index
        self.length = length
        

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
