"""Тесты для модуля search"""

import unittest

import search  # pylint: disable=E0401


TEST_SEARCH_ONE_SYMBOL = [
    ('', 'a', False, 'first', 1, None),
    ('', 'a', True, 'first', 1, None),
    ('', 'a', False, 'last', 1, None),
    ('', 'a', True, 'last', 1, None),

    ('a', 'a', False, 'first', 1, (0, )),
    ('a', 'a', True, 'first', 1, (0, )),
    ('a', 'a', False, 'last', 1, (0, )),
    ('a', 'a', True, 'last', 1, (0, )),

    ('aaa', 'a', False, 'first', 3, (0, 1, 2)),
    ('aaa', 'a', True, 'first', 3, (0, 1, 2)),
    ('aaa', 'a', False, 'last', 3, (2, 1, 0)),
    ('aaa', 'a', True, 'last', 3, (2, 1, 0)),

    ('bca', 'c', False, 'first', 1, (1, )),
    ('bca', 'c', True, 'first', 1, (1, )),
    ('bca', 'c', False, 'last', 1, (1, )),
    ('bca', 'c', True, 'last', 1, (1, )),

    ('aaa', 'a', False, 'first', 2, (0, 1)),
    ('aaa', 'a', True, 'first', 1, (0, )),
    ('aaa', 'a', False, 'last', 2, (2, 1)),
    ('aaa', 'a', True, 'last', 10, (2, 1, 0)),
]

TEST_SEARCH_MANY_SYMBOL = [
    ('', 'abc', False, 'first', 1, None),
    ('', 'abc', True, 'first', 1, None),
    ('', 'abc', False, 'last', 1, None),
    ('', 'abc', True, 'last', 1, None),

    ('a', 'abc', False, 'first', 1, None),
    ('a', 'abc', True, 'first', 1, None),
    ('a', 'abc', False, 'last', 1, None),
    ('a', 'abc', True, 'last', 1, None),

    ('abc', 'abc', False, 'first', 1, (0, )),
    ('abc', 'abc', True, 'first', 1, (0, )),
    ('abc', 'abc', False, 'last', 1, (0, )),
    ('abc', 'abc', True, 'last', 1, (0, )),

    ('abcabc', 'abc', False, 'first', 2, (0, 3)),
    ('abcabc', 'abc', True, 'first', 2, (0, 3)),
    ('abcabc', 'abc', False, 'last', 2, (3, 0)),
    ('abcabc', 'abc', True, 'last', 2, (3, 0)),

    ('aabcbccaabc', 'abc', False, 'first', 2, (1, 8)),
    ('aabcbccaabc', 'abc', True, 'first', 2, (1, 8)),
    ('aAbCbccaabc', 'AbC', False, 'first', 2, (1, 8)),
    ('aabcbccaAbC', 'AbC', True, 'first', 1, (8, )),
    ('aabcbccaabc', 'abc', False, 'last', 2, (8, 1)),
    ('aabcbccaabc', 'abc', True, 'last', 2, (8, 1)),
    ('aAbCbccaabc', 'AbC', False, 'last', 2, (8, 1)),
    ('aabcbccaAbC', 'AbC', True, 'last', 1, (8, )),

    ('abcabc', 'abc', False, 'first', 1, (0, )),
    ('abcabcabc', 'abc', True, 'first', 2, (0, 3)),
    ('abcabc', 'abc', False, 'last', 9, (3, 0)),
    ('abcabc', 'abc', True, 'last', 2, (3, 0)),
]

TEST_SEARCH_FEW_SUBSTR = [
    ('', ('abc', 'a'), False, 'first', 1, None),
    ('', ('abc', 'a'), True, 'first', 1, None),
    ('', ('abc', 'a'), False, 'last', 1, None),
    ('', ('abc', 'a'), True, 'last', 1, None),

    ('a', ('abc', 'a'), False, 'first', 1, {'abc': None, 'a': (0, )}),
    ('a', ('abc', 'a'), True, 'first', 1, {'abc': None, 'a': (0, )}),
    ('a', ('abc', 'a'), False, 'last', 1, {'abc': None, 'a': (0, )}),
    ('a', ('abc', 'a'), True, 'last', 1, {'abc': None, 'a': (0, )}),

    ('ababbababa', ('aba', 'bba'), False, 'first', 4, {'aba': (0, 5, 7), 'bba': (3, )}),
    ('ababbababa', ('aba', 'bba'), True, 'first', 4, {'aba': (0, 5, 7), 'bba': (3, )}),
    ('ababbababa', ('aba', 'bba'), False, 'last', 4, {'aba': (7, 5, 0), 'bba': (3, )}),
    ('ababbababa', ('aba', 'bba'), True, 'last', 4, {'aba': (7, 5, 0), 'bba': (3, )}),

    ('ababbababa', ('aba', 'bba'), False, 'first', 3, {'aba': (0, 5), 'bba': (3, )}),
    ('ababbababa', ('aba', 'bba'), True, 'first', 2, {'aba': (0, ), 'bba': (3, )}),
    ('ababbababa', ('aba', 'bba'), False, 'last', 1, {'aba': (7, ), 'bba': None}),
    ('ababbababa', ('aba', 'bba'), True, 'last', 10, {'aba': (7, 5, 0), 'bba': (3, )}),
]


class TestSearch(unittest.TestCase):
    """Тест-кейс модуля search"""
    def test_binary_search_one_symbol(self):
        """Тест функции search для поиска строки из одного символа"""
        for string, sub_string, case_sensitivity, method, count, expected in TEST_SEARCH_ONE_SYMBOL:
            with self.subTest():
                self.assertEqual(
                    search.search(
                        string, sub_string, case_sensitivity, method, count
                    ),
                    expected
                )

    def test_binary_search_many_symbol(self):
        """Тест функции search для поиска строки из нескольких символов"""
        for string, sub_string, case_sensitivity, method, count, expected in TEST_SEARCH_MANY_SYMBOL:
            with self.subTest():
                self.assertEqual(
                    search.search(
                        string, sub_string, case_sensitivity, method, count
                    ),
                    expected
                )

    def test_binary_search_few_substr(self):
        """Тест поиска нескольких подстрок"""
        for string, sub_string, case_sensitivity, method, count, expected in TEST_SEARCH_FEW_SUBSTR:
            with self.subTest():
                self.assertEqual(
                    search.search(
                        string, sub_string, case_sensitivity, method, count
                    ),
                    expected
                )
                