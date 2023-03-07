from GameState import GameState


class Score:

    def __init__(self):
        self.__currentScore = 0

    def getCurrentScore(self):  # Gets the current score
        return self.__currentScore

    def setCurrentScore(self, points):  # Sets the current score
        self.__currentScore += points

    def resetScoreObject(self):  # Resets the score for the Score object
        self.__currentScore = 0

    def resetScoreList(self, score_list):  # Resets the score for the list
        for score in score_list:
            score.resetScoreObject()
        
    def addScoreToState(state : GameState):
        
