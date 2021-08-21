"""Тесты для модуля dragon_curve.py"""

import unittest
from dragon_curve import dragon_curve

TEST_DRAGON_CURVE = [
    # Первая итерация
    ('fx', 'fx+yf+'),
    # Вторая итерации
    ('fx+yf+', 'fx+yf++-fx-yf+'),
    # Третья итерации
    ('fx+yf++-fx-yf+', 'fx+yf++-fx-yf++-fx+yf+--fx-yf+')
]


class TestDragonCurve(unittest.TestCase):

    def test_dragon_curve(self):
        for data, expected in TEST_DRAGON_CURVE:
            with self.subTest():
                self.assertEqual(dragon_curve(data), expected)


if __name__ == '__main__':
    unittest.main()
