import unittest

import bowling


class BowlingTests(unittest.TestCase):
    def test_empty_game_has_score_of_zero(self):
        self.assert_game_score(0, [])

    def test_score_of_one_throw_is_number_of_pins_knocked_down(self):
        self.assert_game_score(4, [4])

    def test_score_of_many_throws_is_total_number_of_pins_knocked_down(self):
        self.assert_game_score(14, [4, 2, 5, 3])
        
    def test_score_of_strike_is_ten_plus_next_two_throws(self):
        self.assert_game_score(21, [10, 2, 3, 1])
        
    def test_score_of_strike_is_ten_if_next_throws_arent_present(self):
        self.assert_game_score(10, [10])
        
    def test_score_of_spare_is_ten_plus_next_throw(self):
        self.assert_game_score(17, [4, 6, 2, 3])
        
    def test_two_throws_totalling_ten_is_not_spare_if_not_in_same_frame(self):
        self.assert_game_score(15, [0, 4, 6, 2, 3])
        
    def test_zero_then_ten_in_same_frame_is_treated_as_spare(self):
        self.assert_game_score(24, [0, 10, 6, 2])

    def test_score_of_perfect_game_is_300(self):
        self.assert_game_score(300, [10] * 12)
    
    def assert_game_score(self, expected_score, game):
        self.assertEqual(expected_score, bowling.score_game(game))
