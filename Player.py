from Score import Score


class Player:

    def __init__(self, name):
        self.name = name
        self.score = Score()  # Creates a Score object for every Player object

    def _getName(self):
        return self.name
    
    def changeName(self, new_name):
        self.name = new_name
