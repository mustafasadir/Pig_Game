from Score import Score


class Player:
    '''
    Every player got a name and a score object
    '''

    def __init__(self, name):
        self.name = name
        self.score = Score()

    def _get_name(self):
        return self.name

    def change_name(self, new_name):
        self.name = new_name
