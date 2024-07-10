from game_result import GameResult


class Game:
    def __init__(self):
        super().__init__()
        self.question = ""

    def guess(self, guessNumber):
        self.assert_illegal_value(guessNumber)
        if self.question == guessNumber:
            return GameResult(True, 3, 0)
        else:
            strike = 0
            ball = 0
            for i in range(len(self.question)):
                if self.question.find(guessNumber[i]) == i:
                    strike += 1
                elif self.question.find(guessNumber[i]) > -1:
                    ball += 1

            return GameResult(False, strike, ball)

    def assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:
            raise TypeError()
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError()
        if self.isDuplicatedNumber(guessNumber):
            raise TypeError()

    def isDuplicatedNumber(self, guessNumber):
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[0] == guessNumber[2] or \
            guessNumber[1] == guessNumber[2]
