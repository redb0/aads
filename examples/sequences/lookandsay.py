"""Последовательность "Посмотри и скажи"

Wiki:
    https://en.wikipedia.org/wiki/Look-and-say_sequence

:Authors:
    - Voronov Vladimir
"""

from itertools import groupby
from typing import Generator, List


def look_and_say(number: int) -> List[str]:
    """Последовательность "Посмотри и скажи"

    :param number: количество первых чисел
    :type number: int
    :return: список первых чисел
    :rtype: List[str]
    """
    res = []
    item = '1'
    for _ in range(number):
        item = ''.join([str(len(list(group))) + key for key, group in groupby(item)])
        res.append(item)
    return res


def look_and_say_inf(number: str='1') -> Generator[str, None, None]:
    """Бесконечный генератор элементов последовательности "Посмотри и скажи"

    :param number: начальное значение, defaults to '1'
    :type number: str, optional
    :yield: очередной элемент последовательности
    :rtype: Generator[str, None, None]
    """
    while True:
        yield number
        number = ''.join(str(len(list(g))) + k for k, g in groupby(number))


def look_and_say_next(number: str='1') -> str:
    """Следующее число последовательности "Посмотри и скажи"

    :param number: число последовательности, defaults to '1'
    :type number: str, optional
    :return: следующее за number число
    :rtype: str
    """
    k, last, result = 1, number[0], ''
    for digit in number[1:]:
        if last == digit:
            k += 1
        else:
            result += str(k) + last
            k = 1
        last = digit
    result += str(k) + last
    return result


def main():
    """Примеры"""
    number = 5
    print(f'Первые {number} чисел: {look_and_say(number)}')
    print('-' * 50)
    print('Бесконечный генератор:')
    for i, item in enumerate(look_and_say_inf()):
        if i == number:
            break
        print(f'{i}-е число: {item}')
    print('-' * 50)
    print('Функция последовательного вычисления:')
    item = '1'
    for i in range(number):
        item = look_and_say_next(item)
        print(f'{i}-е число: {item}')


if __name__ == '__main__':
    main()
