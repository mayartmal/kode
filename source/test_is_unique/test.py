import unittest

from kode.source.test_is_unique.word import Word


class TestIsUnique(unittest.TestCase):

    def test__for_unique_chars__returns_True(self):
        word = Word('дом')

        result = word.is_unique()

        self.assertTrue(result)

    def test__for_repeated_chars__returns_False(self):
        word = Word('домофон')

        result = word.is_unique()

        self.assertFalse(result)
