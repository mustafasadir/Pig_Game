class GameState:
    '''
    Here the score list and cheat mode are being configured
    '''
    def __init__(self):
        self.difficulty = None  # Type ENUM
        self.is_cheat_mode = False
        self.score_list = {}

    def get_state(self):
        return self
