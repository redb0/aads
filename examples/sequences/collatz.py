"""Проверка гипотезы Коллатца

Wiki:
    https://en.wikipedia.org/wiki/Collatz_conjecture
"""

from typing import List


def collatz(number: int) -> List[int]:
    """Проверка гипотезы Коллатца

    Подробнее:
        https://en.wikipedia.org/wiki/Collatz_conjecture

    Параметры:
    :param number: число для которого проверяется гипотеза
    :type number: int

    :return: Сипсок чисел, соответствующих шагам проверки
    :rtype: List[int]
    """
    res = [number]
    if number == 1:
        return res
    while number != 1:
        if not number % 2:
            number //= 2
        else:
            number = 3 * number + 1
        res.append(number)
    return res


def main():
    """Демонстрация работы"""
    for i in range(1, 20):
        print(f'{i:<2} - {collatz(i)}')


if __name__ == '__main__':
    main()
