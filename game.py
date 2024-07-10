class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()

        if len(guessNumber) != 3:
            raise TypeError()

        for number in guessNumber:
            if not ord('0') <= number <= ord('9'):
                raise TypeError()

        if number[0] == number[1] or \
            number[0] == number[2] or \
            number[1] == number[2]:
            raise TypeError()
