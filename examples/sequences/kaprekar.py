from typing import Tuple, Union, Generator


def kaprekar_function(n: int) -> Tuple[int, int]:
    """Функция Капрекара.
    Совершает действие: вычислить разницу между числом, 
    состоящим из цифр исходного числа, стоящих по убыванию, 
    и числом, состоящим из цифр исходного числа, стоящих 
    по возрастанию. 
    Шаги прекращаются когда число совпадает 
    с постоянной Капрекара.
    Подробнее см.: https://en.wikipedia.org/wiki/Kaprekar%27s_routine

    >>> kaprekar_function(876)
    (495, 5)
    >>> kaprekar_function(3412)
    (6174, 3)
    
    :param n: исходное число
    :type n: int
    :return: пару чисел (x, y), где x - константа к которой 
             сходится исходное число, y - число шагов.
    :rtype: Tuple[int, int]
    """
    count = 0
    old_n = 0
    while n != old_n and n > 0:
        old_n = n
        digits = list(str(n))
        n1 = int(''.join(sorted(digits, reverse=True)))
        n2 = int(''.join(sorted(digits)))
        n = n1 - n2
        count += 1
    return old_n, count - 1 if count > 1 else count


def gkaprekar(start: int, stop: Union[int]=None, /) -> Generator[Tuple[int, Tuple[int, int]], None, None]:
    """Генератор для функции Капрекара.
    Подробнее см. kaprekar_function.

    >>> list(gkaprekar(5))
    [(0, (0, 0)), (1, (0, 1)), (2, (0, 1)), (3, (0, 1)), (4, (0, 1))]
    >>> list(gkaprekar(10, 15))
    [(10, (0, 1)), (11, (0, 1)), (12, (0, 1)), (13, (0, 5)), (14, (0, 3))]

    :param start: Когда функция вызывается с одним параметрам 
                  этот аргумент означает правую границу 
                  интервала [0, start). В случае вызова функции 
                  с двумя аргументами, он характеризует левую 
                  границу [start, stop).
    :type start: int
    :param stop: В случае вызова функции с двумя аргументами, stop 
                 характеризует правую границу [start, stop).
    :type stop: int

    :return: Пары вида (i, K(i)), где i - проверяемое число, 
             K(i) - значение функции Капрекара (см. kaprekar_function).
    :rtype: Generator[Tuple[int, Tuple[int, int]], None, None]
    """
    if stop is None:
        start, stop = 0, start
    for i in range(start, stop):
        yield i, kaprekar_function(i)


def main():
    for j, item in gkaprekar(10, 15):
        print(j, item)


if __name__ == '__main__':
    main()
