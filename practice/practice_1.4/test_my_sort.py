"""Тесты для модуля my_sort"""

import unittest

import my_sort  # pylint: disable=E0401


TEST_NUMBER = [
    [],
    [1],
    [1, 2, 3, 4, 5],
    [0, 0, 0, 55, 55, 60],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [8, 0, 42, 3, 4, 8, 0, 45, 50, 9999, 7],
    [-5, 0, 9, -999, 874, 35, -4, -5, 0],
    [1, 1, 1],
]


TEST_STR = [
    [],
    ['a'],
    ['a', 'b', 'c', 'd', 'e'],
    ['aa', 'aa', 'aa', 'ab', 'ac', 'b'],
    ['e', 'd', 'c', 'b', 'a'],
    ['abc', 'a', 'foo', 'bar', 'booz', 'baz', 'spam', 'love'],
    ['abc', 'abc', 'abc'],
    [''],
]


class TestSort(unittest.TestCase):
    """Тест-кейс модуля my_sort"""
    def test_sort_number_increase(self):
        """Тест функции сортировки числовых данных по возрастанию"""
        for data in TEST_NUMBER:
            with self.subTest():
                self.assertEqual(my_sort.my_sort(data), sorted(data))

    def test_sort_number_decrease(self):
        """Тест функции сортировки числовых данных по невозрастанию"""
        for data in TEST_NUMBER:
            with self.subTest():
                self.assertEqual(
                    my_sort.my_sort(data, reverse=True),
                    sorted(data, reverse=True)
                )

    def test_sort_str_increase(self):
        """Тест функции сортировки строковых данных по возрастанию"""
        for data in TEST_STR:
            with self.subTest():
                self.assertEqual(my_sort.my_sort(data), sorted(data))

    def test_sort_str_decrease(self):
        """Тест функции сортировки строковых данных по невозрастанию"""
        for data in TEST_STR:
            with self.subTest():
                self.assertEqual(
                    my_sort.my_sort(data, reverse=True),
                    sorted(data, reverse=True)
                )
