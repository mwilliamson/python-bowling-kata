import unittest

import bowling


class BowlingTests(unittest.TestCase):
    def test_empty_game_has_score_of_zero(self):
        self.assert_game_score(0, [])

    def test_score_of_one_throw_is_number_of_pins_knocked_down(self):
        self.assert_game_score(4, [4])

    def test_score_of_many_throws_is_total_number_of_pins_knocked_down(self):
        self.assert_game_score(14, [4, 2, 5, 3])
        
    def assert_game_score(self, expected_score, game):
        self.assertEqual(expected_score, bowling.score_game(game))
