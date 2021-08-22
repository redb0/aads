"""Тесты модуля ferma.py"""

import unittest
from ferma import ferma  # pylint: disable=E0401


TEST_DATA = [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (199, True),
    (200, False),
    (3571, True),
    (410041, False),
    (1207252621, False),
]


class TestFerma(unittest.TestCase):
    """Тест-кейс функции ferma"""
    def test_ferma(self):  # pylint: disable=C0116
        for data, expected in TEST_DATA:
            with self.subTest():
                self.assertEqual(ferma(data), expected)


if __name__ == '__main__':
    unittest.main()
