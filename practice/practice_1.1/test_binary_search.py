"""Тесты для модуля binary_search"""

import unittest

import binary_search  # pylint: disable=E0401


TEST_DATA = [
    ([42], 42, 0),
    ([1, 2, 3], 2, 1),
    ([1, 2, 3], 1, 0),
    ([1, 2, 3], 3, 2),
    ([0, 0, 1, 4, 4, 10], 0, 0),
    ([0, 0, 1, 4, 4, 10], 4, 3),
    ([0, 0, 1, 4, 4, 10], 10, 5),
    (['c'], 'c', 0),
    ('c', 'c', 0),
    (['a', 'b', 'c', 'd'], 'a', 0),
    (['a', 'b', 'c', 'd'], 'd', 3),
    ('abcd', 'a', 0),
    ('abcd', 'd', 3),
    ([], 42, None),
    ([0], 42, None),
    ([1, 2, 3], 4, None),
    ([0, 0, 0, 0], 4, None),
    ('', 'a', None),
]


class TestBinarySearch(unittest.TestCase):
    """Тест-кейс модуля binary_search"""
    def test_binary_search(self):
        """Тест функции search"""
        for iterable_obj, item, expected in TEST_DATA:
            with self.subTest():
                self.assertEqual(binary_search.search(iterable_obj, item), expected)
