from enum import Enum
from random import randint
from Player import Player
import os




class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Game:
    def __init__(self):
        self.difficulty = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]

        
    def quitGame():
        # implementation for quitting the game
        os._exit
        pass

    def resetGame(self):
       
        pass

    def setCheatMode(self):
        # implementation for setting cheat mode
        pass

    def setDifficulty(self, game_state):
        # implementation for setting the game difficulty based on the game state
        #  should return an ENUM value representing
        pass

    def printScore(self):
        # implementation for printing the game score
        pass

    def throwDice():
        # for loop 1 to 6 that returns int
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return list(dice1, dice2)
    
  
    def playGame():
        print("Welcome to Pig Game!\n\nThe instructions of the game are simple, blab blab bla\n")
        pri
        p1 = Player()
    
    if __name__ == "__main__":
        playGame()
