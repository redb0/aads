"""Модуль "заглушка" для тестов"""


class LinkedListItem:
    """Узел связного списка"""
    def __init__(self, data=None):
        raise NotImplementedError()

    @property
    def next_item(self):
        """Следующий элемент"""
        raise NotImplementedError()

    @next_item.setter
    def next_item(self, value):
        raise NotImplementedError()

    @property
    def previous_item(self):
        """Предыдущий элемент"""
        raise NotImplementedError()

    @previous_item.setter
    def previous_item(self, value):
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()


class LinkedList:
    """Связный список"""
    def __init__(self, first_item=None):
        raise NotImplementedError()

    @property
    def last(self):
        """Последний элемент"""
        raise NotImplementedError()

    def append_left(self, item):
        """Добавление слева"""
        raise NotImplementedError()

    def append_right(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def append(self, item):
        """Добавление справа"""
        raise NotImplementedError()

    def remove(self, item):
        """Удаление"""
        raise NotImplementedError()

    def insert(self, previous, item):
        """Вставка справа"""
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def __iter__(self):
        raise NotImplementedError()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __contains__(self, item):
        raise NotImplementedError()

    def __reversed__(self):
        raise NotImplementedError()
