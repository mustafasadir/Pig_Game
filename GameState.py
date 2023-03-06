from ast import Dict
from Game import Difficulty


class GameState:
    def __init__(self):
        self.difficulty = None #Type ENUM
        self.isCheatMode = False
        #self.highScoreList : Dict[Player,Score]{}
        
    def getState(self):
        return self