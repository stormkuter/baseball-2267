class GameResult:
    def __init__(self, solved, strike, ball):
        self.__solved = solved
        self.__strikes = strike
        self.__balls = ball

    def get_solved(self):
        return self.__solved

    def get_strikes(self):
        return self.__strikes

    def get_balls(self):
        return self.__balls
