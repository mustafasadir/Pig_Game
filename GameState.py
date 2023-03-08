from ast import Dict
from Difficulty import Difficulty


class GameState:
    def __init__(self):
        self.difficulty = None #Type ENUM
        self.isCheatMode = False
        self.highScoreList = {}
        
    def getState(self):
        return self