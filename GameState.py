from ast import Dict
from Game import Difficulty
from Player import Player
from Score import Score

class GameState:
    def __init__(self):
        self.difficulty = None #Type ENUM
        self.isCheatMode = False
        self.highScoreList : Dict[Player,Score]{}
        
    def getState(self):
        return self