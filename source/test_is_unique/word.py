

class Word:

    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

    def is_unique(self) -> bool:
        memo = set()

        for symbol in self.text:
            if symbol in memo:
                return False
            memo.add(symbol)

        return True
