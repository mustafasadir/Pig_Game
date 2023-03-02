import unittest
from Score import Score  # Need to import Score, otherwise can't test it
from Player import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        # Test that Player object is initialized correctly
        player = Player("Kristoffer")  #Creates a new player object
        self.assertEqual(player._getName(), "Kristoffer")  # Tests the name in the constructor
        self.assertIsInstance(player.score, Score)  # Tests the score in object

    def testGetName(self):
        # Test the _getName method of Player class
        player = Player("Mustafa") #Creates a new player object
        self.assertEqual(player._getName(), "Mustafa")  # Tests the name in the method


if __name__ == '__main__':
    unittest.main()