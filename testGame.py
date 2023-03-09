import unittest
from Game import *


class testGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_quitGame(self):
        with self.assertRaises(SystemExit):
            self.game.quitGame()

    def test_resetGame(self):
        self.game.game_state.isCheatMode = True
        self.game.resetGame()
        self.assertFalse(self.game.game_state.isCheatMode)
        for player in self.game.game_state.highScoreList:
            self.assertEqual(player.score.scoreValue, 0)
    
    
if __name__ == '__main__':
    unittest.main()