"""Тесты для модуля dynamic_array"""

import unittest
import array

import dynamic_array


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
    ('d', [], 1, array.array('d', [1.0])),
    ('d', [1.0], 1, array.array('d', [1.0, 1.0])),
    ('d', [2.0], 1.0, array.array('d', [2.0, 1.0])),
    ('d', [2.0, 5.0], 1, array.array('d', [2.0, 5.0, 1.0])),
    ('i', [], 1, array.array('i', [1])),
    ('i', [1], 1, array.array('i', [1, 1])),
    ('i', [2], 1, array.array('i', [2, 1])),
    ('i', [2, 5], 1, array.array('i', [2, 5, 1])),
]


TEST_INSERT = [
    ('d', [], 0, 8, array.array('d', [8.0])),
    ('d', [1.0], 0, 8, array.array('d', [8.0, 1.0])),
    ('d', [2.0, 5.0], 1, 8, array.array('d', [2.0, 8.0, 5.0])),
    ('d', [2.0, 5.0], 2, 8, array.array('d', [2.0, 5.0, 8.0])),
    ('d', [2.0, 5.0], 10, 8, array.array('d', [2.0, 5.0, 8.0])),
    ('d', [2.0, 5.0], -1, 8, array.array('d', [2.0, 8.0, 5.0])),
    ('d', [2.0, 5.0], -2, 8, array.array('d', [8.0, 2.0, 5.0])),
    ('d', [2.0, 5.0], -10, 8, array.array('d', [8.0, 2.0, 5.0])),
    ('i', [], 0, 8, array.array('i', [8])),
    ('i', [1], 0, 8, array.array('i', [8, 1])),
    ('i', [2, 5], 1, 8, array.array('i', [2, 8, 5])),
    ('i', [2, 5], 2, 8, array.array('i', [2, 5, 8])),
    ('i', [4, 4], 10, 8, array.array('i', [4, 4, 8])),
    ('i', [4, 4, 1], -1, 8, array.array('i', [4, 4, 8, 1])),
    ('i', [4, 4, 1], -3, 8, array.array('i', [8, 4, 4, 1])),
    ('i', [4, 1], -10, 8, array.array('i', [8, 4, 1])),
]


TEST_REMOVE = [
    ('d', [1.0], 1.0, array.array('d', [])),
    ('d', [2.0, 2.0, 2.0], 2.0, array.array('d', [2.0, 2.0])),
    ('d', [2.0, 5.0], 5.0, array.array('d', [2.0])),
    ('i', [1], 1, array.array('i', [])),
    ('i', [2, 2, 2], 2, array.array('i', [2, 2])),
    ('i', [2, 5], 5, array.array('i', [2])),
]


TEST_POP = [
    ('d', [1.0], 0, 1.0, array.array('d', [])),
    ('d', [2.0, 1.0, 6.0], 1, 1.0, array.array('d', [2.0, 6.0])),
    ('d', [2.0, 5.0], 1, 5.0, array.array('d', [2.0])),
    ('d', [2.0, 5.0], -1, 5.0, array.array('d', [2.0])),
    ('d', [2.0, 5.0], -2, 2.0, array.array('d', [5.0])),
    ('i', [1], 0, 1, array.array('i', [])),
    ('i', [2, 1, 4], 1, 1, array.array('i', [2, 4])),
    ('i', [2, 5], 1, 5, array.array('i', [2])),
    ('i', [2, 5], -1, 5, array.array('i', [2])),
    ('i', [2, 5], -2, 2, array.array('i', [5])),
]


TEST_POP_INDEX_ERROR = [
    ('d', [], 1),
    ('d', [10.0], 5),
    ('d', [2.0], -2),
    ('i', [], 1),
    ('i', [3, 1], 5),
    ('i', [4], -2),
]


TEST_REVERSED = [
    ('d', [], array.array('d', [])),
    ('d', [1.0], array.array('d', [1.0])),
    ('d', [2.0, 2.0, 2.0], array.array('d', [2.0, 2.0, 2.0])),
    ('d', [2.0, 5.0], array.array('d', [5.0, 2.0])),
    ('i', [], array.array('i', [])),
    ('i', [1], array.array('i', [1])),
    ('i', [2, 2, 2], array.array('i', [2, 2, 2])),
    ('i', [2, 5], array.array('i', [5, 2])),
]


TEST_EQ = [
    ('d', [], array.array('d', [])),
    ('d', [1.0], array.array('d', [1.0])),
    ('d', [2.0, 2.0, 2.0], array.array('d', [2.0, 2.0, 2.0])),
    ('d', [2.0, 5.0], array.array('d', [2.0, 5.0])),
    ('i', [], array.array('i', [])),
    ('i', [1], array.array('i', [1])),
    ('i', [2, 2, 2], array.array('i', [2, 2, 2])),
    ('i', [2, 5], array.array('i', [2, 5])),
]


class TestArray(unittest.TestCase):
    """Тест-кейс модуля dynamic_array"""
    def test_len(self):
        """Тест метода len"""
        for typecode, data, expected in TEST_LEN:
            with self.subTest(typecode=typecode, data=data, expected=expected):
                test_array = dynamic_array.Array(typecode, data)
                self.assertEqual(len(test_array), expected)

    def test_append(self):
        """Тест метода append"""
        for typecode, data, item, expected in TEST_APPEND:
            with self.subTest(typecode=typecode, data=data,
                              item=item, expected=expected):
                test_array = dynamic_array.Array(typecode, data)
                test_array.append(item)
                self.assertEqual(len(test_array), len(expected))
                for i, expected_item in enumerate(expected):
                    array_item = test_array[i]
                    if typecode == 'd':
                        self.assertTrue(isinstance(array_item, float))
                    elif typecode == 'i':
                        self.assertTrue(isinstance(array_item, int))
                    self.assertEqual(array_item, expected_item)

    def test_insert(self):
        """Тест метода insert"""
        for typecode, data, index, item, expected in TEST_INSERT:
            with self.subTest(typecode=typecode, data=data, index=index,
                              item=item, expected=expected):
                test_array = dynamic_array.Array(typecode, data)
                test_array.insert(index, item)
                self.assertEqual(len(test_array), len(expected))
                for i, expected_item in enumerate(expected):
                    array_item = test_array[i]
                    if typecode == 'd':
                        self.assertTrue(isinstance(array_item, float))
                    elif typecode == 'i':
                        self.assertTrue(isinstance(array_item, int))
                    self.assertEqual(array_item, expected_item)

    def test_remove(self):
        """Тест метода remove"""
        for typecode, data, item, expected in TEST_REMOVE:
            with self.subTest(typecode=typecode, data=data,
                              item=item, expected=expected):
                test_array = dynamic_array.Array(typecode, data)
                test_array.remove(item)
                self.assertEqual(len(test_array), len(expected))
                for i, expected_item in enumerate(expected):
                    array_item = test_array[i]
                    if typecode == 'd':
                        self.assertTrue(isinstance(array_item, float))
                    elif typecode == 'i':
                        self.assertTrue(isinstance(array_item, int))
                    self.assertEqual(array_item, expected_item)

    def test_pop(self):
        """Тест метода pop"""
        for typecode, data, index, expected_item, expected_array in TEST_POP:
            with self.subTest(typecode=typecode, data=data, index=index,
                              expected_item=expected_item,
                              expected_array=expected_array):
                test_array = dynamic_array.Array(typecode, data)
                item = test_array.pop(index)
                self.assertEqual(item, expected_item)
                self.assertEqual(len(test_array), len(expected_array))
                for i, ex_item in enumerate(expected_array):
                    array_item = test_array[i]
                    if typecode == 'd':
                        self.assertTrue(isinstance(array_item, float))
                    elif typecode == 'i':
                        self.assertTrue(isinstance(array_item, int))
                    self.assertEqual(array_item, ex_item)

    def test_pop_failed(self):
        """Тест метода pop с исключением IndexError"""
        for typecode, data, index in TEST_POP_INDEX_ERROR:
            with self.subTest(typecode=typecode, data=data, index=index):
                test_array = dynamic_array.Array(typecode, data)
                with self.assertRaises(IndexError):
                    test_array.pop(index)

    def test_reversed(self):
        """Тест метода reversed"""
        for typecode, data, expected in TEST_REVERSED:
            with self.subTest(typecode=typecode, data=data, expected=expected):
                test_array = dynamic_array.Array(typecode, data)
                reversed_array = list(reversed(test_array))
                for i, expected_item in enumerate(expected):
                    array_item = reversed_array[i]
                    if typecode == 'd':
                        self.assertTrue(isinstance(array_item, float))
                    elif typecode == 'i':
                        self.assertTrue(isinstance(array_item, int))
                    self.assertEqual(array_item, expected_item)

    def test_eq(self):
        """Тест сравнения с array.array"""
        for typecode, data, expected in TEST_EQ:
            with self.subTest(typecode=typecode, data=data, expected=expected):
                my_array = dynamic_array.Array(typecode, data)
                self.assertEqual(my_array, expected)
