def score_game(game):
    total = 0
    for index, pins_knocked_down in enumerate(game):
        total += pins_knocked_down
        if pins_knocked_down == 10:
            total += game[index + 1] + game[index + 2]
        
    return total
