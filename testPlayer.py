import unittest
from Score import Score 
from Player import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        # Test that Player object is initialized correctly
        player = Player("Kristoffer")  
        self.assertEqual(player._get_name(), "Kristoffer")  # Tests the name in the constructor
        self.assertIsInstance(player.score, Score)  # Tests the score in object

    def testGetName(self):
        # Test the _getName method of Player class
        player = Player("Mustafa") 
        self.assertEqual(player._get_name(), "Mustafa")  


if __name__ == '__main__':
    unittest.main()