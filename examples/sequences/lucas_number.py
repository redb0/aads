"""Числа Люка

Wiki:
    https://en.wikipedia.org/wiki/Lucas_number

:Authors:
    - Voronov Vladimir
"""


from typing import Generator


GOLDEN_RATIO = (1 + 5**0.5) / 2


def lucas_number(n: int) -> Generator[int, None, None]:
    """Числа Люка

    :param n: первые n чисел Люка
    :type n: int
    :yield: очередное число Люка
    :rtype: Generator[int, None, None]
    """
    for i in range(n):
        yield int(GOLDEN_RATIO**i + (-GOLDEN_RATIO)**(-i))
   


def lucas_number_recurrent(n: int) -> Generator[int, None, None]:
    """Числа Люка

    Числа вычисляются через рекуррентную формулу.

    :param n: первые n чисел Люка
    :type n: int
    :yield: очередное число Люка
    :rtype: Generator[int, None, None]
    """
    b = [2, 1]
    for i in range(n):
        if 0 <= i <= 1:
            yield b[i]
        else:
            b = [b[-1], b[-1] + b[-2]]
            yield b[-1]


def main():
    recurrent = map(str, lucas_number_recurrent(10))
    analogue = map(str, lucas_number(10))
    print(f'Recurrent formula     : {" ".join(recurrent)}')
    print(f'Analogue Binet formula: {" ".join(analogue)}')


if __name__ == '__main__':
    main()
