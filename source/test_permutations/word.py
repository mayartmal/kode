

class Word:

    def __init__(self, text: str):
        self.__text = text

    def __str__(self):
        return self.__text

    def is_permutation(self, word) -> bool:
        if not str(self) or not str(word):
            return False

        if len(str(self)) != len(str(word)):
            return False

        if str(self) == str(word):
            return False

        if self.is_different_from(word):
            return False

        if word.is_different_from(self):
            return False

        return True

    def is_different_from(self, word):
        for symbol in str(word):
            if symbol not in str(self):
                return True
        return False
