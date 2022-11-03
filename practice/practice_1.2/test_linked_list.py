"""Тесты модуля linked_list"""

import unittest

from linked_list import LinkedListItem, LinkedList  # pylint: disable=E0401


TEST_LEN = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
]

TEST_LAST = TEST_LEN

TEST_REMOVE = [
    ([1], 1),
    ([1, 1, 1], 1),
    ([2, 1, 1, 3], 1),
    ([2, 3, 4], 2),
    ([2, 3, 4], 4),
]

TEST_REMOVE_FAILED = [
    ([], 1),
    ([1], 2),
    ([1, 1, 1, 3, 4], 2),
]

TEST_CONTAINS = [
    ([], 1, False),
    ([1], 1, True),
    ([1], 2, False),
    ([1, 1, 1], 1, True),
    ([2, 3], 5, False),
    ([2, 3], 3, True),
]

TEST_GETITEM = [
    ([2], 0),
    ([4], -1),
    ([5, 1], 1),
    ([5, 1], -2),
    ([2, 0, 1, 4, 2], 2),
]

TEST_GETITEM_FAILED = [
    ([], 0),
    ([1], 1),
    ([1], -2),
    ([1, 2, 3], 3),
    ([1, 2, 4], -4),
]

TEST_INSERT = [
    # (create_linked_list([]), 0, 42),
    ([1], 0, 42),
    # (create_linked_list([2]), 1, 42),
    ([1, 2, 3], 1, 42),
    ([1, 2, 3], 0, 42),
]


def create_linked_list(nodes_list):
    """Создание связного списка"""
    first = previous = None
    for item in nodes_list:
        node = LinkedListItem(item)
        if previous:
            previous.next_item = node
        elif not first:
            first = node
        previous = node
    if previous:
        previous.next_item = first
    return LinkedList(first)


class TestLinkedListItem(unittest.TestCase):
    """Тест-кейс класса LinkedListItem"""
    def test_next_item(self):
        """Тест соединения узлов через next_item"""
        node_a = LinkedListItem(42)
        node_b = LinkedListItem(196)
        node_a.next_item = node_b
        self.assertTrue(node_a.next_item is node_b)
        self.assertTrue(node_a.previous_item is None)
        self.assertTrue(node_b.next_item is None)
        self.assertTrue(node_b.previous_item is node_a)

    def test_previous_item(self):
        """Тест соединения узлов через previous_item"""
        node_a = LinkedListItem(42)
        node_b = LinkedListItem(196)
        node_b.previous_item = node_a
        self.assertTrue(node_a.next_item is node_b)
        self.assertTrue(node_a.previous_item is None)
        self.assertTrue(node_b.next_item is None)
        self.assertTrue(node_b.previous_item is node_a)


class TestLinkedList(unittest.TestCase):
    """Тест-кейс класса LinkedList"""
    def test_len(self):
        """Тест метода len"""
        for expected_len in TEST_LEN:
            first = None
            previous = None
            for i in range(expected_len):
                node = LinkedListItem(i)
                if previous:
                    previous.next_item = node
                previous = node
                if i == 0:
                    first = node
            if previous and first:
                previous.next_item = first
            linked_list = LinkedList(first)
            with self.subTest(expected_len=expected_len):
                self.assertEqual(len(linked_list), expected_len)

    def test_last(self):
        """Тест свойства last"""
        for expected_len in TEST_LAST:
            first = None
            previous = None
            last = None
            for i in range(expected_len):
                node = LinkedListItem(i)
                if previous:
                    previous.next_item = node
                previous = node
                if i == 0:
                    first = node
                if i == expected_len - 1:
                    last = node
            if previous and first:
                previous.next_item = first
            with self.subTest(expected_len=expected_len):
                if expected_len != 0:
                    last.next_item = first
                linked_list = LinkedList(first)
                self.assertEqual(linked_list.last, last)

    def test_append_left(self):
        """Тест метода append_left"""
        for expected_len in TEST_LAST:
            first = previous = None
            for i in range(expected_len):
                node = LinkedListItem(i)
                if previous:
                    previous.next_item = node
                previous = node
                if i == 0:
                    first = node
            if previous and first:
                previous.next_item = first
            linked_list = LinkedList(first)
            with self.subTest(expected_len=expected_len):
                last_first = linked_list.first_item
                linked_list.append_left(42)
                first_item = linked_list.first_item  # pylint: disable=E1101
                self.assertTrue(first_item is not last_first)
                if expected_len == 0:
                    self.assertTrue(first_item.next_item is first_item)
                else:
                    self.assertTrue(first.previous_item is first_item)
                    self.assertTrue(first_item.next_item is first)
                self.assertEqual(len(linked_list), expected_len + 1)

    def test_append_right(self):
        """Тест метода append_right"""
        for expected_len in TEST_LAST:
            first = None
            previous = None
            for i in range(expected_len):
                node = LinkedListItem(i)
                if previous:
                    previous.next_item = node
                previous = node
                if i == 0:
                    first = node
            if previous and first:
                previous.next_item = first
            linked_list = LinkedList(first)
            with self.subTest(expected_len=expected_len):
                linked_list.append_right(42)
                appended_item = linked_list.last
                if expected_len == 0:
                    self.assertTrue(appended_item.data == 42)
                    self.assertTrue(appended_item.next_item is appended_item)
                else:
                    self.assertTrue(first.previous_item is appended_item)
                    self.assertTrue(appended_item.next_item is first)
                self.assertEqual(len(linked_list), expected_len + 1)

    def test_append(self):
        """Тест метода append"""
        for expected_len in TEST_LAST:
            first = None
            previous = None
            for i in range(expected_len):
                node = LinkedListItem(i)
                if previous:
                    previous.next_item = node
                previous = node
                if i == 0:
                    first = node
            if previous and first:
                previous.next_item = first
            linked_list = LinkedList(first)
            with self.subTest(expected_len=expected_len):
                linked_list.append(42)
                appended_item = linked_list.last
                if expected_len == 0:
                    self.assertTrue(appended_item.data == 42)
                    self.assertTrue(appended_item.next_item is appended_item)
                else:
                    self.assertTrue(first.previous_item is appended_item)
                    self.assertTrue(appended_item.next_item is first)
                self.assertEqual(len(linked_list), expected_len + 1)

    def test_remove(self):
        """Тест метода remove"""
        for node_list, remove_item in TEST_REMOVE:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, remove_item=remove_item):
                linked_list.remove(remove_item)
                self.assertEqual(len(linked_list), len(node_list) - 1)

    def test_remove_failed(self):
        """Тест метода remove с исключением ValueError"""
        for node_list, remove_item in TEST_REMOVE_FAILED:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, remove_item=remove_item):
                with self.assertRaises(ValueError):
                    linked_list.remove(remove_item)

    def test_insert(self):
        """Тест метода insert"""
        for node_list, index, data in TEST_INSERT:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, index=index,
                              data=data):
                linked_list.insert(linked_list[index], data)
                self.assertEqual(len(linked_list), len(node_list) + 1)
                node_list.insert(index + 1, data)
                self.assertEqual([i.data for i in linked_list], node_list)

    def test_getitem(self):
        """Тест индексации"""
        for node_list, index in TEST_GETITEM:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, index=index):
                item = linked_list[index]
                self.assertEqual(item, node_list[index])

    def test_getitem_failed(self):
        """Тест индексации с исключением IndexError"""
        for node_list, index in TEST_GETITEM_FAILED:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, index=index):
                with self.assertRaises(IndexError):
                    _ = linked_list[index]

    def test_contains(self):
        """Тест поддержки оператора in"""
        for node_list, item, expected in TEST_CONTAINS:
            linked_list = create_linked_list(node_list)
            with self.subTest(node_list=node_list, item=item, expected=expected):
                self.assertTrue((item in linked_list) is expected)

    def test_reversed(self):
        """Тест поддержки функции reversed"""
        for i in TEST_LEN:
            linked_list = create_linked_list(list(range(i)))
            with self.subTest(node_list=list(range(i))):
                self.assertEqual(
                    [item for item in reversed(linked_list)],
                    list(range(i - 1, -1, -1))
                )
