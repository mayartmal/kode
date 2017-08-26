import unittest

from kode.source.test_check_permutation.word import Word


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
