#from GameState import GameState


class Score:

    def __init__(self):
        self.__currentScore = 0


    def resetScore(self, score):
        self.__currentScore = 0


    def getCurrentScore(self):
        return self.__currentScore


    def setCurrentScore(self, points):
        self.__currentScore += points 


    def addScoreToState(state : GameState):
        pass
