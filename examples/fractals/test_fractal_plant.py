"""Тесты для модуля fractal_plant.py"""

import unittest
from fractal_plant import fractal_plant  # pylint: disable=E0401

TEST_FRACTAL_PLANT = [
    # Первая итерация
    ('x', 'f+[[x]-x]-f[-fx]+x'),
    # Вторая итерации
    ('f+[[x]-x]-f[-fx]+x', 'ff+[[f+[[x]-x]-f[-fx]+x]-f+[[x]-x]-f[-fx]+x]-ff[-fff+[[x]-x]-f[-fx]+x]+f+[[x]-x]-f[-fx]+x'),
    # Проверка правил
    ('f+-[]x', 'ff+-[]f+[[x]-x]-f[-fx]+x')
]


class TestFractalPlant(unittest.TestCase):
    """Тест-кейс функции fractal_plant"""
    def test_fractal_plant(self):  # pylint: disable=C0116
        for data, expected in TEST_FRACTAL_PLANT:
            with self.subTest():
                self.assertEqual(fractal_plant(data), expected)


if __name__ == '__main__':
    unittest.main()