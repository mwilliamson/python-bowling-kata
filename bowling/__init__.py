def score_game(throws):
    game = Game(throws)
    total = 0
    for index, pins_knocked_down in enumerate(game):
        total += pins_knocked_down
        if pins_knocked_down == 10:
            total += game.pins_knocked_down(index + 1) + game.pins_knocked_down(index + 2)
        
    return total


class Game(object):
    def __init__(self, throws):
        self._throws = throws
        
    def pins_knocked_down(self, index):
        if index < len(self._throws):
            return self._throws[index]
        else:
            return 0
            
    def __iter__(self):
        return iter(self._throws)
