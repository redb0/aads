"""Числа Фибоначчи

Wiki:
    https://en.wikipedia.org/wiki/Fibonacci_number

:Authors:
    - Voronov Vladimir
"""


from typing import Generator


GOLDEN_RATIO = (1 + 5**0.5) / 2


def fibonacci_recurrent(number: int) -> Generator[int, None, None]:
    """Числа Фибоначчи

    Числа вычисляются через рекуррентную формулу,
    используя подход динамического программирования.

    :param number: первые number чисел Фибоначчи
    :type number: int
    :yield: очередное число Фибоначчи
    :rtype: Generator[int, None, None]
    """
    # рекуррентная формула
    last = [0, 1]
    for i in range(number - 2):
        if i in (0, 1):
            yield last[i]
        last = [last[-1], sum(last)]
        yield last[-1]


def fibonacci_binet(number: int) -> Generator[int, None, None]:
    """Числа Фибоначчи

    Числа вычисляются по формуле Бине (замкнутая форма),
    используя золотое сечение.

    :param number: первые number чисел Фибоначчи
    :type number: int
    :yield: очередное число Фибоначчи
    :rtype: Generator[int, None, None]
    """
    for i in range(number):
        yield int((GOLDEN_RATIO**i - (-GOLDEN_RATIO)**(-i)) / (2*GOLDEN_RATIO - 1))


def main():
    recurrent = map(str, fibonacci_recurrent(10))
    binet = map(str, fibonacci_binet(10))
    print(f'Recurrent formula: {" ".join(recurrent)}')
    print(f'Binet formula    : {" ".join(binet)}')


if __name__ == '__main__':
    main()
