class Score:
    def __init__(self):
        self.__current_score = 0

    def get_current_score(self):
        return self.__current_score

    def set_current_score(self, points):
        self.__current_score += points

    def reset_score_object(self):
        '''  
        Resets the score for the Score object
        '''
        self.__current_score = 0
