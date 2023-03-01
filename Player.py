from Score import Score

class Player:
    def __init__(self, name):
        self.__name = name
        self.score = Score() #type Score


    def getName(self):
        return self.__name
    
    
