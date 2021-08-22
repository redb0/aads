"""Пример использования модуля my_array"""

import sys

import my_array  # pylint: disable=E0401



x = my_array.array('d', 5)

print(f'{x = }')
print(f'{x.length = }')

x[0] = 123
x[1] = 0
x[2] = 0
x[3] = 1
x[4] = 2

print(f'{x[0] = }')
print(f'{x[1] = }')
print(f'{x[2] = }')
print(f'{x[3] = }')
print(f'{x[4] = }')
print('-' * 50)

x.initialize()
print(f'{x[0] = }')
print(f'{x[1] = }')
print(f'{x[2] = }')
print(f'{x[3] = }')
print(f'{x[4] = }')
print('-' * 50)

y = [0.0, 1.0, 2.0, 3.0, 4.0]
print(f'{sys.getsizeof(x) = }')
print(f'{sys.getsizeof(y) = }')
