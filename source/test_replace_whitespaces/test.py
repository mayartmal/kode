import unittest

from kode.source.test_replace_whitespaces.word import Word


class TestWithReplacedWhitespaces(unittest.TestCase):

    def test__one_whitespace__returns_one_replaced_sequence(self):
        expected = Word('%20')
        word = Word(' ')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__one_symbol_between_whitespaces__returns_one_symbol_between_replaced_sequence(self):
        expected = Word('%20X%20')
        word = Word(' X ')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__one_whitespace_between_symbols__returns_one_replaced_sequence_between_symbols(self):
        expected = Word('X%20X')
        word = Word('X X')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)

    def test__space_after_space__returns_replaced_sequence_after_replaced_sequencce(self):
        expected = Word('X%20%20X')
        word = Word('X  X')

        result = word.with_replaced_whitespaces()

        self.assertEquals(expected, result)
