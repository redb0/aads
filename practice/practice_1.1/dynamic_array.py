"""Шаблон реализации массива"""


class Array:
    """Массив"""
    def __init__(self, typecode, initializer):
        pass

    def append(self, item):  # pylint: disable=R0201
        """Добавление элемента"""
        raise NotADirectoryError()

    def insert(self, index, item):  # pylint: disable=R0201
        """Операция вставки"""
        raise NotADirectoryError()

    def remove(self, item):  # pylint: disable=R0201
        """Операция удаления"""
        raise NotADirectoryError()

    def pop(self, index):  # pylint: disable=R0201
        """Операция удаления с возвратом"""
        raise NotADirectoryError()

    def __reversed__(self):
        raise NotADirectoryError()

    def __len__(self):
        raise NotADirectoryError()

    def __sizeof__(self):
        raise NotADirectoryError()
