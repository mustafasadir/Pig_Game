from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Game:
    

    def __init__(self):
        self.difficulty = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
        self.instruction = "This is the game instruction"
    
    def quitGame(self):
        # implementation for quitting the game
        pass

    def resetGame(self):
        # implementation for resetting the game
        pass

    def setCheatMode(self):
        # implementation for setting cheat mode
        pass

    def setDifficulty(self, game_state):
        # implementation for setting the game difficulty based on the game state
        # should return an ENUM value representing
        pass
    
    def printInstruction(self):
        # implementation for printing the game instruction
        print(self.instruction)

    def printScore(self):
        # implementation for printing the game score
        pass

    def throwDice():
        # for loop 1 to 6 that returns int
        return int