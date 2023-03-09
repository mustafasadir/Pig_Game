import unittest
from Score import *


class testScore(unittest.TestCase):

    def testGetCurrentScore(self):  # Test getter
        score = Score()  
        self.assertEqual(score.getCurrentScore(), 0)  
    
    def testSetCurrentScore(self):  # Test setter
        score = Score()  
        score.setCurrentScore(10)  
        self.assertEqual(score.getCurrentScore(), 10)  
    
    def testResetScoreObject(self):  # Test reset one object
        score = Score()  
        score.setCurrentScore(10)  
        score.resetScoreObject()  
        self.assertEqual(score.getCurrentScore(), 0)  
    
    def testResetScoreList(self):  # Test reset the score list
        score1 = Score()  
        score2 = Score()
        score3 = Score()
        score1.setCurrentScore(5)  
        score2.setCurrentScore(25)  
        score3.setCurrentScore(50)  
        
        scores_list = [score1, score2, score3]  # Makes a list of the scores
        Score().resetScoreList(scores_list)  # Resets the scores
        self.assertEqual(score1.getCurrentScore(), 0)  
        self.assertEqual(score2.getCurrentScore(), 0)  
        self.assertEqual(score3.getCurrentScore(), 0)  
    

if __name__ == '__main__':
    unittest.main()