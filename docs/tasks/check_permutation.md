Перестановки
=================


### Условие задачи

Даны две сторки.
Определить является ли первая строка перестановкой второй строки.


### Примеры

Напишем несколько примеров таких строк.

Первая строка  | Вторая строка | Результат
:-------------:|:-------------:|:------------:
лось           | соль          |  True
лось           | лось          |  False
лось           | лось2         |  False
               |               |  False
медвед         | лось          |  False
лось           | лоська        |  False


### Решение

В каком случает строка 2 является перестановкой строки 1?
    
    1. Если длины строк совпадают
    2. В строке 2 есть все символы строки 1.

В каком случае строка 2 не является перестановкой строки 1?

    1. Если длины строк не совпадают
    2. Строки абсолютно равны.
    3. Если в строке 1 есть хотя бы один символ, которого нет в строке 2.


### Тесты

Напишем тесты на несколько основных случаев.

```python
class TestIsPermutation(unittest.TestCase):

    def test__mixed_strings__returns_True(self):
        """
            Вторая строка является перестановкой первой строки
        """
        word_1 = Word('лось')
        word_2 = Word('соль')

        result = word_1.is_permutation(word_2)

        self.assertTrue(result)

    def test__equal_strings__returns_False(self):
        """
            Две равные строки не являются перестановками 
        """
        word_1 = Word('лось')
        word_2 = Word('лось')

        result = word_1.is_permutation(word_2)

        self.assertFalse(result)

    def test__not_equal_lengths_strings__returns_False(self):
        """
            Строки разной длины не являютсся перестановками
        """
        word_1 = Word('лось')
        word_2 = Word('лось2')

        result = word_1.is_permutation(word_2)

        self.assertFalse(result)

    def test__empty_strings__returns_False(self):
        """
            Две пустые строки не являются перестановками 
        """
        word_1 = Word('')
        word_2 = Word('')

        result = word_1.is_permutation(word_2)

        self.assertFalse(result)

    def test__different_strings__returns_False(self):
        """
            Строки с разными символами не являются перестановками 
        """
        word_1 = Word('медвед')
        word_2 = Word('лось')

        result = word_1.is_permutation(word_2)

        self.assertFalse(result)

    def test__same_strings__returns_False(self):
        """
            Строки, которые частично совпадают  
        """
        word_1 = Word('лось')
        word_2 = Word('лоська')

        result = word_1.is_permutation(word_2)

        self.assertFalse(result)

```

Напишем тесты для определения того, что строки являются отличными друг от друга

```python
class TestIsDifferentFrom(unittest.TestCase):

    def test__equal_strings__returns_False(self):
        """
            Строки не отличаются  
        """
        word_1 = Word('лось')
        word_2 = Word('лось')

        result = word_1.is_different_from(word_2)

        self.assertFalse(result)

    def test__not_equal_strings__returns_True(self):
        """
            Строки отличаются  
        """
        word_1 = Word('лось')
        word_2 = Word('лоська')

        result = word_1.is_different_from(word_2)

        self.assertTrue(result)

```

### Код

Напишем код класса Word. Метод is_permutation  использует сторожевые условия для того, чтобы сразу вернуть результат.

```python
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

```
