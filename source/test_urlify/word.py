

class Word:

    def __init__(self, text: str):
        self.__text = text

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return '"{}"'.format(self.text)

    def __eq__(self, other):
        return bool(self.text == other.text)

    def with_replaced_whitespaces(self):
        result_str = ''
        replaced_sequence = '%20'
        is_previous_symbol_space = False

        for symbol in self.text:
            if symbol == ' ':
                if is_previous_symbol_space:
                    continue
                result_str += replaced_sequence
                continue
            result_str += symbol

        return Word(result_str)
