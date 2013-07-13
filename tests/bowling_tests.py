import unittest

import bowling


class BowlingTests(unittest.TestCase):
    def test_empty_game_has_score_of_zero(self):
        self.assertEqual(0, bowling.score_game([]))
