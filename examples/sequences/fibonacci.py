"""Числа Фибоначчи

Wiki:
    https://en.wikipedia.org/wiki/Fibonacci_number

:Authors:
    - Voronov Vladimir
"""


from typing import Generator


GOLDEN_RATIO = (1 + 5**0.5) / 2


def fibonacci_recurrent(n: int) -> Generator[int, None, None]:
    """Числа Фибоначчи

    Числа вычисляются через рекуррентную формулу.

    :param n: первые n чисел Фибоначчи
    :type n: int
    :yield: очередное число Фибоначчи
    :rtype: Generator[int, None, None]
    """
    # рекуррентная формула
    b = [0, 1]
    for i in range(n - 2):
        if i in (0, 1):
            yield b[i]
        b = [b[-1], sum(b)]
        yield b[-1]


def fibonacci_binet(n: int) -> Generator[int, None, None]:
    """Числа Фибоначчи

    Числа вычисляются по формуле Бине, используя золотое сечение.

    :param n: первые n чисел Фибоначчи
    :type n: int
    :yield: очередное число Фибоначчи
    :rtype: Generator[int, None, None]
    """
    for i in range(n):
        yield int((GOLDEN_RATIO**i - (-GOLDEN_RATIO)**(-i)) / (2*GOLDEN_RATIO - 1))


def main():
    recurrent = map(str, fibonacci_recurrent(10))
    binet = map(str, fibonacci_binet(10))
    print(f'Recurrent formula: {" ".join(recurrent)}')
    print(f'Binet formula    : {" ".join(binet)}')


if __name__ == '__main__':
    main()
