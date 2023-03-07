from Score import Score


class Player:

    def __init__(self, name : str ):
        self.__name = name
        self.score = Score().getCurrentScore  # Creates a Score object for every Player object

    def _getName(self):
        return self.__name
