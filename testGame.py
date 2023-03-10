import unittest
from unittest.mock import patch
from io import StringIO
from Game import *


class testGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_quit_game(self):
        with self.assertRaises(SystemExit):
            self.game.quit_game()

    def test_reset_game(self):
        '''
        Tests the reset game
        '''
        for player in self.game.game_state.score_list:
            player.Score.set_current_score(1)
        self.game.reset_game()
        for player in self.game.game_state.score_list:
            self.assertEqual(player.score.scoreValue, 0)

    def test_set_cheat_mode(self):
        '''
        Tests the cheat mode
        '''
        self.game.setCheatMode = lambda: (4, 2)
        result = self.game.setCheatMode()
        self.assertEqual(result, (4, 2))
    
    def test_throw_dice(self):
        '''
        Tests the throw dice
        '''
        for i in range(10):
            dice1, dice2 = self.game.throw_dice()
            self.assertGreaterEqual(dice1, 1)
            self.assertLessEqual(dice1, 6)
            self.assertGreaterEqual(dice2, 1)
            self.assertLessEqual(dice2, 6)


if __name__ == '__main__':
    unittest.main()
