#from GameState import GameState


class Score:

    def __init__(self):
        self.__currentScore = 0

    def getCurrentScore(self):
        return self.__currentScore

    def setCurrentScore(self, points):
        self.__currentScore += points

    def resetScoreObject(self): # NEW Resets the score for the Score object. Might not be needed?
        self.__currentScore = 0

    def resetScore(list):  # For the high score list. Reset the score for each element in the list to zero
        for element in list:
            element.setCurrentScore(0)

    #def addScoreToState(state : GameState):
   #     pass
