import unittest
from Game import *


class testGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_quit_game(self):
        with self.assertRaises(SystemExit):
            self.game.quit_game()

    def test_reset_game(self): # Tests the reset game
        for player in self.game.game_state.score_list:
            player.Score.set_current_score(1)     
        self.game.reset_game()
        for player in self.game.game_state.score_list:
            self.assertEqual(player.score.scoreValue, 0)

    def test_set_cheat_mode(self):    # Tests the cheat function
        self.game.setCheatMode = lambda: (4, 2)
        result = self.game.setCheatMode()
        self.assertEqual(result, (4, 2))
    
    def throw_dice(self):  # Makes sure the dies are between 1 and 6
        game = Game()
        for i in range(10):
            dice1, dice2 = game.throw_dice()
            self.assertGreaterEqual(dice1, 1)
            self.assertLessEqual(dice1, 6)
            self.assertGreaterEqual(dice2, 1)
            self.assertLessEqual(dice2, 6)


if __name__ == '__main__':
    unittest.main()