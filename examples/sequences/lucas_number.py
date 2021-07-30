"""Числа Люка

Wiki:
    https://en.wikipedia.org/wiki/Lucas_number

:Authors:
    - Voronov Vladimir
"""


from typing import Generator


GOLDEN_RATIO = (1 + 5**0.5) / 2


def lucas_number(number: int) -> Generator[int, None, None]:
    """Числа Люка

    Числа вычисляются через золотое сечение с использованием замкнутой
    формы.

    :param number: первые number чисел Люка
    :type number: int
    :yield: очередное число Люка
    :rtype: Generator[int, None, None]
    """
    for i in range(number):
        yield int(GOLDEN_RATIO**i + (-GOLDEN_RATIO)**(-i))


def lucas_number_recurrent(number: int) -> Generator[int, None, None]:
    """Числа Люка

    Числа вычисляются через рекуррентную формулу,
    используя подход динамического программирования.

    :param number: первые number чисел Люка
    :type number: int
    :yield: очередное число Люка
    :rtype: Generator[int, None, None]
    """
    last = [2, 1]
    for i in range(number):
        if 0 <= i <= 1:
            yield last[i]
        else:
            last = [last[-1], sum(last)]
            yield last[-1]


def main():
    """Примеры"""
    recurrent = map(str, lucas_number_recurrent(10))
    analogue = map(str, lucas_number(10))
    print(f'Recurrent formula     : {" ".join(recurrent)}')
    print(f'Analogue Binet formula: {" ".join(analogue)}')


if __name__ == '__main__':
    main()
