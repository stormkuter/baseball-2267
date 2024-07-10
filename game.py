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
            for i in range(len(self.question)):
                char = guessNumber[i]
                index = self.question.find(char)
                if index == i:
                    strike += 1

            return GameResult(False, strike, 0)

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
