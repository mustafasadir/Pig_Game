from enum import Enum
from random import randint
import sys


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Game:
    def __init__(self):
        self.difficulty = [Difficulty.EASY, Difficulty.MEDIUM, Difficulty.HARD]
        self.instruction = '''\tOn a turn, a player rolls the die repeatedly.\n
        The goal is to accumulate as many points as possible, adding up the\n 
        numbers rolled on the die. However, if a player rolls a 1, the player's\n
        turn is over and any points they have accumulated during this turn are\n
        forfeited. Rolling a 1 doesn't wipe out your entire score from previous\n
        turns, just the total earned during that particular roll.\n
        A player can also choose to hold (stop rolling the die) if they \n
        do not want to take a chance of rolling a 1 and losing all of their\n
        points from this turn. If the player chooses to hold, all of the\n
        points rolled during that turn are added to his or her score.\n
        When a player reaches a total of 100 or more points, the game\n
        ends and that player is the winner.
        '''    



    def quit_Game():
        # implementation for quitting the game
        sys.exit()

    def reset_Game(self):pass

    def set_CheatMode(self):
        # implementation for setting cheat mode
        pass

    def set_Difficulty(self, game_state):
        # implementation for setting the game difficulty based on the game state
        #  should return an ENUM value representing
        pass

    def print_Score(self):
        # implementation for printing the game score
        pass

    def throw_Dice():
        # for loop 1 to 6 that returns int
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        return list(dice1, dice2)

   
if __name__ == "__main__":
    print("\t\tWelcome to Pig Game!\n")
    print(Game().instruction)