"""Модуль "заглушка" для тестов"""


from array import array


class Array:
    """Массив"""
    def __init__(self, typecode, initializer):
        self.typecode = typecode
        self.my_array = initializer

    def append(self, item):
        """Добавление элемента"""
        if self.typecode == 'd':
            self.my_array.append(float(item))
        else:
            self.my_array.append(int(item))

    def insert(self, index, item):
        """Операция вставки"""
        if self.typecode == 'd':
            self.my_array.insert(index, float(item))
        else:
            self.my_array.insert(index, int(item))

    def remove(self, item):
        """Операция удаления"""
        self.my_array.remove(item)

    def pop(self, index):
        """Операция удаления с возвратом"""
        return self.my_array.pop(index)

    def __getitem__(self, index):
        return self.my_array[index]

    def __setitem__(self, index, value):
        self.my_array[index] = value

    def __reversed__(self):
        return self.__class__(self.typecode, list(reversed(self.my_array)))

    def __len__(self):
        return len(self.my_array)

    def __sizeof__(self):
        return self.my_array.__sizeof__()

    def __eq__(self, o: object):
        if isinstance(o, array):
            return o.typecode == self.typecode and list(o) == self.my_array
        return False
