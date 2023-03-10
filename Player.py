from Score import Score


class Player:
    '''
    This class lets the player choose a name and creates a Score object for every Player object
    '''

    def __init__(self, name):
        self.name = name
        self.score = Score() 

    def _get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name

