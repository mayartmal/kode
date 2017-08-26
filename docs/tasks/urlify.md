Замена пробела специальным символом
=================


### Условие задачи

Дана сторка с пробелами.
Замеменить символом %20 все пробелы, 
которые следуют по одному или друг за другом.


### Решение

Напишем алгоритм.

    Для всех символов в строке {
        Читаем тикущий символ
        Это пробел? {
            Уже был пробел? {
                Переходим к следующему символу
            }
            Копируем %20 в результирующую строку
            Переходим к следующему символу
        }
        Копируем текущий символ в результирующую строку
    }

### Тесты

Напишем тесты на несколько основных случаев.

```python
class TestWithReplacedWhitespaces(unittest.TestCase):

    def test__one_whitespace__returns_one_replaced_sequence(self):
        """
            Заменим одиночный пробел одним символом %20 
        """
        expected = Word('%20')
        word = Word(' ')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__one_symbol_between_whitespaces__returns_one_symbol_between_replaced_sequence(self):
        """
            Заменим два пробела по краям строки одним символом %20 
        """
        expected = Word('%20X%20')
        word = Word(' X ')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__one_whitespace_between_symbols__returns_one_replaced_sequence_between_symbols(self):
        """
            Заменим один пробел между символами 
        """
        expected = Word('X%20X')
        word = Word('X X')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__space_after_space__returns_replaced_sequence_after_replaced_sequencce(self):
        """
            Заменим несколько пробелов, следующих друг за другом 
        """
        expected = Word('X%20%20X')
        word = Word('X  X')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)
```


Напишем код класса Word

```python



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


```
