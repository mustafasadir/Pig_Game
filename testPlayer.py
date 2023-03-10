import unittest
from Score import Score
from Player import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        player = Player("Kristoffer")
        self.assertEqual(player._get_name(), "Kristoffer")  
        self.assertIsInstance(player.score, Score)  

    def test_get_name(self):
        player = Player("Mustafa")
        self.assertEqual(player._get_name(), "Mustafa")


if __name__ == '__main__':
    unittest.main()
