"""Тесты для модуля dynamic_array"""

import unittest

import dynamic_array  # pylint: disable=E0401


TEST_LEN = [
    ('d', [], 0),
    ('d', [1.0], 1),
    ('d', [1.0, 1.0], 2),
    ('d', [1.0, 2.0], 2),
    ('d', [1.0, 9999.0, 3.0, 4.0, 1.0], 5),
    ('i', [], 0),
    ('i', [1], 1),
    ('i', [1, 1], 2),
    ('i', [1, 2], 2),
    ('i', [1, 9999, 3, 4, 1], 5),
]


TEST_APPEND = [
    ('d', [], 1, [1.0]),
    ('d', [1.0], 1, [1.0, 1.0]),
    ('d', [2.0], 1.0, [2.0, 1.0]),
    ('d', [2.0, 5.0], 1, [2.0, 5.0, 1.0]),
    ('i', [], 1, [1]),
    ('i', [1], 1, [1, 1]),
    ('i', [2], 1, [2, 1]),
    ('i', [2, 5], 1, [2, 5, 1]),
]


TEST_INSERT = [
    ('d', [], 0, 8, [8.0]),
    ('d', [1.0], 0, 8, [8.0, 1.0]),
    ('d', [2.0, 5.0], 1, 8, [2.0, 8.0, 5.0]),
    ('d', [2.0, 5.0], 2, 8, [2.0, 5.0, 8.0]),
    ('i', [], 0, 8, [8]),
    ('i', [1], 0, 8, [8, 1]),
    ('i', [2, 5], 1, 8, [2, 8, 5]),
    ('i', [2, 5], 2, 8, [2, 5, 8]),
]


TEST_REMOVE = [
    ('d', [1.0], 1.0, []),
    ('d', [2.0, 2.0, 2.0], 2.0, [2.0, 2.0]),
    ('d', [2.0, 5.0], 5.0, [2.0]),
    ('i', [1], 1, []),
    ('i', [2, 2, 2], 2, [2, 2]),
    ('i', [2, 5], 5, [2]),
]


TEST_POP = [
    ('d', [1.0], 0, 1.0, []),
    ('d', [2.0, 1.0, 6.0], 1, 1.0, [2.0, 6.0]),
    ('d', [2.0, 5.0], 1, 5.0, [2.0]),
    ('i', [1], 0, 1, []),
    ('i', [2, 1, 4], 1, 1, [2, 4]),
    ('i', [2, 5], 1, 5, [2]),
]


TEST_REVERSED = [
    ('d', [], []),
    ('d', [1.0], [1.0]),
    ('d', [2.0, 2.0, 2.0], [2.0, 2.0, 2.0]),
    ('d', [2.0, 5.0], [5.0, 2.0]),
    ('i', [], []),
    ('i', [1], [1]),
    ('i', [2, 2, 2], [2, 2, 2]),
    ('i', [2, 5], [5, 2]),
]


class TestArray(unittest.TestCase):
    """Тест-кейс модуля dynamic_array"""
    def test_len(self):
        """Тест метода len"""
        for typecode, data, expected in TEST_LEN:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                self.assertEqual(len(my_array), expected)

    def test_append(self):
        """Тест метода append"""
        for typecode, data, item, expected in TEST_APPEND:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                my_array.append(item)
                self.assertEqual(my_array, expected)

    def test_insert(self):
        """Тест метода insert"""
        for typecode, data, item, index, expected in TEST_INSERT:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                my_array.insert(index, item)
                self.assertEqual(my_array, expected)

    def test_remove(self):
        """Тест метода remove"""
        for typecode, data, item, expected in TEST_REMOVE:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                my_array.remove(item)
                self.assertEqual(my_array, expected)

    def test_pop(self):
        """Тест метода pop"""
        for typecode, data, index, expected_item, expected_array in TEST_POP:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                item = my_array.pop(index)
                self.assertEqual(item, expected_item)
                self.assertEqual(my_array, expected_array)

    def test_reversed(self):
        """Тест метода reversed"""
        for typecode, data, expected in TEST_REVERSED:
            with self.subTest():
                my_array = dynamic_array.Array(typecode, data)
                self.assertEqual(reversed(my_array), expected)
