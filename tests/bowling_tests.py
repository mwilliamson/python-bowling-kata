import unittest

import bowling


class BowlingTests(unittest.TestCase):
    def test_empty_game_has_score_of_zero(self):
        self.assertEqual(0, bowling.score_game([]))

    def test_score_of_one_throw_is_number_of_pins_knocked_down(self):
        self.assertEqual(4, bowling.score_game([4]))

    def test_score_of_many_throws_is_total_number_of_pins_knocked_down(self):
        self.assertEqual(14, bowling.score_game([4, 2, 5, 3]))
