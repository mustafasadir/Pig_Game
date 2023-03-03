import unittest
from Score import *


class testScore(unittest.TestCase):

    def testGetCurrentScore(self):  # Test getter
        score = Score()  # Creates new Score object
        self.assertEqual(score.getCurrentScore(), 0)  # Makes sure score = 0
    
    def testSetCurrentScore(self):  # Test setter
        score = Score()  # Creates new Score object
        score.setCurrentScore(10)  # Sets score = 10
        self.assertEqual(score.getCurrentScore(), 10)  # Makes sure score is set score = 10
    
    def testResetScoreObject(self):  # Test reset one object
        score = Score()  # Creates new Score object
        score.setCurrentScore(10)  # Set score = 10
        score.resetScoreObject()  # Reset score = 0
        self.assertEqual(score.getCurrentScore(), 0)  # Makes sure that score is set = 0
    
    def testResetScoreList(self):  # Test reset the score list
        score1 = Score()  
        score2 = Score()
        score3 = Score()
        score1.setCurrentScore(5)  # Sets the score for score1
        score2.setCurrentScore(25)  # Sets the score for score2
        score3.setCurrentScore(50)  # Sets the score for score3
        
        scores_list = [score1, score2, score3]  # Makes a list of the scores
        Score().resetScoreList(scores_list)  # Resets the scores
        self.assertEqual(score1.getCurrentScore(), 0)  # Make sure that score1 = 0
        self.assertEqual(score2.getCurrentScore(), 0)  # Make sure that score2 = 0
        self.assertEqual(score3.getCurrentScore(), 0)  # Make sure that score3 = 0
    

    #Add score to state test here


if __name__ == '__main__':
    unittest.main()