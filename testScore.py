import unittest
from Score import *


class testScore(unittest.TestCase):

    def testGetCurrentScore(self):  # Test getter
        score = Score()  
        self.assertEqual(score.get_current_score(), 0)

    def testset_current_score(self):  # Test setter
        score = Score()
        score.set_current_score(10)
        self.assertEqual(score.get_current_score(), 10)

    def test_reset_score_object(self):  # Test reset one object
        score = Score()
        score.set_current_score(10)
        score.reset_score_object()
        self.assertEqual(score.get_current_score(), 0)


if __name__ == '__main__':
    unittest.main()
