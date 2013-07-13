def score_game(throws):
    game = Game(throws)
    total = 0
    index = 0
    while index < len(game):
        total += game.pins_knocked_down(index) + game.pins_knocked_down(index + 1)
        if game.pins_knocked_down(index) == 10:
            total += game.pins_knocked_down(index + 2)
            index += 1
        elif game.pins_knocked_down(index) + game.pins_knocked_down(index + 1) == 10:
            total += game.pins_knocked_down(index + 2)
            index += 2
        else:
            index += 2
        
    return total


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
