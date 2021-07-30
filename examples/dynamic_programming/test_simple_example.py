"""Тесты для модуля simple_example.py"""

import unittest
from .simple_example import my_len, my_max


LEN_TEST_DATA = [
    # пустые последовательности
    ([], 0),
    ('', 0),
    ((), 0),
    # последовательности из одного элемента
    ([8], 1),
    ('a', 1),
    # однородные последовательности
    ([1, 2, 3, 4, 5], 5),
    ('foo_bar', 7),
    ((1, 2, 3), 3),
    (['', '', ''], 3),
    # разнородные последовательности
    ([4, 'r', '7', [], 'dgdfg'], 5),
    ([[5, 8, 'fs'], 9], 2),
]

MAX_TEST_DATA = [
    # пустые последовательности
    ([], None),
    ((), None),
    # последовательности из одного элемента
    ([6], 6),
    ((7, ), 7),
    # максимум первый в последовательности
    ([9, 2, 4], 9),
    ((5, 3, 4, 1), 5),
    # максимум последний в последовательности
    ([1, 2, 6], 6),
    ((3, 7), 7),
    # несколько максимальных элементов
    ([5, 5, 5], 5),
    ((3, 7, 3, 7, 3, 7), 7),
    # с отрицательными числами
    ([-1, 0, -3], 0),
    ((-5, -1, -200, -4), -1),
]


class TestMyLen(unittest.TestCase):
    def test_my_len(self):
        for data, expected in LEN_TEST_DATA:
            with self.subTest():
                self.assertEqual(my_len(data), expected)


class TestMyMax(unittest.TestCase):
    def test_my_max(self):
        for data, expected in MAX_TEST_DATA:
            with self.subTest():
                self.assertEqual(my_max(data), expected)


if __name__ == '__main__':
    unittest.main()
