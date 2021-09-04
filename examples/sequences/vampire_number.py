"""Числа вампиры

Первые несколько чисел вампиров:

1260, 1395, 1435, 1530, 1827, 2187, 6880, 102510, 104260, 105210, ...

Wiki: https://en.wikipedia.org/wiki/Vampire_number

Последовательность A014575 в OEIS: https://oeis.org/A014575

:Authors:
    - Vladimir Voronov
"""

from contextlib import suppress
from math import prod
from itertools import permutations
from typing import Generator, Optional


def is_vampire(number: int) -> bool:
    """Проверка на число-вампир

    >>> is_vampire(7520)
    False
    >>> is_vampire(1395)
    True
    >>> is_vampire(6880)
    True
    >>> is_vampire(125460)
    True
    >>> is_vampire(13078260)
    True

    :param number: Проверяемое число.
    :type number: int
    :raises ValueError: Длина проверяемого числа не кратна двум.
    :return: True Если число является числом-вампиром
             и False в противном случае.
    :rtype: bool
    """
    return bool(fangs(number))


def fangs(number: int) -> Optional[list[tuple[int, int]]]:
    """"Пары клыков" числа вампира

    Функция ищет все пары клыков чисел-вампиров. Если число не является
    числом-вампиром, результатом будет None.

    >>> fangs(7520) is None
    True
    >>> fangs(1395)
    [(15, 93)]
    >>> fangs(6880)
    [(86, 80)]
    >>> fangs(125460)
    [(204, 615), (246, 510)]
    >>> fangs(13078260)
    [(1620, 8073), (1863, 7020), (2070, 6318)]

    :param number: Число, для которого необходимо найти
                   разложение на множители.
    :type number: int
    :raises ValueError: Длина проверяемого числа не кратна двум.
    :return: Список пар клыков, если это число является числом-вампиром.
             В противном случае None.
    :rtype: Optional[list[tuple[int, int]]]
    """
    set_fangs = set()
    as_str = str(number)
    len_number = len(as_str)
    if len_number % 2:
        raise ValueError('Length of the number must be a multiple of two')
    for permuntation in permutations(as_str, len_number):
        permuntation = ''.join(permuntation)
        left = permuntation[:len_number // 2]
        right = permuntation[len_number // 2:]
        if left[-1] == '0' and right[-1] == '0':
            continue
        pair = int(left), int(right)
        if prod(pair) == number and pair[::-1] not in set_fangs:
            set_fangs.add(pair)
    if set_fangs:
        return sorted(list(set_fangs))
    return None


def all_vampire(start: int, end: int) -> Generator[int, None, None]:
    """Поиск всех чисел вампиров в диапазоне [start, end)

    >>> list(all_vampire(10, 100))
    []
    >>> list(all_vampire(1000, 2000))
    [1260, 1395, 1435, 1530, 1827]

    :param start: Левая граница интервала поиска.
    :type start: int
    :param end: Правая граница интервала поиска, не включается.
    :type end: int
    :raises ValueError: Стартовое значение превышает конечное.
    :yield: Очередное число вампир.
    :rtype: Generator[int, None, None]
    """
    if start > end:
        raise ValueError('Start value must be less than end value.')
    for i in range(start, end):
        with suppress(ValueError):
            if is_vampire(i):
                yield i


def first_k_vampire(start: int, count: int,
                    max_iter: int=1_000_000) -> Generator[int, None, None]:
    """Первые несколько чисел вампиров

    >>> list(first_k_vampire(100, 10))
    [1260, 1395, 1435, 1530, 1827, 2187, 6880, 102510, 104260, 105210]

    :param start: Левая граница интервала поиска.
    :type start: int
    :param count: Количество искомых чисел.
    :type count: int
    :param max_iter: Максимальное количество итераций.
                     Введена как дополнительная защита, defaults to 1_000_000
    :type max_iter: int, optional
    :raises ValueError: Количество чисел <= 0.
    :yield: Очередное число вампир
    :rtype: Generator[int, None, None]
    """
    if count <= 0:
        raise ValueError('Number of numbers must be greater than zero.')

    number = start
    while count > 0 and max_iter > 0:
        with suppress(ValueError):
            if is_vampire(number):
                count -= 1
                yield number
        number += 1
        max_iter -= 1


def main():
    """Пример использования"""

    print(f'Все пары клыков числа 13078260: {fangs(13078260)}')
    print(f'Проверка числа 2187: {is_vampire(2187)}')
    print(f'Все числа вампиры от 1000 до 2000: {list(all_vampire(1000, 2000))}')
    print(f'Первые 10 чисел вампиров: {list(first_k_vampire(1000, 10))}')


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
