Дубликаты символов
=================


### Условие задачи

Дана сторка.
Определить все ли символы встречаются в строке 1 раз.


### Примеры

Напишем несколько примеров таких строк.

Первая строка  | Результат
:-------------:|:------------:
дом            |  True
домофон        |  False


### Тесты

Напишем тесты на несколько основных случаев.

```python
class TestIsUnique(unittest.TestCase):

    def test__for_unique_chars__returns_True(self):
        word = Word('дом')

        result = word.is_unique()

        self.assertTrue(result)

    def test__for_repeated_chars__returns_False(self):
        word = Word('домофон')

        result = word.is_unique()

        self.assertFalse(result)

```


### Код

Напишем код класса Word. Одно из решений с использованием структуры данных "Множество"

```python
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

```
