# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = len(word)*'_'

    def guess(self, char):
        if self.status == STATUS_WIN:
            raise ValueError('You Win!')
        elif self.status == STATUS_LOSE:
            raise ValueError('You Lose!')
        else:
            ocurr = self._find_new_ocurr(char)
            if len(ocurr) == 0:
                self._decrease_guesses()
            else:
                self._update_masked_word(ocurr, char)

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

    def _update_masked_word(self, ocurr, char):
        for index in ocurr:
            self.masked_word = self.masked_word[:index] + self.word[index] + self.masked_word[index + 1:]
        if self.masked_word.count('_') == 0:
            self.status = STATUS_WIN

    def _decrease_guesses(self):
        self.remaining_guesses -= 1
        if self.remaining_guesses >= 0:
            self.status = STATUS_ONGOING
        else:
            self.status = STATUS_LOSE

    def _find_new_ocurr(self, char):
        if self.masked_word.count(char) > 0:
            return []
        else:
            return [index for index, letter in enumerate(self.word) if letter == char]
        